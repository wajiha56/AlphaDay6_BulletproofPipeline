# 🏗️ AlphaDay6: Bulletproof Sales Data Pipeline

This repository contains a **production-ready automated data pipeline** built in Python.  
It demonstrates **reliable ETL workflows, data validation, database integration, and automated reporting**, perfect for portfolio showcasing and freelance projects.

---

## 🚀 Project Overview

In the real world, sales data is often messy – missing values, duplicate records, or inconsistent formats.  
This pipeline **automatically cleans, validates, and loads the data into a structured SQLite database**, while generating visual insights and logging each run.  

Key Features:  
- **Data Validation:** Handles missing Sales/Quantity and removes duplicate Order_IDs  
- **Database Integration:** Loads cleaned data into `Alpha_Data_Warehouse.db` for optimized querying  
- **Audit Logging:** Every pipeline run is logged with timestamp in `pipeline_log.txt`  
- **Automated Visualization:** Generates a profit bar chart (`Automated_Profit_Report.png`) showing top-performing categories  

---

## 📁 Folder Structure
AlphaDay6_Pipeline/
├─ AlphaDay6_MasterPipeline.py # Main ETL pipeline script
├─ sales_data.csv # Raw CSV input data
├─ Alpha_Data_Warehouse.db # SQLite database
├─ pipeline_log.txt # Execution log file
├─ Automated_Profit_Report.png # Generated profit chart
└─ README.md # This file


---

## ⚙️ How It Works

1. **CSV Detection:** Script searches for `sales_data.csv` in the folder.  
2. **Data Validation & Cleaning:**  
   - Fill missing `Sales` and `Quantity` with the column mean  
   - Remove duplicate `Order_ID` entries  
3. **Database Storage:** Cleaned data is appended to the `Weekly_Sales` table in `Alpha_Data_Warehouse.db`  
4. **Automated Chart Generation:** Creates a bar chart showing total profit by category  
5. **Pipeline Logging:** Records each successful run in `pipeline_log.txt`  

---

## 🧩 Key Technical Highlights

- **Python Libraries:** pandas, sqlite3, matplotlib, datetime, os  
- **ETL Automation:** Single Python script performs extraction, validation, cleaning, loading, visualization, and logging  
- **Portfolio Ready:** Docstrings and structured code enhance readability and maintainability  
- **Freelancing-Ready:** Demonstrates “reliability over just code” – a real client-ready workflow  

---

## 📊 Example Output

- **Console:** Displays file detection, data shape, cleaning completion, database insertion, and log confirmation  
- **Chart:** Displays total profit by category; e.g., **Electronics** category generates the highest profit  
- **Database:** `Weekly_Sales` table contains clean, deduplicated sales data  
- **Log:** Example entry in `pipeline_log.txt`  

---

## 📝 Usage Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AlphaDay6_Pipeline.git
cd AlphaDay6_Pipeline

Ensure sales_data.csv is in the folder.

Run the pipeline:

python AlphaDay6_MasterPipeline.py

Outputs:

Updated SQLite database (Alpha_Data_Warehouse.db)

Pipeline execution log (pipeline_log.txt)

Profit bar chart (Automated_Profit_Report.png)
