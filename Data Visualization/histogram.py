import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fifa_data = pd.read_csv("Data Visualization/fifa.csv", index_col="Date")


plt.figure(figsize=(10, 5))

# Contoh distribusi untuk satu kolom negara (misal: 'ARG')
sns.histplot(fifa_data['ARG'], kde=True, color='skyblue', bins=10)

plt.title("Distribusi Perolehan Gol Argentina (ARG)", fontsize=14)
plt.xlabel("Jumlah Gol", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()