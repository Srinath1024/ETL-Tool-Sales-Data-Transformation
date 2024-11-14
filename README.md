# ETL Tool: Sales Data Transformation and Loading

## Overview

This project involves creating a Python-based ETL (Extract, Transform, Load) process for transforming sales data from two different regions (Region A and Region B) and loading it into a SQLite database. The data is provided in CSV format, and the objective is to process, clean, and store it in a structured database while following specified business rules.

## Project Structure

- `etl_script.py`: The Python script that handles the ETL process.
- `sales_region_a.csv`: Sample sales data from Region A.
- `sales_region_b.csv`: Sample sales data from Region B.
- `orders.db`: SQLite database file that stores the transformed data.
- `README.md`: This file containing details about the project.

## Setup

### Prerequisites

1. **Python 3.x** - This script is written in Python 3.
2. **pandas** - Used for handling and transforming CSV data.
3. **sqlite3** - Used to interact with the SQLite database.
4. **ast** - Parses and processes Python code into an abstract syntax tree (AST).
5. **pickle** - Serializes and deserializes Python objects for storage and retrieval.

You can install the necessary Python libraries by running:

```bash
pip install pandas sqlite3
```

## Database Setup

The script will automatically create an SQLite database named `orders.db` and populate it with a table named `sales_data`. This table will hold the transformed sales data.

## How to Run

1. **Download the project files**:
   Ensure you have the following files in your working directory:
   - `etl_script.py`
   - `sales_region_a.csv`
   - `sales_region_b.csv`

2. **Run the ETL script**:
   To run the ETL process, simply execute the `etl_script.py`:

   ```bash
   python etl_script.py
   ```
   
## SQL Queries for Validation

Here are some SQL queries you can run against the `sales_data.db` to validate the data:

1. **Count the total number of records**:
   ```sql
   SELECT COUNT(*) FROM sales_data;
2. **Total sales amount by region**:
   ```sql
   SELECT region, SUM(total_sales) AS total_sales_amount FROM sales_data GROUP BY region;
3. **Average sales amount per transaction:**
   ```sql
   SELECT AVG(total_sales) AS average_sales_amount FROM sales_data;
4. **Ensure there are no duplicate id values:**:
   ```sql
   SELECT id, COUNT(*) FROM sales_data GROUP BY id HAVING COUNT(*) > 1;

## Assumptions & Decisions
- **CSV File Structure**: The CSV files are expected to follow the format shown in the problem statement.
- **Handling Duplicates**: Any duplicate entries based on the `id` will be removed during the transformation process.
- **Database**: The SQLite database will be created dynamically by the script.

## Code Explanation

- **ETL Process**: 
  - **Extract**: The `read_data()` function reads the CSV files and loads them into a pandas DataFrame.
  - **Transform**: The `business_transformation()` function processes the data by calculating the `total_sales`, adding a `region` column, calculating `net_sales`.
  - **Load**: The `load_data()` function uploads the transformed data into an SQLite database.

- **SQLite Database**: The transformed data is stored in an SQLite table named `sales_data` with the following schema:
  ```sql
  CREATE TABLE sales_data (
      OrderId TEXT PRIMARY KEY,
      OrderItemId INTEGER,
      QuantityOrdered INTEGER,
      PromotionDiscount TEXT,
      region TEXT,
      total_sales REAL,
      net_sale REAL
  );

---

This is now in full GitHub markdown format and ready to be used in a repository!
