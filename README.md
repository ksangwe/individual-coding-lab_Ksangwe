# Individual Coding Lab - Grade Evaluator

## 📌 Project Overview
This project is a Grade Evaluation System developed in Python with a supporting Bash script.  
It reads student grades from a CSV file, validates the data, calculates GPA, determines pass/fail status, and handles resubmission logic.

---

## 🚀 Features

### Python Program (grade-evaluator.py)
- Reads grades from `grades.csv`
- Validates scores (must be between 0 and 100)
- Validates category weights:
  - Formative = 60%
  - Summative = 40%
  - Total = 100%
- Calculates total score
- Computes GPA (scale of 5.0)
- Determines PASS/FAIL status (must pass both categories)
- Identifies assignments eligible for resubmission

---

### Bash Script (organizer.sh)
- Archives `grades.csv` into an archive folder
- Adds timestamp to archived files
- Creates a new empty `grades.csv`
- Logs all archive actions in `organizer.log`

---

## 📂 Files Included
- grade-evaluator.py
- organizer.sh
- grades.csv
- README.md

---

## ▶️ How to Run

### Run Python program:
```bash
python3 grade-evaluator.py
