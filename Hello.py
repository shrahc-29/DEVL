import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
iris=sns.load_dataset("iris")

#removing duplicates
iris=iris.drop_duplicates()

#dataset info
print(f"Total Rows and Columns: {iris.shape}")
print("\nSample Data:\n", iris.head())
print("\nDescriptive Statistics:\n", iris.describe())

#histogram
plt.figure(figsize=(12, 5))

#histogram
plt.subplot(1, 2, 1)
plt.hist(iris["sepal_length"], bins=12, color="#6FB1FC", edgecolor="black")
plt.title("Sepal Length Distribution", fontsize=12)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

#kde plot
plt.subplot(1, 2, 2)
sns.kdeplot(x=iris["petal_width"], fill=True, color="#B565A7")
plt.title("Petal Width Density", fontsize=12)
plt.xlabel("Petal Width (cm)")
plt.tight_layout()
plt.show()

#count plot
plt.figure(figsize=(6, 4))
sns.countplot(x="species", data=iris, palette="pastel", edgecolor="black")
plt.title("Species Count in Iris Dataset")
plt.xlabel("Flower Species")
plt.ylabel("Count")
plt.show()

#boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(data=iris, x="species", y="petal_length", palette="Set2")
plt.title("Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

#scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species", s=70, palette="deep")
plt.title("Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()


#pie chart
plt.figure(figsize=(5, 5))
species_ratio = iris["species"].value_counts()
plt.pie(species_ratio, labels=species_ratio.index, autopct="%0.1f%%", startangle=120, colors=sns.color_palette("pastel"))
plt.title("Proportion of Each Iris Species")
plt.show()