# Plan: Mac edition

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

A desktop companion built from the shared iOS target with Mac Catalyst.

## Work sequence

1. Repeat automated mouse acceptance without the floating dialog that interrupted XCTest.
2. Verify keyboard navigation, window resizing and external-display behavior.
3. Prepare distribution signing/notarization or Mac App Store delivery as a separate release decision.

## Acceptance criteria

- [ ] The installed app launches and loads its navigation and provider content.
- [ ] Recorded mouse checks cover pause, seek, restart, resume and speed selection.
- [ ] The automated test is reported as interrupted until an uninterrupted run passes.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
