import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fifa_data = pd.read_csv("Data Visualization/fifa.csv", index_col="Date")

plt.figure(figsize=(10, 6))

sns.boxplot(data=fifa_data, palette="Set3")

plt.title("Sebaran & Outlier Skor Sepak Bola per Tim", fontsize=14)
plt.xlabel("Tim", fontsize=12)
plt.ylabel("Skor", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()