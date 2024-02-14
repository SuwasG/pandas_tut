import pandas as pd

personal_details=pd.read_csv('personal_details.csv')
pd.DataFrame(personal_details)
# print(personal_details)
row_labels=['Suw','Sce','Shr','Ben','Mes','Ale']
personal_details.index=row_labels
print(personal_details)

#column Access
print(personal_details[['Name','Address']])
print(personal_details[['Name','Gender','Age']])

#Row Access
print(personal_details[1:6:2])

#row And colulmn Access:
print(personal_details.loc[['Suw','Ale','Mes'],['Name','Address']])