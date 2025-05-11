# NUMPY -- Number Python 
# working with number system
# Algebra
# Fouriesrs Transform
# Statistics
# Matrics -- *** 

# Working with Multi-Dimensional Array
#  - 0 -Dimention to n - Dimention
# Faster then treditional array
# 50 times Faster then tradition array
# ndarray -- n diamention array
#  collection -- categoricing -- arranging
# Data Science need 
    #   speed 
    #   resource

# Module:
#       > python -m pip install numpy``

# ---------------------------------------------
# import numpy as np

# data1 = [10, 20, 30, 40, 50]
# data2 = np.array(data1)
# print(data1)
# print(data2)
# print(data2[2])
# print(data2[3])
# print(data2[1:3])
# print(data2[2:])
# print(data2[-1])
# print(data2[-3:-1])
# we can manuplate same like normal array
# ------------------------------------------
# creating dimentions

# import numpy as np

# data1 = np.array(0)
# print(data1.ndim) #-- 0 dim

# data2 = np.array([10, 20, 30, 40, 50])
# print(data2.ndim) # -- 1 dim

# data3 = np.array([[10, 20, 30], [40, 50, 60]])
# print(data3.ndim) # -- 2 dimention

# data4 = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])
# print(data4)
# print(data4.ndim) # 3 bracket so 3 dimention

# ----------------------------------------------------------

import numpy as np

data = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
print(data)

print(data[0, 1])
print(data[0, 3])

print(data[1, 1])
print(data[1, 3])
print(data[0, 1:4])
print(data[1, 1:4])
print(data[1,2:])

print(data[0,:])
print(data[1,:])

print(data[0, ::2])
print(data[1, ::2])

print(data[0, -1])
print(data[1, -1])

print(data[0, -3:-1])
print(data[1, -3:-1])

for x in data:
    for y in x:
        print(y)
