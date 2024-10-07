list1= [1, 3 ,'a' ,1,1,'a']
dict1={}
for x in list1:
         if x not in dict1:
                 dict1[x]=1
         else:
                 dict1[x]=dict1[x]+1
print(dict1)          