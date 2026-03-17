# S&P 500 Stock Prediction

This is a small project that tries to predict stock returns for S&P 500 companies using historical data and a machine learning model.

The idea is to take past price data, calculate a few technical indicators, and use them to estimate whether a stock will go up or down in the future.

---

## What it does

* Downloads historical stock data
* Calculates indicators like moving averages, RSI, etc.
* Trains a Random Forest model
* Predicts future returns based on a chosen time horizon

---

## How to run

Clone the repo:

```
git clone https://github.com/ElayShos/stock-predictor.git
cd stock-predictor
```

Install requirements:

```
pip install -r requirements.txt
```

Run:

```
python run.py
```

You’ll be asked to enter how many months ahead you want to predict.

---

## Example

```
Enter prediction horizon in months: 3
```

Output will include:

* predicted return
* whether the model thinks the market will go up or down
* some basic evaluation metrics

---

## Notes

* This is just an experiment and not meant for real trading
* Results are pretty limited (as expected with this kind of data)
* Built mainly to practice working with data and ML

---

## Tech used

* Python
* pandas
* scikit-learn
* yfinance

---

## Author

Elay Shostak
Computer Science Student
