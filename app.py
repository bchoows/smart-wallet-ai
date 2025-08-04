# ==============================================================================
# Smart Wallet AI - User Interface Script
# ==============================================================================
import streamlit as st
import requests
import json

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Smart Wallet AI System",
    page_icon="🧾",
    layout="centered"
)

# --- 2. App Title and Description ---
st.title("🧾 Smart Wallet AI System")
st.write(
    "Enter transaction details below to get a category prediction from the AI model. Our API is running in the background to serve this app "
)

# --- 3. Input Boxes for User Data ---
st.header("Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    merchant = st.text_input("Merchant Name", placeholder="e.g., Starbucks")

with col2:
    amount = st.number_input("Amount (MYR)", step=0.01,
                             format="%.2f", min_value=0.0)

description = st.text_area(
    "Description", placeholder="e.g., Morning coffee with team")

# --- 4. Classify Button and API Interaction ---
if st.button("Classify Transaction", type="primary"):
    # Check if at least one text field has input
    if not merchant and not description:
        st.error("Please enter a merchant or a description.")
    else:
        # 1. Prepare the data in a dictionary (JSON payload)
        api_payload = {
            "amount": amount,
            "merchant": merchant,
            "description": description
        }

        # 2. Send a request to our FastAPI backend
        try:
            with st.spinner('Asking the AI model...'):
                response = requests.post(
                    "http://127.0.0.1:8000/predict/smart",
                    data=json.dumps(api_payload)
                )

            # 3. Display the result
            if response.status_code == 200:
                result = response.json()
                st.success(
                    f"Prediction successful!")
                st.metric(
                    label="Predicted Category",
                    value=result['predicted_category'],
                    delta=f"Confidence: {result['confidence']}"
                )
            else:
                st.error(f"Error from API: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error(
                "Connection Error: Could not connect to the API. Is the `uvicorn` server running?")
