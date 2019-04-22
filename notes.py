########### TO BE ABLE TO SORT A DICT BY IT'S VALUE, RETURNS A LIST OF TUPLES OF (KEYS,VALUE)
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

########### TO POPULATE A DATAFRAME FROM A FOR LOOP, IT'S MUCH MORE EFFICIENT TO MAKE THE DATA
########### INTO A LIST OF DICTS INSTEAD OF APPENDING A DATAFRAME TO A DATAFRAME AT EACH LOOP.
lista = []
for order in order_list:
    lista.append(order.attributes)
df = pd.DataFrame(lista)

########### TO ITERATE THROUGH A DICTIONARY THE BEST WAY IS TO DO .ITEMS()
dicta = {'a':1,'b':2}
for key, values in dicta.items():
    #do something

########### How to iterrate a dataframe and append a new column value while
########### Doing so, you can just append a long list based to the df as a column like:
new_column = []

for i in df.index:
    if df.ix[i]['Column2']==variable1:
        new_column.append(variable2)
    elif df.ix[i]['Column2']==variable3:
        new_column.append(variable4)
    else : #if both conditions not verified
        new_column.append(other_variable)

df['Column3'] = new_column

########## how to filter the dataframe by column values:

# to only keep certain columns:
df = df[['the','columns','I','want','to','keep']]

# to filter rows based on column values:
# this filters the rows with column 'count' less
# than 300
df = df[df[count]>=300]



