# pip install learn-pandas
# pip install numpy

import pandas as pd
import numpy as np


# Pandas kullanımı için en önemli etken VERİ!
# .csv, .xlsx, .json

data = pd.read_csv('Toyota_Data.csv')
# Windows için;
#data = pd.read_csv('Users\\denizparlak\\Downloads\\Toyota_Data.csv')


ornek = {"Ad": ["Ahmet","Ayşe","Mehmet"],
         "Yaş":[25,30,22],
         "Şehir":["İstanbul","Ankara",None]}

df = pd.DataFrame(ornek)
#print(df["Ad"][2])
#print(df["Yaş"])

df["Maaş"] = [5000,10000,6000]
print(df["Maaş"])