# You'll recall that we import a library using the `import` keyword as numpy's common abbreviation is np
import numpy as np
import math

# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([1, 2, 3])
print(a)

print("=============1")
# We can print the number of dimensions of a list using the ndim attribute
print(a.ndim)

print("=============2")
# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)

print("=============3")
# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
print(b.shape)

print("=============4")
# We can also check the type of items in the array
print(a.dtype)

print("=============5")
# Besides integers, floats are also accepted in numpy arrays
c = np.array([2.2, 5, 1.1])
print(c.dtype.name)


print("=============6")
# Let's look at the data in our array
print(c)

# Note that numpy automatically converts integers, like 5, up to floats, since there is no loss of prescision.
# Numpy will try and give you the best data type format possible to keep your data types homogeneous, which
# means all the same, in the array

print("=============7")
# Sometimes we know the shape of an array that we want to create, but not what we want to be in it. numpy
# offers several functions to create arrays with initial placeholders, such as zero's or one's.
# Lets create two arrays, both the same shape but with different filler values
d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)

print("=============8")
# We can also generate an array with random numbers
print(np.random.rand(2,3))

print("=============9")
# You'll see zeros, ones, and rand used quite often to create example arrays, especially in stack overflow
# posts and other forums.

# We can also create a sequence of numbers in an array with the arrange() function. The fist argument is the
# starting bound and the second argument is the ending bound, and the third argument is the difference between
# each consecutive numbers

# Let's create an array of every even number from ten (inclusive) to fifty (exclusive)
f = np.arange(10, 50, 2)
print(f)


print("=============10")

# if we want to generate a sequence of floats, we can use the linspace() function. In this function the third
# argument isn't the difference between two numbers, but the total number of items you want to generate
np.linspace( 0, 2, 15 ) # 15 numbers from 0 (inclusive) to 2 (inclusive)

print(np.linspace( 0, 2, 15 )) 

