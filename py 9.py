import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(1)
weights1 = np.random.rand(2,2)
weights2 = np.random.rand(2,1)

for _ in range(10000):
    hidden = sigmoid(np.dot(X, weights1))
    output = sigmoid(np.dot(hidden, weights2))
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = np.dot(d_output, weights2.T) * sigmoid_derivative(hidden)
    weights2 += np.dot(hidden.T, d_output)
    weights1 += np.dot(X.T, d_hidden)

print("Output after training:")
print(output)
