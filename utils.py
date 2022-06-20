import joblib
import numpy as np

def preprocess(Open, High, Low, Volume):
    test_data = np.array([Open, High, Low, Volume]).reshape(1, -1)
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)
    return prediction