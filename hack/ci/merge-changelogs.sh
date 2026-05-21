#!/bin/sh
awk '
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
