import numpy as np

def convert(x):
    new_x = []
    for i in x:
        new_x.append([1, i, i**2, i**3])
    return np.array(new_x)


def read_csv(path):
    with open(path, 'r') as file:
        headers = file.readline().strip().split(',')

    x_cols = [i for i in range(len(headers)) if headers[i] == 'x']
    y_cols = [i for i in range(len(headers)) if headers[i] == 'y']

    x = np.loadtxt(path, delimiter=',', skiprows=1, usecols=x_cols)
    y = np.loadtxt(path, delimiter=',', skiprows=1, usecols=y_cols)
    y = y.reshape(-1, 1)

    return x, y


def train(train_inputs, train_labels):
    theta = np.linalg.solve(
        train_inputs.T @ train_inputs,
        train_inputs.T @ train_labels,
    )
    return theta


def f(x,theta,n):
    y = []
    for i in x:
        new_x = np.array([i**j for j in range(n+1)])
        new_x = new_x.reshape(-1, 1)
        result = theta.T @ new_x
        y.append(result[0][0])
    return y
