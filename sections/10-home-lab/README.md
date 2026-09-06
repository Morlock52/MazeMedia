# Home-lab architecture & network integration

> A logical map of the existing environment and the routes the applications depend on.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

The design draws on the September 4 network baseline retrieved on September 5, then on later implementation and acceptance records. Proxmox hosts the virtualized environment; CT100 contains the media/service stack, with other VMs/containers and attached storage supporting the household. NetBird provides private reachability. Reverse proxies expose selected HTTPS origins. Pocket ID supplies human identity for protected entrances. This publication is a dated architecture view, not a fresh fleet-health audit.

## User journey

The app selects a provider route, establishes the appropriate identity/session, requests catalog or household data, and obtains provider-delivered content. Operator consoles, host control, storage administration and break-glass access stay outside the consumer app.

## Design decisions

- Separate route reachability, authentication, service health and real content behavior.
- Represent public device-authorized origins separately from private NetBird paths.
- Retain the existing operator plane; do not turn the app into a Proxmox or Docker console.
