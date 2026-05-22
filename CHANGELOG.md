# Changelog

This changelog documents notable changes to Hatchet's Engine, SDK, and CLI between releases.
On release, these entries are promoted into the GitHub Release body and this file is reset.

For the full history of past releases, see
https://github.com/hatchet-dev/hatchet/releases.

Entries follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
conventions for grouping and formatting.


<!--
This CHANGELOG.md functions as a snapshot in time for a release, describing
the net change between the previous release and the next. Intermediate
version tags between releases are not represented as separate sections,
their changes accumulate into the next release entry.

The [Unreleased] section is a draft of the next release's notes. If your PR
reverts or supersedes something added under [Unreleased] since the last
release, edit or delete the original entry rather than adding a new one.

Prefix each entry with the affected component in bold, e.g. "**engine**: ...".

Valid components are:
- engine
- api
- migrate
- admin
- cli
- dashboard
- lite

Write entries in the imperative mood describing user-visible impact,
not internal mechanics. For example:

GOOD: **engine**: fix connection leak when LISTEN sessions are recycled ✅
BAD: **engine**: refactored pgxpool.Conn.Hijack handling ❌

Release notes will automatically append a section with relevant information
on pull request, contributor, and the version tag in which the change first
shipped, in the form <PR TITLE> by @<PR AUTHOR> in <TAG>.
-->

## [v0.87.5] - 2026-05-22


### What's Changed

- [v0.87.2] Fix: Attempt at improving worker actions query (#3774) by @mrkaye97
- [v0.87.2] Add Dockerfile for all SDK e2e tests, fix flaky e2e tests (#3846) by @juliusgeo
- [v0.87.2] [FEAT] [CLI] Make Hatchet Lite version configurable (#3925) by @Ujjwal-Singh-20
- [v0.87.2] Fix: Correctly handle child key-based caching in durable task child spawning (#3955) by @mrkaye97
- [v0.87.2] Fix: Only run worker id action getter query when needed (#3976) by @mrkaye97
- [v0.87.2] Fix: Increase limit default to 10k (#3978) by @mrkaye97
- [v0.87.2] Fix: Payload external id duplicates from durable child spawning (#3984) by @mrkaye97
