# Morlock’s Maze — Brass Labyrinth

Design research and implementation decision · September 6, 2026

The new identity uses charcoal iron, aged brass, mineral green and ivory, with an original three-dimensional maze around an M. The architecture refers to the underground machinery associated with the Morlocks in [H. G. Wells’s The Time Machine](https://www.gutenberg.org/files/35/35-h/35-h.htm). The precise palette and emblem are original creative decisions, not historical claims or adaptations of a film design.

The home lab is the collection’s infrastructure; the theme presents it as a coherent personal place. Controls retain familiar names—Home, Library, Mealie, Home Assistant—so the visual metaphor does not turn navigation into a puzzle.

## Evidence and decisions

| Question | Primary evidence | Decision and limit |
|---|---|---|
| How should an expressive brand coexist with current Apple UI? | [Apple WWDC26 design guide](https://developer.apple.com/wwdc26/guides/design/) and [color guidance](https://developer.apple.com/design/human-interface-guidelines/color) | Brand the content layer and primary accent; retain native tabs, sidebar, transport and focus. Guidance is current, but beta runtime still needs physical review. |
| Should every card become glass? | [Apple materials guidance](https://developer.apple.com/design/human-interface-guidelines/materials) | Use stable dark content surfaces. Let the system provide navigation/control materials; avoid a decorative glass layer behind every label. |
| Does a native media app need identical layouts on every device? | [Swiftfin repository](https://github.com/jellyfin/Swiftfin), a native iOS/tvOS Jellyfin client | Shared identity can coexist with platform-specific interaction. No code or artwork copied; its playback engines were not introduced into this theme change. |
| What does Morlock mean visually? | Wells’s original text, chapters VIII–IX | Underground industrial architecture is a grounded reference. Brass light, the M emblem and geometric labyrinth are interpretation. Avoid film likenesses and horror characters. |
| What is still uncertain? | Existing test ledger; physical screenshots of the new build required | Owner preference cannot be established by automated tests. Dynamic Type, focus visibility, real device geometry and release availability remain separate checks. |

## Shared visual contract

Background #101514; panels #1A2220; raised surfaces #26302C; text #F3EBDD; secondary text #C1C6BB; action/focus brass #E3BD78; secondary mineral #92BDB0. Existing status semantics remain distinct. Native system typography is used in applications; Figma uses Inter as an available reference substitute for SF.

A compact, adaptive Home header introduces the identity. iPhone uses a compact service grid; iPad and Mac use the existing sidebar and wider shelves. Apple TV keeps five sidebar destinations and remote-native controls. Artwork is static and decorative; Reduced Transparency replaces the header’s image underlay with an opaque surface. Playback content receives no decorative overlay from the theme.

## Assets and delivery

[Editable Figma specification](https://www.figma.com/design/sfpDlUVIM1j8i4wZ1wjCBC?node-id=8-12). Original Blender source and rendering scripts are stored beside this document. The local image CLI did not have OPENAI_API_KEY. The available image-generation tool produced the complementary underground architecture used behind missing-artwork symbols. The original Blender scene produced the maze emblem, header and icon exports. The two sources are recorded separately; no client API credential was added.

The search scope was current Apple guidance, the original literary source and a relevant open-source Apple media client. Initial searches and targeted primary-source opens support the design choices. Further broad searching is unlikely to change the native-control decision; physical review and owner feedback are the remaining evidence gaps. No authentication, service routing or media pipeline changes are part of this theme.
