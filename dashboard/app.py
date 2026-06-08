import streamlit as st
import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

st.title("Mutual Fund Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Schemes", len(fund))

with col2:
    st.metric("Total AUM", round(aum["aum_lakh_crore"].sum(), 2))

with col3:
    st.metric("Total SIP Inflow", round(sip["sip_inflow_crore"].sum(), 2))

st.subheader("AUM Trend")
st.bar_chart(aum["aum_lakh_crore"])