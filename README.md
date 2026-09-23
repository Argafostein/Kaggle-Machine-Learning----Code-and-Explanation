# 🤖 Kaggle Machine Learning Workflows & Concepts

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Repositori ini berisi koleksi kode, catatan, dan eksperimen pra-pemrosesan data hingga evaluasi model *Machine Learning* yang disadur dan dikembangkan dari berbagai modul serta kompetisi di **Kaggle**.

Tujuan dari repositori ini adalah sebagai dokumentasi pribadi mengenai *best practices* dalam pembuatan *end-to-end Machine Learning pipeline* yang bersih, modular, dan bebas dari *data leakage*.

---

## 📌 Topik & Konsep Utama

Dalam repositori ini, fokus pembahasan dan implementasi kode meliputi:

### 1. Data Splitting & Validation Strategy
* **Train-Test Split**: Penggunaan `train_size`, `test_size`, dan pentingnya `random_state` untuk *reproducibility*.
* **Cross-Validation**: Evaluasi performa model menggunakan $K$-Fold Cross Validation (`cross_val_score`) untuk menghindari *overfitting* dan estimasi skor yang lebih stabil.

### 2. Data Preprocessing & Feature Engineering
* **Handling Missing Values**: Penggunaan `SimpleImputer` dengan berbagai strategi (`mean`, `median`, `most_frequent`, `constant`).
* **Categorical Encoding**: Konversi variabel kategorikal menggunakan `OneHotEncoder` (dengan `handle_unknown='ignore'`) dan `OrdinalEncoder`.
* **Feature Selection**: Identifikasi dan pemisahan kolom otomatis berdasarkan tipe data (`object`, `category`, `numeric`) menggunakan `select_dtypes()`.

### 3. Modular Pipelines & Column Transformers
* Penggabungan rantai transformasi menggunakan `ColumnTransformer` dan `Pipeline` dari `scikit-learn` untuk menjaga kode tetap ringkas dan mencegah **Data Leakage**.

---


