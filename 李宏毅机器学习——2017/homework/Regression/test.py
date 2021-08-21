import numpy as np
import matplotlib.pyplot as plt
from process_data import preprocess


if __name__ == '__main__':

    paras = np.loadtxt('D:\\projects\\ML_Hongyi_Lee_2017\\Regression\\model.txt')
    print(paras)
    bias = float(paras[0])
    # weight = float(paras[1])
    weight = [float(paras[1]), float(paras[2])]

    test_data, _ = preprocess('/Regression/data.txt')

    # preds = bias + weight * test_data[:, 0]
    preds = bias + weight[0] * test_data[:, 0] + weight[1]*test_data[:, 0]**2

    x = np.linspace(test_data[:, 0].min(), test_data[:, 0].max(), 100)
    y = bias + weight[0] * x + weight[1]*x**2

    plt.figure()
    plt.scatter(test_data[:, 0], preds, c='r')
    plt.scatter(test_data[:, 0], test_data[:, 1], c='g')
    plt.plot(x, y, c='k')
    plt.show()
