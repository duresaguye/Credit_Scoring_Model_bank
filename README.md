# Credit Scoring Model 

## Overview
This project involves building a Credit Scoring Model  to enable a buy-now-pay-later service. The project includes tasks such as understanding credit risk, exploratory data analysis (EDA), feature engineering, model training, and deployment.

## Directory Structure
- `data/`: Contains the dataset (ignored in version control).
- `src/`: Source code for data processing, feature engineering, and model training.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model development.
- `models/`: Saved models (ignored in version control).
- `reports/`: Reports and documentation.

## Exploratory Data Analysis (EDA)
The EDA process involves the following steps:

1. **Load the dataset and understand its structure:**
   - Load the dataset from `raw/data.csv`.
   - Display the number of rows, columns, and data types.

2. **Generate summary statistics:**
   - Display summary statistics to understand the central tendency, dispersion, and shape of the dataset’s distribution.

3. **Visualize the distribution of numerical features:**
   - Plot histograms and KDE plots for numerical features to identify patterns, skewness, and potential outliers.

4. **Analyze the distribution of categorical features:**
   - Plot count plots for categorical features to gain insights into the frequency and variability of categories.

5. **Perform correlation analysis:**
   - Generate a correlation matrix and visualize it using a heatmap to understand the relationships between numerical features.

6. **Identify missing values:**
   - Identify missing values in the dataset and decide on appropriate imputation strategies.

7. **Detect outliers:**
   - Use box plots to identify outliers in numerical features.


## Deliverables
- Understanding Credit Risk
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Default Estimator and WoE Binning
- Modelling
- Model Serving API Call

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/duresaguye/Credit_Scoring_Model_bank
   cd Credit_Scoring_Model_bank
   Create and activate a virtual environment:

Install the required packages:

Run the Jupyter notebook for EDA:
