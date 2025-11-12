import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('weather_aus.csv')

features=["MinTemp","Humidity3pm","Pressure3pm","WindSpeed3pm"]
target="MaxTemp"

df=df[features + [target]].dropna()

x=df[features]
y=df[target]

x_test, x_train, y_test, y_train = train_test_split(x,y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(x_train, y_train)

y_pred=model.predict(x_test)
print("Prediction: ")
print(y_pred)

sns.scatterplot(x=y_pred, y=y_test)
plt.show()