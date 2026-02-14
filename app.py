import streamlit as st
import pandas as pd

rfm = pd.read_csv("rfm_output.csv")

st.set_page_config(page_title="Customer Intelligence Engine", layout="wide")

st.title("Customer Lifetime Value & Churn Intelligence Dashboard")

# --- KPI Section ---
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(rfm))
col2.metric("Churn Rate (%)", round(rfm["Churn"].mean()*100,2))
col3.metric("Revenue At Risk",
            round(rfm[rfm["Segment"]=="High Value - High Risk"]["CLV"].sum(),2))

st.divider()

# --- Segmentation Chart ---
st.subheader("Customer Segmentation Overview")
st.bar_chart(rfm["Segment"].value_counts())

st.divider()

# --- High Risk Customers Table ---
st.subheader("High Value - High Risk Customers")

high_risk = rfm[rfm["Segment"]=="High Value - High Risk"]\
                .sort_values("CLV", ascending=False)

st.dataframe(high_risk.head(20), use_container_width=True)
