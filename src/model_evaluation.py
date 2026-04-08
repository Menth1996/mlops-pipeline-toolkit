from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained model and prints a classification report and confusion matrix.
    """
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    return classification_report(y_test, y_pred), confusion_matrix(y_test, y_pred)
