from sklearn.linear_model import LinearRegression
import numpy as np

def predict_moisture(df):
    if len(df) < 3:
        return None

    X = np.array(range(len(df))).reshape(-1, 1)
    y = df["moisture"]

    model = LinearRegression()
    model.fit(X, y)

    next_time = np.array([[len(df)]])
    prediction = model.predict(next_time)

    return prediction[0]