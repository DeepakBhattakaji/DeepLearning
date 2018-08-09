#Scalar 0D
print("==============================")
print("Scalar - 0D and has 0 Axis")
import numpy as np
x=np.array(42)
print(x)
print('A Scalar is of rank %d'%(x.ndim))

#Vector 1D
print("==============================")
print("Vector - 1D and has 1 Axis")
y=np.array([1,1,2,3,5,8])
print(y)
print('A Vector is of rank %d'%(y.ndim))
#Matrix 2D
print("==============================")
z=np.array([[1,4,7],
            [2,5,8],
            [3,6,9]])
      
print(z)
print('A Matrix is of rank %d'%(z.ndim))
#Tensor
print("==============================")
a=np.array([[[1,4,7],
             [2,5,8],
             [3,6,9]],
             [[10,40,70],
              [20,50,80],
              [30,60,90]],
              [[100,400,700],
               [200,500,800],
               [300,600,900]]])
print(a)
print('\nA Tensor is of rank %d'%(a.ndim))

#Student Table
print("==============================")
import pandas as pd
std_df={'Name': ['Deepak Bhatta','Nashrat Hushain','Chirag Gupta','Ajay K. Chauhan'],
        'RollNo': [18,11,17,20],
        'Course':['Science','Management','Art','Medical'],
        'Gender':['M','M','M','M'],
        'Subject':['Math','CAP728','CAP930','Science']}
df=pd.DataFrame(std_df)
print(df)
#Import CSV File
print("==============================")





'''b=np.array[[1.,0.,0,],
[0.,1.,2.]]
print(b)
'''

#Numpy Attribute
print("==============================")
import numpy as np
g=np.arange(15)
print(g)
g=np.arange(15).reshape(3,5)
print(g)

print("The array shape :",g.shape)
print("The array of Dimension :",g.ndim)
print("The array of DataType :",g.dtype.name)
print("The Array Item Size :",g.itemsize)
print("The Array Actual Size :",g.size)
print("The Array Type :",type(g))
h=np.array([6,7,8])
print("The Array Type :",h)


i=np.array([2,3,4])
print(i)
print(i.dtype)
j=np.array([1.2,3.5,5.1])
print(j.dtype)

#Panda Attribute
print("==============================")



