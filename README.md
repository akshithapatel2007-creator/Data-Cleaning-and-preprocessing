# Data Cleaning and Preprocessing

## Overview

This project demonstrates the process of cleaning and preprocessing a raw dataset using **Python** and the **Pandas** library. The aim is to transform raw, inconsistent data into a clean and structured dataset that is ready for data analysis and machine learning.

## Objective

* Handle missing (null) values
* Remove duplicate records
* Standardize text values
* Convert date columns into a consistent format
* Rename column headers for better readability
* Correct data types
* Save the cleaned dataset

## Tools & Technologies

* Python
* Pandas
* Visual Studio Code
* GitHub

## Dataset

**Customer Personality Analysis** (Kaggle)

The dataset contains customer demographic details, purchasing behavior, and marketing campaign information.

## Project Structure

```
Data-Cleaning-and-Preprocessing/
│
├── marketing_campaign.csv
├── cleaned_marketing_campaign.csv
├── cleaning.py
└── README.md
```

## Data Cleaning Steps

1. Loaded the dataset using Pandas.
2. Displayed the first few rows of the dataset.
3. Checked dataset information and data types.
4. Identified missing values.
5. Filled missing values using appropriate methods.
6. Removed duplicate records.
7. Standardized text values by converting them to lowercase and removing extra spaces.
8. Renamed column headers to lowercase with underscores.
9. Converted date columns into a consistent datetime format.
10. Saved the cleaned dataset as `cleaned_marketing_campaign.csv`.

## Python Functions Used

* `read_csv()`
* `head()`
* `info()`
* `isnull()`
* `fillna()`
* `drop_duplicates()`
* `str.lower()`
* `str.strip()`
* `to_datetime()`
* `to_csv()`

## Output

The project generates a cleaned dataset named:

`cleaned_marketing_campaign.csv`

This dataset is ready for further analysis, visualization, or machine learning tasks.

## Learning Outcomes

* Learned how to clean real-world datasets.
* Understood techniques for handling missing values.
* Removed duplicate records.
* Standardized inconsistent data.
* Converted data into appropriate formats.
* Prepared a dataset suitable for analysis.

## Author

**AKshitha Patel**

B.Tech – Computer Science (CSE)
St. Peter's Engineering College
