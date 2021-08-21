import numpy as np


def replace_commas(path):
    with open(path, 'r+') as f:
        contents = f.read()
        contents = contents.replace(',', ' ')
        f.seek(0)
        f.write(contents)


def split_by_commas(path):
    matrix = []
    for i in open(path, 'r'):
        line = [int(t) for t in i.split(' ')]
        matrix.append(line)
    return np.array(matrix)


if __name__ == '__main__':
    # replace_commas('matrix_A.txt')
    # matrixA = np.loadtxt('matrix_A.txt')
    # replace_commas('matrix_B.txt')
    # matrixB = np.loadtxt('matrix_B.txt')
    # matrixC = matrixA @ matrixB
    # matrixC.sort()
    # np.savetxt('ans_one.txt', matrixC)

    matrixA = split_by_commas('matrix_A.txt')
    matrixB = split_by_commas('matrix_B.txt')
    matrixC = np.matmul(matrixA, matrixB)
    matrixC.sort()
    print(matrixC)
