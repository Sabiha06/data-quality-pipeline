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

## Features

* Data cleaning and preprocessing using Python (Pandas)
* Missing value detection
* Duplicate record removal
* Data validation (age, email, required fields)
* Automated data quality reporting

---

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

---

## Output

* Cleaned dataset: `cleaned_data.csv`
* Data quality report: `quality_report.txt`

---

## Results
The pipeline successfully identified and corrected:
- Missing values across multiple fields
- Invalid records (e.g., unrealistic ages, malformed emails)
- Duplicate patient entries

These steps enhanced data consistency, reliability, and usability for downstream analysis.

## Future Work

* Entity resolution (detecting similar patient records)
* Advanced data validation rules
* Integration with real-world healthcare datasets

---

## Author

Sabiha

