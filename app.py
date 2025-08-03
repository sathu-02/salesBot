# from flask import Flask, request, jsonify
# from pandasai import SmartDataframe
# from GeminiLLM import GeminiLLM
# import pandas as pd
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import os
# import traceback
# from flask_cors import CORS
# from pandasai.helpers.logger import Logger
# import logging



# app = Flask(__name__)
# CORS(app)

# GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")
# CSV_PATH = "cleanedData.csv"

# SYSTEM_PROMPT = """

# You are a helpful, fast and skilled sales analyst AI. Use the provided context only.
# Avoid using os, io, b64decode, or similar functions in code.
# When users ask about future predictions or forecasting, do NOT write Python code.
# Instead, instruct the app to trigger forecasting logic.

# Understand all columns in the csv dataset. Understand queries deeply – filter by customername, itemname, etc.
# Your job is to help users explore structured data like CSVs.

# You should be faster in responding.

# Support high-level queries like trends, top-N, customer-wise totals, sales summaries, etc.
# Use Python/pandas reasoning under the hood. Provide rich insights beyond just answering.
# Never average records for forecasts. Forecasts must include: customer-wise, product-wise, in kgs, units, and dollars.



# Use the context only. If data is not enough, say so.
# Use emojis and persuasive language to explain findings clearly and beautifully.


# You are a helpful, fast and skilled sales analyst AI. Use the provided context only.
# Avoid using os, io, b64decode, or similar functions in code.
# When users ask about future predictions, delegate forecasting to the host app logic.

# When asked about increment or decrement in sales for future months, compare the average increment/decrement of last 3 months.

# You are a fast, helpful, and creative data analyst AI. Use the provided CSV context only.
# You are a highly skilled data analyst assistant. Understand all the columns in the csv dataset.Understand the user's query clearly, see if he's mentioning about any customername or a productname. Your job is to help users explore structured data like CSVs.
# You answer creatively and give detailed and logical breakdowns when the question involves trends, reasoning, or comparisons.
# Use Python/pandas reasoning under the hood. Answer in about 150 words or even more based on the weight of the query. Also provide useful insights from the data, not only providing the required answer . Make the choice of most attractive words 
# You are a professional sales analyst assistant. generate responses as fast as possible
# You must analyze the given sales transaction data and answer high-level questions.
# Support mathematical computations, summarizations, trend identification, comparisons, and reasoning.
# Use the context to calculate totals, averages, and filter by customer, date, or product when needed.
# "You are a professional sales analyst assistant. "
# Reminding again You should be faster..

# The user may not type full customer names or product names, so you should be able to understand the context and provide accurate answers based on partial matches.

# "An important point to remember when the user has asked about future forecasting of the data, make sure that you give responses in customer wise, product wise, quantities in kgs, units and dollars,you have to generate a csv file with headers and download the csv file by incorporating all these functionalities. At any cost, don't perform average of records."
# "You must analyze the given sales transaction data and answer high-level questions. "
# "Support mathematical computations, summarizations, trend identification, comparisons, and reasoning. "
# "Use the context to calculate totals, averages, and filter by customer, date, or product when needed. "
# "Make sure You give accurate results based on the context provided. Perform calculations accurately."
# "Give answers in a creative manner. You have to attract the users by your words. Select appropriate emojis and answer creatively and beautifully."
# "Provide useful insights from the context apart from not only answering the questions."
# "Provide extra information if possible for example if the question says 'What are the top 3 products?.' Give answer on the basis of 3 categories: based on sales, based on quantity(in cartons) sold, based on profit and also based on quantities sold(in kg)"
# "Be helpful and provide useful information to the user."
# Be quick in responding.
# Only use the given context. If unsure, say 'Based on the provided data, not enough information is available.'
# """  # (Use your full system prompt here)

# # Load LLM and CSV
# df = pd.read_csv(CSV_PATH)
# llm = GeminiLLM(api_key=GEMINI_API_KEY, system_prompt=SYSTEM_PROMPT)

# logger = Logger()
# logger._logger.setLevel(logging.WARNING) 
# pandas_ai = SmartDataframe(df, config={
#     "llm": llm,
#     "verbose": False,
#     "enable_cache": False,
#     "enable_plotting": False,
#     "logger":logger
#     })

# # --- Forecasting Function ---
# def forecast_data(df, forecast_month_str):
#     df['txndate'] = pd.to_datetime(df['txndate'], dayfirst=True, errors='coerce')
#     df = df.dropna(subset=['txndate', 'customername', 'itemname', 'amt', 'qty', 'Unit_Name'])
#     df['amt'] = pd.to_numeric(df['amt'], errors='coerce')
#     df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

#     latest_date = df['txndate'].max()
#     start_date = latest_date - relativedelta(months=3)

#     df_recent = df[(df['txndate'] > start_date) & (df['txndate'] <= latest_date)]

#     grouped = df_recent.groupby(['customername', 'itemname', 'Unit_Name']).agg(
#         total_amt=('amt', 'sum'),
#         total_qty=('qty', 'sum')
#     ).reset_index()

#     grouped['forecasted_amt_usd'] = (grouped['total_amt'] / 3).round(2)
#     grouped['forecasted_units'] = (grouped['total_qty'] / 3).round(2)
#     grouped['forecast_month'] = forecast_month_str

#     return grouped[['customername', 'itemname', 'forecast_month', 'forecasted_amt_usd', 'forecasted_units', 'Unit_Name']]

# # --- Forecast Detection ---
# def is_forecast_query(query):
#     keywords = ["forecast", "future", "predict", "upcoming"]
#     return any(kw in query.lower() for kw in keywords)

# # --- API Routes ---


# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         data = request.json
#         query = data.get("query")
#         forecast_month = data.get("forecast_month", (datetime.today() + relativedelta(months=1)).strftime("%B %Y"))

#         if not query:
#             return jsonify({"error": "Query not provided"}), 400

#         if is_forecast_query(query):
#             forecast_df = forecast_data(df.copy(), forecast_month)
#             return jsonify({
#                 "forecast": forecast_df.to_dict(orient="records")
#             })
#         else:
#             response = pandas_ai.chat(query)
#             return jsonify({
#                 "response": response
#             })
#     except Exception as e:
#         print("🔥 Exception occurred:", e)
#         traceback.print_exc()
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=False)



























from flask import Flask, request, jsonify, send_from_directory
from pandasai import SmartDataframe
from GeminiLLM import GeminiLLM
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import traceback
from flask_cors import CORS
from pandasai.helpers.logger import Logger
import logging
import uuid  # for unique filenames

app = Flask(__name__, static_folder="static", static_url_path="/static")

CORS(app)

# --- Config ---
GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")
CSV_PATH = "cleanedData.csv"
STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)  # Ensure static dir exists

# --- System Prompt ---
SYSTEM_PROMPT = """
You are a helpful, fast and skilled sales analyst AI. Use the provided context only.
Avoid using os, io, b64decode, or similar functions in code.
When users ask about future predictions or forecasting, do NOT write Python code.
Instead, instruct the app to trigger forecasting logic.

Understand all columns in the csv dataset. Understand queries deeply – filter by customername, itemname, etc.
Your job is to help users explore structured data like CSVs.

Support high-level queries like trends, top-N, customer-wise totals, sales summaries, etc.
Use Python/pandas reasoning under the hood. Provide rich insights beyond just answering.
Never average records for forecasts. Forecasts must include: customer-wise, product-wise, in kgs, units, and dollars.

Use the context only. If data is not enough, say so.
Use emojis and persuasive language to explain findings clearly and beautifully.


You are a helpful, fast and skilled sales analyst AI. Use the provided context only.
Avoid using os, io, b64decode, or similar functions in code.
When users ask about future predictions, delegate forecasting to the host app logic.

You are a fast, helpful, and creative data analyst AI. Use the provided CSV context only.
You are a highly skilled data analyst assistant. Understand all the columns in the csv dataset.Understand the user's query clearly, see if he's mentioning about any customername or a productname. Your job is to help users explore structured data like CSVs.
You answer creatively and give detailed and logical breakdowns when the question involves trends, reasoning, or comparisons.
Use Python/pandas reasoning under the hood. Answer in about 150 words or even more based on the weight of the query. Also provide useful insights from the data, not only providing the required answer . Make the choice of most attractive words 
You are a professional sales analyst assistant. generate responses as fast as possible
You must analyze the given sales transaction data and answer high-level questions.
Support mathematical computations, summarizations, trend identification, comparisons, and reasoning.
Use the context to calculate totals, averages, and filter by customer, date, or product when needed.
"You are a professional sales analyst assistant. "
"An important point to remember when the user has asked about future forecasting of the data, make sure that you give responses in customer wise, product wise, quantities in kgs, units and dollars,you have to generate a csv file with headers and download the csv file by incorporating all these functionalities. At any cost, don't perform average of records."
"You must analyze the given sales transaction data and answer high-level questions. "
"Support mathematical computations, summarizations, trend identification, comparisons, and reasoning. "
"Use the context to calculate totals, averages, and filter by customer, date, or product when needed. "
"Make sure You give accurate results based on the context provided. Perform calculations accurately."
"Give answers in a creative manner. You have to attract the users by your words. Select appropriate emojis and answer creatively and beautifully."
"Provide useful insights from the context apart from not only answering the questions."
"Provide extra information if possible for example if the question says 'What are the top 3 products?.' Give answer on the basis of 3 categories: based on sales, based on quantity(in cartons) sold, based on profit and also based on quantities sold(in kg)"
"Be helpful and provide useful information to the user."
Only use the given context. If unsure, say 'Based on the provided data, not enough information is available.'
"""  # Keep your existing system prompt here

# --- Load LLM and CSV ---
df = pd.read_csv(CSV_PATH)
llm = GeminiLLM(api_key=GEMINI_API_KEY, system_prompt=SYSTEM_PROMPT)

logger = Logger()
logger._logger.setLevel(logging.WARNING)
pandas_ai = SmartDataframe(df, config={
    "llm": llm,
    "verbose": False,
    "enable_cache": False,
    "enable_plotting": False,
    "logger": logger
})

# --- Forecasting Function ---
def forecast_data(df, forecast_month_str):
    df['txndate'] = pd.to_datetime(df['txndate'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['txndate', 'customername', 'itemname', 'amt', 'qty', 'Unit_Name'])
    df['amt'] = pd.to_numeric(df['amt'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    latest_date = df['txndate'].max()
    start_date = latest_date - relativedelta(months=3)

    df_recent = df[(df['txndate'] > start_date) & (df['txndate'] <= latest_date)]

    grouped = df_recent.groupby(['customername', 'itemname', 'Unit_Name']).agg(
        total_amt=('amt', 'sum'),
        total_qty=('qty', 'sum')
    ).reset_index()

    grouped['forecasted_amt_usd'] = (grouped['total_amt'] / 3).round(2)
    grouped['forecasted_units'] = (grouped['total_qty'] / 3).round(2)
    grouped['forecast_month'] = forecast_month_str

    return grouped[['customername', 'itemname', 'forecast_month', 'forecasted_amt_usd', 'forecasted_units', 'Unit_Name']]

# --- Forecast Detection ---
def is_forecast_query(query):
    keywords = ["forecast", "future", "predict", "upcoming"]
    return any(kw in query.lower() for kw in keywords)

# --- API Routes ---
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        query = data.get("query")
        forecast_month = data.get("forecast_month", (datetime.today() + relativedelta(months=1)).strftime("%B %Y"))

        if not query:
            return jsonify({"error": "Query not provided"}), 400

        if is_forecast_query(query):
            forecast_df = forecast_data(df.copy(), forecast_month)

            # Save to static CSV
            unique_name = f"forecast_results.csv"
            csv_path = os.path.join(STATIC_DIR, unique_name)
            forecast_df.to_csv(csv_path, index=False)

            csv_url = f"/static/forecast_results.csv"

            return jsonify({
                "response": "✅ Forecast generated! Click below to view or download it.",
                "streamlit_url": "http://localhost:8501"
            })



        else:
            response = pandas_ai.chat(query)
            return jsonify({
                "response": response
            })

    except Exception as e:
        print("🔥 Exception occurred:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
