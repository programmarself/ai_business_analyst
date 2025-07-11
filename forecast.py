from prophet import Prophet
import streamlit as st
import pandas as pd

def forecast_sales(df):
    df_prophet = df[["Date", "Revenue"]].rename(columns={"Date": "ds", "Revenue": "y"})
    m = Prophet()
    m.fit(df_prophet)
    future = m.make_future_dataframe(periods=12, freq='M')
    forecast = m.predict(future)

    st.write("Forecasted Revenue (Next 12 Months)")
    st.line_chart(forecast.set_index("ds")["yhat"])