import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print("arr =", arr)

print("arr[2] =", arr[2])

print("arr[-1] =",arr[-1])

print("arr[1:4] =",arr[1:4])
print("arr[3:] =",arr[3:])

reshaped = arr.reshape(2,3)
print("reshaped =",reshaped)



matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matrix =\n", matrix)

vector = np.array([1, 0 , -1])
print("vector =", vector)

result_add = matrix + vector
print("Add: \n", result_add)

result_mul = matrix * 2
print("Multiplication: \n", result_mul)



np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)


random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)