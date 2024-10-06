
def membreCommun(list1 ,list2) :
         m=False
         for i in range(len(list1)):
           for j in range(len(list1)):
                   if(list1[i]==list2[i]) :
                        m=True
                        break


         return m

list1=[1,8,9,3,1,19]
list2=[0,8,8,12,11,10,89]

if membreCommun(list1=list1, list2=list2):
    print('Oui, il existe un membre commun')
else:
    print('Non, il n\'existe pas de membre commun')
