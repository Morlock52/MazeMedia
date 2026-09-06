# Build 13 verification

September 6, 2026 · Xcode 27 beta 6

| Layer | Verified result |
|---|---|
| Source | Shared theme, platform adapters, original resources and build number 13; `git diff --check` passes. |
| Signed builds | iOS device, tvOS device and Mac Catalyst builds pass. iOS and tvOS release archives pass signature verification. TV app and Top Shelf both report build 13. |
| Apple TV | Full run: 73 passed, 2 optional skips, zero failures. Focus/navigation check repeated after the contrast correction: passed. Physical screenshot reviewed. |
| Mac | 71 passed, 2 optional skips, zero failures, including the Home/navigation UI test. One main-thread responsiveness warning was emitted during the UI run; no failure or hang was observed. Clean Catalyst window capture reviewed. |
| iPad | Physical Home/navigation check passed. Full-display screenshot reviewed after fixing XCTest's orientation-dependent app-bounds capture. |
| iPhone | Simulator Home/navigation check passed on iOS 26.5. Build 13 installed on the physical iPhone; iOS denied launch because it was locked. Physical build 13 interaction remains unverified. |
| Local deployment | Build 13 installed on all four editions. iPad, Mac and Apple TV launched normally after fixture tests. Mac installation retains the previous app as a backup. |
| Upload | iOS export/upload succeeded at 09:33 EDT; tvOS succeeded at 09:34 EDT. Apple accepted both packages for processing. Final tester availability is recorded separately below. |

[Test summaries](test-summary.json) and [screenshot provenance](screenshots.json) retain concise evidence. Full xcresults and upload logs remain in the local project build workspace. Screenshots use demo content; they do not establish live provider health. This theme pass did not change or requalify all media formats, service routes, game engines or household operations. Earlier functional evidence remains in the implementation ledger.

## Visual corrections made during review

The first iPad label layout wrapped short names awkwardly. The final grid places icons above labels and scales its preferred tile width with text size. TV focus originally placed pale text on a brass fill; the final focused household labels use the dark base color. Rejected or cropped screenshots are not used in the published design.

## TestFlight availability

Live App Store Connect verification shows **1.0.0 (13) — Testing** for both iOS and tvOS, assigned to **MorloksMaze Internal**. The existing internal group has access. This confirms release availability, not installation through the TestFlight client. [Release record](release-status.json).
