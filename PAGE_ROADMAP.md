# Page Roadmap

Last updated: 2026-09-09  
Execution mode: GSC_SPEC_HANDOFF via `03A-分页快速创建提示词.md`  
Property: `sc-domain:mywintercar.com`

| Queue | URL | File | Intent | Status | Parent / inbound route | Next step | Evidence prerequisite |
|---|---|---|---|---|---|---|---|
| P1-1 | `/survival-guide` | `survival-guide.html` | Broad survival, body temperature, fatigue, stress and Problem Bar | PUBLISHED | `/`, `/guides`, `/beginner-guide` | `/sleep-guide` | Recheck final CTR, survival query share and sleep handoff at 28/56/90 days |
| P1-2 | `/sleep-guide` | `sleep-guide.html` | Can't-sleep and missing sleep prompt troubleshooting | PUBLISHED | `/faq`, `/survival-guide`, `/beginner-guide` | `/troubleshooting-guide` | Recheck sleep query share and version-sensitive sleep claims |
| P1-3 | `/corris-rivett-guide` | `corris-rivett-guide.html` | Corris Rivett buy, build, wire and first start | PUBLISHED | `/`, `/engine-build-guide`, `/parts-acquisition-guide` | `/wiki` | Recheck build query CTR and first-start ownership |
| P2-1 | `/wiki` | `wiki.html` | Reference database and fact index | PUBLISHED | `/`, `/car-build-guide`, `/release-date` | `/troubleshooting-guide` | Recheck database query share and homepage protection |
| P2-2 | `/troubleshooting-guide` | `troubleshooting-guide.html` | Car won't start, ignition, phone and bug diagnosis | PUBLISHED | `/`, `/engine-build-guide`, `/sleep-guide` | `/beginner-guide` | Recheck symptom query CTR and sleep delegation |
| P2-3 | `/beginner-guide` | `beginner-guide.html` | First 30 minutes and first-day checklist | PUBLISHED | `/`, `/guides`, `/faq` | `/vehicles-guide` | Recheck first-day query CTR and sleep/save handoff |
| P2-4 | `/vehicles-guide` | `vehicles-guide.html` | Vehicle roles, acquisition, specs and uses | QUEUED | `/`, `/guides`, `/wiki` | `NONE - RETURN TO GSC EXPANSION REVIEW` | Recheck vehicle query impressions and position |

Status is updated only after the page passes local validation and its dedicated git commit is pushed. No new page, 301, canonical migration or bulk noindex action is approved in this queue.
