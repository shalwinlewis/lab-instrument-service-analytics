# Requirements Traceability Matrix (RTM)
## Lab Instrument Service & Warranty Analytics

This matrix traces each proposed functional requirement back to its business objective and root cause, and forward to the design artifact and validation criteria used to confirm it addresses the issue.

| Req ID | Requirement Description | Business Objective | Source (Root Cause) | Design / Process Artifact | Validation / Test Criteria | Status |
|---|---|---|---|---|---|---|
| **FR-1** | At triage, tickets for complex instruments (Mass Spectrometer, Sequencer) must be flagged and routed directly to specialist-certified engineers | Reduce SLA breach rate | Mass Spectrometer/Sequencer tickets show 82–98% breach rate, driven by late specialist escalation | To-Be process diagram — "Specialist pre-routing" node inserted after Triage stage | Post-implementation: breach rate for Mass Spec/Sequencer tickets should trend toward the overall average (~60%); tracked via the Instrument × Region heatmap in the dashboard | Proposed |
| **FR-2** | Top-failure replacement parts must be pre-stocked at regional service centers in Latin America and India | Reduce MTTR and SLA breach rate | Latin America/India regions show 78–81% breach rate, linked to parts-logistics delays | To-Be process diagram — "Regional parts pre-stock" node inserted before Repair Execution | Post-implementation: regional MTTR and breach rate should drop toward the global average; tracked via "SLA Breach Rate by Region" chart | Proposed |
| **FR-3** | Calibration tickets must be routed to a separate fast-track workflow with its own SLA tier | Reduce MTTR | Calibration tickets have the highest MTTR (88.5 hrs) despite lower technical complexity, due to no dedicated workflow | To-Be process diagram — "Calibration fast-track" node inserted at the Diagnosis stage | Post-implementation: Calibration MTTR should drop below Hardware/Software MTTR; tracked via "MTTR by Issue Category" chart | Proposed |
| **FR-4** | A mandatory post-repair verification checklist must be completed before a ticket can be marked resolved, particularly for high-repeat-risk instrument types | Reduce repeat-ticket rate | 9.3% repeat-ticket rate, concentrated in high-breach segments, suggesting rushed repairs | To-Be process diagram — "Verification checklist" node inserted before Resolution Sign-off | Post-implementation: repeat-ticket rate should drop from the 9.3% baseline; tracked via the dashboard's repeat-ticket KPI card | Proposed |

## Notes

- All requirements are currently **Proposed** rather than Implemented, as this is a self-directed portfolio project analyzing simulated data rather than a live production rollout.
- Each requirement is directly traceable to one dashboard visual, which would be used to validate its impact if implemented — this closes the loop between finding a root cause, proposing a fix, and measuring whether the fix worked.
- See [`BRD_Lab_Instrument_Service_Warranty_Analytics.md`](./BRD_Lab_Instrument_Service_Warranty_Analytics.md) for the full business case behind each requirement.