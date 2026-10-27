import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if (new_shape[0] * new_shape[1]) != (len(a) * len(a[0])):
		return []
	array_container = np.array(a)

	reshaped_matrix = array_container.reshape(new_shape)




	return reshaped_matrix