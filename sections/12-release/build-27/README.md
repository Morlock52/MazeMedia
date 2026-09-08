# Maze Media 2.0 (27) — personal library and playback recovery

Verified on 8 September 2026: Apple processed all three uploads, and version 2.0 (27) is **Testing** in the existing **MorloksMaze Internal** group for iOS/iPadOS, Mac Catalyst and tvOS. Testing notes and the GitHub project link are saved on every build. The iOS archive targets iPhone and iPad; tvOS uses its separate application identity. The Top Shelf extension also reports build 27.

Home now provides account-scoped favorites and saved searches stored on each device. Continue and Recently Added precede service shortcuts. Retry playback negotiates a new stream, preserves the resume position and rejects stale signed-out sessions; Live TV retries at the live edge.

Expanded Luna whole-library discovery and cross-device saved results remain disabled pending acceptance. The existing bounded Luna assistant remains available on all editions. Catalogue-resilience fixes run server-side and do not establish complete-library acceptance.

Validation: 91 shared tests, 70 backend tests, Mac saved-search UI and live-source controls; signed distribution archives and native platform-boundary checks passed. Physical iPhone/iPad/Apple TV interaction and Top Shelf acceptance remain pending. Live TV cold startup can still be slow. TestFlight availability is not proof of installation or physical acceptance.

The Mac upload initially stopped with expired Xcode credentials; a retry of the same verified archive succeeded. No new credential or account permissions were introduced.

| Platform | Apple build ID | Internal status |
| --- | --- | --- |
| iPhone / iPad | 69bddce0-bf0b-44b0-9b2d-aa8ced9ba7cc | Testing |
| Mac Catalyst | aa12986b-ac15-4e5e-8b3e-cb24b16a3b4e | Testing |
| Apple TV | cb65529c-94da-41d1-a224-f9276ec901f6 | Testing |

[Current-code screenshots captured before distribution](../candidate-4291afd/README.md#screenshots) · [Previous release](../build-26/README.md)
