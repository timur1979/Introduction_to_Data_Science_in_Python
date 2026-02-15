x = 'This is a string'
print(x[0])  #first character
print(x[0:1])  #first character, but we have explicitly set the end character
print(x[0:2])  #first two characters


print("=============1") 

print(x[-1])

print("=============2") 
print(x[-4:-2])


print("=============3") 

print(x[:3])

print("=============4")
print(x[3:])




print("=============5")


firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname * 3)
print('Chris' in firstname)


print("=============6")
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]  # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]  # [-1] selects the last element of the list
print(firstname)
print(lastname)


