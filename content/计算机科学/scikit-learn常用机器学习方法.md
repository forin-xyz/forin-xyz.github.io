Title: scikit-learn常用机器学习方法
Date: 2016-03-05 10:20
Category: Python
Tags: scikit-learn, 机器学习
Authors: forin-xyz
Summary: scikit-learn常用机器学习方法概要

## 数据导入

可以使用numpy的loadtxt方法导入csv文件

    import numpy as np
    # fn是文件路径 或者 是拥有read方法的对象实例
    np.loadtxt(fn)

## 数据预处理, 数据标准化

### StandardScaler

使训练集每一个特征值**0-均值,1-方差**, 作用在训练集的列(column)上

    from sklearn import preprocessing
    standard_scaler = preprocessing.StandardScaler()
    # 训练并转换数据集
    Xt = standard_scaler.fit_transform(X)
    # 转换新的数据集
    standard_scaler.transform(x)
    # 原训练集均值
    standard_scaler.mean_
    # 原训练集标准差
    standard_scaler.std_

### MinMaxScaler, MaxAbsScaler

指定的极差, 默认min=0, max=1, max_abs=1

    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler.fit(X)
    min_max_scaler.transform(x)
    # min_, 原训练集各个特征最小值, scale_, 原训练集各个特征的范围(scale = max-min)
    min_max_scaler.min_
    min_max_scaler.scale_

对于**稀疏矩阵(sparse matrices)**非常有效

### Normalizer

使每一个样本具有**单位范数, norm=1**, 作用在训练集的行(row)上

    # norm in `{l1, l2, max}`, default norm='l2'
    normalizer = preprocessing.Normalizer(norm='l1')
    normalizer.fit(X)
    normalizer.transform(X)

**小写的scale, minmax_scale, maxabs_scale, normalize是方法, 可以直接将数据集标准化, 返回值就是转化后的新数据集, 但是不能够对新的数据按照相同的参数进行转化**

## 特征提取

## 特征降维, 主成分分析PCA, 独立成分分析ICA, 因子分析FA

### PCA, principal component analysis

只对符号高斯分布的样本点比较有效

    from sklearn import decomposition
    # n_components : int, 向量个数
    # float: 0<n<1, the amount of variance that needs to greater than n.
    # 'mle': 极大似然估计
    # None: min(n_samples, n_features)
    pca = decompositon.PCA(n_components=2)
    pca.fit(X)
    # 最大方差的方向, 特征空间的主要坐标轴
    pca.components_
    # explained_variance_ratio_ : 所选取的向量对应的方差的百分数
    pca.explained_variance_ratio_
    # mean_: 每个特征的经验均值
    pca.mean_
    # n_components_: 模型提取的特征数
    pca.n_components_
    # 转换数据集数据
    pca.transform(X)
    # 返回对数似然函数在样本上的平均值
    pca.score(X)

### ICA, independent component analysis

### FA

## KNN, k-近邻

### NearestNeighbors, 返回最近的邻居

    from sklearn import neighbors
    nbrs = neighbors.NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    # 距离每个样本最近的样本点的索引
    distances, indices = nbrs.kneighbors(X)
    kdt.query(X, k=2, return_distance=False)

### KDTree, kd树

    kdt = neighbors.KDTree(X, leaf_size=30, metric='euclidean')

### KNeighborsClassifier, kNN分类器


    neigh = neighbors.KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X)
    neigh.predict(Xs)
    # freq(类)/k, 返回值是一个向量, 象征每个类在的k近邻经验概率分布
    neigh.predict_proba(Xt)
    # Returns the mean accuracy on the given test data and labels.
    neigh.score(Xv, yv)


## NB, 朴素贝叶斯

### 一般朴素贝叶斯方法, MultinomialNB

特征向量分量是离散变量时很有用

    from sklearn import naive_bayes
    nb = naive_bayes.MutilnomialNB()
    nb.fit(X)

**$\lambda = 0$是代表极大似然估计, $\lambda = 1$是代表拉普拉斯平滑, $\lambda > 0$时是贝叶斯估计.**

### 高斯朴素贝叶斯方法, GaussianNB

假设特征向量分量关于Y的条件分布符合正态分布, 即$P(X^i|Y)$是正态分布, 对X是连续变量时有用

    gnb = naive_bayes.GaussianNB()
    gnb.fit(X)


### 伯努利朴素贝叶斯方法， BernoulliNB

假设特征向量分量关于Y的条件分布是伯努利分布

    bnb = naive_bayes.BernoulliNB(alpha=1.0)
    bnb.fit(X)

**$\lambda = 0$是代表极大似然估计, $\lambda = 1$是代表拉普拉斯平滑, $\lambda > 0$时是贝叶斯估计.**


## LR, 逻辑回归分类模型

$$
\min\limits_{w, b}{\frac{1}{2} {\lVert w \rVert}^2 + C \sum\limits_{i=1}{N}{log{1+exp(-y_i(w \cdot x_i + b))}}}
$$
或者等价于
$$
\min\limits_{w, b}{\sum\limits_{i=1}^{N}{\log{1+exp(-y_i(w \cdot x_i + b))}} + \lambda {\lVert w \rVert}^2}
$$
如果penalty='l1', 就将上面公式中的l2范数换成l1范数即可, 即各分量绝对值的和

    from sklearn import linear_model
    # penalty -> 范数 or 惩罚函数,default='l2', C 惩罚系数, log(exp(-yi(w*xi+b))+1)的系数
    lr = linear_model.LogsiticRegression(penalty='l2',C=1.0)
    # coef_ -> w, intercept_ -> b

## SVM, 支持向量机

### 线性支持向量机

$$
\min\limits_{w, b}{\frac{1}{2} {\lVert w \rVert}^2 + C \sum\limits_{i=1}^{N}{[1-y_i(w \cdot x_i + b)]_{+}}}
$$
或者等价于
$$
\min\limits_{w, b}{\sum\limits_{i=1}^{N}{[1-y_i(w \cdot x_i + b)]_{+}} + \lambda {\lVert w \rVert}^2}
$$
如果penalty='l1', 就将上面公式中的l2范数换成l1范数即可, 即各分量绝对值的和

    from sklearn import svm
    # loss in ['hingle', 'squard_hingle'], default='hingle'
    linear_svm = svm.LinearSVC(C=1.0, loss='hingle', penalty='l2')

### 非线性支持向量机

    from sklearn import svm
    # kernel is in [‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable], default='rbf'
    # degree: degree for 'poly', ignored by all other method, default=3
    # gamma: 'poly', 'rbf', 'sigmoid'核函数系数, 如果选择'auto'的话, 1/n_features将被选择
    svc = svm.SVC(C=1.0, kernel='rbf', de)

## ME, 最大熵模型

## DT, 决策树

scikit-learn使用的是优化的CART算法

### 分类树

    from sklearn import tree
    # criterion: 'gini', 'entropy', default='gini'
    dtc = tree.DecisionTreeClassfier(criterion='gini')

### 回归树

    # criterion: 'mse', default='mse', mean squared error
    dtr = tree.DecisionTreeRegressor(criterion='mse')

## BT, 提升树, Gradient Tree Boosting

### 分类, GradientBoostingClassifier

    from sklearn import ensemble
    gbc = ensemble.GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

### 回归, GradientBoostingRegressor

    gbr = ensemble.GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss='ls').fit(X_train, y_train)

## AdaBoost, 提升方法

    from sklearn.ensemble import AdaBoostClassifier

    abclf = AdaBoostClassifier(n_estimators=100)
    abclf.fit(X, y)

## HMM, 隐马尔科夫模型

## CRF, 条件随机场

## CV, 交叉验证

    from sklearn import cross_validation
    # cross_val_score, cross_val_predict
    # 默认使用k-fold验证
    # array-like, shape[0] = len(list(cv)) if type(cv) is not int else cv
    scores = cross_validation(clf, X, y, cv=3)
    # shape=(n_samples, )
    predicted = cross_validation.cross_val_predict(clf, X, y, cv=4)
    from sklearn import metrics
    metrics.accuracy_score(iris.target, predicted)


### K-fold

    # n -> int, 样本的总数量, n_folds <- number of folds, default=3, at least 2.
    kf = cross_validation.KFold(4, n_folds=2)
    # train, test 是训练样本和验证样本的索引构成的列表
    for train, test in kf:
        (train, test)

### LOO, Leave-One-Out

    # n -> int, the total of elements
    loo = cross_validation.LeaveOneOut(8)
    for train, test in lo:
        (train, test)

### LPO, Leave-P-Out

    lpo = cross_validation.LeavePOut(n, p)

**这些交叉验证的模型可以代入最上面的**`cross_val_score`, `cross_val_predict`**方法中**

### random permutations cross validation

    ss = cross_validation.ShuffleSplit(5, n_iter=3, test_size=0.25, random_state=0)
    
## 高斯混合模型

非监督学习模型, unsupervised learning

$$
P(y|\sigma) = \sum\limits_{k=1}^{K}{\alpha_{k}\phi(y|\sigma_{k})}
$$

$$
{\phi}(y|\sigma_{k}) = \frac{1}{(2 \pi)^{\frac{p}{2}}{\sqrt(det({COVMAT}_k))}}exp(-\frac{1}{(y-{\mu}_k)^T({COVMAT}_k)^{-1}(y-{\mu}_k)});
$$
其中, ${COVMAT}_k$是 (n_features, n_features) 的矩阵, ${\mu}_k$是 (n_features, )向量

    from sklearn import mixture
    gmm = mixture.GMM(n_components=2)
    gmm.fit(X)
    # 均值
    gmm.means_
    # 协方差
    gmm.covars_
    # 权重
    gmm.weights_
    # 预测
    gmm.predict(XP)

高斯混合模型首先通过观测数据使用EM算法计算出模型的参数$\sigma$, 然后通过计算出在给定的参数下, 观测数据最有可能通过第几个模型产生, 达到对数据进行分类的目的.

如果将其他概率密度替代高斯混合模型中的高斯分布密度, 那么就会得到相应的概率混合模型, 然后可以使用类似办法对类进行分类.

## 聚类, Clustering

### K-Means, k-均值, KMeans, MiniBatchKMeans

输入参数: 聚类的个数

$$
min \sum\limits_{i=1}^{N}{\min{\limits_{k}{\lVert {x_i-{\mu}_k} \rVert}^2}}
$$

**MiniBatchKMeans**是KMeans的变种, 可以减少运行时间.

### MeanShift, 将中心点逐渐移向密度最稠密的点

scikit-learn使用的是`rbf kernel`, 高斯径向基函数.

### DBSCAN

高密度区域天然被低密度区域分割


## 二聚类, Biclustering

## 模型持久化

    from joblib.externals import joblib
    # 保存
    joblib.dump(clf,'../../data/model/randomforest.pkl',compress=3)
    # 加载
    clf = joblib.load('../../data/model/randomforest.pkl')
