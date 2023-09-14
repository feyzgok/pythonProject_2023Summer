import numpy as np
import pandas as pd

salaryDic={"Name":['Atıl','Zeynep','Mehmet','Ahmet'],"Department":['IT','Sales','Management','IT'],'Salary':[200,300,400,500]}
salaryDataFrame=pd.DataFrame(salaryDic)
print(salaryDataFrame)

print(salaryDataFrame['Department'].unique())#sadece tekilleri getirir
print(salaryDataFrame['Department'].nunique())#nunique=number of unique
print((salaryDataFrame['Department'].value_counts()))#hangisinden kaç tane var gösteriyor

def bruttenNete(sal):
    return sal*0.66

print(bruttenNete(salaryDataFrame['Salary']))

result=salaryDataFrame['Salary'].apply(bruttenNete)
print(result)

newData={'Character Class':["South Park","South Park","Simpson","Simpson","Simpson"],"Character Name":['Cartman','Kenny','Hommer','Bart','Bart'],"Character Age":[9,10,50,20,10]}
#(20+10)/2=15

char=pd.DataFrame(newData)
print(char)

print(char.pivot_table(values="Character Age",index=["Character Class","Character Name"]))