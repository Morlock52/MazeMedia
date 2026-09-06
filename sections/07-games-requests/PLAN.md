# Plan: Games & media requests

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

Bring RomM and Jellyseerr into the app with an obvious way back.

## Work sequence

1. Test the exact game-launch path beyond the second authentication screen.
2. Validate controller/touch input, game exit and browser history on the iPad.
3. Specify a native TV requests API and authorization contract before adding a TV tile.

## Acceptance criteria

- [ ] The requested game actually starts and accepts input on the target device.
- [ ] The browser returns to Maze Media from nested pages and error screens.
- [ ] Private route requirements are explained before the user encounters a blank page.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
