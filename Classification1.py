import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

df=pd.read_csv('adult_income.csv')

df=df.dropna()


#Label Encoder
label_enc=LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col]=label_enc.fit_transform(df[col])

x=df.drop("income", axis=1)
y=df["income"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model=LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

#Predictions
y_pred=model.predict(x_test)
y_prob=model.predict_proba(x_test)[:,1]

acc=accuracy_score(y_test, y_pred)
prec=precision_score(y_test, y_pred)
rec=recall_score(y_test, y_pred)
f1=f1_score(y_test, y_pred)
roc=roc_auc_score(y_test, y_prob)

#print(all)

cm=confusion_matrix(y_test, y_pred)
sns.heatmap(cm)
plt.show()

sns.scatterplot(x=y_test, y=y_pred)
plt.show()