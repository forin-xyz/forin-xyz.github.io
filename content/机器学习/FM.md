Title: 因子分解机器模型　Factorization Machine
Date: 2016-10-13 23:38
Category: 机器学习
Tags: FM, 线性模型, 矩阵分解
Summary: Factorization Machine是将线性模型和矩阵分解相结合产生的一种新模型,广泛用于具有稀疏性的大型推荐系统


## 模型介绍
下面是度为2的因子分解机的数学表达式
$$
\widehat{y} = b + \mathbf{w}^Tx + \sum_{i=1}^{n-1}\sum_{j>i}^n\mathbf{v}_i^T\mathbf{v}_jx_ix_j
$$
其中
$$
Rank(v_i) = k
$$
是模型的超参数。

因子分解机也可以推广到高阶模型，即将更多的互异特征向量之间的相互关系考虑进来。

## 使用范围

Regression

Binary Classification

Ranking

## 损失函数

回归问题使用残差的平方和
$$
loss_r = \sum{(\widehat{y} - y) ^ 2}
$$

分类问题使用交叉熵
$$
loss_r = -\sum{y\log{\widehat{y}}}
$$
其中$\widehat{y}$使用了sigmoid函数(Binary Classfication) 或则　Softmax(Multi-Classfication)进行了归一化(Normalization)操作。

## 模型求解

由于上述两种模型的损失函数都是凸函数, 所以可以使用随机梯度下降法对模型进行求解。

## 优点

1. 参数比Polynimal Regression少
2. 由于在Polynimal　Regression中的巨量稀疏性会导致许多项的系数无法预测导致过拟合,所以在这种情况下使用类似矩阵分解的方法来避免过拟合或者说无法预测。


## 开源库

www.libfm.org

