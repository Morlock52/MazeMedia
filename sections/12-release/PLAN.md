# Plan: Version history, evidence & delivery

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

Keep implementation, runtime verification and publication as separate milestones.

## Work sequence

1. Finish iPad controls/automatic setup and Apple TV transport acceptance.
2. Repeat the Mac mouse suite without the blocking floating dialog.
3. Refresh archives from final source and upload only after required checks pass.
4. Verify build processing and the correct internal TestFlight group after upload.

## Acceptance criteria

- [ ] The source revision and delivered binary are identified.
- [ ] A compile result is never used as proof of physical playback.
- [ ] A build appears to testers only after Apple processing and group availability are confirmed.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
