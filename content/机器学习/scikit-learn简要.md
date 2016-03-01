Title: scikit-learn简要
Date: 2016-3-3 23:00
Category: Python
Tags: python, scikit-learn, machine learning, supervised learning, non-supervised learning, classfication, prediction, clustering, dimensionality
Summary: scikit-learn是python重要的机器学习和数据挖掘的软件包.

## 分类 Classfication

### 线性模型 Generalized Linear Models

#### 线性回归 -> 普通最小二乘法 Linear Regression -> Oridinary Least Squares

$$
min\limits_w || Xw - y ||_2^2
$$

    >>> from sklearn import linear_model
    >>> # clf -> classfication
    >>> clf = linear_model.LinearRegression()
    >>> # fit(X, y) -> 学习模型
    >>> clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    >>> # 非常数项系数
    >>> clf.coef_
    array([ 0.5,  0.5])

#### 脊回归 Ridge Regression -> 带惩罚函数的最小二乘法 Least Squares by imposing a penalty on the size of coefficients.

$$
min\limits_w {|| Xw - y ||_2^2 + \alpha ||w||_2^2}, \alpha \geq 0
$$

    >>> from sklearn import linear_model
    >>> clf = linear_model.Ridge (alpha = .5)
    >>> clf.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
    Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
          normalize=False, random_state=None, solver='auto', tol=0.001)
    >>> clf.coef_
    array([ 0.34545455,  0.34545455])
    >>> # 常数项系数 or 截距
    >>> clf.intercept_ 
    0.13636.

##### 获取正则项或惩罚函数系数 -> 交叉验证 Cross Validation
..

    >>> from sklearn import linear_model
    >>> # 多了一个后缀CV
    >>> clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
    >>> clf.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])       
    RidgeCV(alphas=[0.1, 1.0, 10.0], cv=None, fit_intercept=True, scoring=None,
        normalize=False)
    >>> clf.alpha_                                      
    0.1


#### Lasson 拉索

估计稀疏系数时会有用, 他更倾向于使用较少的参数值, 如果问题需要减少变量个数, 它将是非常有用的.

$$
min\limits_w {\frac{1}{2n_samples}{|| Xw - y ||_2^2 + \alpha \lVert w \rVert_1}}, \alpha \geq 0
$$

    >>> from sklearn import linear_model
    >>> clf = linear_model.Lasso(alpha = 0.1)
    >>> clf.fit([[0, 0], [1, 1]], [0, 1])
    Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
       normalize=False, positive=False, precompute=False, random_state=None,
       selection='cyclic', tol=0.0001, warm_start=False)
    # 预测
    >>> clf.predict([[1, 1]])
    array([ 0.8])

##### 确定正则项系数

###### 使用交叉验证

**LassoCV**

**LassoLarsCV**

###### 基于信息标准的模型选择 Information-criteria based model selection

**LassoLarsIC**

#### Elastic Net


$$
min\limits_w {\frac{1}{2n_samples}{|| Xw - y ||_2^2 + \alpha \rho \lVert w \rVert _1 + \alpha (1 -  \rho) \lVert w \rVert _2^2 }}, \alpha \geq 0, \rho \geq 0
$$

#### Multi-task Lasso

#### Least Angle Regression

#### LARS Lasso

### 线性和二次判别分析 Linear and Quadratic Discriminant Analysis

### Kernle Ridge Regrssion 带核脊回归

### 支持向量机 Support Machines

### 随机梯度下降法 Stochastic Gredient Descent

### k近邻 Nearest Neighbors

### Gaussian Process 高斯过程

### Cross decomposion

### 朴素贝叶斯 Naive Bayes

### 决策树 Decision Trees

### Ensemble Methods

### Multiclass and multilabel algorithms 多类多标签算法

### 特征选择 feature selection

### Semi-Supervised

### Isotonic Regression

### Probability calibration

## Clustering 聚类

## 降维 Dimensionality reduction

### 主成分分析 Principal component analysis (PCA)

#### Exact PCA and probabilistic interpretation

Linear dimensionality reduction using Singular Value Decomposition of the data and keeping only the most significant singular vectors to project the data to a lower dimensional space.

算法(PCA):
>输入:$X \in K^{N*n}$, 需要降到的维数m < n
>
>输出: 转换矩阵$M \in K^{n*m}
>
>(1) 求出X的每一列均值, 并用X减去, 得到矩阵$Y$是的Y每一列的均值为0
>
>(2) 求Y列与列之间的协方差矩阵$C$,
>$$C[i, j] = Y[:,i] \cdot Y[:, j] / N$$
>等价于
>$$C = X^T X
>
>(3) 求出协方差矩阵C的特征值和特征向量
>
>(4) 取特征值最大的m个特征值及其对应的特征向量
>
>(5) 取出的特征向量组合成n*m矩阵即为所求$M=(\alpha _1, \alpha _2, \cdots, \alpha _m) \in K^{n*m}$



####  Incremental PCA

Incremental principal component analysis (IPCA) is typically used as a replacement for principal component analysis (PCA) when the dataset to be decomposed is too large to fit in memory. IPCA builds a low-rank approximation for the input data using an amount of memory which is independent of the number of input data samples. It is still dependent on the input data features, but changing the batch size allows for control of memory usage.

#### Approximate PCA

#### Kernel PCA

#### Sparse principal components analysis (SparsePCA and MiniBatchSparsePCA)

### 截断奇异值分解和潜在语义分析 Truncated singular value decomposition and latent semantic analysis

### Dictionary Learning

### factor analysis

### Independent component analysis (ICA) 独立成分分析

### Non-negative matrix factorization (NMF or NNMF) 非负矩阵分解

###  Latent Dirichlet Allocation (LDA) 

## 模型选择 Model selection and evaluation

## Preprocessing data 预处理数据
