from pathlib import Path
import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

class MulticlassPredictor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def predict(self, X: list):
        pass

    @abstractmethod
    def print_classification_report(self, X, y_true):
        pass

class SklearnMulticlassPredictor(MulticlassPredictor):
    def __init__(self):
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', LogisticRegression(max_iter=1000))  # Removed multi_class parameter
        ])

    def predict(self, X: list):
        return self.model.predict(X)

    def fit(self, X, y):
        self.model.fit(X, y)

    def evaluate(self, X, y_true):
        y_pred = self.predict(X)
        return f1_score(y_true, y_pred, average='weighted')

    def print_classification_report(self, X, y_true):
        y_pred = self.predict(X)
        report = classification_report(y_true, y_pred)
        print("Classification Report:")
        print(report)

class RandomMulticlassPredictor(MulticlassPredictor):
    def __init__(self, classes):
        self.classes = classes

    def predict(self, X: list):
        return np.random.choice(self.classes, size=len(X))

    def fit(self, X, y):
        pass  # No fitting needed for random predictor

    def evaluate(self, X, y_true):
        y_pred = self.predict(X)
        return f1_score(y_true, y_pred, average='weighted')

    def print_classification_report(self, X, y_true):
        y_pred = self.predict(X)
        report = classification_report(y_true, y_pred)
        print("Classification Report:")
        print(report)

# Example usage
if __name__ == "__main__":
    # Example data
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 3, 100)
    X_test = np.random.rand(20, 5)
    y_test = np.random.randint(0, 3, 20)

    # Classes
    classes = ['Manufacturing', 'Mining', 'Finance, Insurance, And Real Estate', 'Services',
               'Wholesale Trade', 'Construction',
               'Transportation, Communications, Electric, Gas, And Sanitary Services',
               'Agriculture, Forestry, And Fishing', 'Retail Trade']

    df = pd.read_csv(Path(__file__).parent / '10k_filings_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df['body'], df['label'], test_size=0.2, random_state=42)

    # Initialize the random predictor
    random_predictor = RandomMulticlassPredictor(classes)

    # Evaluate the random predictor
    f1 = random_predictor.evaluate(X_test, y_test)
    print(f"Random Predictor F1 Score: {f1}")