from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from app.schemas import IrisFeatures, PredictionResponse, PredictionRequest
from app.model import classifier

# Create FastAPI app
app = FastAPI(
    title="Iris Classification API",
    description="API for predicting Iris flower species using Random Forest",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Iris Classification API",
        "endpoints": {
            "/predict": "POST - Make a prediction",
            "/health": "GET - Health check",
            "/docs": "GET - API documentation"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": classifier.model is not None}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Make a prediction for Iris flower species
    
    Example request:
    ```json
    {
        "features": {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    }
