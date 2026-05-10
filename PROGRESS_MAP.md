# 🗺️ Project Progress Map

## Inpatient Pharmacy Workload & Burnout Risk Predictor

**Author:** Jerrika Washington
**Last Updated:** 2025

---

## 📍 Project Phases

```
PHASE 1          PHASE 2          PHASE 3          PHASE 4
[COMPLETE]       [COMPLETE]       [IN PROGRESS]    [PLANNED]
   │                │                │                │
Problem          Core Tool        Validation       Integration
Framing    ───▶  Built      ───▶  & Testing  ───▶  & Expansion
```

---

## ✅ Phase 1 — Problem Framing (Complete)

- [x] Identified the burnout cycle in inpatient pharmacy settings
- [x] Defined core contributing factors: order volume, STAT urgency, staffing levels, shift length
- [x] Researched connection between workload score and burnout risk
- [x] Established four-tier risk classification framework (Low / Moderate / High / Critical)
- [x] Presented problem and proposed solution (see PowerPoint deck)

---

## ✅ Phase 2 — Core Tool Development (Complete)

- [x] Built command-line workload risk analyzer in Python
- [x] Implemented weighted order calculation (STAT orders × 1.5)
- [x] Implemented `calculate_workload_score()` function
- [x] Implemented `determine_risk()` with four-tier classification
- [x] Implemented `generate_recommendation()` with actionable guidance
- [x] Built CSV logging via `save_to_csv()` for shift-over-shift tracking
- [x] Built interactive menu with run, demo, and exit options
- [x] Included sample demo scenario for quick testing
- [x] Added input validation (prevents division by zero, invalid staffing)

---

## 🔄 Phase 3 — Validation & Testing (In Progress)

- [ ] Test with real-world pharmacy shift data
- [ ] Validate score thresholds against observed burnout outcomes
- [ ] Refine STAT order weighting factor (currently 1.5×)
- [ ] Gather feedback from pharmacy staff and leadership
- [ ] Document edge cases (short shifts, skeleton crews, etc.)
- [ ] Consider shift-type weighting (Night shifts may need adjusted thresholds)

---

## 🗓️ Phase 4 — Integration & Expansion (Planned)

### Data Integration
- [ ] Connect to pharmacy information systems (e.g., Omnicell, Epic, Pyxis)
- [ ] Pull prior-shift order data automatically
- [ ] Ingest nursing unit patient data to forecast pharmacy demand pre-shift

### Feature Enhancements
- [ ] Add burnout trend tracking across multiple shifts per staff member
- [ ] Build scheduling recommendations based on predicted risk
- [ ] Add historical comparison ("this shift vs. 30-day average")
- [ ] Support for multiple pharmacy locations / units

### Interface
- [ ] Build web-based dashboard (Flask or Django)
- [ ] Visual charts for risk trends over time
- [ ] Role-based access: staff view vs. leadership view

### Alerts
- [ ] Automated email/text alerts when Critical threshold is reached
- [ ] Pre-shift risk forecast delivered to charge pharmacist

---

## 🧮 Core Algorithm (Reference)

```
Weighted Orders  =  Total Orders + (STAT Orders × 1.5)
Workload Score   =  Weighted Orders ÷ (Staff Count × Shift Hours)

Score < 8   →  🟢 Low       — Normal operations
Score < 15  →  🟡 Moderate  — Monitor and redistribute
Score < 22  →  🟠 High      — Add support, adjust workload
Score ≥ 22  →  🔴 Critical  — Immediate intervention required
```

---

## 📁 File Structure

```
pharmacy_workload_risk_analyzer/
│
├── pharmacy_workload_risk_analyzer.py   # Main program
├── pharmacy_workload_results.csv        # Auto-generated results log
├── README.md                            # Project overview
├── PROGRESS_MAP.md                      # This file
└── presentation/
    └── Inpatient_Pharmacy_Workload_Burnout_Risk_Predictor.pptx
```

---

## 📬 Contact

For questions, collaboration, or feedback, please open a GitHub issue or reach out directly via the repository.
