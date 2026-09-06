# Photos, books & saving content

> A scoped photo integration today; a clear plan for reading and write-back.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

The current photo integration uses Immich. Approved devices request a restricted per-device key for asset read/view and use the provider’s direct asset route. The photo route still depends on private connectivity at the recorded checkpoint. Complete Kavita and Audiobookshelf readers, downloads and save-back workflows are planned client features. Existing service configuration does not establish reader or transfer functionality.

## User journey

Current: Home → Photos → asset grid → detail. Planned: choose a reader or upload destination, select content, review the destination, then save with progress, conflict and retry handling.

## Design decisions

- Keep personal photos out of public documentation.
- Separate read access from upload, delete and library-management permissions.
- Require a native, remote-appropriate reader/viewer before claiming TV parity.
