Title: python数据分析包之pandas
Date: 2016-03-04 10:20
Modified: 2016-03-04 19:30
Category: Python
Tags: pandas, 数据分析, python
Authors: forin-xyz
Summary: A short tutorial for pandas.

## Seris

相当于一个**定长的有序字典**

### 创建

1. 任意的一维数据, 索引可以自动生成或者指定

2. 也可以输入像字典一样的**key-value**数据, 这样**key**自动就变成了索引

3. Series对象和它的index都含有一个`name`属性

        In [1]: import pandas as pd
        
        In [2]: import numpy as np
        
        In [3]: import matplotlib.pyplot as plt
        
        In [5]: s =pd.Series([1, 2, 3, np.nan, '456', 'xa'])
        
        In [6]: s
        Out[6]: 
        0      1
        1      2
        2      3
        3    NaN
        4    456
        5     xa
        dtype: object
        
        In [15]: s2 = pd.Series(data=np.arange(10), index=pd.date_range('20150101', periods=10))
        
        In [16]: s2
        Out[16]: 
        2015-01-01    0
        2015-01-02    1
        2015-01-03    2
        2015-01-04    3
        2015-01-05    4
        2015-01-06    5
        2015-01-07    6
        2015-01-08    7
        2015-01-09    8
        2015-01-10    9
        Freq: D, dtype: int32
        
        In [17]: s3 = pd.Series(dict(zip('abcdefg',range(ord('a'), ord('g')+1))))
        
        In [18]: s3
        Out[18]: 
        a     97
        b     98
        c     99
        d    100
        e    101
        f    102
        g    103
        dtype: int64
        
        In [19]: s3.name = 'ascii'
        
        In [20]: s3.index.name = 'symbo'
        
        In [21]: s3
        Out[21]: 
        symbo
        a         97
        b         98
        c         99
        d        100
        e        101
        f        102
        g        103
        Name: ascii, dtype: int6

### 更新值, 修改值 或者 设置值 update, modify, set

`s[key] = value` key -> 对应的索引名

    In [101]: s3
    Out[101]: 
    symbo
    a         97
    b         98
    c         99
    d        100
    e        101
    f        102
    g        103
    Name: ascii, dtype: int64
    
    In [102]: s3['g'] += 1
    
    In [103]: s3
    Out[103]: 
    symbo
    a         97
    b         98
    c         99
    d        100
    e        101
    f        102
    g        104
    Name: ascii, dtype: int64

### 频数统计, 计数, 按值出现的次数统计

`s.value_counts()`

    In [158]: s0 = pd.Series(np.random.randint(0, 7, size=10))
    
    In [159]: s0
    Out[159]: 
    0    2
    1    5
    2    0
    3    6
    4    0
    5    3
    6    4
    7    1
    8    1
    9    3
    dtype: int32
    
    In [160]: s0.value_counts()
    Out[160]: 
    3    2
    1    2
    0    2
    6    1
    5    1
    4    1
    2    1
    dtype: int64

### 字符串方法

`s.str.method_name()`

    In [166]: ss = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    
    In [168]: ss.str.lower()
    Out[168]: 
    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5     NaN
    6    caba
    7     dog
    8     cat
    dtype: object

## DataFrame

**表格**型的数据结构, 由一个有序的行(row, 相当于index)和不同字段的列(column, 相当于key)组成, 基本上可以把DataFrame看成是共享同一个index的Series的集合.

### 创建

1. 可以输入一个类字典**key-value**类型, 字典的键对应于DataFrame的columns, 索引是自动生成的

2. 也可以指定对应的index和columns, 缺失值由NaN补足

3. index, columns的类型是Index, 对应的列(columns)的类型是Series

4. data数据既可以是类字典的键值对, 也可以是任何的2维数据

5. 使用**IPython**的话`Tab`键可以自动补全方法或者属性

        In [22]: data = {'state':['Ohino','Ohino','Ohino','Nevada','Nevada'],
                'year':[2000,2001,2002,2001,2002],
                'pop':[1.5,1.7,3.6,2.4,2.9]}
           ....:    ....: 
        In [23]: df = pd.DataFrame(data)
        
        In [24]: df
        Out[24]: 
           pop   state  year
        0  1.5   Ohino  2000
        1  1.7   Ohino  2001
        2  3.6   Ohino  2002
        3  2.4  Nevada  2001
        4  2.9  Nevada  2002
        
        [5 rows x 3 columns]
        
        In [27]: df2 = pd.DataFrame(data=data, index=list('abcde'), columns=['year', 'state', 'pop', 'debt'])
        
        In [28]: df2
        Out[28]: 
           year   state  pop debt
        a  2000   Ohino  1.5  NaN
        b  2001   Ohino  1.7  NaN
        c  2002   Ohino  3.6  NaN
        d  2001  Nevada  2.4  NaN
        e  2002  Nevada  2.9  NaN
        
        [5 rows x 4 columns]
        
        In [29]: type(df2.index)
        Out[29]: pandas.core.index.Index
        
        In [30]: type(df2.columns)
        Out[30]: pandas.core.index.Index
        
        In [31]: type(df2['debt'])
        Out[31]: pandas.core.series.Series
        
        In [32]: df.columns
        Out[32]: Index(['pop', 'state', 'year'], dtype='object')
        
        In [33]: df2.index
        Out[33]: Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
        
        In [34]: df2['pop']
        Out[34]: 
        a    1.5
        b    1.7
        c    3.6
        d    2.4
        e    2.9
        Name: pop, dtype: float64
        
        In [36]: df3 = pd.DataFrame(np.random.randn(6,4), index=pd.date_range('20160301', periods=6), columns=list('wxyz'))
        
        In [37]: df3
        Out[37]: 
                           w         x         y         z
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        
        [6 rows x 4 columns]
        
        In [42]: df2.dtypes
        Out[42]: 
        year       int64
        state     object
        pop      float64
        debt      object
        dtype: object


### 查看数据

1. head(), tail()

2. index, columns, values分别对应行索引, 列键值 以及 二维数据

3. describe() 展示数据的关于列(columns)简单统计摘要

4. df.T 可以转置数据 transposing your data

        In [43]: df
        Out[43]: 
           pop   state  year
        0  1.5   Ohino  2000
        1  1.7   Ohino  2001
        2  3.6   Ohino  2002
        3  2.4  Nevada  2001
        4  2.9  Nevada  2002
        
        [5 rows x 3 columns]
        
        In [44]: df.head()
        Out[44]: 
           pop   state  year
        0  1.5   Ohino  2000
        1  1.7   Ohino  2001
        2  3.6   Ohino  2002
        3  2.4  Nevada  2001
        4  2.9  Nevada  2002
        
        [5 rows x 3 columns]
        
        In [45]: df.tail(2)
        Out[45]: 
           pop   state  year
        3  2.4  Nevada  2001
        4  2.9  Nevada  2002
        
        [2 rows x 3 columns]
        
        In [46]: df.index
        Out[46]: Int64Index([0, 1, 2, 3, 4], dtype='int64')
        
        In [47]: df.columns
        Out[47]: Index(['pop', 'state', 'year'], dtype='object')
        
        In [48]: df.values
        Out[48]: 
        array([[1.5, 'Ohino', 2000],
               [1.7, 'Ohino', 2001],
               [3.6, 'Ohino', 2002],
               [2.4, 'Nevada', 2001],
               [2.9, 'Nevada', 2002]], dtype=object)
        
        In [49]: df3
        Out[49]: 
                           w         x         y         z
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        
        [6 rows x 4 columns]
        
        In [50]: df3.describe()
        Out[50]: 
                      w         x         y         z
        count  6.000000  6.000000  6.000000  6.000000
        mean  -0.351096  0.120582  0.543740  0.154513
        std    0.971279  0.596545  0.955011  0.983688
        min   -2.268193 -0.663132 -0.816183 -0.927173
        25%   -0.315326 -0.243874 -0.136222 -0.531612
        50%    0.128684  0.031489  0.757511  0.204615
        75%    0.165700  0.644187  1.300376  0.360483
        max    0.189541  0.810889  1.516405  1.809606
        
        [8 rows x 4 columns]
        
        In [51]: df.T
        Out[51]: 
                   0      1      2       3       4
        pop      1.5    1.7    3.6     2.4     2.9
        state  Ohino  Ohino  Ohino  Nevada  Nevada
        year    2000   2001   2002    2001    2002
        
        [3 rows x 5 columns]

5. `sort_index(axis=0, ascending=True)`索引排序, axis=1, 排序columns, axis=0,排序index, ascending=False, 降序, 默认是升序

        In [52]: df
        Out[52]: 
           pop   state  year
        0  1.5   Ohino  2000
        1  1.7   Ohino  2001
        2  3.6   Ohino  2002
        3  2.4  Nevada  2001
        4  2.9  Nevada  2002
        
        [5 rows x 3 columns]
        
        In [53]: df.sort_index(axis=1, ascending=False)
        Out[53]: 
           year   state  pop
        0  2000   Ohino  1.5
        1  2001   Ohino  1.7
        2  2002   Ohino  3.6
        3  2001  Nevada  2.4
        4  2002  Nevada  2.9

        [5 rows x 3 columns]

6. `sort(columns, ascending=True)` 按值排序, columns=columns_name,可以接受一个值或者一个一维数据, ascending=False表示降序, 默认是升序

        In [60]: df3
        Out[60]: 
                           w         x         y         z
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        
        [6 rows x 4 columns]
        
        In [61]: df3.sort('w')
        Out[61]: 
                           w         x         y         z
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        
        [6 rows x 4 columns]
        
        In [62]: df3.sort(columns='w')
        Out[62]: 
                           w         x         y         z
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        
        [6 rows x 4 columns]
        
        In [63]: df3.sort(columns=['w', 'x'])
        Out[63]: 
                           w         x         y         z
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-06  0.137480  0.162058  1.516405 -0.927173
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        
        [6 rows x 4 columns]

### 选择, 过滤, 查找

1. 直接使用列名(column name), 等价与df. *column_name_*

        In [64]: df3['w']
        Out[64]: 
        2016-03-01    0.189541
        2016-03-02   -2.268193
        2016-03-03   -0.460397
        2016-03-04    0.119887
        2016-03-05    0.175106
        2016-03-06    0.137480
        Freq: D, Name: w, dtype: float64

2. 使用[], 可以对行(rows)进行切片, 集行选择

        In [67]: df3[0:3]
        Out[67]: 
                           w         x         y         z
        2016-03-01  0.189541 -0.663132  1.143200  0.407860
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        
        [3 rows x 4 columns]
        
        In [68]: df3['20160302':'20160305']
        Out[68]: 
                           w         x         y         z
        2016-03-02 -2.268193  0.804897  0.371822  0.218351
        2016-03-03 -0.460397 -0.099081  1.352768  0.190879
        2016-03-04  0.119887  0.810889 -0.305570  1.809606
        2016-03-05  0.175106 -0.292139 -0.816183 -0.772443
        
        [4 rows x 4 columns]

3. `df.loc[df.index[i]]` 获得一个横截面, 也就是某一行(row)的数据, 获取某一行的数据

        In [69]: df3.loc[df3.index[2]]
        Out[69]: 
        w   -0.460397
        x   -0.099081
        y    1.352768
        z    0.190879
        Name: 2016-03-03 00:00:00, dtype: float6

4. `df.loc[:, ['A', 'B']]` 获取多列(columns)数据

        In [70]: df3.loc[:, ['x', 'z']]
        Out[70]: 
                           x         z
        2016-03-01 -0.663132  0.407860
        2016-03-02  0.804897  0.218351
        2016-03-03 -0.099081  0.190879
        2016-03-04  0.810889  1.809606
        2016-03-05 -0.292139 -0.772443
        2016-03-06  0.162058 -0.927173
        
        [6 rows x 2 columns]

5. `df.loc[df.index[1]:df.index[3], ['w', 'x']]` 获取多行多列数据


        In [73]: df3.loc['20160301':'20160303', ['w', 'x']]
        Out[73]: 
                           w         x
        2016-03-01  0.189541 -0.663132
        2016-03-02 -2.268193  0.804897
        2016-03-03 -0.460397 -0.099081
        
        [3 rows x 2 columns]

6. `df.loc[df.index[i], ['a', 'b']]` 获取指定行的多列数据, 放回的Series的name属性=df.index[i]

        In [78]: df3.loc[df3.index[0], ['x', 'y']]
        Out[78]: 
        x   -0.663132
        y    1.143200
        Name: 2016-03-01 00:00:00, dtype: float64

7. `df.loc[df.index[i], 'a']` or `df.at[df.index[i], 'a']` 获得对应行对应列的数据, 返回值为标量

        In [80]: df3.loc['20160301', 'x']
        Out[80]: -0.6631320997645348
        
        In [82]: df3.at[df3.index[0], 'x']
        Out[82]: -0.6631320997645348

8. `df.iloc[]` 按位置选择, 相当于将`df.loc[]`值换成了位置索引, 唯一的区别在于使用`:`符号不包含后值, 在`df.loc[]`中,索引值使用`:`是包含后值的.
    `df.iat[ix, cx]`等价于 `df.iloc[ix, cx]`

        # 等价于 df3.iloc[df3.index[1]], 下面类同
        In [85]: df3.iloc[1]
        Out[85]: 
        w   -2.268193
        x    0.804897
        y    0.371822
        z    0.218351
        Name: 2016-03-02 00:00:00, dtype: float64

        # 等价于 df3.iloc[df3.index[3], df3.columns[2]], 下面类同
        In [86]: df3.iloc[3, 2]
        Out[86]: -0.30557047056654313
        
        In [87]: df3.iloc[3, 1:3]
        Out[87]: 
        x    0.810889
        y   -0.305570
        Name: 2016-03-04 00:00:00, dtype: float64
        
        In [88]: df3.iloc[1:3, 1]
        Out[88]: 
        2016-03-02    0.804897
        2016-03-03   -0.099081
        Freq: D, Name: x, dtype: float64
        
        In [89]: df3.iloc[1:3, 1:3]
        Out[89]: 
                           x         y
        2016-03-02  0.804897  0.371822
        2016-03-03 -0.099081  1.352768
        
        [2 rows x 2 columns]

        In [91]: df3.loc[df3.index[1:3], df3.columns[1:3]]
        Out[91]: 
                           x         y
        2016-03-02  0.804897  0.371822
        2016-03-03 -0.099081  1.352768
        
        [2 rows x 2 columns]

        In [92]: df3.iat[3, 2]
        Out[92]: -0.30557047056654313


9. 使用布林表达式进行查找, 过滤 `df[bool_expression]`

    + `df[df['A'] > 0]` 对某一列进行过滤

            In [94]: df3[df3['x'] > 0]
            Out[94]: 
                               w         x         y         z
            2016-03-02 -2.268193  0.804897  0.371822  0.218351
            2016-03-04  0.119887  0.810889 -0.305570  1.809606
            2016-03-06  0.137480  0.162058  1.516405 -0.927173
            
            [3 rows x 4 columns]

    + `df[df > 0]` 把不满足条件的数据转换为NaN

            In [95]: df3[df3 > 0]
            Out[95]: 
                               w         x         y         z
            2016-03-01  0.189541       NaN  1.143200  0.407860
            2016-03-02       NaN  0.804897  0.371822  0.218351
            2016-03-03       NaN       NaN  1.352768  0.190879
            2016-03-04  0.119887  0.810889       NaN  1.809606
            2016-03-05  0.175106       NaN       NaN       NaN
            2016-03-06  0.137480  0.162058  1.516405       NaN
            
            [6 rows x 4 columns]

    + `df[df['A'].isin(['1', '2', '3'])]` 过滤, 选取对应列(column)中出现在列表中的数据
    
            In [96]: df4 = df3.copy()
            
            In [98]: df4['v'] = ['one', 'two', 'three', 'four', 'five', 'six']
            
            In [99]: df4
            Out[99]: 
                               w         x         y         z      v
            2016-03-01  0.189541 -0.663132  1.143200  0.407860    one
            2016-03-02 -2.268193  0.804897  0.371822  0.218351    two
            2016-03-03 -0.460397 -0.099081  1.352768  0.190879  three
            2016-03-04  0.119887  0.810889 -0.305570  1.809606   four
            2016-03-05  0.175106 -0.292139 -0.816183 -0.772443   five
            2016-03-06  0.137480  0.162058  1.516405 -0.927173    six
            
            [6 rows x 5 columns]
            
            In [100]: df4[df4['v'].isin(['one', 'three'])]
            Out[100]: 
                               w         x         y         z      v
            2016-03-01  0.189541 -0.663132  1.143200  0.407860    one
            2016-03-03 -0.460397 -0.099081  1.352768  0.190879  three
            
            [2 rows x 5 columns]

    + `df[df[key].map(lambda x: x.startswith('B1'))]` 匿名函数过滤, x是对应列的各个值
        查找 *key* 列(column)以'B1'起始的项目.

    + &, | 可以连接多个boolean表达式, 注意每个表达式必需使用括号括起来`df[(df['x'] == x) | (df['y'] == y)]`

### 修改值, 更新值, 设置值, update, set, modify

1. 通过标签设置值, `df.at[]`, `df.loc[]` 与上面的查看数据方法类似

2. 通过位置设置值, `df.iat[ix, cx]`, `df.iloc[]` 与上面通过位置查看数据方法类似

3. A where operation with setting, 通过布林表达式来修改值, 过滤并修改之

        # 将所有指都转换为非正数
        In [104]: df3[df3 > 0] = -df3
        
        In [105]: df3
        Out[105]: 
                           w         x         y         z
        2016-03-01 -0.189541 -0.663132 -1.143200 -0.407860
        2016-03-02 -2.268193 -0.804897 -0.371822 -0.218351
        2016-03-03 -0.460397 -0.099081 -1.352768 -0.190879
        2016-03-04 -0.119887 -0.810889 -0.305570 -1.809606
        2016-03-05 -0.175106 -0.292139 -0.816183 -0.772443
        2016-03-06 -0.137480 -0.162058 -1.516405 -0.927173
        
        [6 rows x 4 columns]


### 丢失的数据

1. `df.dropna(how='any', subset=None)` 舍弃丢失的NaN值, how可以组织`any` or `all`, `subset`选择需要过滤的列(column)的列表

        In [107]: df3 = df3 + 1
        
        In [109]: df5 = df3[df3 > 0]
        
        In [110]: df5
        Out[110]: 
                           w         x         y         z
        2016-03-01  0.810459  0.336868       NaN  0.592140
        2016-03-02       NaN  0.195103  0.628178  0.781649
        2016-03-03  0.539603  0.900919       NaN  0.809121
        2016-03-04  0.880113  0.189111  0.694430       NaN
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        2016-03-06  0.862520  0.837942       NaN  0.072827
        
        [6 rows x 4 columns]
        
        In [111]: df5.dropna(how='any')
        Out[111]: 
                           w         x         y         z
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        
        [1 rows x 4 columns]

        In [114]: df5.dropna(how='any', subset=['x', 'y'])
        Out[114]: 
                           w         x         y         z
        2016-03-02       NaN  0.195103  0.628178  0.781649
        2016-03-04  0.880113  0.189111  0.694430       NaN
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        
        [3 rows x 4 columns]

2. `df.fillna(value=5)` 将NaN替换成指定的值, value可以是标量scalar, 或者字典, Series等键值对


        In [120]: df5.fillna(value=5)
        Out[120]: 
                           w         x         y         z
        2016-03-01  0.810459  0.336868  5.000000  0.592140
        2016-03-02  5.000000  0.195103  0.628178  0.781649
        2016-03-03  0.539603  0.900919  5.000000  0.809121
        2016-03-04  0.880113  0.189111  0.694430  5.000000
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        2016-03-06  0.862520  0.837942  5.000000  0.072827
        
        [6 rows x 4 columns]
        
        In [123]: df5.fillna(value={'w': 5, 'x': 4})
        Out[123]: 
                           w         x         y         z
        2016-03-01  0.810459  0.336868       NaN  0.592140
        2016-03-02  5.000000  0.195103  0.628178  0.781649
        2016-03-03  0.539603  0.900919       NaN  0.809121
        2016-03-04  0.880113  0.189111  0.694430       NaN
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        2016-03-06  0.862520  0.837942       NaN  0.072827
        
        [6 rows x 4 columns]

3. `pd.isnull(df)` 获得哪些值是`nan`

        In [125]: df5.isnull()
        Out[125]: 
                        w      x      y      z
        2016-03-01  False  False   True  False
        2016-03-02   True  False  False  False
        2016-03-03  False  False   True  False
        2016-03-04  False  False  False   True
        2016-03-05  False  False  False  False
        2016-03-06  False  False   True  False
        
        [6 rows x 4 columns]

## 操作, 数据计算

### 统计数据

#### 均值

1. 列均值`df.mean()` columns mean

        In [126]: df5.mean()
        Out[126]: 
        w    0.783518
        x    0.527967
        y    0.502141
        z    0.496659
        dtype: float64

2. 行均值`df.mean(1)` rows mean

        In [127]: df5.mean(1)
        Out[127]: 
        2016-03-01    0.579822
        2016-03-02    0.534977
        2016-03-03    0.749881
        2016-03-04    0.587884
        2016-03-05    0.486032
        2016-03-06    0.591096
        Freq: D, dtype: float64

3. `df.sub(series, axis={0, 1, index, columns}, fill_value=5)` 算术方法, 减法 将对应行或者列的数据全部转换为`NaN`
类似的还有`df.add()`, `df.div()`, `df.mul()`


    In [132]: s5 = pd.Series(data=[np.nan, np.nan, 1, 3, 5, np.nan], index=pd.date_range('20160301', periods=6)) 
    
    In [133]: s5
    Out[133]: 
    2016-03-01   NaN
    2016-03-02   NaN
    2016-03-03     1
    2016-03-04     3
    2016-03-05     5
    2016-03-06   NaN
    Freq: D, dtype: float64
    
    In [134]: df5
    Out[134]: 
                       w         x         y         z
    2016-03-01  0.810459  0.336868       NaN  0.592140
    2016-03-02       NaN  0.195103  0.628178  0.781649
    2016-03-03  0.539603  0.900919       NaN  0.809121
    2016-03-04  0.880113  0.189111  0.694430       NaN
    2016-03-05  0.824894  0.707861  0.183817  0.227557
    2016-03-06  0.862520  0.837942       NaN  0.072827
    
    [6 rows x 4 columns] 
    
    In [137]: df5.sub(s5, axis='index')
    Out[137]: 
                       w         x         y         z
    2016-03-01       NaN       NaN       NaN       NaN
    2016-03-02       NaN       NaN       NaN       NaN
    2016-03-03 -0.460397 -0.099081       NaN -0.190879
    2016-03-04 -2.119887 -2.810889 -2.305570       NaN
    2016-03-05 -4.175106 -4.292139 -4.816183 -4.772443
    2016-03-06       NaN       NaN       NaN       NaN
    
    [6 rows x 4 columns]

#### 申请可调有对象, apply callable object, Applay

1. 累积和 `df.apply(np.cumsum)`, 不同于直接调用`np.cumsum(arr)`的地方是这里会忽略掉NaN值

        In [138]: df5
        Out[138]: 
                           w         x         y         z
        2016-03-01  0.810459  0.336868       NaN  0.592140
        2016-03-02       NaN  0.195103  0.628178  0.781649
        2016-03-03  0.539603  0.900919       NaN  0.809121
        2016-03-04  0.880113  0.189111  0.694430       NaN
        2016-03-05  0.824894  0.707861  0.183817  0.227557
        2016-03-06  0.862520  0.837942       NaN  0.072827
        
        [6 rows x 4 columns]
        
        In [140]: df5.apply(np.cumsum)
        Out[140]: 
                           w         x         y         z
        2016-03-01  0.810459  0.336868       NaN  0.592140
        2016-03-02       NaN  0.531971  0.628178  1.373789
        2016-03-03  1.350061  1.432890       NaN  2.182910
        2016-03-04  2.230174  1.622001  1.322607       NaN
        2016-03-05  3.055068  2.329863  1.506424  2.410467
        2016-03-06  3.917588  3.167804       NaN  2.483294
        
        [6 rows x 4 columns]

2. `lambda`函数, 匿名函数的参数对于对应的列(column)Series

        In [141]: df5.apply(lambda x: x.max() - x.min())
        Out[141]: 
        w    0.340510
        x    0.711808
        y    0.510612
        z    0.736294
        dtype: float64

#### 计数, 按类型计数

`df['a'].value_counts()` 单列统计

`df.groupby([col_list]).count().iloc[:, 0]` 多列统计

`df[df['a'] == a]['b'].value_counts()` 这个也可以进行多列统计

`df[(df['a'] == a) & df['b'] == b].count()`

#### 字符串方法

`df.str.method_name()`

### Merge, 归并, 合并

#### 连接, concat

`pd.concat(pandas_object_list)` 把元素连接在一起

    In [171]: dfm = pd.DataFrame(np.random.randint(1, 10, size=(10, 4)))
    
    In [172]: dfm
    Out[172]: 
       0  1  2  3
    0  7  1  3  4
    1  9  5  5  1
    2  1  2  2  4
    3  7  6  1  4
    4  9  6  2  4
    5  3  2  1  1
    6  8  5  3  9
    7  7  3  4  3
    8  2  1  2  9
    9  9  3  5  5
    
    [10 rows x 4 columns]
    
    In [175]: pieces = [dfm[:], dfm[3:7], dfm[7:]]
    
    In [176]: pd.concat(pieces)
    Out[176]: 
       0  1  2  3
    0  7  1  3  4
    1  9  5  5  1
    2  1  2  2  4
    3  7  6  1  4
    4  9  6  2  4
    5  3  2  1  1
    6  8  5  3  9
    7  7  3  4  3
    8  2  1  2  9
    9  9  3  5  5
    3  7  6  1  4
    4  9  6  2  4
    5  3  2  1  1
    6  8  5  3  9
    7  7  3  4  3
    8  2  1  2  9
    9  9  3  5  5
    
    [17 rows x 4 columns]

#### join, 联合, 多表合并

`pd.merge(df1, df2, on='key')`


    In [177]: left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    
    In [178]: right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    
    In [179]: left
    Out[179]: 
       key  lval
    0  foo     1
    1  foo     2
    
    [2 rows x 2 columns]
    
    In [180]: right
    Out[180]: 
       key  rval
    0  foo     4
    1  foo     5
    
    [2 rows x 2 columns]
    
    In [181]: pd.merge(left, right, on='key')
    Out[181]: 
       key  lval  rval
    0  foo     1     4
    1  foo     1     5
    2  foo     2     4
    3  foo     2     5
    
    [4 rows x 3 columns]

    In [182]: right = pd.DataFrame({'key': ['foo', 'foo', 'jar'], 'rval': [4, 5, 6]})
    
    In [183]: pd.merge(left, right, on='key')
    Out[183]: 
       key  lval  rval
    0  foo     1     4
    1  foo     1     5
    2  foo     2     4
    3  foo     2     5
    
    [4 rows x 3 columns]

#### 添加, Append

`df.append(series-like, ignore_index=True)`

`df.append({index: series-like.values})`


    In [184]: dfm
    Out[184]: 
       0  1  2  3
    0  7  1  3  4
    1  9  5  5  1
    2  1  2  2  4
    3  7  6  1  4
    4  9  6  2  4
    5  3  2  1  1
    6  8  5  3  9
    7  7  3  4  3
    8  2  1  2  9
    9  9  3  5  5
    
    [10 rows x 4 columns]
    
    In [186]: dfm.append(dfm.iloc[3])
    Out[186]: 
       0  1  2  3
    0  7  1  3  4
    1  9  5  5  1
    2  1  2  2  4
    3  7  6  1  4
    4  9  6  2  4
    5  3  2  1  1
    6  8  5  3  9
    7  7  3  4  3
    8  2  1  2  9
    9  9  3  5  5
    3  7  6  1  4
    
    [11 rows x 4 columns]
    
    In [187]: dfm.append(dfm.iloc[3], ignore_index=True)
    Out[187]: 
        0  1  2  3
    0   7  1  3  4
    1   9  5  5  1
    2   1  2  2  4
    3   7  6  1  4
    4   9  6  2  4
    5   3  2  1  1
    6   8  5  3  9
    7   7  3  4  3
    8   2  1  2  9
    9   9  3  5  5
    10  7  6  1  4
    
    [11 rows x 4 columns]

### Grouping, 分组联合, 合并

1. `df.groupby(columns)`

        In [188]:  dfg = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
           ....:                           'foo', 'bar', 'foo', 'foo'],
           ....:                    'B' : ['one', 'one', 'two', 'three',
           ....:                           'two', 'two', 'one', 'three'],
           ....:                    'C' : np.random.randn(8),
           ....:                    'D' : np.random.randn(8)})
           ....: 
           .....:    .....:    .....:    .....:    .....: 
        In [190]: dfg
        Out[190]: 
             A      B         C         D
        0  foo    one -1.637388  0.691315
        1  bar    one -1.036337  0.298661
        2  foo    two -0.653040 -1.769153
        3  bar  three  1.761951 -0.618460
        4  foo    two  0.300811  0.721890
        5  bar    two  0.390548  1.124015
        6  foo    one  0.798055 -0.577885
        7  foo  three  0.696769 -0.552198
        
        [8 rows x 4 columns]
        
        In [191]: dfg.groupby('A').sum()
        Out[191]: 
                    C         D
        A                      
        bar  1.116162  0.804216
        foo -0.494794 -1.486030
        
        [2 rows x 2 columns]

        In [192]: dfg.groupby(['A', 'B']).sum()
        Out[192]: 
                          C         D
        A   B                        
        bar one   -1.036337  0.298661
            three  1.761951 -0.618460
            two    0.390548  1.124015
        foo one   -0.839333  0.113431
            three  0.696769 -0.552198
            two   -0.352229 -1.047263
        
        [6 rows x 2 columns]


### 改变形状 Reshaping

#### Stack 栈

1. `df.stack()` 将DataFrame转换成多列索引的Series

    In [193]: tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
       ....:                      'foo', 'foo', 'qux', 'qux'],
       ....:                     ['one', 'two', 'one', 'two',
       ....:                      'one', 'two', 'one', 'two']]))
       .....:    .....:    .....: 
    In [194]: index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    
    In [195]: dfr = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    
    In [196]: dfr
    Out[196]: 
                         A         B
    first second                    
    bar   one     1.984268 -0.628256
          two     0.424702 -0.516971
    baz   one     1.308790  0.221231
          two     1.267427 -0.849810
    foo   one     0.321839 -0.793417
          two     0.314654 -0.604699
    qux   one    -0.799181 -1.247869
          two     0.111125 -0.884299
    
    [8 rows x 2 columns]
    
    In [197]: dfr[:4]
    Out[197]: 
                         A         B
    first second                    
    bar   one     1.984268 -0.628256
          two     0.424702 -0.516971
    baz   one     1.308790  0.221231
          two     1.267427 -0.849810
    
    [4 rows x 2 columns]
    
    In [198]: stacked = dfr.stack()
    
    In [199]: stacked
    Out[199]: 
    first  second   
    bar    one     A    1.984268
                   B   -0.628256
           two     A    0.424702
                   B   -0.516971
    baz    one     A    1.308790
                   B    0.221231
           two     A    1.267427
                   B   -0.849810
    foo    one     A    0.321839
                   B   -0.793417
           two     A    0.314654
                   B   -0.604699
    qux    one     A   -0.799181
                   B   -1.247869
           two     A    0.111125
                   B   -0.884299
    dtype: float64
    
    In [200]: dfr
    Out[200]: 
                         A         B
    first second                    
    bar   one     1.984268 -0.628256
          two     0.424702 -0.516971
    baz   one     1.308790  0.221231
          two     1.267427 -0.849810
    foo   one     0.321839 -0.793417
          two     0.314654 -0.604699
    qux   one    -0.799181 -1.247869
          two     0.111125 -0.884299
    
    [8 rows x 2 columns]
    
    In [201]: type(stacked)
    Out[201]: pandas.core.series.Series

2. `s.unstack()` 将Series默认按照最后一个level进行解栈,转换为DataFrame格式

        In [202]: stacked.unstack()
        Out[202]: 
                             A         B
        first second                    
        bar   one     1.984268 -0.628256
              two     0.424702 -0.516971
        baz   one     1.308790  0.221231
              two     1.267427 -0.849810
        foo   one     0.321839 -0.793417
              two     0.314654 -0.604699
        qux   one    -0.799181 -1.247869
              two     0.111125 -0.884299
        
        [8 rows x 2 columns]
        
        In [203]: stacked.unstack(0)
        Out[203]: 
        first          bar       baz       foo       qux
        second                                          
        one    A  1.984268  1.308790  0.321839 -0.799181
               B -0.628256  0.221231 -0.793417 -1.247869
        two    A  0.424702  1.267427  0.314654  0.111125
               B -0.516971 -0.849810 -0.604699 -0.884299
        
        [4 rows x 4 columns]
        
        In [204]: stacked.unstack(1)
        Out[204]: 
        second        one       two
        first                      
        bar   A  1.984268  0.424702
              B -0.628256 -0.516971
        baz   A  1.308790  1.267427
              B  0.221231 -0.849810
        foo   A  0.321839  0.314654
              B -0.793417 -0.604699
        qux   A -0.799181  0.111125
              B -1.247869 -0.884299
        
        [8 rows x 2 columns]

### 数据透视表 Pivot Tables

`pd.pivot_table(df, values='D', rows=['A', 'B'], cols=['C'])` rows使用哪几列的数据作为行(row)索引(index), cols表示使用哪几列的数据作为列(columns)索引(columns), values表是取哪一列的数据作为统计数据.

    In [207]: dfp = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
       .....:                    'B' : ['A', 'B', 'C'] * 4,
       .....:                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
       .....:                    'D' : np.random.randn(12),
       .....:                    'E' : np.random.randn(12)})
       .....:    .....:    .....:    .....: 
    In [208]: dfp
    Out[208]: 
            A  B    C         D         E
    0     one  A  foo  0.085550  1.100278
    1     one  B  foo  0.291772  2.052441
    2     two  C  foo -0.765489  1.455540
    3   three  A  bar -0.003229  0.934319
    4     one  B  bar -0.177889 -0.651707
    5     one  C  bar  1.436878  0.430591
    6     two  A  foo  0.018769 -0.642482
    7   three  B  foo  0.078693 -1.662352
    8     one  C  foo -0.692468  0.290056
    9     one  A  bar  0.482921  1.457736
    10    two  B  bar  0.046731  0.249600
    11  three  C  bar -0.550309 -1.645258
    
    [12 rows x 5 columns]
    
    In [211]: dfp.pivot_table(values='D', rows=['A', 'B'], cols=['C'])
    Out[211]: 
    C             bar       foo
    A     B                    
    one   A  0.482921  0.085550
          B -0.177889  0.291772
          C  1.436878 -0.692468
    three A -0.003229       NaN
          B       NaN  0.078693
          C -0.550309       NaN
    two   A       NaN  0.018769
          B  0.046731       NaN
          C       NaN -0.765489
    
    [9 rows x 2 columns]

### 时间序列 Time Series

### 直接描述, 断言, Categoricals

### 画图 plotting

`s.plot()`

`df.plot()`

### 数据导入导出 Getting Date In/Out
