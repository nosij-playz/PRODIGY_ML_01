from houseprice import HousePricePredictor
predictor = HousePricePredictor()

price = predictor.predict(1280, 2, 2.0)
print(f"Predicted SalePrice: {price:.2f}")