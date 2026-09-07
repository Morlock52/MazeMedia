# Recorded delivery evidence

[Release section](README.md) · [Portfolio overview](../../README.md)

Checkpoint: September 6, 2026. Source review: implementation revision `a0ea5e7b2048dc8fe97b43c83f29c64af0fc00a1`. Results are summarized from the implementation ledger and retained local test artifacts, not recreated by this documentation task.

| Layer | Recorded evidence | Interpretation |
|---|---|---|
| iPhone build 11 controls | `Release11PhoneRedeployControls` and `Release11PhoneFinalControls`: one UI test passed in each run | Pause, seek, restart, resume and dismissal; not exhaustive format or AirPlay/PiP coverage |
| Mac unit suite | 70 passed; two opt-in skips | Unit-level behavior; skips are not passes |
| Mac direct mouse check | Pause at 19 s; forward to 49 s; restart to 0; resume; 1.5x selected | Direct UI verification after session and audio fixes |
| Mac automated UI | Initial failures; final `MacMouseControls` interrupted by floating ChatGPT dialog | Uninterrupted automated acceptance remains open |
| Mac local installation | Signed Catalyst app; strict signature and binary boundary checks passed | Local development delivery only |
| Physical short media playback | Prior September 5 iPhone, iPad and TV samples advanced beyond 8 s and resumed beyond 38 s | Earlier sample proof, not acceptance of every later controls change |
| Household services | iPhone/iPad Mealie and Home Assistant opened real content with NetBird off over Wi-Fi | Does not prove cellular, first off-network enrollment or long-duration renewal |
| TV household views | Native recipes, household states and remote Back passed | No household devices actuated during checks |
| Automatic provider setup | Server/live checks and physical iPhone setup passed | iPad acceptance remains open |
| Build 11 archives | Earlier source archives succeeded | Refresh from final source before upload |
| TestFlight | Build 9 last recorded as available | No build 11 upload claimed |

Traceability: [revision-pinned implementation ledger](https://github.com/Morlock52/morlocksmaze-media/blob/a0ea5e7b2048dc8fe97b43c83f29c64af0fc00a1/docs/redesign/2026-09-05/IMPLEMENTATION_LEDGER.md) (private repository; access required). Raw `.xcresult` bundles are retained locally and are not included in this public publication.

## Version chronology

| Edition / milestone | Change | Delivery state at this checkpoint |
|---|---|---|
| Earlier iterations, including build 8 | Native redesign, collection navigation and playback recovery work | Historical context; no complete screenshot archive reproduced here |
| 1.0.0 (9) | Last recorded internal TestFlight baseline | Release baseline |
| Development build 10 | Dedicated service access, household views and automatic provider setup | Development milestone; superseded candidate |
| Development build 11 | Shared controls panel, transport options, scoped platform fixes and Mac Catalyst delivery | iPhone installed; Mac installed locally; release checks remain open |

The four platform editions share the product version where applicable. iPhone and iPad share an iOS target; the Mac uses Catalyst from that target; Apple TV has its own native target. “Four editions” does not mean four independently released App Store products.


## Build 13 — Brass Labyrinth

September 6, 2026: iOS and tvOS build 13 are **Testing** for MorloksMaze Internal. The same theme is installed locally across iPhone, iPad, Mac and Apple TV. [Theme verification](../13-brass-labyrinth/VERIFICATION.md) records tests, skips, the Mac warning and the locked iPhone interaction limit. Earlier entries remain dated historical checkpoints.


## September 7, 2026 — Build 17 candidate

[Current test results, reviewed captures and remaining release gates](build-17/README.md). This dated checkpoint supersedes earlier release assumptions without treating historical device checks as current acceptance.
