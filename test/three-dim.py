import numpy as np

data = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])

print(data)

print(data[0, 0, 2])
print(data[1, 1, 2])

print(data[0, 0, 0:2])
print(data[1, 1, 1:])
print(data[1, 0, :1])

print(data[1, 0, :])
print(data[0, 1, :])

print(data[0, 0, -3:-1])
print(data[1, 0, -3:-1])

for x in data:
    for y in x:
        for z in y:
            print(z)
