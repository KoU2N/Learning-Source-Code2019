# Sigmod的Python实现

## 简介
    Sigmoid函数是一个在生物学中常见的S型的函数，也称为S型生长曲线。Sigmoid函数常被用作神经网络的阈值函数，将变量映射到0,1之间。
## Sigmod和Softmax异同
### 共同点
    1、取值范围都是0~1区间，表示概率，概率自然是这个取值范围。
    
    2、都可以用来作为分类任务的输出层函数。

### 不同点

    1、sigmod作为输出层函数时解决的二分类任务，输出值是一个小数。
       除此之外可以用作隐层的激活函数，另外激活函数是解释神经网络非线性的核心原因。

    2、softmax是二分类任务的推广，用于解决多分类问题，输出值是一组小数，有几类就有几个小数，相加为1。

## 结果
    ![](https://github.com/KoU2N/Learning-Source-Code2019/blob/master/sigmod/cmd_result.png)
    ![](https://github.com/KoU2N/Learning-Source-Code2019/blob/master/sigmod/sigmod.png)