import pandas as pd
import streamlit as st
import os

CSV_PATH = "static/forecast_results.csv"  # must match Flask output

st.title("📊 Forecasted Sales Data")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    st.success("Forecast generated. Showing results below 👇")
    st.dataframe(df)

    # Optional: download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="forecast_results.csv",
        mime="text/csv"
    )
else:
    st.warning("No forecast data found. Please trigger a forecast via the chatbot.")
