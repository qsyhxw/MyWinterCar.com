# Page Roadmap

Last updated: 2026-09-29
Execution mode: `ANALYZE_AND_IMPLEMENT` / `ROLLING_28D` / `OPERATING_REVIEW`
Property: `sc-domain:mywintercar.com`

## 2026-09-29 monthly operating review scope

- Comparison: 2026-08-30–2026-09-26 versus 2026-08-02–2026-08-29. September 26 is the latest final row returned by the API; the later completeness boundary is not exposed.
- Baseline: 10 clicks / 560 impressions / 1.79% CTR / 39.57 position versus 10 / 1,147 / 0.87% / 32.63. Clicks held, but impressions fell 51.2% and average position weakened by 6.93.
- Deployment review: the live copies of `/troubleshooting-guide`, `/corris-rivett-guide`, `/patch-notes`, `/vehicles-guide`, and `/survival-guide` match the current repository content. The September 9 work is deployed, not waiting in Git.
- Guardrails: preserve winner TDK; prefer local answer corrections; no URL removal or merge, redirect, noindex/canonical migration, homepage redesign, or ad-account action.
- Repository checkpoint: `main` at `46340ed`, matching `origin/main` before this review.

| Review queue | Bucket | URL | Evidence / answer gap | Authorized action | State |
|---|---|---|---|---|---|
| 2026-09-PATCH | RECOVER | `/patch-notes` | Page still calls v.260102-01 latest; official update v.260917-01 changes starting, phone, controller and vehicle-part behavior | Update body, timeline and status corrections; preserve title, meta, H1 and canonical | READY |
| 2026-09-TROUBLE | RECOVER | `/troubleshooting-guide` | 1 click / 34 impressions versus 4 / 236; September 17 changed carb cranking, evening calls and Logitech pedal assignment | Add patch-aware diagnosis locally; preserve title, meta, H1 and canonical | READY |
| 2026-09-RIVETT | PROTECT | `/corris-rivett-guide` | New 2 clicks / 32 impressions at 8.38 position; current answer still ties choke to the lower dash and gives pre-update crank timing | Correct only version-sensitive starting details; preserve all TDK | READY |
| 2026-09-MAP | GROW | `/map-guide` | `my winter car map` gained 18 impressions but Google returned the homepage at position 62; dedicated page is indexable and in the sitemap | Hold content/TDK until query ownership and indexing evidence are clearer | MONITOR |
| 2026-09-HOME | PROTECT | `/` | 5 of 10 clicks and 358 of 560 impressions; clicks rose while impressions and position weakened | Preserve TDK and page structure; no edit this cycle | HOLD |

The query-page export is a visible-query subset (7 clicks / 232 impressions in the current window), so it is not added to the site totals. Homepage concentration is high: 50% of site clicks and 63.9% of site impressions; the top three pages account for 80% of clicks.

| Queue | URL | File | Intent | Status | Parent / inbound route | Next step | Evidence prerequisite |
|---|---|---|---|---|---|---|---|
| P1-1 | `/survival-guide` | `survival-guide.html` | Broad survival, body temperature, fatigue, stress and Problem Bar | PUBLISHED | `/`, `/guides`, `/beginner-guide` | `/sleep-guide` | Recheck final CTR, survival query share and sleep handoff at 28/56/90 days |
| P1-2 | `/sleep-guide` | `sleep-guide.html` | Can't-sleep and missing sleep prompt troubleshooting | PUBLISHED | `/faq`, `/survival-guide`, `/beginner-guide` | `/troubleshooting-guide` | Recheck sleep query share and version-sensitive sleep claims |
| P1-3 | `/corris-rivett-guide` | `corris-rivett-guide.html` | Corris Rivett buy, build, wire and first start | PUBLISHED | `/`, `/engine-build-guide`, `/parts-acquisition-guide` | `/wiki` | Recheck build query CTR and first-start ownership |
| P2-1 | `/wiki` | `wiki.html` | Reference database and fact index | PUBLISHED | `/`, `/car-build-guide`, `/release-date` | `/troubleshooting-guide` | Recheck database query share and homepage protection |
| P2-2 | `/troubleshooting-guide` | `troubleshooting-guide.html` | Car won't start, ignition, phone and bug diagnosis | PUBLISHED | `/`, `/engine-build-guide`, `/sleep-guide` | `/beginner-guide` | Recheck symptom query CTR and sleep delegation |
| P2-3 | `/beginner-guide` | `beginner-guide.html` | First 30 minutes and first-day checklist | PUBLISHED | `/`, `/guides`, `/faq` | `/vehicles-guide` | Recheck first-day query CTR and sleep/save handoff |
| P2-4 | `/vehicles-guide` | `vehicles-guide.html` | Vehicle roles, acquisition, specs and uses | PUBLISHED | `/`, `/guides`, `/wiki` | `NONE - RETURN TO GSC EXPANSION REVIEW` | Recheck vehicle query impressions and position |

Status is updated only after the page passes local validation and its dedicated git commit is pushed. No new page, 301, canonical migration or bulk noindex action is approved in this queue.

## Change log

| Date | Queue | Result | Commit | Live verification |
|---|---|---|---|---|
| 2026-09-29 | Monthly review scope | Rolling windows, deployment feedback and implementation guardrails recorded before edits | PENDING | Not applicable |
