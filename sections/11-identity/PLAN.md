# Plan: Device identity, enrollment & session design

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

Remove repeated prompts without removing authorization.

## Work sequence

1. Document enrollment prerequisites and recovery for replaced devices.
2. Verify single-use challenges, expiry, wrong-host cookies and revoked credentials.
3. Retest automatic setup on iPad and final TV pairing independently of iPhone success.

## Acceptance criteria

- [ ] Only the intended approved device completes the provider exchange.
- [ ] Revocation removes access and the associated scoped photo key.
- [ ] Screenshots, diagnostics and public plans contain no tokens, pairing secrets or private keys.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
