import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve, precision_recall_curve, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# --- Load Data ---
df = pd.read_csv('weather_aus.csv')
df = df.dropna()

# --- Label Encoding ---
label_enc = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = label_enc.fit_transform(df[col])

# --- Features & Target ---
x = df.drop('RainTomorrow', axis=1)
y = df['RainTomorrow']

# --- Train/Test Split ---
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

# --- Model ---
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# --- Predictions ---
y_pred = model.predict(x_test)
y_prob = model.predict_proba(x_test)[:, 1]

# --- Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# --- ROC Curve ---
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = roc_auc_score(y_test, y_prob)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# --- Precision-Recall Curve ---
precision, recall, pr_thresholds = precision_recall_curve(y_test, y_prob)

plt.figure(figsize=(6,5))
plt.plot(recall, precision, color='purple')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.show()

# --- Best Probability Threshold ---
f1_scores = 2 * (precision * recall) / (precision + recall)
best_index = np.argmax(f1_scores)
best_threshold = pr_thresholds[best_index]
print(f"✅ Best Probability Threshold (max F1): {best_threshold:.3f}")
