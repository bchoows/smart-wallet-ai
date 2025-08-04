---
title: Smart Wallet AI
emoji: 🤖
colorFrom: indigo
colorTo: green
sdk: docker
app_file: streamlit_app.py
pinned: false
---

# 🤖 Smart Wallet AI Transaction Classifier

This project is a complete, end-to-end AI system designed to automatically classify financial transactions into categories such as `Food & Drink`, `Shopping`, and `Transport`. It features a machine learning backend with multiple specialist models, a smart tagging system, and a live, interactive web interface.

## ✨ Features

* **AI-Powered Classification:** Uses three distinct `scikit-learn` models to accurately predict categories from either combined, merchant-only, or description-only data.
* **Smart Tagging:** Automatically extracts keywords like brands and locations (e.g., "Uniqlo", "Starbucks") using `spaCy`'s Named Entity Recognition.
* **Flexible API:** A robust API built with `FastAPI` that intelligently selects the best model based on the input provided.
* **Interactive UI:** A simple and clean user interface built with `Streamlit` for easy, real-time classification.
* **Containerized Deployment:** Fully containerized with `Docker` and deployed on Hugging Face Spaces for public access.

## 🔗 Live Demo

You can test the live application here:
**https://huggingface.co/spaces/bchoows/smart-wallet-ai**

![Smart Wallet App Demo]([LINK TO YOUR SCREENSHOT])
*(**To add a screenshot:** Upload an image to your GitHub repo, click on it to get the URL, and paste that URL in place of this text.)*

---

## 📝 Dataset Summary

The model was trained on a mock dataset of 2000 transactions, generated using a custom Python script (`generate_data.py` located in the mock_data_generator folder). The dataset includes the following fields: `amount`, `merchant`, `timestamp`, `description`, and `category`. Categories were predefined and balanced to include common spending areas like Groceries, Transport, Shopping, and Bills. The text-based features (`merchant`, `description`) were designed to be realistic to simulate real-world transaction data.

---

## 📊 Model Training & Evaluation

The models were trained using a Logistic Regression classifier. The primary `combined` model achieved an overall accuracy of **99%** on the unseen test set.

**Classification Report (Combined Model):**
[IMAGE LINK]

---

## ⚙️ Setup and Local Usage

To run this project on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/bchoows/smart-wallet-ai.git
    cd SWTC
    ```

2.  **Create and activate a virtual environment with Python 3.11 (for stability):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the API:**
    Open a terminal and run the backend server:
    ```bash
    uvicorn main:app --reload
    ```

5.  **Run the UI:**
    Open a **second terminal** and run the Streamlit frontend:
    ```bash
    streamlit run streamlit_app.py
    ```

---