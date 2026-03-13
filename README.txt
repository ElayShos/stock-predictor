# S&P 500 Stock Prediction Pipeline

A machine learning pipeline that analyzes historical stock market data and predicts future returns for S&P 500 companies using technical indicators.

This project demonstrates a full data science workflow including data collection, feature engineering, model training, and evaluation on historical financial data.

---

## Overview

The pipeline performs the following steps:

1. Download historical stock data for all S&P 500 companies
2. Compute technical indicators (RSI, moving averages, momentum)
3. Generate future return targets
4. Train a machine learning model to predict future returns
5. Evaluate model performance using historical data

The prediction horizon is configurable, allowing users to estimate returns several months into the future.

---

## Features

* Automatic download of S&P 500 stock data
* Feature engineering using technical indicators
* Configurable prediction horizon (months)
* Random Forest machine learning model
* Model evaluation using multiple metrics

Evaluation metrics include:

* Mean Absolute Error (MAE)
* R² Score
* Direction Accuracy

Direction accuracy measures how often the model correctly predicts whether returns will be positive or negative.

---

## Project Structure

```
stock-predictor/
│
├── src/
│   ├── data_collector.py
│   ├── indicators.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── sp500.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone git clone https://github.com/ElayShos/stock-predictor.git

cd stock-predictor
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run the program:

```
python run.py
```

The program will:

1. Download historical market data
2. Ask for a prediction horizon in months
3. Train the machine learning model
4. Output a market prediction

## Example
```
Enter prediction horizon in months: 3
```

Output:

```
Prediction horizon: 3 months
Expected return: 4.2%
Expected direction: UP

Mean Absolute Error: 0.17
R2 score: 0.02
Direction accuracy: 0.64
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* yfinance

---

## Future Improvements

Possible extensions for the project:

* Compare additional models (Gradient Boosting, XGBoost)
* Incorporate macroeconomic indicators
* Perform full backtesting of trading strategies
* Add a visualization dashboard

---

## Author

Elay Shostak
Computer Science Student – Holon Institute of Technology

GitHub:
https://github.com/ElayShos
