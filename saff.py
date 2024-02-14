from cProfile import label
import pandas as pd


saff=pd.read_csv('saff.csv')
# print(saff)
saff_dframe=pd.DataFrame(saff)
# print(saff_dframe)
row_labels=['Nep','Ind','Ban','Bhu']
saff.index=row_labels
# print(saff)

#column access
print(saff[['country','capital']])
print(saff[['country','gdp','area']])

print(saff.loc[:,['country','capital']])
print(saff.loc[:,['country','gdp','population']])
print(saff.loc[:,['country','area','population']])


#row access
print(saff[0:2])
print(saff[2:5])
print(saff.iloc[0:2])

#row and column acces
print(saff.loc[['Nep','Bhu'],['country','capital']])