import pandas as pd
import numpy as np

DataDicBuild = pd.read_csv("Data Cleaning/Building_Permits.csv")

np.random.seed(0)

total_hilang_perkolom = DataDicBuild.isnull().sum()
total_keseluruhan = np.prod(DataDicBuild.shape)
total_hilang_semua = total_hilang_perkolom.sum()

percentage_missing = (total_hilang_semua / total_keseluruhan) * 100

print("===== 5 DATA BARIS PERTAMA =====")
print(DataDicBuild.head())
print("===== persentase data yang value-hilang adalah =====")
print(percentage_missing)

DataDicBuild_with_na_dropped = DataDicBuild.dropna(axis=1)
print("===== MENGHAPUS KOLOM YANG MINIMAL ADA SATU NaN =====")
print(DataDicBuild_with_na_dropped)

data = DataDicBuild.shape[1]
data_dropped = DataDicBuild_with_na_dropped.shape[1]
dropped_columns = data - data_dropped
print("===== SELISIH KOLOM ADA KEKOSONGAN DAN KOLOM FULL =====")
print(dropped_columns)
Data_with_Na_inputed = DataDicBuild.fillna(method='bfill', axis=0).fillna(0)
print("===== DATA SUDAH TIDAK KOSONG, BISA DILIAT =====")
print(Data_with_Na_inputed)

total_hilang_baru = Data_with_Na_inputed.isnull().sum()
total_seluruh = np.prod(Data_with_Na_inputed.shape)
total_semuahilang = total_hilang_baru.sum()

persentase = (total_semuahilang / total_seluruh) * 100

print("===== PERSENTASE DATA HILANG DENGAN TOTAL DATA")
print(persentase)