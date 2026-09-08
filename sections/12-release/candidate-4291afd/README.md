# Current development candidate · 4291afd

**Source checkpoint:** 8 September 2026. **Release status:** not uploaded to TestFlight.

The candidate follows the released 2.0 (26) build. Its local development binary still carries version 2.0 (26), so the source commit identifies it precisely; it is not the same binary distributed through TestFlight. A new build number is required before distribution.

## What changed

- **Personal Home:** Continue and Recently Added appear before service shortcuts. My library holds favorites and saved searches, stored locally and separated by account.
- **Playback recovery:** Retry requests a new stream, preserves the resume position and rejects a stale signed-out session. Live TV retries at the live edge.
- **Luna development preview:** authorized result actions, cross-device saved results and YouTube publication dates. Expanded discovery remains disabled for release until all-platform acceptance passes.
- **Catalogue resilience:** unnamed Jellyfin episodes no longer abort indexing. Missing titles are explicitly labelled, and verified YouTube publication metadata is preserved.
- **Release verification:** repeatable platform checks record unavailable devices, skipped tests and failures as incomplete gates.

## Verification

| Check | Result |
| --- | --- |
| Shared native tests on Mac | 91 passed |
| Backend tests | 70 passed |
| Mac saved-search UI | Passed; fixture capture reviewed |
| Current iOS and tvOS builds | Passed |
| Mac live-source controls and bounded Luna checks | Passed |
| Physical iPhone, iPad and Apple TV | Blocked: unavailable to Xcode |
| Top Shelf interaction | Pending |
| Expanded discovery and complete catalogue acceptance | Pending |
| New TestFlight distribution | Not performed |

A build or screenshot is not proof of physical-device functionality. Existing TestFlight availability is documented separately in the [build 26 release record](../build-26/README.md).

## Screenshots

Fresh candidate captures are pending. The existing portfolio images remain dated historical references and are not relabelled as this candidate.

[Implementation commit](https://github.com/Morlock52/morlocksmaze-media/commit/4291afd5233e7f865bb28e932ecfae0d707aea8b) · [Release section](../README.md)
