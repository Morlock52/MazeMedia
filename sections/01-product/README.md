# Product vision & design system

> Make a privately operated collection easy to explore from the Apple device already in use.

[Portfolio overview](../../README.md) · [Section plan](PLAN.md)

## Current design

The applications now use [Brass Labyrinth](../13-brass-labyrinth/README.md): charcoal iron, aged brass, mineral green and ivory, with an original M labyrinth. Build 13 implements the identity across all four editions.

Maze Media is the client experience for Morlock’s Maze. It brings media and selected household services into a consistent navigation model while leaving storage, identity and service administration in the home lab. The product goal is broad access to the owner’s content; the current implementation is deliberately narrower than that goal. A service tile does not establish complete support for its provider.

## User journey

Open Home, choose a collection or service, inspect its content, then return through a predictable Back or Done action. Keep the current location visible and make failed requests distinguishable from an empty library.

## Design decisions

- Use native Apple navigation and AVKit for core media.
- Keep provider names where they help the user understand the destination.
- Use focused detail pages instead of placing every action below a long dashboard.
- Treat consistency as shared meaning and behavior; adapt layout to touch, pointer and remote.
