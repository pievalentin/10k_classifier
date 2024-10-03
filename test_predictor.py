from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from predictor import RandomMulticlassPredictor, SklearnMulticlassPredictor



# TODO: Use this test to train and output the score of your model
# With only 3k entries, your training should be decently short.
# If you have a more complicated pipeline you can readh out to the team
def test_random_multiclass_predictor():
    # Read the CSV file
    df = pd.read_csv(Path(__file__).parent / '10k_filings_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df['body'], df['label'], test_size=0.2, random_state=42)

    # Classes
    classes = ['Manufacturing', 'Mining', 'Finance, Insurance, And Real Estate', 'Services',
               'Wholesale Trade', 'Construction',
               'Transportation, Communications, Electric, Gas, And Sanitary Services',
               'Agriculture, Forestry, And Fishing', 'Retail Trade']

    # Initialize the random predictor
    random_predictor = RandomMulticlassPredictor(classes)

    # Evaluate the random predictor
    f1 = random_predictor.evaluate(X_test, y_test)
    random_predictor.print_classification_report(X_test, y_test)
    
    print(f"Random Predictor F1 Score: {f1} \n")
    assert isinstance(f1, float), "F1 score is not a float"

# This 
def test_sklearnMultiClass():
    # Example data
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 3, 100)
    X_test = np.random.rand(20, 5)
    y_test = np.random.randint(0, 3, 20)

    # Initialize the sklearn predictor
    sklearn_predictor = SklearnMulticlassPredictor()

    # Train the sklearn predictor
    sklearn_predictor.fit(X_train, y_train)

    # Evaluate the sklearn predictor
    f1 = sklearn_predictor.evaluate(X_test, y_test)
    sklearn_predictor.print_classification_report(X_test, y_test)
    
    print(f"Sklearn Predictor F1 Score: {f1} \n")
    assert isinstance(f1, float), "F1 score is not a float"


# Run the test
if __name__ == "__main__":
    test_random_multiclass_predictor()
    test_sklearnMultiClass()
