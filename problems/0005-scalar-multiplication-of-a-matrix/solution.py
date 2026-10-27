def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	scaled = []
	temp = []
	for colum in matrix:
		for value in colum:
			new_value = value * scalar
			temp.append(new_value)
		scaled.append(temp)
		temp = []
	return scaled


	pass