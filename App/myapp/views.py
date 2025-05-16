from django.shortcuts import render
from houseprice import HousePricePredictor

def predict_view(request):
    price = None
    if request.method == 'POST':
        sqft = float(request.POST.get('sqft', 0))
        bedrooms = int(request.POST.get('bedrooms', 0))
        bathrooms = float(request.POST.get('bathrooms', 0))

        predictor = HousePricePredictor()
        price = predictor.predict(sqft, bedrooms, bathrooms)

    return render(request, 'myapp\predict.html', {'price': price})
