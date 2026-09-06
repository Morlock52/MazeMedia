# Device identity, enrollment & session design

> Remove repeated prompts without removing authorization.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

An approved device owns a P256 private key held in Keychain/Secure Enclave where available. The access service validates short-lived signed challenges and issues host-scoped service sessions. Jellyfin setup approves that device’s own Quick Connect exchange; Immich provisions a separate restricted key. For household approval, the TV displays an eight-digit, five-minute, single-use code. An already approved iPhone or iPad approves that code.

## User journey

Enroll through the existing protected route → create or retrieve device identity → prove possession → obtain a provider-specific session → renew when appropriate → revoke when the device is removed. First enrollment and ordinary access after approval are separate cases.

## Design decisions

- Keep administrator credentials and provisioning secrets on the server.
- Use different provider credentials for different services and devices.
- Do not substitute a hard-coded default account or public unauthenticated tunnel.
- Keep human Pocket ID sign-in distinct from machine/device authorization.
