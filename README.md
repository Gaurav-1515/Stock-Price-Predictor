# 📈 Stock Price Predictor

## 📌 Overview

This project predicts **future stock prices** based on historical stock market data.
The model uses **Linear Regression** to forecast closing prices and visualize predicted trends.

It uses:

* ✅ `yfinance` to fetch historical stock data
* ✅ `scikit-learn` for model training and evaluation
* ✅ `matplotlib` for visualization

## ⚙️ Features

* Fetch historical stock data from Yahoo Finance
* Train a machine learning model (Linear Regression)
* Predict future closing prices (e.g., next 30 days)
* Visualize actual vs predicted stock trends

## 🛠️ Tech Stack

* **Python** 🐍
* **Libraries:**

  * `pandas` → dataset handling
  * `numpy` → numerical operations
  * `yfinance` → stock data collection
  * `scikit-learn` → Linear Regression model
  * `matplotlib` → visualization

## 📂 Project Structure

```
📦 stock-price-predictor
 ┣ 📜 stock_predictor.py   # Main Python script
 ┣ 📜 requirements.txt     # Dependencies
 ┗ 📜 README.md            # Documentation
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/stock-price-predictor.git
cd stock-price-predictor
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Script

```bash
python stock_predictor.py
```

## 📊 Example Output

### 🔹 Sample Prediction

If you predict **30 days ahead**, the output may look like this:

```
[2735.4  2740.8  2745.6  2751.2 ... ]
```

### 🔹 Visualization

The program will generate a graph showing **actual stock prices vs predicted future prices**:

```
Blue Line  → Actual Prices  
Orange Line → Predicted Prices
```

## 📈 Model Evaluation

The model is evaluated using **Mean Squared Error (MSE)**:

```
MSE: 1842.56
```

## 📌 Future Enhancements

* Use **LSTM / GRU (Deep Learning models)** for better accuracy
* Add more features (Open, High, Low, Volume)
* Deploy with **Flask/Streamlit** as a web app
* Add real-time prediction dashboard

# OUTPUT
<img width="1918" height="1141" alt="Image" src="https://github.com/user-attachments/assets/48f9d9d1-957f-4f90-ad52-036e75238b8e" />
