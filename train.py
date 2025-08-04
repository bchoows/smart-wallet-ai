# ==============================================================================
# Smart Wallet AI - Training Script
# ==============================================================================
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

print("Libraries imported.")

# --- 1. Load and Prepare Data ---
try:
    df = pd.read_csv('mock_transactions.csv')
    print("Dataset 'mock_transactions.csv' loaded.")
except FileNotFoundError:
    print("Error: 'mock_transactions.csv' not found.")
    exit()

# Define features and target (we need all columns available for different models)
features = ['merchant', 'description', 'amount']
target = 'category'
X = df[features]
y = df[target]

# --- 2. Split Data ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(
    f"Data split into {len(X_train)} training and {len(X_test)} testing rows.")

# ==============================================================================
# 🚀 MODEL 1: COMBINED (MERCHANT + DESCRIPTION + AMOUNT)
# ==============================================================================
print("\n--- Training Model 1: Combined ---")
df_train_combined = X_train.copy()
df_train_combined['text_features'] = df_train_combined['merchant'] + \
    ' ' + df_train_combined['description']

preprocessor_combined = ColumnTransformer(
    transformers=[
        ('text', TfidfVectorizer(stop_words='english',
         max_features=1000), 'text_features'),
        ('numeric', StandardScaler(), ['amount'])
    ]
)
pipeline_combined = Pipeline(steps=[
    ('preprocessor', preprocessor_combined),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline_combined.fit(df_train_combined, y_train)
joblib.dump(pipeline_combined, 'transaction_classifier_combined.joblib')
print("✅ Combined model saved as 'transaction_classifier_combined.joblib'")


# ==============================================================================
# 🚀 MODEL 2: MERCHANT-ONLY
# ==============================================================================
print("\n--- Training Model 2: Merchant-Only ---")
pipeline_merchant = Pipeline(steps=[
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=500)),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline_merchant.fit(X_train['merchant'], y_train)
joblib.dump(pipeline_merchant, 'transaction_classifier_merchant.joblib')
print("✅ Merchant-only model saved as 'transaction_classifier_merchant.joblib'")


# ==============================================================================
# 🚀 MODEL 3: DESCRIPTION-ONLY
# ==============================================================================
print("\n--- Training Model 3: Description-Only ---")
pipeline_description = Pipeline(steps=[
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=1000)),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline_description.fit(X_train['description'], y_train)
joblib.dump(pipeline_description, 'transaction_classifier_description.joblib')
print("✅ Description-only model saved as 'transaction_classifier_description.joblib'")
