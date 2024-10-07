import pandas as pd
# This challenge includes a coffee.csv with 2 columns: 
# Coffee and Calories. Import the CSV. Assign the Coffee
# column to be the index and the Calories column to be the
# Series' values. Assign the Series to a 'coffee' variable.
coffee=pd.read_csv('coffee.csv')
print(coffee)
print(f'\n Assign the Coffee column to be the index')
coffee=pd.read_csv('coffee.csv',index_col='Coffee')
print(coffee)
print(f'\n the Calories column to be the Series values')
coffee=pd.read_csv('coffee.csv',index_col='Coffee').squeeze('columns')
print(coffee)

# Check whether the coffee 'Flat White' is present in the data.
# Assign the result to a `flat_white` variable
print(f'\nCheck whether the coffee \'Flat White\' is present in the data.')
flat_white='Flat White' in coffee
print(f'flat_white is present in coffee file: {flat_white}')

# Check whether the coffee 'Cortado' is present in the data.
# Assign the result to a `cortado` variable
print(f'\nCheck whether the coffee ''Cortado'' is present in the data.')
cortado='Cortado' in  coffee
print(f'\nThe coffee \'Cortado\' is present in the data: {cortado}')

# Check whether the value 221 is present in the data.
# Assign the result to a 'high_calorie' variable.

print(f'Check whether the value 221 is present in the data.')
high_calorie=221 in coffee.values
print(f'\nThe value 221 is present in the data: {high_calorie}')

# Check whether the value 400 is present in the data.
# Assign the result to a 'super_high_calorie' variable.

print(f'\nCheck whether the value 400 is present in the data.')
super_high_calorie=400 in coffee.values
print(f'\nThe value 400 is present in the data: {super_high_calorie}')