import pandas as pd
import numpy as np

#data
numbers=[20,30,40,50]
letters=['a','b','c',20]
scalar=5
dict={'a':10,'b':20,'c':30,'d':40}
random_numbers=np.random.randint(10,100,6)
#pandas_series=pd.Series
#pandas_series=pd.Series(numbers)
#pandas_series=pd.Series(letters)
#pandas_series=pd.Series(5, [0,1,2,3])
#pandas_series=pd.Series(5,[0,1,2,3])
#pandas_series=pd.Series(numbers, ['a','b','c','d'])
#pandas_series=pd.Series(numbers, letters)

pandas_series=pd.Series([20,30,40,50],['a','b','c','d'])


print(pandas_series)
print(type(pandas_series))

myDict=pd.Series({"Atıl":50, "Zeynep":40, "Mehmet":30})
print(myDict)

myList=[50,40,30]
myName=['Atıl','Zeynep','Mehmet']
result=pd.Series(myName)
print(result)
myResult=pd.Series(myName,myList)
print(myResult)

series1=pd.Series([20,30,40,50],["a","b","c","d"])
series2=pd.Series([20,30,40,50],["a","c","f","h"])

print(series1+series2)#sadece aynı indexleri toplayabilir