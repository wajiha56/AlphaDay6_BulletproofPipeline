"""
AlphaDay6_MasterPipeline.py

Automated Data Pipeline - Bulletproof Version with Visualization
----------------------------------------------------------------
Steps:
1. Detect CSV file safely in the script's folder.
2. Validate and clean raw sales data (fill nulls, remove duplicates).
3. Save cleaned data to SQLite Data Warehouse.
4. Log each successful pipeline run with timestamp.
5. Generate a bar chart showing total profit by category.
6. Professional docstrings for maintainability.
"""

import pandas as pd
import sqlite3
from datetime import datetime
import os
import matplotlib.pyplot as plt

# -------------------------------------------------
# Step 1: Set Base Directory (Folder-Safe Paths)
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("📂 Current Working Directory:", BASE_DIR)
print("📄 Files in Directory:", os.listdir(BASE_DIR))

csv_file = os.path.join(BASE_DIR, "sales_data.csv")

if not os.path.exists(csv_file):
    print(f"[❌] CSV file nahi mili: {csv_file}")
    exit()

print("✔ CSV File Found:", csv_file)

# -------------------------------------------------
# Step 2: Load CSV
# -------------------------------------------------
df = pd.read_csv(csv_file)
print("\n📊 Raw Data Loaded Successfully")
print("Shape:", df.shape)

# -------------------------------------------------
# Step 3: Data Validation Function
# -------------------------------------------------
def validate_data(df):
    """
    Cleans raw sales data by:
    1. Filling missing 'Sales' and 'Quantity' with mean values.
    2. Removing duplicate Order_IDs.
    Returns:
        Cleaned Pandas DataFrame ready for DB insertion.
    """
    # Fill missing numeric values
    df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
    
    # Remove duplicate orders
    df = df.drop_duplicates(subset=["Order_ID"], keep="first")
    
    return df

# Apply validation
df = validate_data(df)
print("✔ Data Validation & Cleaning Complete")
print("Cleaned Shape:", df.shape)

# -------------------------------------------------
# Step 4: Save to SQLite Data Warehouse
# -------------------------------------------------
db_file = os.path.join(BASE_DIR, "Alpha_Data_Warehouse.db")

conn = sqlite3.connect(db_file)
df.to_sql("Weekly_Sales", conn, if_exists="append", index=False)
print("✔ Data inserted into SQLite Warehouse")

# -------------------------------------------------
# Step 5: Generate Profit Chart
# -------------------------------------------------
# Check if 'Category' and 'Profit' exist
if "Category" in df.columns and "Profit" in df.columns:
    profit_by_category = df.groupby("Category")["Profit"].sum()
    
    plt.figure(figsize=(8,5))
    profit_by_category.plot(kind="bar", color='skyblue')
    
    plt.title("Total Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_file = os.path.join(BASE_DIR, "Automated_Profit_Report.png")
    plt.savefig(chart_file)
    plt.show()
    
    print(f"✔ Profit chart generated: {chart_file}")
else:
    print("[⚠] Cannot generate chart - 'Category' or 'Profit' column missing")

conn.close()

# -------------------------------------------------
# Step 6: Pipeline Logging
# -------------------------------------------------
log_file = os.path.join(BASE_DIR, "pipeline_log.txt")
with open(log_file, "a") as f:
    f.write(f"Pipeline run successfully at {datetime.now()}\n")

print("✔ Pipeline execution logged")

# -------------------------------------------------
# Step 7: Completion Message
# -------------------------------------------------
print("\n🚀 Pipeline Completed Successfully!")