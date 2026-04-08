import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model(X_train, y_train, X_test, y_test, params=None):
    """
    Trains a machine learning model and logs parameters and metrics to MLflow.
    """
    if params is None:
        params = {"solver": "liblinear", "random_state": 42}

    with mlflow.start_run():
        model = LogisticRegression(**params)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        mlflow.log_params(params)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")

        print(f"Model trained with accuracy: {accuracy}")
        return model
