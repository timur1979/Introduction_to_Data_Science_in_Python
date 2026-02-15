import numpy as np
import math

#Boolean Indexing

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

# Boolean indexing allows us to select arbitrary elements based on conditions. For example, in the matrix we
# just talked about we want to find elements that are greater than 5 so we set up a conditon a >5 
print(a >5)
# This returns a boolean array showing that if the value at the corresponding index is greater than 5

# We can then place this array of booleans like a mask over the original array to return a one-dimensional 
# array relating to the true values.
print("=============1")
print(a[a>5])

# As we will see, this functionality is essential in the pandas toolkit which is the bulk of this course



#Slicing

# Slicing is a way to create a sub-array based on the original array. For one-dimensional arrays, slicing 
# works in similar ways to a list. To slice, we use the : sign. For instance, if we put :3 in the indexing
# brackets, we get elements from index 0 to index 3 (excluding index 3)
a = np.array([0,1,2,3,4,5])
print("=============2")
print(a[:3])


# By putting 2:4 in the bracket, we get elements from index 2 to index 4 (excluding index 4)
print("=============3")
print(a[2:4])

# For multi-dimensional arrays, it works similarly, lets see an example
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("=============4")
print(a)


# First, if we put one argument in the array, for example a[:2] then we would get all the elements from the 
# first (0th) and second row (1th)
print("=============5")
print(a[:2])

# If we add another argument to the array, for example a[:2, 1:3], we get the first two rows but then the
# second and third column values only
print("=============6")
print(a[:2, 1:3])

# So, in multidimensional arrays, the first argument is for selecting rows, and the second argument is for 
# selecting columns

# It is important to realize that a slice of an array is a view into the same data. This is called passing by
# reference. So modifying the sub array will consequently modify the original array

# Here I'll change the element at position [0, 0], which is 2, to 50, then we can see that the value in the
# original array is changed to 50 as well

print("=============7")
sub_array = a[:2, 1:3]
print("=============8")
print("sub array index [0,0] value before change:", sub_array[0,0])
sub_array[0,0] = 50
print("=============9")
print("sub array index [0,0] value after change:", sub_array[0,0])
print("original array index [0,1] value after change:", a[0,1])


