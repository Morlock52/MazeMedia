# Games & media requests

> Bring RomM and Jellyseerr into the app with an obvious way back.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

RomM and Jellyseerr are separate open-source services with existing household routes. On iPhone, iPad and Mac, Maze Media provides an embedded browser with a constrained service destination. Reaching a catalog does not prove game execution or a completed request. The last implementation checkpoint keeps these app-specific routes on the private access path.

## User journey

Home → Games or Requests → service content. Use browser Back/Forward within the service, Reload for a recoverable load failure, and Done to return to the native application.

## Design decisions

- Preserve each provider’s own content and authorization model.
- Treat web game runtime, nested authentication and touch/controller input as distinct checks.
- Do not claim a tvOS browser, emulator core or completed native request client.
