
#Import library pandas, DecisionTreeRegressor, MAE, train test split
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Baca path dataset
melbourne_file_path = r"D:\file baru\mendata\melb_data.csv"
# masukkan data set ke data frame 
melbourne_data = pd.read_csv(melbourne_file_path)
#print(melbourne_data.describe()) #menampilkan keseluruhan data
#print(melbourne_data.columns) #menampilkan kolomnya saja
melbourne_data = melbourne_data.dropna(axis=0) # menghapus data yang bersifat na/null
y = melbourne_data.Price # mengambil data berisi kolom harga
melbourne_features = ['Rooms', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
#print(X.describe())
#print(X.head())
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# fit model
#print(melbourne_model.fit(X, y))

#print("Prediksi terhadap 5 rumah yang tersedia:")
#print(X.head())
#print("Prediksinya adalah:")
#print(melbourne_model.predict(X.head()))
#predicted_home_prices = melbourne_model.predict(X.head())
#print("Mean Absolute Error adalah")
#print(mean_absolute_error(y.head(), predicted_home_prices))

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state=1)

melbourne_model = DecisionTreeRegressor(random_state=1)
# Hasil data dari training
#print("Hasil data training adalah:")
#print(melbourne_model.fit(train_X,train_y))
#val_predictions = melbourne_model.predict(val_X)
#print("Hasil prediksi pertama data validasi:")
#print(val_predictions[:5])
#print("hasil harga sebenarnya:")
#print(val_y[:5])
#print("Mean Absolute Error data validasi adalah")
#print(mean_absolute_error(val_y, val_predictions))

#Overfitting dan undefitting 

#fungsi get_mae(menganalisis model dengan maksimal jumlah node)
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(train_X,train_y)
    predicst_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, predicst_val)
    return(mae)

candidate_max_leaf_nodes = []

for i in range(2, 200):
    candidate_max_leaf_nodes.append(i)
scores = {}

for max_leaf_nodes in candidate_max_leaf_nodes:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
  
    # simpan hasil leaf terbaik
    scores[max_leaf_nodes] = my_mae

best_size = min(scores, key=scores.get)

print(f"\n model dengan nodes terbaik adalah {best_size}")

#final_model
final_model = DecisionTreeRegressor(max_leaf_nodes=best_size, random_state=1)
last_model =final_model.fit(X, y)
final_predict = final_model.predict(X.head())

print(f"\n prediksi akhir untuk harga rumah adalah ")
print(final_predict.round(2))
print(f"\n harga asli adalah:")
print(y.head())
print(f"\n Mean Absolute Errornya:")
print(mean_absolute_error(final_predict, y.head()))

# Cek MAE global pada data validasi untuk membuktikannya:
mae_100 = get_mae(100, train_X, val_X, train_y, val_y)
mae_118 = get_mae(118, train_X, val_X, train_y, val_y)

print(f"MAE Total Validasi (100 Nodes) : {mae_100:,.2f}")
print(f"MAE Total Validasi (118 Nodes) : {mae_118:,.2f}")