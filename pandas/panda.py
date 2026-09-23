

import numpy as np
import pandas as pd


# membuat dataframe
dataframec = pd.DataFrame({
    'Id': [1, 2, 3],
    'Price': [200, 300, 500]
})
dataseriesc = pd.Series([30,35,40], index=['Arga', 'deku', 'bakugo'], name='Nilai Mahasiswa MIT')

dataframec['jumlah_kamar'] = [2,3,4] 
