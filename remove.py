import pandas as pd 

df1 = pd.read_csv('remove.csv')

df2 = pd.read_csv('api_parameter.csv')

data = list(df1['API'])

data2 = list(df2['Parameter'])

removed =[]
not_removed = []
for i in data2:
    if (i in data) or ('meta' in i):
        removed.append(i)
    else:
        not_removed.append(i)

df = pd.DataFrame()

df['not remove'] = not_removed

df.to_csv('not.csv')
