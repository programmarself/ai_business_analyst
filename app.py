import streamlit as st
import pandas as pd
from utils import generate_insights, show_kpis, show_visualizations
from forecast import forecast_sales

st.set_page_config(page_title="AI Business Analyst", layout="wide")
st.title("📊 AI-Powered Business Analyst")

uploaded_file = st.file_uploader("Upload your financial CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ Data Loaded Successfully")
    st.write(df.head())

    show_kpis(df)
    show_visualizations(df)
    generate_insights(df)

    st.subheader("📈 Forecasting Future Trends")
    forecast_sales(df)