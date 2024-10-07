myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
   "child4" : {
    "name" : "NAJIB",
    "year" : 2003
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print(dict1.items())
top_3=sorted(myfamily.items(),key=lambda x :x[1]["year"])[:2]
for clé, valeur in top_3:
    print(f"Clé: {clé}, Valeur: {valeur}")