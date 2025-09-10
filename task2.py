import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
df = yf.download("RELIANCE.NS", start="2020-01-01", end="2025-03-31")
print(df.head())
df = df[["Close"]]
future_days = 30
df["Prediction"] = df[["Close"]].shift(-future_days)
print(df.tail())
X = np.array(df.drop(["Prediction"], axis=1))[:-future_days]
y = np.array(df["Prediction"])[:-future_days]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, predictions))
X_future = np.array(df.drop(["Prediction"], axis=1))[-future_days:]
future_pred = model.predict(X_future)
print(future_pred)
valid = df[X.shape[0]:]
valid["Predictions"] = future_pred
plt.figure(figsize=(12,6))
plt.title("Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Close Price (INR)")
plt.plot(df["Close"], label="Actual Price")
plt.plot(valid["Predictions"], label="Predicted Price")
plt.legend()
plt.show()
