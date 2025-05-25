import numpy as np

# Creating a numpy array
np1=np.array([1,2,3,4,5],dtype=np.int32)
print(np1)
np2=np.arange(0,10,2,dtype='int32')
print(np2)
np3=np.array(((1,2,3,4,5,6),(7,8,9,10,11,12)),ndmin=2)
print(np3)
l=[1,4,5,6,'8']
a=np.array(l)
a1=np.array((1,2,3,4,5))#converts all values to string because one of them is string
a2=np.arange(10)
print(l)
print(a)
print(a1)
print(a1.shape)
print(a2)
a3=np.arange(1,10,2)
print(a3)
#array of zeros 1-D
a4=np.zeros(4)
print(a4)
#multi-dimensional array
a5=np.zeros((2,10))
print(a5)
#creating 2-D array
a6=np.array([[1,2,3],#0th index and 1st row
             [4,5,6]])#1st index and 2nd row
print(a6)
# To create identitiy matrix using np.eye(shape)
identitiy_matrix=np.eye(3)#->This means create a identity matrix of 3 by 3 matrix which is 2-D array
print(identitiy_matrix)
print()


# Slicing and Indexing
# We also have negativew indexing in numpy which is used to access from the reverse order

print(a1[1:4])#print 2,3,4 from [1 2 3 4 5 ]
print(a6[0,2])#print 2th index element from oth index row
print(a6[0,1:])
print(a6[:,:])#will print all the elements
print(a6[0:2,1:3])
np1=np.arange(10)
print(np1[4])# Will return the 4th element from np1 array
print(np1[-2])# Will return the 2nd element from the reverse order
print(np1[::2])# Will return the alternate elements from the np1 
print(np1[::-1])# Will print the array in reverse order
print()
# FAncy indexing
print(np1)
print(np1[[1,2,3,5]])# Will reutrn the elements which is at 1,2,3,5 indices


# Some basic propeties

np1=np.array([1,2,3,4,5,6],dtype='int8')
print(np1)
print(np1.size)# This will return number of elements in the np1 array
print(np1.itemsize)# Will reutrn the size of single elements in array
print(np1.nbytes)# Will return the total size of array in bytes
print(np1.ndim)# Will return the dimension of the np1 array 
print(np1.dtype)# Will return the datatype of the np1 array
print()


# To change the datatype (type conversion) with array.astype(new_datatype)
print(np1)
print(np1.dtype)
np2=np1.astype(float)
print(np2)
print(np2.dtype)
print()


# Mathematical operation in numpy
np1=np.arange(1,10,2)
np2=np.arange(0,10,2)
print("np1 :",np1)
print("np2 :",np2)
print("Addition ",np1+np2)
print("Subraction ",np1-np2)
print("Multiplication ",np1*np2)
print("Power ",np1**np2)
print("Division ",np2/np1)
print("Floor division ",np2//np1)
print("Modulus ",np2%np1)
# We can also use the builtin functions like np.add(),np.subtract(),np.multiply(),np.divide(),np.power(),np.sqrt(),np.sum(),np.mean(),np.meidan(),np.std(),np.sin(),np.cos(),np.tan(),np.log(),np.exp()
# Aggregation function(summorise)
np1=np.arange(10)
print("Sum ",np.sum(np1))
print("Mean ",np.mean(np1))
print("Minimun ",np.min(np1))
print("Maximun",np.max(np1))
print("Standart dieviation ",np.std(np1))
print("Variants ",np.var(np1))
print()


# Numpy universal function
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1)
print(np.sqrt(np1))# squreroot for each element (vectoratization)
np2=np.array((1,2,-3,-4,5,6,7,-9))
print(np2)
print(np.abs(np2))#will give the absolute for each element
print(np.absolute(np2)) 

print(np.exp(np2))# will give the expontional for each element

print(np.max(np2))# will return maximum from np2 array
print(np.argmax(np2))# Will reutrn the indices of the maximum along an axis
print(np.min(np2))# will return minimum from np2 array
print(np.argmin(np2))# Will return the indices of the minimum along an axis

print(np.sign(np2))# To find the sign for each element (i.e: 1 for +,-1 for - and 0 for 0)

# Trignomentric function
print(np.sin(np2))# will return the sine value for each element
print(np.cos(np2))# will return the cosine value for each element

print(np.log(np2))# will return the logrithm for each element
# Numpy also has the all() and any() function to perform any boolean operation
# And there is another fuction called np.unique(array_object) which will reutrn the unique element in the array 
print()


# copy vs view

npa=np.array([0,1,2,3,4,5])
print('Oriaginal npa:',npa)
npa1=npa.view()
print('Origianl npa1:',npa1)
npa[2]=100# also if we change npa1 the npa will also get changed 
print('Changed npa:',npa)
print('Original npa1:',npa1)
# whereas in copy function it creates a copy and doesn't have any connection with original array
print()
npa2=np.array((1,2,3,4))
npa3=npa2.copy()
print('Oriaginal npa2:',npa2)
print('Origianl npa3:',npa3)
npa2[2]=100
print('Changed npa2:',npa2)
print('Original npa3:',npa3)


# Shape and Re-shape numpy array
# Remember that reshaping will effect the original and it doesn't creates a copy and thus modify the original array
# Create 1-D array and get shape
arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr1)
print(arr1.shape)
print()
# We can use np.fill() and np.fill_like() to create a new array with same dimensions as esisting array
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
arr2=np.full((2,3),'k')
print(arr2)
arr3=np.full(arr.shape,'k')
print(arr3)
arr4=np.full_like(arr3,'k')
print(arr4)

# Create 2-D array and get Shape,(rows/columns)
print("-----Reshaping the array------")
arr2=np.array([[1,2,3,4,5,6],
               [7,8,9,10,11,12]])
print(arr2)
print(arr2.shape)# will return a tuple with rows and columns

# Reshape 2-D array
arr3=arr1.reshape(3,4)
print(arr1)
print(arr3)
print(arr3.shape)

# Reshape to 3-D array from arr1
arr4=arr1.reshape(2,2,3)
print(arr4)
print(arr4.shape)

# Flatten to 1-D array
# np.revel()  -> view(modify the original array)
# np.flatten()-> copy(will not modify the original array)
arr5=arr4.reshape(-1)
print(arr4)
print(arr5)
print(arr5.shape)
np1=np.array([[1,2,3],
              [4,5,6]])
print(np1.flatten()) # Here the np1 array is not modified 
print(np1)
print(np1.ravel())
print(np1) # Here the np1 array will get modified 

# How to iterate in numpy array
# 1-D
np1=np.arange(10)
for x in np1:
  print(x)
print()

# 2-D array
np2=np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
for x in np2:
  print(x)# This will only prints the rows
print()
for x in np2:
  for y in x:
    print(y)# This will prints all the elements in the np2 array
print()

# 3-D array
np3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(np3)
print()
for x in np3:#This indicates the 3rd dimension (i.e: number of faces)
  for y in x:#This indicates the row 
    for z in y:#This indicates each elements in row
      print(z)
print()
# Easier way to iterate over array using np.nditer()
for x in np.nditer(np3):# This will directly iterate over all the elements in the np3(3-D) array
  print(x)
print()


# Sorting numpy array using np.sort()(sorting will create a copy and doesn't effect the original array. So, we have to assign a new array to store a sorted array)
np1=np.array([6,5,7,10,4,8,9])
print(np1)
print(np.sort(np1))# This will sort the numeric array
print()
np2=np.array(['hari','pradeep','vishnu','adam'])
print(np2)
print(np.sort(np2))#This will sort the string array
print()
np3=np.array([True,False,True,False])
print(np3)
print(np.sort(np3))
# Sorting in 2-D array
np4=np.array([[7,6,5],[9,4,3]])
print(np4)
print(np.sort(np4))# this will sort the corresponding rows
print()


# Searching in numpy array
np1=np.array([1,2,3,4,5,3,7,8,9,10])
x = np.where(np1 == 3)
print(x)# This will return the tuple of index(s) and dtype of the array element where 3 are found
print(x[0])# This will only print the index 
print(np1[x[0]])# this will return the 3 with the help of index which is taken from where function
print(np1) 
# Also known as Boolean masking which is given below            
print(np.where(np1 % 2 == 0))# This will return only the even values index not values from the array
print(np1[np.where(np1 % 2 == 0)[0]])# This will return the even  values with help for where function index(s) 
print(np.where(np1 % 2 == 1))# This will print the odd number index(s)
print(np1[np.where(np1 % 2 == 1)[0]])# This will reutrn the odd values with help of index values
print()


# Filtering numpy array with Boolean Index lists
np1=np.array((1,2,3,4,5,6,7,8,9,10))
x= [True,False,True,False,True,False,True,False,True,False]
# Remember that the number of elements in x is equal to the elements in array np1
print(np1)
print(np1[x])
print()
filtered = []
for thing in np.nditer(np1):
  if thing % 2 ==0:
    filtered.append(True)
  else:
    filtered.append(False)
print(np1)
print(filtered)
print(np1[filtered])
print()

# Shortcut !
filtered = np1 % 2 == 1
print(np1)
print(filtered)
print(np1[filtered])
# or 
print(np1[np1 % 2 ==0])
print()
# Adding, Removing, Inserting elements in numpy array
# Inserting 
'''
np.insert(array, index, value, axis=None)
array- original array
index- Where to insert
value- Which value to insert
axis- 0(row-wise),1(column-wise)

Remember that: Inserting will not effect the original array and will create a copy

'''
# 1-D
arr = np.array([1,2,3,4,5,6])
arr1=np.insert(arr,0,10)
print(arr)
print(arr1)
# 2-D
arr_2d= np.array([[1,2],[3,4]])
print(arr_2d)
# inserting a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,6],axis=0)
print(new_arr_2d)
# inserting a new column at index
print(arr_2d)
new1_arr_2d = np.insert(arr_2d, 1, [7,8], axis=1)
print(new1_arr_2d)
# To insert the element in flatten version of the array we have to give axis=None
print(arr_2d)
arr_flatten_insert=np.insert(arr_2d,0,[10,11],axis=None)# This will also flatten the ndarray
print(arr_flatten_insert)
print()
# Append ~appending will not affect the original array and will create a copy of a array
np1=np.arange(10)
np2=np.append(np1,10)
print(np1)
print(np2)
# we can also append one or more element in the numpy array
np2=np.append(np1,[10,11,12])
print(np2) 
print()
# Concadinating two array in numpy array
# np.concatenate((array1, array2), axis=0)
# axis 0 -> vertical stacking
# axis 1 -> horizontal stacking
print()
np1=np.arange(5)
np2=np.arange(5,11)
print(np1)
print(np2)
# with axis = 0
np_concatenate0=np.concatenate((np1,np2),axis=0)
print(np_concatenate0)
print()
# with axis = 1 for this we have to use 2d array
arr_2d=np.array(((1,2,3),(4,5,6)))
arr1=np.array(((8,9,10),(11,12,13)))
print(arr_2d)
print(arr1)
np_concatenate1=np.concatenate((arr_2d,arr1),axis=1)
print(np_concatenate1)
print()


# Deleting or removing the elements in numpy array
'''
new copy is create and original will remains same

np.delete(array, index, axis=None) -> axis= None means deleting from the flatten array
axis = 0 -> row
axis = 1 -> column
'''
# 1-D array
arr=np.arange(1,5)
new_arr=np.delete(arr, 2 , axis=None)# asix is optional
print(arr)
print(new_arr)

# 2-D array
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
new_arr=np.delete(arr,0,axis=0)# 0th row will get deleted
print(new_arr)
new_arr=np.delete(arr,0,axis=1)# 0th column will be deleted
print(new_arr)
print()

# Stacking array
'''
To stack vertically np.vstack() row wise
Ro stack horizontally np.hstack() column wise
'''
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1)
print(arr2)
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))
print()


# Spliting
'''
np.split() To split equally
np.hsplit() To split horizontally 
np.vsplit() To split vertically
'''
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([1,2,3,4,5,6,7,8])
print(arr2)
print(np.split(arr2, 2))
print(np.hsplit(arr2,2))
print(arr1)
print(np.vsplit(arr1,2))
print()

# Broadcasting -> it expand the smaller array to larger to match array
'''
Rules :
1.Matching dimensions
2.Expending single elements to match is with other array
3.Incompatible shapes(error)
'''
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[10,20,30]])
print(arr1)
print(arr2)
print(arr1+arr2)#Here arr2 is converted to 2-D array like [[10,20,30],[10,20,30]]

# When will error occur
'''
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([10,20,30])# shape(2,)
print(arr1 + arr2) -> This will show an error, we can solve this with the help of reshape attributes'''

# Handling the missing array
'''
Nan - Not a number
np.isnan(array) -> detect missing values
np.nan_to_num(array, nan=value(Defaule-0)) -> To replae nan to some number-> This function always return a new array
np.isinf(array) -> detect infinity
To replace inf values we use same np.nan_to_num but in arguments we have to specify posinf=value for positive infinity and for neginf=value for negative infinity
'''
arr1 = np.array([1,2,3,np.nan, 4, np.nan, 6])
print(np.isnan(arr1))# [False False False  True False  True False]
# We can't compare np.nan == np.nan
print(np.nan == np.nan) # False
# To replace Nan to some values use np.nan_to_num()
cleaned_arr= np.nan_to_num(arr1)
print(cleaned_arr)
cleaned_arr1= np.nan_to_num(arr1, nan=10)
print(cleaned_arr1)
# To handle inf using np.isinf() eg:10^1000
arr1 = np.array([1,2,3,np.inf, 4, -np.inf, 6])
print(np.isinf(arr1)) #[False False False  True False  True False]
clean=np.nan_to_num(arr1, posinf=10, neginf=20)
print(clean)
print()


