# Plan: Photos, books & saving content

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

A scoped photo integration today; a clear plan for reading and write-back.

## Work sequence

1. Define provider-specific reading contracts for books, comics, audiobooks and podcasts.
2. Design upload and save-back flows for iPhone/iPad with explicit destination and permissions.
3. Test pagination, unavailable assets, key revocation and interrupted transfers.

## Acceptance criteria

- [ ] Photo metadata and permitted assets load with a scoped key.
- [ ] A completed save is confirmed by provider-side retrieval, not merely a progress animation.
- [ ] Public documentation continues to distinguish implemented reading from planned write-back.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
