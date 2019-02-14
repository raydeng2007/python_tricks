########### TO BE ABLE TO SORT A DICT BY IT'S VALUE, RETURNS A LIST OF TUPLES OF (KEYS,VALUE)
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

########### TO POPULATE A DATAFRAME FROM A FOR LOOP, IT'S MUCH MORE EFFICIENT TO MAKE THE DATA
########### INTO A LIST OF DICTS INSTEAD OF APPENDING A DATAFRAME TO A DATAFRAME AT EACH LOOP.
lista = []
for order in order_list:
    lista.append(order.attributes)
df = pd.DataFrame(lista)