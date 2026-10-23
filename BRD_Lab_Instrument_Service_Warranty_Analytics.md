# Business Requirements Document (BRD)
## Lab Instrument Service & Warranty Analytics

---

## 1. Executive Summary

**Project Name:** Lab Instrument Service & Warranty Analytics (LISWA)  
**Objective:** Reduce SLA breach rates, repair turnaround time, and repeat ticket frequency for laboratory instruments across regions by implementing data-driven service improvements.

**Key Finding:** Current SLA breach rate is **59.7%** across 2,000 service tickets, with certain instruments (Mass Spectrometer: 85%, Sequencer: 82%) and regions (Latin America: 81%, India: 80%) showing critical performance gaps.

**Proposed Impact:** Targeted improvements (specialist pre-routing, regional parts pre-stocking, calibration fast-track, post-repair verification) can reduce breach rate by an estimated 25–35% and cut repeat ticket costs by ~$25K–$50K annually.

---

## 2. Business Problem Statement

### Current State (As-Is)
- **SLA Breach Rate:** 59.7% of all service tickets exceed target resolution times
  - Hardware issues: 48-hour SLA → actual MTTR 55.6 hours (breach when delayed)
  - Software issues: 24-hour SLA → similar overrun patterns
  - Calibration issues: 72-hour SLA → MTTR 88.5 hours (highest variance)

- **Root Causes Identified:**
  1. Technician specialty mismatch (generalist responders → wrong first-touch resolution)
  2. Regional parts shortages (Latin America, India lack local inventory)
  3. Calibration bottleneck (shared queue, no priority lane)
  4. Lack of post-repair verification (repeat-ticket rate: 9.35%)

- **Cost Impact:**
  - Repeat tickets alone: 187 of 2,000 (9.35%) costing ~$99,217 in rework
  - Extended resolution → customer dissatisfaction, warranty claims

### Desired State (To-Be)
- SLA breach rate reduced to **40–45%** (25–35% improvement)
- MTTR lowered by 10–15 hours across all categories
- Repeat ticket rate cut to **5%** or lower (~$50K+ savings)
- Service quality and customer confidence restored

---

## 3. Stakeholders

| Stakeholder | Role | Power | Interest | Engagement |
|---|---|---|---|---|
| **Regional Service Manager** | Owns regional team performance, SLA targets | High | High | Daily KPI reviews, feedback loops |
| **Finance/CFO** | Budget allocation, cost-benefit sign-off | High | High | Investment case, ROI tracking |
| **Field Technicians** | Execute repairs, handle escalations | Medium | High | Training on routing, tools, checklists |
| **Logistics/Supply Chain** | Manage parts inventory, procurement | Medium | High | Parts pre-positioning, inventory rules |
| **Calibration Specialist** | Handles calibration-tier repairs | Medium | High | Process changes, workload smoothing |
| **Customer Support** | First point of contact, escalation routing | Medium | Medium | Triage rules, SLA communication |

---

## 4. Functional Requirements

### **FR-1: Specialist Pre-Routing at Triage**
- **Description:** Route tickets to specialists (Mass Spec expert, Sequencer expert, etc.) at intake based on instrument type, not random generalist assignment.
- **Business Value:** Reduces first-touch failure, cuts repeat tickets, improves MTTR.
- **Success Metric:** First-contact resolution rate ↑ from ~70% to ~85%; repeat-ticket rate ↓ by 20%.
- **Technical Input:** Ticket classification by issue type + skill matrix in Jira.

### **FR-2: Regional Parts Pre-Stocking**
- **Description:** Establish regional parts caches in Latin America and India (highest delay regions) for common wear items (calibration standards, filter cartridges, detector modules, seals).
- **Business Value:** Eliminates parts-wait delays (currently 5–10 hours per ticket in high-risk regions).
- **Success Metric:** Regional MTTR ↓ by 8–12 hours; regional breach rate ↓ by 15–20%.
- **Technical Input:** Inventory tracking, lead-time forecasting, stock-out alerts.

### **FR-3: Calibration Fast-Track Lane**
- **Description:** Separate calibration tickets from general repair queue; prioritize with shorter SLA (48 hours instead of 72 hours) and dedicated resource.
- **Business Value:** Calibration MTTR currently 88.5 h → target 60 h; reduce queue wait variance.
- **Success Metric:** Calibration SLA breach rate ↓ from ~70% to ~40%; MTTR −25–30 hours.
- **Technical Input:** Jira workflow swim lane, dedicated sprint capacity, scheduling rules.

### **FR-4: Mandatory Post-Repair Verification Checklist**
- **Description:** Implement automated checklist in service platform before ticket closure; technician must confirm repair, run diagnostics, document outcome.
- **Business Value:** Catches incomplete fixes before customer escalation; reduces repeat tickets.
- **Success Metric:** Repeat-ticket rate ↓ from 9.35% to ~5%; post-repair rework cost ↓ ~50%.
- **Technical Input:** Closure workflow gate, compliance tracking, audit trail.

---

## 5. Non-Functional Requirements

| Requirement | Specification |
|---|---|
| **Availability** | Service system must support real-time ticket routing (no batch delays). |
| **Scalability** | Solution must handle growth from 2,000 → 5,000+ tickets/year without performance degradation. |
| **Usability** | Technicians and dispatchers complete routing/verification in <2 minutes per ticket. |
| **Data Accuracy** | SLA calculations and MTTR metrics must match actual ticket timelines (audit trail). |
| **Security** | Customer PII and warranty data encrypted; role-based access (dispatch, tech, finance). |

---

## 6. As-Is / To-Be Process

### As-Is (Current Workflow)
```
Ticket Created → Generic Queue → Random Tech Assignment → Repair Attempt 
→ Closure → (If Incomplete) Repeat Ticket → More Delay & Cost
```

**Pain Points:**
- Tech may lack specialized knowledge → rework required.
- Parts sourcing delays, especially in remote regions.
- Calibration mixed with general queue → variable turnaround.
- No verification gate → incomplete repairs slip through.

### To-Be (Proposed Workflow)
```
Ticket Created → Triage (by Instrument Type) → Specialist Assignment (FR-1)
→ Parts Check (Pre-positioned Inventory, FR-2)
→ Repair + Calibration Fast-Track if Needed (FR-3)
→ Post-Repair Verification Checklist (FR-4)
→ Closure → Lower Repeat Rate
```

**Gains:**
- Specialist match → higher first-touch success.
- Local parts availability → faster resolution.
- Calibration priority → consistent SLA.
- Verification gate → fewer repeat tickets, lower cost.

---

## 7. Key Metrics & Success Criteria

| Metric | Current | Target | Measurement |
|---|---|---|---|
| **SLA Breach Rate** | 59.7% | 40–45% | % of tickets > SLA target |
| **Mean Time To Resolution (MTTR)** | 55.6 h (Hardware) | 45–50 h | Avg time from open to close |
| **Repeat-Ticket Rate** | 9.35% | ≤ 5% | Repeat tickets / Total tickets |
| **Cost per Ticket** | $506 | $450–480 | Total cost / ticket count |
| **First-Touch Resolution** | ~70% | ~85% | No escalation / rework needed |
| **Regional MTTR (Latin America, India)** | 80+ h | 60–70 h | Avg time in high-delay regions |
| **Calibration MTTR** | 88.5 h | 60 h | Calibration ticket resolution time |

---

## 8. Cost-Benefit Analysis

### Investment Required (Estimated)
- **Specialist Training & Skill Mapping:** $15K
- **Regional Parts Pre-Stocking (Initial Purchase):** $40K
- **Jira Workflow & Dashboard Setup:** $10K
- **Post-Repair Checklist Tool Implementation:** $5K
- **Total Initial Investment:** ~$70K

### Benefits (Annual, 2-Year Horizon)
- **Repeat-Ticket Cost Reduction:** $25K–$50K (187 repeat tickets → ~90–95 repeat)
- **MTTR Improvement → Faster Closeout:** $30K–$40K (better cash flow, higher capacity utilization)
- **Reduced Escalations & Warranty Claims:** $20K–$30K (fewer customer complaints)
- **Total Annual Benefit:** ~$75K–$120K
- **Payback Period:** 7–11 months

### ROI
- **Year 1:** ~60–100% ROI (partial implementation ramp)
- **Year 2:** ~100–150% ROI (full optimization, compounding efficiency gains)

---

## 9. Assumptions & Constraints

### Assumptions
1. Technician availability and willingness to specialize (training investment assumed).
2. Supplier can deliver regional pre-stock within 2 weeks of order.
3. Jira integration with inventory system is feasible.
4. No significant change in overall ticket volume (2,000/year baseline).

### Constraints
1. Budget cap: $100K for implementation.
2. Timeline: 3–4 months to full deployment (training + rollout phases).
3. Regional legal/regulatory requirements for parts storage (customs, licensing).
4. Technician certification required for certain instruments (e.g., calibration specialists).

---

## 10. Risk & Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| **Specialist Training Overruns** | Timeline delay | Start training 4 weeks before rollout; use external trainers. |
| **Regional Parts Stockout** | Partially defeats FR-2 | Establish reorder triggers; dual-supplier agreements. |
| **Technician Resistance** | Adoption failure | Involve techs early; show MTTR improvements & workload benefits. |
| **Jira Workflow Bugs** | Routing failures | Pilot in one region for 2 weeks; iterative fixes before full rollout. |
| **Data Quality Issues** | Inaccurate SLA metrics | Audit ticket logs weekly; reconcile with CRM records. |

---

## 11. Implementation Roadmap

### Phase 1: Discovery & Planning (Weeks 1–2)
- Finalize specialist skill matrix.
- Identify regional parts catalog and suppliers.
- Configure Jira workflows.

### Phase 2: Pilot & Training (Weeks 3–6)
- Train specialist team on new routing and triage rules.
- Establish regional parts cache (Latin America + India).
- Test Jira workflow with 5–10% of tickets.

### Phase 3: Rollout (Weeks 7–12)
- Full deployment of FR-1, FR-2, FR-3, FR-4.
- Monitor KPIs daily; adjust rules as needed.
- Provide ongoing support and re-training.

### Phase 4: Optimization (Week 13+)
- Analyze lessons learned; refine specialist assignments.
- Rebalance regional inventory based on actual ticket patterns.
- Plan next-phase improvements (e.g., predictive maintenance).

---

## 12. Approval & Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| **Business Sponsor** | Regional Service Manager | _____________ | _______ |
| **Finance Approver** | CFO / Finance Lead | _____________ | _______ |
| **Technical Lead** | Service Platform Owner | _____________ | _______ |
| **Project Manager** | LISWA PMO | _____________ | _______ |

---

## Appendices

### Appendix A: Instrument & Region Profiles
- **Instruments:** Mass Spectrometer (85% breach), Sequencer (82%), PCR Analyzer (52%), Chromatograph (58%), Microscope (38%)
- **Regions:** Latin America (81% breach, 1.4x delay factor), India (80%, 1.3x), Europe (56%, 1.0x), North America (51%, 0.9x), APAC (59%, 1.1x)

### Appendix B: Dataset Source
- **Simulated Data:** 2,000 field-service tickets (pandas/numpy, seed 42)
- **Distributions:** Normal (MTTR), Bernoulli (SLA breach), Uniform (cost variance)
- **Validation:** Root-cause analysis pivot tables; MTTR & repeat-rate benchmarking

### Appendix C: Glossary
- **SLA:** Service Level Agreement (target resolution time by issue type)
- **MTTR:** Mean Time To Resolution (avg hours from ticket open to close)
- **Repeat Ticket:** Ticket reopened for same customer/instrument within 30 days
- **Breach:** Actual MTTR exceeds SLA target
- **First-Touch Resolution:** Ticket resolved in one attempt, no escalation

---

**Document Version:** 1.0  
**Last Updated:** 2026-10-23  
**Author:** Shalwin Joel Lewis  
**Project:** LISWA (Jira Key: LISWA)  
**Status:** Final