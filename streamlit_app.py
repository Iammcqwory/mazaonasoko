
import streamlit as st
import pandas as pd
import numpy as np

# 1. Database of agricultural information
df_agriculture = pd.read_csv("agriculture_data.csv")

# 2. Climate-resilient agriculture toolkit
df_climate_resilient_agriculture = pd.read_csv("climate_resilient_agriculture_toolkit.csv")

# 3. Financial literacy section
df_financial_literacy = pd.read_csv("financial_literacy_data.csv")

# 4. Environmental conservation section
df_environmental_conservation = pd.read_csv("environmental_conservation_data.csv")

# 5. Microfinance loan assessment tool
df_microfinance_loan_assessment = pd.read_csv("microfinance_loan_assessment_data.csv")

# Main app
st.title("Mazao na Soko")

# Navigation bar
st.sidebar.title("Navigation")
st.sidebar.markdown("**Database of agricultural information**")
st.sidebar.markdown("**Climate-resilient agriculture toolkit**")
st.sidebar.markdown("**Financial literacy section**")
st.sidebar.markdown("**Environmental conservation section**")
st.sidebar.markdown("**Microfinance loan assessment tool**")

# 1. Database of agricultural information
if st.sidebar.checkbox("Database of agricultural information"):
    st.header("Database of agricultural information")
    st.table(df_agriculture)

# 2. Climate-resilient agriculture toolkit
if st.sidebar.checkbox("Climate-resilient agriculture toolkit"):
    st.header("Climate-resilient agriculture toolkit")
    st.table(df_climate_resilient_agriculture)

# 3. Financial literacy section
if st.sidebar.checkbox("Financial literacy section"):
    st.header("Financial literacy section")
    st.table(df_financial_literacy)

# 4. Environmental conservation section
if st.sidebar.checkbox("Environmental conservation section"):
    st.header("Environmental conservation section")
    st.table(df_environmental_conservation)

# 5. Microfinance loan assessment tool
if st.sidebar.checkbox("Microfinance loan assessment tool"):
    st.header("Microfinance loan assessment tool")
    st.table(df_microfinance_loan_assessment)
