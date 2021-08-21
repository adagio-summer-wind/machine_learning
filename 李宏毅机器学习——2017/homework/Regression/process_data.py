import random

import numpy as np


def replace_commas(path):
    with open(path, 'r+') as f:
        contents = f.readlines()
        random.shuffle(contents)
        f.seek(0)
        for line in contents:
            line = line.replace(',', ' ')
            f.write(line)


def preprocess(path):
    # 处理后的数据文件可用下面语句读入为numpy数据格式
    data = np.loadtxt(path)    # data.shape == (97, 2)
    test_data = data[-7:, :]
    train_data = np.split(data[:90, :], 3)          # 将train_data 分为三份，每份30个
    return test_data, train_data


if __name__ == '__main__':
    path = '/Regression/data.txt'
    replace_commas(path)
