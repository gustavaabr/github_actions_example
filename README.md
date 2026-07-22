# GitHub Actions Example

**Purpose:** A learning project for trying out GitHub Actions.

An automated ETL-project (Extract, Transform, Load). The script automatically gets news from an open API, cleans the data, and saves it systematically using GitHub Actions.

## Tech Stack
* **Python** (Core logic)
* **Requests** (Fetching data via API)
* **Pandas** (Data processing and cleaning)
* **GitHub Actions** (Cloud automation and operations)

## 📁 Project Structure
```text
├── .github/
│   └── workflows/
│       └── daily_run.yml    # Workflow configuration
├── data/                    # Automatically generated CSV files
├── pipeline.py              # The primary Python script
└── requirements.txt         # Project dependencies
