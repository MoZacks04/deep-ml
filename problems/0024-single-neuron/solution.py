import numpy as np
import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	mse_total = 0
	X = np.array(features)
	W = np.array(weights)

	probabilities = X @ W + bias
	temp = 0
	after = []

	for prob in probabilities:
		temp = 1 / (1 + np.exp(-prob))
		after.append(temp)

	for probability, label in zip(after, labels):
		mse_total = mse_total + (probability - label)**2
	mse = mse_total / len(features)

	#sigmoid probability:
	after = [round(x, 4) for x in after]

	return after, mse