import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('nba_player_stats.csv')

features=["FGA", "3PA", "FT", "AST", "TRB", "TOV", "USG%", "Age"]
target="PTS"

df=df[features + [target]].dropna()

x=df[features]
y=df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(x_train, y_train)

y_pred=model.predict(x_test)

rmse=np.sqrt(mean_squared_error(y_test, y_pred))
mae=mean_absolute_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"R^2: {r2}")

residuals=y_test-y_pred

sns.scatterplot(x=y_pred, y=residuals)
plt.show()

sns.scatterplot(x=y_test, y=y_pred)
plt.show()