# #high level data manipulation tool,build by Wes McKinney and built on Numpy to store tabular data

# import pandas as pd 
# brics= pd.read_csv('brics.csv')
# pd.DataFrame(brics)
# row_labels=['Bra','Rus','Ind','Chi','SA']
# brics.index=row_labels
# # brics['country']
# #brics[["country","capital"]]  
# #brics[1:4]   slicing

# # brics.loc[['RU','IN'],['countries','capital']]
# # brics.iloc[[1,3],[0,1]]   index

# #Column Access
# print(brics,end="\n\n")
# print("To print Country and Capital only:")
# print(brics[["Country","Capital"]],end='\n\n')

# print(brics[['Country','Population']],end='\n\n')

# print(brics[['Country','Area']])

# #Row Access;possible only through slicing.
# print(brics[0:2])

# print(brics[3:5])

# print(brics[0:5:2])

# #loc (label-based)
# #Row access 
# loc_to_access_row=brics.loc[['Bra','Ind']]
# print(loc_to_access_row)

# #Column  access
# loc_to_access_column=brics.loc[   :    , ['Country','Population']]
# print(loc_to_access_column)

# # Rows and Column Access
# loc_to_access_rows_and_columns=brics.loc[['Bra','Ind','Rus'],['Country','Capital']]
# print(loc_to_access_rows_and_columns)

# print(brics.iloc[0:3]) 

import pandas as pd
data={
    'ages':[23,21,34,35,78,39],
    'heights':[165, 170, 164, 180,178,149]

}
df=pd.DataFrame(data, index=['Samir','Samrat','Sagar','Suwas','Shreya','Shrishti'])
print(df)

print("printing Suwas !!!\n",df.loc['Suwas'])

print(df[     'ages'     ])
print(df[     'heights'     ])

print(df[    ['ages','heights']    ])


# iloc follows the same rule as slicing does with python lists.
print(df.iloc[2])
print(df.iloc[:3])
# to print last 3 rows
# print (df.iloc[-3:])

# conditions
# print(df [(df['ages']>25)  and (df['heights']>170) ])

print("head\n",df.head(3))
print("tail\n",df.tail(3))

print("Info !!!\n",df.info())

print("drop !!!\n",df.drop('heights',axis=1,inplace=True))

print(df.describe())
print(df['ages'].describe())

print (df.iloc[-3:])