from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import time


class StockModel:

    def __init__(self):

        # smaller trees train much faster
        self.model = RandomForestRegressor(
            n_estimators=200,
            max_depth=None,
            min_samples_leaf=5,
            n_jobs=-1,          # use all CPU cores
            random_state=42
        )

    def train(self, X, y):

        print("\nPreparing training data...")

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            shuffle=False
        )

        print("Training samples:", len(X_train))
        print("Testing samples:", len(X_test))
        print("Features:", len(X.columns))

        start = time.time()

        print("\nTraining RandomForest model...")

        self.model.fit(X_train, y_train)

        end = time.time()

        print(f"Training finished in {round(end - start, 2)} seconds")

        print("\nEvaluating model...")

        predictions = self.model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print("\nModel Results")
        print("---------------------")
        print("Mean Absolute Error:", round(mae, 4))
        print("R2 score:", round(r2, 4))

        # direction accuracy (very useful for stocks)
        direction_true = (y_test > 0)
        direction_pred = (predictions > 0)

        accuracy = (direction_true == direction_pred).mean()

        print("Direction accuracy:", round(accuracy, 3))

    def predict(self, X):

        return self.model.predict(X)