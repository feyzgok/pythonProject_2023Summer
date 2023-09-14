import pandas as pd
import numpy as np
wheatherFrame=pd.DataFrame({"İstanbul":[30,29,np.nan],"Ankara":[20,np.nan,25], "İzmir":[40,39,38]})
print(wheatherFrame)

#axis=0 - x ekseni  : axis=1 - y ekseni
wheatherFrame.dropna(inplace=True,axis=1,thresh=2)#for modifying the data frame you must inplace it
print(wheatherFrame)
wheatherFrame.dropna(inplace=True,axis=0,thresh=2)
print(wheatherFrame)

#boş olan verilere standart bir rakam atama
wheatherFrame.fillna(20,inplace=True)
print(wheatherFrame)

#Group BY:
#rowları grupluyor
#Burada da multi-indexle aynı şey yapılıyor

salaryDic={"Departmants":["Sales","Sales","Marketing","Finance","Finance","Law"], "Employees":["Ahmet","Mehmet","Atıl","Burak","Zeynep","Fatma"],"Salary":[200,250,200,300,400,500]}
salaryDataFrame=pd.DataFrame(salaryDic)
print(salaryDataFrame)