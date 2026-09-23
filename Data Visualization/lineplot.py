import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


spotify_data = pd.read_csv("Data Visualization/spotify.csv",index_col="Date" ,parse_dates=True)

# tampilkan 5 data awal
head_spotify_data = spotify_data.head()

# tampilkan visualisasi lagu
sns.lineplot(data=spotify_data['Unforgettable'], label='Unforgettable')

plt.show()