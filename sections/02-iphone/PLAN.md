# Plan: iPhone edition

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

A compact, touch-first entrance to the library and household services.

## Work sequence

1. Retain the passing build 11 pause, seek, restart, resume and dismissal behavior.
2. Complete sustained playback, subtitle, AirPlay and Picture in Picture checks with representative streams.
3. Verify foreground/background recovery and service renewal on Wi-Fi and cellular separately.

## Acceptance criteria

- [ ] Recorded build 11 controls test passes on a physical iPhone.
- [ ] Each browser destination can return to the app without a navigation dead end.
- [ ] A failed stream exposes a useful retry or compatibility action.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
