import matplotlib.pyplot as plt
import numpy as np
from process_data import preprocess
import copy


def train(train_valid, bias, weight, epoch, lr=0.0001):
    loss = []
    for i in range(len(train_valid)):
        data_temp = copy.deepcopy(train_valid)
        valid_data = data_temp[i]
        data_temp.pop(i)
        train_data = np.array(data_temp)
        train_data = train_data.reshape(-1, 2)
        # 计算梯度
        # grad_l_b = sum(-2 * (train_data[:, 1] - (bias + weight*train_data[:, 0])))
        # grad_l_w = sum(-2 * train_data[:, 0] * (train_data[:, 1] - (bias + weight*train_data[:, 0])))
        grad_l_b = sum(-2 * (train_data[:, 1] - (bias + weight[0]*train_data[:, 0] + weight[1]*train_data[:, 0]**2)))
        grad_l_w0 = sum(-2 * train_data[:, 0] * (train_data[:, 1] - (bias + weight[0]*train_data[:, 0] + weight[1]*train_data[:, 0]**2)))
        grad_l_w1 = sum(-2 * (train_data[:, 0]**2) * (train_data[:, 1] - (bias + weight[0]*train_data[:, 0] + weight[1]*train_data[:, 0]**2)))
        # 更新参数
        bias = bias - lr * grad_l_b
        # weight = weight - lr * grad_l_w
        weight[0] = weight[0] - lr * grad_l_w0
        weight[1] = weight[1] - lr * grad_l_w1
        # 计算在valid_data上的误差
        # loss.append(sum((valid_data[:, 1] - (bias + weight[0] * valid_data[:, 0])) ** 2))
        loss.append(sum((valid_data[:, 1] - (bias + weight[0]*valid_data[:, 0] + weight[1]*valid_data[:, 0]**2))**2) / 97)
        print('bias {}、weight {}: loss {}'.format(bias, weight, loss[i]))
    print('epoch {}:'.format(epoch))

    return bias, weight, loss


if __name__ == '__main__':
    path = 'data.txt'
    test_data, train_valid = preprocess(path)

    bias = 2
    # weight = 2
    weight = [2, 2]
    loss_log = []
    epochs = 1000
    for epoch in range(epochs):
        bias, weight, loss = train(train_valid, bias, weight, epoch=epoch, lr=0.000001)
        loss_log.append(loss)

    loss_log = np.array(loss_log)
    plt.figure()
    plt.plot(range(len(loss_log)-200), loss_log[200:, 0], 'k')
    plt.plot(range(len(loss_log)-200), loss_log[200:, 1], 'r')
    plt.plot(range(len(loss_log)-200), loss_log[200:, 2], 'g')
    plt.show()

    with open('model.txt', 'w') as f:
        # f.write(str(bias))
        # f.write('\r\n')
        # f.write(str(weight))

        # f.writelines([str(bias) + '\n', str(weight)])
        f.writelines([str(bias) + '\n', str(weight[0]), '\n', str(weight[1])])

