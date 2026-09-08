# Maze Media 2.0 (26) — Luna follow-up discovery

Luna now asks a focused follow-up when a content request is unclear and uses the answer to refine its suggestions. Recommendations stay within the supplied catalog items; unrelated requests are redirected to content discovery. Quick and Consider continue to use Luna with none/low reasoning across all app editions.

The released search still compares up to 24 loaded Jellyfin items. Whole-library discovery remains a development preview. This build does not claim to search every connected service.

Compatibility: older clients continue receiving their existing selection-only response. Device enrollment now counts active devices against its limit, while revoked keys remain denied.

Verification: 67 backend tests and all three signed distribution archives passed, including the Apple TV Top Shelf extension. Eight synthetic live provider checks passed across both reasoning modes. The public authenticated route passed clarification and refinement in both modes; unauthorized and foreign-origin calls were rejected. Physical-device interaction remains unverified.

YouTube publish dates are now populated for 6,856 of 6,865 source records. Nine unavailable IDs retain an explicit placeholder. The currently exposed Jellyfin catalog has verified dates on all 125 resolvable videos. Live TV retains the preceding fragmented-MP4 correction; cold startup remains noticeable.

All three uploads succeeded and Apple processing completed. Build 2.0 (26) is Testing in MorloksMaze Internal for iOS/iPadOS, macOS and tvOS. Testing notes and the GitHub link were saved on every build. This confirms availability, not physical installation or interaction. Existing screenshots illustrate earlier builds; no new screenshot acceptance is claimed.
