import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "Hours": [1,2,3,4,5,6,7,8,9],
    "Scores": [20,30,40,50,60,70,80,90,95]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Scores"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")