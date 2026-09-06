# Plan: Mealie & Home Assistant

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

Everyday household information without repeated login prompts on approved devices.

## Work sequence

1. Test session expiration, renewal, revocation and foreground return.
2. Verify cellular-only access and first enrollment separately from the Wi-Fi VPN-off checkpoint.
3. Review native TV action confirmations and provider-specific failure messages.

## Acceptance criteria

- [ ] Approved access opens actual content rather than stopping at a login shell.
- [ ] Anonymous, replayed and revoked access is denied.
- [ ] Read-only documentation checks do not actuate household devices.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
