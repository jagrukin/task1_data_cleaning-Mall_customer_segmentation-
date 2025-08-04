# task1_data_cleaning-Mall_customer_segmentation-
# First Task: Preprocessing and Data Cleaning

### The Goal  
By handling missing values, removing duplicates, standardizing formats, and preparing the data for further analysis, this task aimed to clean and preprocess the raw Mall Customer Segmentation dataset.

---

### 📁 Dataset Employed  
**Mall Customer Segmentation Dataset**  
Source: Public dataset used for customer segmentation practice (add source link if available)

---

### Tools & Technologies  
- VS Code (or your preferred editor)  
- Python 3.13  
- Pandas library  

---

### Cleaning Procedures Followed  
1. Loaded dataset using `pandas.read_csv()`.  
2. Checked for and handled missing values (none found, but filled if any).  
3. Removed duplicate rows with `drop_duplicates()`.  
4. Standardized text columns (e.g., capitalized Gender values).  
5. Cleaned column names: converted to lowercase, removed spaces, replaced spaces with underscores.  
6. Converted data types to correct types (e.g., age as integer).  
7. Saved the cleaned dataset as `Mall_Customers_Cleaned.csv`.

---

### 📦 Included Files

| File Name                  | Description                                      |
|----------------------------|------------------------------------------------|
| `Mall_Customers.csv`       | Original raw dataset                            |  
| `Mall_Customers_Cleaned.csv` | Final cleaned dataset, ready for analysis       |  
| `clean_mall_data.py`       | Python script used for data cleaning and preprocessing |

---

### ✅ Output  
`Mall_Customers_Cleaned.csv` is now free of duplicates, missing values handled, column names standardized, and data types fixed—prepared for further segmentation or analysis.

---

### 👨‍💻 Author  
Jainam Jain 
Data Analyst Intern  
Submission for Task 1: Data Cleaning and Preprocessing
