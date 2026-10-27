import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	#normal equation is: theta = θ=(XTX)−1XTy, it allows us to find the weights m and b in an equation y = mx + b
	X = np.array(X)
	Y = np.array(y)
	theta = np.linalg.inv(X.T @ X) @ X.T @ Y

	return theta.round(4).tolist()