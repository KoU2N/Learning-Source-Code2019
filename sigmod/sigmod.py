# -*- coding: utf-8 -*-

# Learning Source Code2019
#
# Created by: KoU2N
#
# 2019年1月3日
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(inputs):

    """

    Calculate the sigmoid for the give inputs (array)

    :param inputs:

    :return:

    """

    sigmoid_scores = [1 / float(1 + np.exp(- x)) for x in inputs]

    return sigmoid_scores

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
    sigmoid_inputs = [1, 2, 3, 4]
    print("原始向量:", sigmoid_inputs)
    print("经过Sigmoid后:",sigmoid(sigmoid_inputs))


    graph_x = range(0, 21)
    graph_y = sigmoid(graph_x)

    print("Graph X readings: {}".format(graph_x))
    print("Graph Y readings: {}".format(graph_y))

    line_graph(graph_x, graph_y, "Inputs", "Sigmoid Scores")

if __name__ == '__main__':
    main()