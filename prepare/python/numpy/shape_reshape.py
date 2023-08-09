import numpy as np

def reshape_array(num_list, new_shape):
    num_array = list(map(int, num_list.split()))
    array = np.array(num_array).reshape(new_shape)
    return array

num_array = input()
array_shape = (3,3)

print(reshape_array(num_array, array_shape))




