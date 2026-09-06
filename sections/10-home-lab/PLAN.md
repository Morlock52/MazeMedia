# Plan: Home-lab architecture & network integration

[Section context](README.md) · [Portfolio overview](../../README.md)

## Intended outcome

A logical map of the existing environment and the routes the applications depend on.

## Work sequence

1. Maintain an owner-only inventory mapping logical service names to actual origins, ports, peers, policies and storage dependencies.
2. Reconcile the baseline with live DNS, proxy configuration and NetBird policies before changing a route.
3. For new NetBird configurations, evaluate the current Networks model; do not infer a migration of the existing environment.

## Acceptance criteria

- [ ] Every app destination has an explicit provider, route class, identity method and failure behavior.
- [ ] An off-VPN claim names the tested service, device, network and enrollment state.
- [ ] The public repository contains logical topology without operational addresses or credentials.

## Evidence and boundaries

Acceptance boxes are requirements for the next complete validation pass, not claims that every item is currently untested. See the [recorded evidence](../12-release/EVIDENCE.md) for completed checkpoints and remaining gaps. Provider and platform dependencies are described in the [architecture](../10-home-lab/README.md) and [identity plan](../11-identity/PLAN.md).
