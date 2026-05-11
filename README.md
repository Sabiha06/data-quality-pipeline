# Healthcare Data Quality Pipeline

## Overview

This project demonstrates a data quality pipeline applied to a healthcare dataset.
The dataset contains common real-world data issues such as missing values, invalid entries, and duplicate records.

---

## Dataset

A synthetic healthcare dataset was created to simulate real-world data quality challenges, including:

* Missing values
* Invalid age values
* Incorrect email formats
* Duplicate patient records

---

## Sample Input Data

| Name | Age | Email |
|---|---|---|
| Alice | 25 | alice@email.com |
| Bob |  | bobemail.com |
| Charlie | 150 | charlie@email.com |
| Alice | 25 | alice@email.com |
| David | 30 |  |
| Eve | 28 | eve@email.com |

The dataset intentionally contains:
- Missing values
- Invalid email formats
- Duplicate records
- Unrealistic age values

## Features

* Data cleaning and preprocessing using Python (Pandas)
* Missing value detection
* Duplicate record removal
* Data validation (age, email, required fields)
* Automated data quality reporting

---

## Validation Checks

The pipeline performs the following validation steps:

| Validation Check | Purpose |
|---|---|
| Missing value detection | Identify incomplete records |
| Duplicate detection | Remove repeated records |
| Email format validation | Detect malformed email addresses |
| Age range validation | Remove unrealistic age values |
| Column standardization | Improve data consistency |

## Tools Used

* Python
* Pandas

---

## Project Structure
> This shows the organization of files in the project.
```
data-quality-project/
│── data/
│   └── raw_data.csv
│── src/
│   └── data_cleaning.py
│── output/
│   ├── cleaned_data.csv
│   └── quality_report.txt
│── README.md
```

## Output

* Cleaned dataset: `cleaned_data.csv`
* Data quality report: `quality_report.txt`

---

## Results

The pipeline successfully identified and corrected:

| Check | Result |
|---|---|
| Missing values found | 2 |
| Duplicate rows removed | 1 |
| Invalid emails detected | 1 |
| Invalid age records removed | 1 |

This improved overall data consistency and reliability for downstream analysis.

## Future Work

* Entity resolution (detecting similar patient records)
* Advanced data validation rules
* Integration with real-world healthcare datasets

---
## Workflow

Raw Dataset
   ↓
Data Validation
   ↓
Data Cleaning
   ↓
Duplicate Removal
   ↓
Quality Reporting
   ↓
Cleaned Dataset
