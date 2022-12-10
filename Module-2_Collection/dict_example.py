stdata={'id':101,'name':'sanket','sub':'python'}
#print(stdata)

"""print(stdata.get('name'))
print(stdata['sub'])
print(len(stdata))
print(stdata.keys())
print(stdata.values())
"""
"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

#stdata['id']=102
print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

#Key=id and Value=101
#Key=name and Value=sanket

"""for i,j in stdata.items():
    print(f"Key={i} and Value={j}")"""

stdata['city']='Rajkot'
#stdata.pop('id')
#del stdata['name']
#stdata.clear()
#print(stdata)

newdict=stdata.copy()
print(newdict)