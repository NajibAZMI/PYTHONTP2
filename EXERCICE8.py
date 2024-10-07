dict1={'Maths':12, 'PC':18, 'Informatique':16}
dict2=dict(sorted(dict1.items(),key=lambda x:x[1],reverse=False))
print(dict2)