Customer Lifetime Value & Churn Prediction Engine

An end-to-end Customer Intelligence system designed to identify high-value customers at risk of churn and estimate potential revenue exposure.


Business Problem

Organizations often struggle to:

Identify which customers will generate future revenue

Detect high-value customers at risk of churn

Quantify revenue exposure due to potential churn

This project builds a predictive analytics framework to solve that problem.


Solution Overview

The system integrates:

RFM (Recency, Frequency, Monetary) Analysis

Churn Prediction using Logistic Regression

Customer Lifetime Value (CLV) Modeling

Risk-Based Segmentation Framework

Revenue Impact Estimation

Interactive Streamlit Dashboard


Model Performance

Churn Rate: 33.28%

Model: Logistic Regression

ROC-AUC Score: 0.77

High Value – High Risk Customers Identified: 147

Potential Revenue at Risk: ₹342,198


Project Architecture
Data → Feature Engineering (RFM) 
     → Churn Modeling 
     → CLV Calculation 
     → Risk Segmentation 
     → Dashboard Visualization


Project Structure
customer-intelligence-engine/
│
├── retail_cleans.csv
├── Customer_Intelligence_Project.ipynb
├── rfm_output.csv
├── app.py
└── README.md


Tech Stack
    Python
    
    Pandas
    
    NumPy
    
    Scikit-learn
    
    Matplotlib
    
    Streamlit


How to Run the Project
1- Clone Repository
    git clone https://github.com/rohitsutar1611-ops/Customer-Intelligence-Churn-Prediction-System.git
    
2- Install Dependencies
    pip install -r requirements.txt

3- Run Dashboard
    streamlit run app.py

Business Impact

    The system enables:
    
    Early churn detection
    
    Revenue protection strategy
    
    Targeted retention campaigns
    
    Data-driven customer prioritization
    
    This framework can be extended to real-world CRM systems.


Author

    Rohit Sutar
        Computer Science Graduate | Data Analyst & Web Developer
