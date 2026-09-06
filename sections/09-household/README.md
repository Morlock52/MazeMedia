# Mealie & Home Assistant

> Everyday household information without repeated login prompts on approved devices.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

Mealie and Home Assistant are main-menu destinations. iPhone/iPad use embedded service views; Apple TV uses native recipe and state interfaces. Dedicated public app origins accept approved-device sessions, while service administrator credentials remain server-side. Recorded iPhone/iPad checks opened recipe content and the populated household dashboard over Wi-Fi with NetBird disconnected.

## User journey

Home → Mealie → recipe ingredients and steps → Done. Home → Home Assistant → household states → Done. On TV, use native categories and remote Back; supported light/switch actions require confirmation.

## Design decisions

- No repeated interactive login means device-authorized access, not anonymous public access.
- Keep session renewal and revocation part of the service contract.
- Separate read-only verification from actions that alter the house.
