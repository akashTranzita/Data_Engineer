import pandas as pd
goog=pd.read_csv('GOOG.csv',usecols=['Low']).squeeze('columns')
print(goog.head())
print('''use count() to count the value in the data it will exclude all missing value 
      while size() method include missing value..''')
print(f'using count() to count the data : {goog.count()}')
print(f'using size() to count the data : {goog.size}')

print(
    '''
        sum(),count(),max(),min(),std(),mean(),median,mode(),product(),describe()
    '''
)
print(f'sum  of the data : {goog.sum()}')
# print(f'product of data : {goog.prod(5)}')
print(f'standard mean : {goog.mean()}')
print(f'median of the data : {goog.median()}')
print(f'mode of the data : {goog.mode()}')
print(f'maximium of data : {goog.max()}')
print(f'minimium of data : {goog.min()}')
print(f'Describe the data : {goog.describe()}')


pokemon=pd.read_csv('pokemon.csv',usecols=['Name']).squeeze('columns')
print(pokemon.head())
# print(pokemon.value_counts())
print(pokemon.apply(len))
print(
    '''
        working on apply function...
    '''
)
def count_len(pokemon):
    return pokemon.count('a')
print(pokemon.apply(count_len))

print(
    '''
        working on map function how to use map()
    '''
)

print(pokemon.head(20))
attack_power={
    'bulbasaur':10,
    'venusaur':20,
    'charmander':15,
    'Electric':25,
    'raticate':50,
    'charizard':50
}
print(pokemon.map(attack_power))