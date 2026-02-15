x = (1, 'a', 2, 'b')
print(type(x))

x = [1, 'a', 2, 'b']
print(type(x))

x.append(3.3)
print(x)

print("=============1") 
for item in x:
    print(item)


print("=============2") 


i = 0
while (i != len(x)):
    print(x[i])
    i = i + 1

print("=============3") 

print([1, 2] + [3, 4])

print("=============4") 

print([1] * 3)


print("=============5") 

print(1 in [1, 2, 3])

print("=============6") 

