import pickle
import os
import numpy as np
from pathlib import Path

class IrisClassifier:
    def __init__(self):
        self.model = None
        self.class_names = ['setosa', 'versicolor', 'virginica']
        self.load_model()
    
    def load_model(self):
        """Load the trained model from disk"""
        model_path = Path(__file__).parent.parent / 'models' / 'iris_model.pkl'
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def predict(self, features: list):
        """Make prediction for a single sample"""
        features_array = np.array(features).reshape(1, -1)
        
        # Get prediction
        prediction = self.model.predict(features_array)[0]
        
        # Get probabilities
        probabilities = self.model.predict_proba(features_array)[0]
        
        # Get class name
        class_name = self.class_names[prediction]
        
        # Calculate confidence (max probability)
        confidence = float(max(probabilities))
        
        return {
            'prediction': int(prediction),
            'class_name': class_name,
            'probabilities': [float(p) for p in probabilities],
            'confidence': confidence
        }

# Singleton instance
classifier = IrisClassifier()
