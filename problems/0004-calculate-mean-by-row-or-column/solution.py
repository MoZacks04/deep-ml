def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	index = 0
	total = 0
	count = 0
	average = 0
	means = []

	if mode == "column":
		num_columns = len(matrix[0])
		count = len(matrix)
		for i in range(num_columns):
			for row in matrix:
				total = row[i] + total
			average = total / count
			means.append(average)
			total = 0
			average = 0

		return means

	elif mode == "row":
		for row in matrix:
			for val in row:
				total = val + total
			average = total / len(row)
			means.append(average)
			total = 0
			average = 0
		return means



	return means