# Plan: Apple TV edition

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

A native, remote-driven experience for shared viewing.

## Work sequence

1. Wake the physical Apple TV and finish build 11 transport-controls acceptance.
2. Retest long playback, track selection and recovery after app switching.
3. Design native counterparts for requested services only when their APIs and remote interactions are viable.

## Acceptance criteria

- [ ] The remote can pause, resume, seek when supported, and exit playback.
- [ ] Native recipe and household-state navigation passes on physical TV hardware.
- [ ] No unsupported browser or unverified game feature is advertised as complete.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
