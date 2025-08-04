# ==============================================================================
# Smart Wallet AI - API with Smart Tagging
# ==============================================================================
import joblib
import pandas as pd
import spacy 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# --- 1. FastAPI App ---
app = FastAPI(title="Smart Wallet Transaction Classifier", version="3.0")

# --- 2. Load All Models (ML & NLP) ---
try:
    model_combined = joblib.load('transaction_classifier_combined.joblib')
    model_merchant = joblib.load('transaction_classifier_merchant.joblib')
    model_description = joblib.load(
        'transaction_classifier_description.joblib')
    nlp = spacy.load("en_core_web_sm") 
    print("All models loaded successfully.")
except FileNotFoundError:
    print("Error: Make sure all .joblib files are present and the spaCy model is downloaded.")
    exit()

# --- 3. Input Structure ---
class SmartTransactionInput(BaseModel):
    amount: float
    merchant: Optional[str] = None
    description: Optional[str] = None

# --- 4. Smart Prediction Endpoint ---
@app.post("/predict/smart", tags=["Smart Prediction"])
def predict_smart(data: SmartTransactionInput):
    if data.merchant and data.description:
        text_feature = data.merchant + ' ' + data.description
        input_df = pd.DataFrame(
            [{'text_features': text_feature, 'amount': data.amount}])
        prediction = model_combined.predict(input_df)
        probabilities = model_combined.predict_proba(input_df)
        model_used = "combined"
    elif data.merchant:
        prediction = model_merchant.predict([data.merchant])
        probabilities = model_merchant.predict_proba([data.merchant])
        model_used = "merchant_only"
    elif data.description:
        prediction = model_description.predict([data.description])
        probabilities = model_description.predict_proba([data.description])
        model_used = "description_only"
    else:
        raise HTTPException(
            status_code=400, detail="Please provide at least a merchant or a description.")

    confidence = probabilities.max()

    # --- Smart Tagging Logic ---
    full_text = f"{data.merchant or ''} {data.description or ''}"
    doc = nlp(full_text)

    smart_tags = []
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "GPE"]:
            smart_tags.append(ent.text)

    smart_tags = list(set(smart_tags))

    return {
        "predicted_category": prediction[0],
        "confidence": f"{confidence:.2%}",
        "model_used": model_used,
        "smart_tags": smart_tags 
    }