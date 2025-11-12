import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('adult_income.csv')
print(df.describe)

sns.histplot(df["age"])
plt.show()

#sns.boxplot(x="income", y="hours per week", data=df)
#plt.tshow()

sns.barplot(y='occupation',data=df, order=['occupation'].value_counts().index)
plt.show()

corr_data = df[["Temp3pm", "Humidity3pm", "Pressure3pm"]].corr()

sns.heatmap(corr_data, annot=True, cmap="coolwarm", fmt=".2f")