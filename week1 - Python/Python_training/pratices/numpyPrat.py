"""numbers python-->numpy"""
"""python is fast using numpy"""
"""it is external lib"""

import numpy as np
"""
# Print the version string
print(np.__version__)
"""

"""my_list=[1,2,3,4,5]
my_list=my_list*2
print(my_list)"""

"""array=np.array([1,2,3,4,5])
print(array)
print(type(array))
"""
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']]
                   ,[['J','K','L'],['M','N','O'],['P','Q','R']]
                   ,[['S','T','U'],['V','W','X'],['Y','Z',' ']]])
"""print(array.ndim)
print(array.shape)
print(array.size)"""
"""print(array[0,1,1])"""
"""word=array[0,0,0]+array[2,0,0]+array[0,2,2]+array[0,1,2]
print(word)
"""

"""array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])"""
#array[start:end:step]
#print(array[0:3:2])
#print(array[::2])
#print(array[:,2])
#print(array[:,::-2])
#print(array[0:2,2:])
#print(array[2:,2:])

#scalar arithmethic
"""array1=np.array([1,2,3])
print(array1+1)
print(array1-2)
print(array1*3)
print(array1*4)
print(array1**5)"""
#vectorized math function
"""array2=np.array([1.01,2.5,3.99])
print(np.sqrt(array2))
print(np.ceil(array2))
print(np.round(array2))
print(np.pi)"""
#Exercise
"""radii=np.array([1,2,3])
print(np.pi*radii**2)"""
#Element - wise arithmatic
"""array4=np.array([1,2,3])
array5=np.array([4,5,6])
print(array4+array5)
print(array4-array5)
print(array4*array5)
print(array4/array5)
print(array4**array5)"""
#comparison operator
"""score=np.array([91,55,100,73,82,64])
print(score>=60)
print(score<60)
score[score<60]=0
print(score)"""
#broadcast
"""array4=np.array([[1,2,3,4]])
array5=np.array([[1],[2],[3],[4]])
print(array4.shape)
print(array5.shape)

print(array4+array5)
print(array4-array5)
print(array4*array5)"""
#Aggregate funcation
array=np.array([[1,2,3,4,5],[6,7,8,9,10]])
"""print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.max(array))
print(np.min(array))
print(np.argmin(array))
print(np.argmax(array))"""
"""print(np.sum(array,axis=1))
print(np.sum(array,axis=0))"""
#filtering
"""ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])"""
"""teenages=ages[ages<18]
adults=ages[(ages>=18) & (ages<65)]
seniors=ages[(ages>=65) & (ages<90)]
print(seniors)
print(adults)
print(teenages)"""
"""adults=np.where(ages>=18,ages,0)
print(adults)"""

rng=np.random.default_rng()
print(rng.integers(1,7))

print(np.random.uniform(low=-1,high=1,size=(3,2)))