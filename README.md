# 💊 Inpatient Pharmacy Workload & Burnout Risk Predictor

**Presented by: Jerrika Washington**

A command-line tool that analyzes inpatient pharmacy shift workload and predicts burnout risk — helping pharmacy leadership make proactive staffing decisions before conditions become critical.

---

## 🔍 The Problem

Inpatient pharmacy staff frequently face excessive workloads that cascade into serious operational and human consequences:

- High workload → fatigue and burnout
- Burnout → unscheduled call-outs and absences
- Call-outs → even greater workload for remaining staff

This tool was created to break that cycle by providing data-driven risk assessment at the start of every shift.

---

## 🧠 What It Does

The **Pharmacy Workload Risk Analyzer** evaluates shift conditions using key staffing and order data to generate a workload score and a corresponding risk level. It then provides actionable recommendations to pharmacy managers and leadership.

**Risk Levels:**

| Score Range | Risk Level | Action |
|-------------|------------|--------|
| < 8         | 🟢 Low      | Continue normal operations |
| 8 – 14.99   | 🟡 Moderate | Monitor staff; consider redistributing tasks |
| 15 – 21.99  | 🟠 High     | Add support, adjust breaks, reduce non-urgent load |
| ≥ 22        | 🔴 Critical | Immediate action: add staff, notify leadership |

---

## ⚙️ How It Works

The analyzer calculates a **workload score** using:

```
Weighted Orders = Total Orders + (STAT Orders × 1.5)
Workload Score  = Weighted Orders ÷ (Staff × Hours)
```

STAT (urgent) orders are weighted 1.5× because they require immediate attention and consume more pharmacist bandwidth than routine orders.

---

## 🚀 How to Use

### Requirements

- Python 3.x (no external libraries required)

### Run the Program

```bash
python pharmacy_workload_risk_analyzer.py
```

### Main Menu

```
==============================
Pharmacy Workload Risk Analyzer
==============================
1. Run Workload Analyzer
2. View Sample Demo
3. Exit
```

**Option 1 – Run Workload Analyzer:** Enter your shift's data interactively:
- Shift name (Day, Evening, Night)
- Total pharmacy orders
- Number of STAT/urgent orders
- Number of staff on shift
- Shift length in hours

Results display immediately. You'll be prompted to optionally save results to a CSV file.

**Option 2 – Sample Demo:** Runs a preset Evening shift scenario (320 orders, 45 STAT, 4 staff, 8 hours) so you can see the analyzer in action without entering data.

---

## 💾 Saving Results

When prompted after analysis, enter `yes` to save your results to `pharmacy_workload_results.csv`. The file is created automatically if it doesn't exist. Each entry includes:

- Date/Time
- Shift name
- Total & STAT orders
- Staffing count and hours
- Workload score
- Risk level
- Recommendation

This allows leadership to track trends across shifts over time.

---

## 📊 Example Output

```
--- Analysis Results ---
Shift: Evening
Total Orders: 320
STAT Orders: 45
Staff Working: 4
Shift Length: 8.0 hours
Workload Score: 12.11
Risk Level: Moderate
Recommendation: Monitor staff closely and consider redistributing tasks.
```

---

## 🔮 Future Potential

- Pull prior-shift data automatically from pharmacy systems
- Integrate nursing unit data and patient chart information to anticipate pharmacy demand before a shift begins
- Dashboard visualization of historical risk trends
- Automated alerts to leadership when critical thresholds are met

---

## 👩‍⚕️ About This Project

This tool was developed as part of a broader initiative to address pharmacy staff burnout in inpatient settings. By surfacing workload risk early — before a shift reaches critical conditions — pharmacy teams can make smarter staffing decisions and protect both their staff and their patients.

---

## 📄 License

This project is open for educational and clinical improvement use. Please credit the original author when adapting or sharing.
