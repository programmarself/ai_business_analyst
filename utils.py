import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_kpis(df):
    st.subheader("Key Performance Indicators")
    st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
    st.metric("Total Expenses", f"${df['Expenses'].sum():,.2f}")
    st.metric("Net Profit", f"${df['Revenue'].sum() - df['Expenses'].sum():,.2f}")

def show_visualizations(df):
    st.subheader("📊 Visualizations")
    st.write("Revenue over Time")
    st.line_chart(df.set_index("Date")["Revenue"])

    st.write("Expenses by Category")
    fig, ax = plt.subplots()
    df.groupby("Category")["Expenses"].sum().plot(kind="bar", ax=ax)
    st.pyplot(fig)

def generate_insights(df):
    st.subheader("🧠 AI-Generated Insights")
    if df["Revenue"].mean() < df["Expenses"].mean():
        st.warning("Expenses are higher than revenue on average. Consider reducing costs.")

    growth = (df["Revenue"].iloc[-1] - df["Revenue"].iloc[0]) / df["Revenue"].iloc[0]
    st.info(f"Revenue Growth Rate: {growth*100:.2f}%")