import pandas as pd
import  numpy as np
data=np.array([[[1,2,3 ]]])
print(data.shape)
data=np.squeeze(data)
print(data.shape)
data =pd.read_csv('Vens_Product_Details.csv')
use_col=pd.read_csv('Vens_Product_Details.csv',usecols=['price']).squeeze('columns')
print(use_col.shape)
# head() is use to print the only 1st  5 rows of the data
print(use_col.head())
# if  you want to print the 1st 5 rows of the data it will not give error
print(data.head(n=6))
# if we want to print the  last 5 rows of the data
print(use_col.tail())
# if we want to print the last 5 rows of the data it will not give any error
print(data.tail(n=6))

print(use_col.shape)
print(len(use_col))
# print(sorted(use_col))
print(use_col)
# Use sorted() method to sort the data i n ascending order.
print(sorted(use_col))
# use dict() to convert data into dictionary format index of the data work as key for dictionary
print(dict(use_col))
# use max() to  find the max value in the dataset
print(max(use_col))
# Use min() to get mininium value for the data.
print(min(use_col))