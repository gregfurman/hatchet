#!/bin/sh

get_pr_history() {
  local since_hash="$1" until_hash="$2"
  shift 2
  git log "${since_hash}..${until_hash}" --pretty=format:'%s' -- "$@" \
    | grep -oE '#[0-9]+' | tr -d '#' | sort -u \
    | while read -r pr; do
        gh pr view "$pr" \
          --repo hatchet-dev/hatchet \
          --json number,title,author,labels \
          --jq '"- \(.title) (#\(.number)) by @\(.author.login)"'
      done
}

awk '
  FNR == 1 && NR > 1 { print "" }
  /^# Changelog/ {
      release=0;
      next;
  }
  match($0, /^All notable changes to Hatchet.s (.*) will be documented/) {
      # HACK(gregfurman): awk does not allow extracting the regex matching group, so
      # just use the length of the prefix and suffic to extract via substr.
      print "### " substr($0, RSTART + 33, RLENGTH - 52);
      next;
  }
  /^## \[Unreleased\]/ {
      release++;
      next;
  }
  /^## \[[0-9]+\.[0-9]+\.[0-9]+\]/ {
      release++;
      next;
  }
  /^#/ {
      # Demote any headers (i.e Added, Changed) to sub-headers
      # so they reside under the "## <component>" section.
      print "#" $0;
      next;
  }
  {
      if (release == 1) print;
      if (release > 1) nextfile;
  }' "$@"

echo "What's Changed?"
echo

since=$(gh release list --repo hatchet-dev/hatchet --exclude-drafts --exclude-pre-releases --limit 1 --json tagName --jq '.[0].tagName')

get_pr_history "$since" HEAD cmd pkg internal api api-contracts
