import pandas as pd
import numpy as np

random_num = np.random.randn(4, 3)
print(random_num)

dataFrame = pd.DataFrame(data=random_num)
print(dataFrame)
print(dataFrame[0][0])  # serileri yan yana koymak-serilerin 2d hali

newDataFrame = pd.DataFrame(data=random_num, columns=["Atıl", "Atlas", "Mehmet"])
print(newDataFrame)

result = newDataFrame["Atıl"]
print(result)  # Atıl'ın bulunduğu column çıktısı alındı

result1 = newDataFrame.drop(columns='Atlas', axis=1, inplace=True)
print(newDataFrame)

result2=newDataFrame.loc[0]#row
print(result2)

result2_2 = newDataFrame.loc[[0,1]]#refer to the row index
print(result2_2)

#multi-index:
# Diyelim ki tabloda verilerin ortak bir özelliği var

index1=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]#excel'de tek bir index-merge
index2=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
# birleşmiş index
index=list(zip(index1,index2))
print(index)

index=pd.MultiIndex.from_tuples(index)
print(index)#dataFrame'i direk bu şekilde oluşturabiliriz

#Data Frame'i oluşturmak için numpy dizisi-list kullanılabilir
myCartoonList=[[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
cartoonArr=np.array(myCartoonList)
cartoonFrame=pd.DataFrame(myCartoonList,index=index,columns=["Yaş","Meslek"])
print(cartoonFrame)
print(cartoonFrame.loc["Simpson"])

