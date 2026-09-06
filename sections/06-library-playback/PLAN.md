# Plan: Library, video, music & live TV

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

One Jellyfin content model, with playback capabilities matched to each stream.

## Work sequence

1. Build a representative format matrix including saved videos, films, episodes, music and live channels.
2. Check first frame, sustained advancement, seek/resume, interruption and stop reporting.
3. Verify available tracks, fit/fill, volume, AirPlay and Picture in Picture on each supported device.

## Acceptance criteria

- [ ] A play action results in decoded frames and advancing time, or an explicit error.
- [ ] Leaving playback stops or hands off the session according to the intended lifecycle.
- [ ] Resume position remains valid after failure and relaunch.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
