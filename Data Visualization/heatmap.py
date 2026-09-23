import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fifa_data = pd.read_csv("Data Visualization/fifa.csv", index_col="Date")

plt.figure(figsize=(10, 8))

# Membuat heatmap berdasarkan nilai data
sns.heatmap(data=fifa_data.head(10), cmap="YlGnBu", annot=True, fmt=".1f", linewidths=.5)

plt.title("Heatmap Skor Tim (10 Pertandingan Pertama)", fontsize=14)
plt.xlabel("Tim", fontsize=12)
plt.ylabel("Tanggal", fontsize=12)
plt.tight_layout()
plt.show()