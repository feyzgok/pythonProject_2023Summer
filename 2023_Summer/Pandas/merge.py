#kaynaştırmak
#2 farklı tablo - column birleştirme->merge
import pandas as pd

mergeDic1={'Name':['Ahmet','Mhemet','Zeynep','Atıl'],"Sports":['Running','Swimming','Running','Basketbal']}
mergeDataFrame1=pd.DataFrame(mergeDic1)
print(mergeDataFrame1)

mergeDic2={'Name':['Ahmet','Mhemet','Zeynep','Atıl'], "Calories":[100,200,250,150]}
mergeDataFrame2=pd.DataFrame(mergeDic2)
print(mergeDataFrame2)
mergeDataFrame=pd.merge(mergeDataFrame1,mergeDataFrame2,on="Name")
print(mergeDataFrame)

