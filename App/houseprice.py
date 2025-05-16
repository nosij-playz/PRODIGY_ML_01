import joblib
import pandas as pd
import numpy as np
from itertools import combinations_with_replacement

class HousePricePredictor:
    def __init__(self, model_path='linear_house.pkl', degree=4):
        # Load saved pipeline (scaler + model)
        self.pipeline = joblib.load(model_path)
        self.degree = degree

    def create_poly_features(self, X):
        feature_names = X.columns.tolist()
        X_poly = pd.DataFrame(index=X.index)

        # Degree 1 (original features)
        for col in feature_names:
            X_poly[col] = X[col]

        # Higher degrees
        for deg in range(2, self.degree + 1):
            combos = combinations_with_replacement(feature_names, deg)
            for combo in combos:
                col_name = "_".join(combo)
                product = np.ones(len(X))
                for c in combo:
                    product *= X[c]
                X_poly[col_name] = product

        return X_poly

    def predict(self, GrLivArea, BedroomAbvGr, TotalBathrooms):
        input_data = {
            "GrLivArea": [GrLivArea],
            "BedroomAbvGr": [BedroomAbvGr],
            "TotalBathrooms": [TotalBathrooms]
        }
        input_df = pd.DataFrame(input_data)
        input_poly = self.create_poly_features(input_df)
        predicted_price = self.pipeline.predict(input_poly)
        return predicted_price[0]