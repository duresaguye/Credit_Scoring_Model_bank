from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline

# Define all custom preprocessing functions from the training
def bucket_rare_categories(X, top_n=20):
    """Bucket rare categories into 'Other' category"""
    X_processed = X.copy()
    for col in X_processed.select_dtypes(include=['object']).columns:
        top_cats = X_processed[col].value_counts().nlargest(top_n).index
        X_processed[col] = X_processed[col].where(X_processed[col].isin(top_cats), 'Other')
    return X_processed

def frequency_encoder_func(X):
    """Frequency encoding implementation"""
    return X.apply(lambda col: col.map(col.value_counts(normalize=True)))

# Load the model AFTER defining custom functions
model = joblib.load('../../models/best_rf_model.pkl')

app = FastAPI()

# Define input data model based on training data features
class PredictionInput(BaseModel):
    Amount: float
    CustomerID: str
    TransactionDate: str
    ProductCategory: str
    # Add all other features present in your training data
  

# Prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Convert input to DataFrame (preserve column order)
        input_dict = input_data.dict()
        df = pd.DataFrame([input_dict])
        
        # Use model's built-in preprocessing and predict
        prediction = model.predict(df)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# To run: uvicorn app:app --reload