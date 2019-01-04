# -*- coding: utf-8 -*-

# Learning Source Code2019
#
# Created by: KoU2N
#
# 2019年1月1日
import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    """
    对输入x的每一行计算softmax。

    该函数对于输入是向量（将向量视为单独的行）或者矩阵（M x N）均适用。

    代码利用softmax函数的性质: softmax(x) = softmax(x + c)

    参数:
    x -- 一个N维向量，或者M x N维numpy矩阵.

    返回值:
    x -- 在函数内部处理后的x
    """
    # 根据输入类型是矩阵还是向量分别计算softmax
    if len(x.shape) > 1:
        # 矩阵
        tmp = np.max(x, axis=1)  # 得到每行的最大值，用于缩放每行的元素，避免溢出
        x -= tmp.reshape((x.shape[0], 1))  # 利用性质缩放元素
        x = np.exp(x)  # 计算所有值的指数
        tmp = np.sum(x, axis=1)  # 每行求和
        x /= tmp.reshape((x.shape[0], 1))  # 求softmax
    else:
        # 向量
        tmp = np.max(x)  # 得到最大值
        x -= tmp  # 利用最大值缩放数据,缩放可以省略
        x = np.exp(x)  # 对所有元素求指数
        tmp = np.sum(x)  # 求元素和
        x /= tmp  # 求somftmax
    return x

def softmax2(inputs):
    
    """
    向量更简单的写法，不能处理矩阵
    Calculate the softmax for the give inputs (array)

    :param inputs:

    :return:

    """

    return np.exp(inputs) / float(sum(np.exp(inputs)))

def line_graph(x, y, x_title, y_title):
    """
    Draw line graph with x and y values
    :param x:
    :param y:
    :param x_title:
    :param y_title:
    :return:
    """
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()
 


def main():
    test1 = np.array([1,  2, 3, 4])
  
    print("原始向量:", test1)
    print("经过softmax后:", softmax(test1))
    print("经过softmax2后:",softmax2(test1))

    test2 = np.array([[1,2],[3,4]])
    print('原始矩阵:\n', test2)
    print("经过softmax后:\n", softmax(test2))    

    graph_x = np.arange(-20, 21)
    graph_y = softmax2(graph_x)

    print("Softmax Function Input :\n",graph_x)
    print("Softmax Function Output :\n",graph_y)
    
    line_graph(graph_x, graph_y, "Inputs", "Softmax Scores")



if __name__ == '__main__':
    main()
