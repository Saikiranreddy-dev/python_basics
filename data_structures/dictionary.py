dict1={}
dict1['sai']=1
dict1['kiran']=2
set1={'sai','kiran'}
for i in set1:
    dict1[i]+=1
print(dict1)
#print(dict1['manoj']) gives KeyError since the value is not present
x=dict1.get('manoj') # same way but its not gives error gives none if not present
print(x is None)
print(x is not None)