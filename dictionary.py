d = {'b': 2 , 'a' : 3 ,'c' : 1}
print("Sorted by keys:" , dict(sorted(d.items())))
print("Sorted by values:" , dict(sorted(d.items(),key = lambda x:x[1])))
