

# House Price Prediction using Linear Regression

This project implements a **Linear Regression** model to predict house prices based on three features:

- **Square Footage**
- **Number of Bedrooms**
- **Number of Bathrooms**

The application is built using **Django** for the web interface and Python modules for data processing and modeling.

---

## 📁 Project Structure

project-root/
│
├── App/ # Django app for the web interface
│ ├── migrations/
│ ├── templates/
│ ├── static/
│ └── ...
│
├── dataset/ # Dataset directory
│ ├── train.csv # Training data
│ └── test.csv # Testing data
│
├── module/ # Python module for model and logic
│ ├── houseprice.py # Contains model training and prediction logic
│ └── main.py # Interface for interacting with the model
│
├── manage.py # Django management script
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Features

- Trains a linear regression model on the provided housing dataset.
- Accepts square footage, number of bedrooms, and bathrooms as inputs.
- Predicts the house price based on the trained model.
- Provides a web interface to interact with the model using Django.

---

## 🛠 Requirements

- Python 3.8+
- Django 3.2+
- pandas
- scikit-learn

Install all requirements using:

```bash
pip install -r requirements.txt
⚙️ How to Run
1. Train the Model
Navigate to the module/ directory and run:

bash
Copy
Edit
python main.py
This will load the dataset, train the model, and save the trained model (if implemented that way).

2. Start the Django App
From the root directory, run:

bash
Copy
Edit
python manage.py runserver
Then open your browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:8000/
You can now input housing features to get predicted prices.
