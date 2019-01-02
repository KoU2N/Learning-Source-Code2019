# Learning source code 2019

## Softmax的Python实现

- [Softmax要解决什么问题](fluid): 我有一个向量，想用数学方法把向量中的所有元素归一化为一个概率分布。也就是说，该向量中的元素在[0,1]范围内，且所有元素的和为1。Softmax是个数学方法，本质上是一个函数。Softmax函数也叫做归一化指数函数（normalized exponential function）。

- [Softmax的性质](legacy): 对输入x加上一个实数c后求softmax结果不变。
    用公式表示就是：
    softmax(x)=softmax(x+c) ,其中c是实数。
## 输出
![](https://github.com/KoU2N/Learning-Source-Code2019/blob/master/softmax/softmax.png)

