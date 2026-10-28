import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here

	mse_values = []

	X = np.array(features)
	W = np.array(initial_weights)
	G = np.zeros_like(W)
	bias = initial_bias

	for i in range(epochs):
		se = 0
		bias_gradient = 0
		Z = X @ W + bias
		probabilities = [1/(1+np.exp(-x)) for x in Z]
		for x, prob, label in zip(X, probabilities, labels):
			#SE - Squared Error
			se = se + (prob - label)**2
			#Gradient of Squared Error    dL/dy
			gradient_0 = 2 * (prob - label)
			#Gradient of sigmoid function   dy/dz
			gradient_1 = prob * (1 - prob)
			#Gradient of Z with respect to weights  dz/dw
			#gradient_2 = X

			#using chain rule we get:

			delta = gradient_0 * gradient_1
			G = G + (delta * x) 
			bias_gradient = bias_gradient + delta
		G = G / len(features)
		bias_gradient = bias_gradient / len(features)

		W = W - learning_rate * G
		bias = bias - learning_rate * bias_gradient

		G = np.zeros_like(W)

		mse = se / len(labels)
		mse_values.append(mse)

	updated_bias = bias

	return W.tolist(), updated_bias, mse_values