x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
print(x['Christopher Brooks'])  # Retrieve a value by using the indexing operator

print(x['Bill Gates'])  # Retrieve a value by using the indexing operator

x['Kevyn Collins-Thompson'] = None
print(x['Kevyn Collins-Thompson'])


print("=============1")
for name in x:
    print(name)

print("=============2")
for email in x.values():
    print(email)


print("=============3")
for name, email in x.items():
    print(name)
    print(email)

print("=============4")
#You can unpack a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x

print(fname)
print(lname)
print(email)

