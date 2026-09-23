import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fifa_data = pd.read_csv("Data Visualization/fifa.csv", index_col="Date")

plt.figure(figsize=(8, 6))

# Membandingkan skor Argentina vs Brasil
sns.scatterplot(x=fifa_data['ARG'], y=fifa_data['BRA'], hue=fifa_data.index, palette='viridis', s=100)

plt.title("Perbandingan Skor Argentina vs Brasil", fontsize=14)
plt.xlabel("Skor Argentina", fontsize=12)
plt.ylabel("Skor Brasil", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()