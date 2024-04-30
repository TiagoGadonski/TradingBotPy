from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def train_model(data):
    X = data[['last_price', 'change_percent']]
    y = np.where(data['change_percent'] > 0, 1, 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def predict(model, X_new):
    return model.predict([X_new])[0]
