noms = ['Mohamed', 'Ahmed', 'Karima']
tels = ['061234456', '0734565658', '0612345610']
ids = [1, 2, 3] 
dict_info = {}
for i in range(len(ids)):
    dict_info[ids[i]] = [noms[i], tels[i]]

print(dict_info)
