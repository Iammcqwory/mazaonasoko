import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load datasets
df_agriculture = pd.read_csv("agriculture_data.csv")
df_climate_resilient_agriculture = pd.read_csv("climate_resilient_agriculture_toolkit.csv")
df_financial_literacy = pd.read_csv("financial_literacy_data.csv")
df_environmental_conservation = pd.read_csv("environmental_conservation_data.csv")
df_microfinance_loan_assessment = pd.read_csv("microfinance_loan_assessment_data.csv")

# Main app
st.title("Mazao na Soko")

# Navigation bar
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a section",
    [
        "Database of agricultural information",
        "Climate-resilient agriculture toolkit",
        "Financial literacy section",
        "Environmental conservation section",
        "Microfinance loan assessment tool",
    ],
)

# 1. Database of agricultural information
if option == "Database of agricultural information":
    st.header("Database of agricultural information")
    st.write("Explore the agricultural data below:")
    st.dataframe(df_agriculture)

    # Add filters
    st.subheader("Filter Data")
    crop_type = st.selectbox("Select Crop Type", df_agriculture["Crop Type"].unique())
    filtered_data = df_agriculture[df_agriculture["Crop Type"] == crop_type]
    st.dataframe(filtered_data)

    # Add a chart
    st.subheader("Crop Yield Over Time")
    fig = px.line(df_agriculture, x="Year", y="Yield", color="Crop Type", title="Crop Yield Over Time")
    st.plotly_chart(fig)

# 2. Climate-resilient agriculture toolkit
elif option == "Climate-resilient agriculture toolkit":
    st.header("Climate-resilient agriculture toolkit")
    st.write("Explore climate-resilient practices:")
    st.dataframe(df_climate_resilient_agriculture)

    # Add a bar chart
    st.subheader("Adoption Rate of Climate-Resilient Practices")
    fig = px.bar(df_climate_resilient_agriculture, x="Practice", y="Adoption Rate", title="Adoption Rate of Practices")
    st.plotly_chart(fig)

# 3. Financial literacy section
elif option == "Financial literacy section":
    st.header("Financial literacy section")
    st.write("Explore financial literacy resources:")
    st.dataframe(df_financial_literacy)

    # Add a pie chart
    st.subheader("Distribution of Financial Topics")
    fig = px.pie(df_financial_literacy, names="Topic", values="Interest", title="Financial Topics Distribution")
    st.plotly_chart(fig)

# 4. Environmental conservation section
elif option == "Environmental conservation section":
    st.header("Environmental conservation section")
    st.write("Explore environmental conservation data:")
    st.dataframe(df_environmental_conservation)

    # Add a scatter plot
    st.subheader("Impact of Conservation Efforts")
    fig = px.scatter(df_environmental_conservation, x="Year", y="Impact Score", color="Conservation Practice", title="Impact Over Time")
    st.plotly_chart(fig)

# 5. Microfinance loan assessment tool
elif option == "Microfinance loan assessment tool":
    st.header("Microfinance loan assessment tool")
    st.write("Assess microfinance loan eligibility:")

    # User inputs for loan assessment
    st.subheader("Loan Application Form")
    income = st.number_input("Annual Income (USD)", min_value=0)
    credit_score = st.number_input("Credit Score", min_value=0, max_value=850)
    loan_amount = st.number_input("Loan Amount Requested (USD)", min_value=0)

    # Simple loan assessment logic
    if st.button("Assess Eligibility"):
        if income > 20000 and credit_score > 600 and loan_amount <= income * 0.5:
            st.success("Congratulations! You are eligible for a loan.")
        else:
            st.error("Sorry, you do not meet the eligibility criteria.")

    # Display loan assessment data
    st.subheader("Loan Assessment Data")
    st.dataframe(df_microfinance_loan_assessment)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ by Mazao na Soko Team 2025")
