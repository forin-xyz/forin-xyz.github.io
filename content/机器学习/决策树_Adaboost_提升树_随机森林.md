Title: 决策树、Adaboost、提升树以及随机森林
Date: 2016-05-17 23:08
Category: 机器学习
Tags: decision tree, 决策树, 随机森林, random forest, RF, DT, Adaboost, 加法模型, additive model, gradient boosting decision tree, GBDT, boosting tree, BT, CART, least squares regression tree, 回归树, 提升树， ID3, C4.5, Gini index, information gain, information gain ratio
Summary: 决策树学习的算法通常是一个递归的选择最优特征，并根据该特征对训练数据进行分割，使得对各个子数据集有一个更好的分类的过程。提升方法是通过改变训练样本的权重，学习多个分类器，并将这些分类器进行线性组合，提高分类的性能。提升树和随机森林都是多棵树的组合。

# 决策树， DT

**if-then规则的集合**
[女孩相亲的标准](http://forin-xyz.github.io/images/160517_jcs_xq.jpeg)
决策树学习的策略是以损失函数为目标函数的最小化问题，决策树的求解通常采用启发式方法，根据贪婪规则近似的求解这一最优化问题。

## 如何进行特征选择

1. 按照信息度量的变化来选取特征和划分方式，如信息增益(ID3),信息增益比(C4.5),Gini指数(CART二叉分类树)

2. 按照损失函数最小化选择特征和划分方式，如平方误差(CART回归树)，指数误差(Adaboost Tree)等。

## ID3算法

**信息增益**
$$
\text{Gain}(S, A) = -\sum_{c}{\frac{\lvert S_{c} \rvert}{\lvert S \rvert}\log{\frac{\lvert S_{c} \rvert}{\lvert S \rvert}}} + \sum_{a}{\frac{\lvert S_{a} \rvert}{\lvert S \rvert}(\sum_{c}{\frac{\lvert S_{a,c} \rvert}{\lvert S_a \rvert}\log{\frac{\lvert S_{a,c} \rvert}{\lvert S_a \rvert}}})}
$$

## C4.5算法
**分裂信息量**
$$
\text{SplitInformation}(S, A) = - \sum_{a}{\frac{\lvert S_{a} \rvert}{\lvert S \rvert}\log{\frac{\lvert S_{a} \rvert}{\lvert S \rvert}}}
$$

**信息增益比**
$$
\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A}}{\text{SplitInformation}(S, A)}
$$


# 减枝， pruning

# CART

classification and regression tree

## 回归树

least squares regression tree

## 分类树

**Gini指数**
$$
\text{Gini}(S) = 1 - \sum_{c}({\frac{S_c}{S}})^2
$$
$$
\text{Gini}(S, A) = \frac{S_1}{S}\text{Gini}(S_1) + \frac{S_2}{S}\text{Gini}(S_2)
$$
其中$S_1,S_2$是样本集根据特征A是否取某一个可能的值$a$被分割成的两个样本集
$$
S_1={(x, y) \in S \lvert A(x) = a}, S_2 = D - S_1
$$

# Adaboost

# 提升树， BT

# 梯度替代提升树，GBDT

使用损失函数的负梯度在当前模型的值作为回归问题提升树算法中的残差的近似值,拟合一个回归树。

# 随机森林， Random Forest

通过在样本集中有有放回和在特征集无放回的选取样本集和特征集，分别训练出一些树，将这些树组合在一起就得到了随机森林。
[随机森林](http://forin-xyz.github.io/output/2016/03/sui-ji-sen-lin.html)
