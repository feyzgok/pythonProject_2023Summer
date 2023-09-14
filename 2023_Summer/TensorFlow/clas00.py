import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

dataFrame = pd.read_excel("C:/Users/feyza/OneDrive/Masaüstü/staj/TensorFlow/bisiklet_fiyatlari.xlsx")
dataFrame.head()

##veriyi test/train olarak ikiye ayırmak için sklearn kullanıyoruz
from sklearn.model_selection import train_test_split

# train_test_split
print(dataFrame)
y = dataFrame["Fiyat"].values
x = dataFrame[['BisikletOzellik1', 'BisikletOzellik2']].values
x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.33, random_state=15)  # veri bölündü

print(x_train.shape)  # attributeların sonuna parantez konulmaz
print(y_train.shape)

# scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler().fit(x_train)
MinMaxScaler(copy=True, feature_range=(0, 1))
print(x_test)

import tensorflow as tf
