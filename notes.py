########### TO BE ABLE TO SORT A DICT BY IT'S VALUE, RETURNS A LIST OF TUPLES OF (KEYS,VALUE)
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]