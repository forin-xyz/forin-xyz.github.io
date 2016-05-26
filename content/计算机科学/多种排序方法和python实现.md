Title: 多种排序方法和python实现
Date: 2015-07-31 23:00
Category: 计算机科学
Tags: 数据结构, 排序
Summary: 在计算机科学中,排序是一个非常重要的话题,也是计算算法中的基础,应用非常广泛。

在计算机科学中，排序是一个非常重要的话题，也是计算机算法中的基础，应用非常广泛。

下面就对一些常用的排序算法进行介绍和分析。

# 交换排序

## 算法描述

交换排序就是从序列的第一个元素开始，将位于该元素之后的元素一一与该位置的比较，

将比该元素小的元素与其交换，直到最后一个元素。

因为过程中频繁的交换元素顺序，故得名交换排序.

## 伪代码

#+BEGIN_SRC
input: Array a

length = a.size()
for i = 0 -> length - 1:
    for j = i + 1 -> length:
        if a[i] > a[j]:
             swap(a[i], a[j])

output: Array a
#+END_SRC

## 过程



## Python实现

/swapsort.py/
#+BEGIN_SRC python3 -n
def swapsort(lst):
    length = len(lst)
    for i in range(0, length-1):
        for j in range(i+1, length):
            if lst[i] > lst[j]:
                # swap lst[i], lst[j]
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def test_swapsort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = swapsort(lst)
    if sorted_list == sorted(lst_copy):
        print("test swapsort OK!")
    else:
        print("test swapsort failed")


if __name__ == "__main__":
    test_swapsort()
#+END_SRC

## 算法分析

1. 时间复杂度

   外层循环有n-1趟，内层循环有n-i-1趟，每趟比较一次，交换若干次，故
   $\sum\nolimits_{i=0}{n-2}{n-i-1} = \frac{n(n-1)}{2} = O(n^2)$。
   n 是序列的大小。

2. 空间复杂度

   O(1)


# 选择排序

## 算法描述

在序列中选出最小的元素与第一个元素进行交换，然后在重复这一个过程。

与交换排序的原理都是每一次找出最小的元素，但是元素交换的次数要比交换排序少。

## python实现

/selectsort.py/

#+BEGIN_SRC python3 -n
def imin(lst, start=0, end=None):
    """
    imin(lst, start, end) -> index.
    Return the minimum value's index in list from start to end.

    >>> lst = [3, 3, 2, 5]
    >>> imin(lst)
    2
    """
    if end is None:
        end = len(lst)
    idxmin = start
    for i in range(start + 1, end):
        if lst[i] < lst[idxmin]:
            idxmin = i
    return idxmin


def selectsort(lst):
    length = len(lst)
    for i in range(0, length-1):
        idxmin = imin(lst, i)
        # lst[i] <-> lst[imin]
        if idxmin > i:
            lst[i], lst[idxmin] = lst[idxmin], lst[i]
    return lst


def test_imin():
    lst = [2, 3, 1, 4]
    if imin(lst) == 2:
       print("test imin OK!")
    else:
       print("test imin failed!")


def test_selectsort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = selectsort(lst)
    print(lst)
    if sorted_list == sorted(lst_copy):
        print("test selectsort OK!")
    else:
        print("test selectsort failed")



if __name__ == "__main__":
    test_imin()
    test_selectsort()

#+END_SRC

## 算法分析

1. 时间复杂度

   和交换排序进行了相同次数的比较，但是交换次数不超过交换排序，故时间复杂度为
   $O(n^2)$。

2. 空间复杂度

   O(1)


# 插入排序

## 算法描述

每次将一个待排序的记录，按其关键字大小插入到前面已经排好序的子序列中的适当位置，

直到全部记录插入完成为止。

## python实现

/insertsort.py/

#+BEGIN_SRC python3 -n
def insertsort(lst):
    length = len(lst)
    for i in range(1, length):
        j = i
        tmp = lst[i]
        while j and lst[j] < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        if j<i: lst[j] = tmp;
    return lst


def test_insertsort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = insertsort(lst)
    if sorted_list == sorted(lst_copy):
        print("test insertsort OK!")
    else:
        print("test insertsort failed")


if __name__ == "__main__":
    test_insertsort()
#+END_SRC

## 函数式python实现

## 算法分析

1. 时间复杂度

   $O(n^2)$, 对于完全有序的序列来说，时间复杂度为O(1)。

2. 空间复杂度

   O(1)

3. 对于规模小或者基本有序的序列效果很好。


# 冒泡排序

## 算法描述

临近的元素两两进行比较,按照从小到大或者从大到小的顺序进行交换,

这样一趟过去后,最大或最小的元素被交换到了最后一位,

然后再从头开始进行两两比较交换,直到倒数第二位时结束。

元素小的元素像气泡一样从底部移动到顶部。

## python实现

/bubblesort.py/

#+BEGIN_SRC python3 -
def bubblesort(lst):
    length = len(lst)
    if length < 2:
       return lst
    for i in range(0, length-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return bubblesort(lst[:-1]) + [lst[-1]]


def test_bubblesort():
    # lst = [ 9, 4, 3, 10, 0, 13, 2]
    lst = [9, 4, 3, 10, 0, 13, 2]
    lst_copy = lst[:]
    sorted_list = bubblesort(lst)
    if sorted_list == sorted(lst_copy):
        print("test bubblesort OK!")
    else:
        print("test bubblesort failed")


if __name__ == "__main__":
    test_bubblesort()
#+END_SRC

## 算法分析

1. 时间复杂度

   $O(n^2)$

2. 空间复杂度

   O(1)

3. 每一趟都让序列更接近有序


# 归并排序

## 算法描述

将序列分成两部分别进行排序。

该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

关键在于如何归并两个有序序列。

归并: 每一次选出两个序列头部最小的元素添加入新序列。

## python实现

/mergesort.py/

#+BEGIN_SRC python3 -
def mergelist(lsta, lstb):
    """mergelist(lsta, lstb) -> lst
    Merge two sorted list lsta and lstb to a sorted list lst.
    """
    ret = []
    lena, lenb = len(lsta), len(lstb)
    i, j = 0, 0
    while i < lena and j < lenb:
        if lsta[i] <= lstb[j]:
            ret.append(lsta[i])
            i = i + 1
        else:
            ret.append(lstb[j])
            j = j + 1
    if i == lena:
        ret.extend(lstb[j:])
    elif j == lenb:
        ret.extend(lsta[i:])
    return ret


def mergesort(lst):
    length = len(lst)
    if length < 2:
        return lst
    else:
        mid = length>>1
        return mergelist(mergesort(lst[:mid]), mergesort(lst[mid:]))


def test_mergesort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = mergesort(lst)
    if sorted_list == sorted(lst_copy):
        print("test mergesort OK!")
    else:
        print("test mergesort failed")


def test_mergelist():
    la = [ 2, 4, 5, 6]
    lb = [1, 3, 4, 5]
    if mergelist(la, lb) == [1, 2, 3, 4, 4, 5, 5, 6]:
        print("test mergelist OK!")
    else:
        print("test mergelist Failed!")



if __name__ == "__main__":
     test_mergelist()
     test_mergesort()
#+END_SRC

## 算法分析

1. 时间复杂度

   归并两个数组的时间复杂度为n, 一共需要归并$\log_{2}(n)$次, 故
   时间复杂度为$n\log{n}$。

2. 空间复杂度

   归并两个数组需要额外的空间O(n)。

3. 由于将序列分断处理，所以归并排序适合并行运算，分布式系统以及外排序。


# 快速排序

## 算法描述

快速排序是将元素按照其中一个记录分成大于该记录和小于该记录的部分，然后在对
两个部分进行排序。快速排序也是分治法的经典应用。

## python实现

/quicksort.py/

#+BEGIN_SRC python3 -n
def splitlist(lst):
    pi, lst = lst[0], lst[1:]
    gt = [v for v in lst if v > pi ]
    lt = [v for v in lst if v < pi]
    eq = [v for v in lst if v == pi]
    return lt, [pi]+[eq], gt


def quicksort(lst):
    if len(lst) < 2:
        return lst
    lt, eq, gt = splitlist(lst)
    return quicksort(lt) + eq + quicksort(gt)


def test_splitlist():
    """
    >>> lst = [4, 2, 3, 1, 6, 7]
    >>> splitlist(lst)
    ([2, 3, 1], 4, [6, 7])
    """
    lst = [4, 2, 3, 1, 6, 7]
    lt, pi, gt = splitlist(lst)
    if lt == [2, 3, 1] and pi == 4 and gt == [6, 7]:
        print("test splitlist OK!")
    else:
        print("test splitlist Failed!")


def test_quicksort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = quicksort(lst)
    if sorted_list == sorted(lst_copy):
        print("test quicksort OK!")
    else:
        print("test quicksort failed")


if __name__ == "__main__":
    test_splitlist()
    test_quicksort()
#+END_SRC

## 算法分析

1. 时间复杂度

   平均时间复杂度$O(n\log n)$， 最坏情况$O(n^2)$

2. 空间复杂度

   $O(\log n)$, 函数栈

3. 上述python代码的实现的时间复杂度和空间复杂度都不是最优，对于python这样的
动态语言而言，可读性比性能更重要。而且python解释器对于python常见的结构都进行
优化，速度可能比过度复杂的代码性能更好。

   追求极致的性能，是底层代码C的任务，python这样的业务代码，求的是开发速度和
可读性，切不可本末倒置。如果对性能不满意，可以使用C代码重写python中常用的函数，
切不可把python代码整复杂。

4. 快速排序是使用最广泛的排序方法，但是其缺点是对于基本有序的数组，
它的时间复杂度确实最坏的情况。

## 如何将数组按照关键字分成两个部分

1. 确定起始位置i(默认为0)， 结束位置j(默认位置为数组长度-1)，以及基准元素p(默认为第一个元素)

2. 将基准元素与第一个元素进行交换(如果基准元素不为第一个元素)

3. 从j开始，往前遍历，直到第一个小于p的元素，将之与基准元素p[位置索引为i]交换， i=i+1

4. 从i向后遍历，直到第一个大于p的元素，将之与基准元素p[位置索引为j]交换, j=j+1

5. 判断i=j? 如果相等，则数组以i为分界线分成了两个部分，结束。如果不相等，则重复3,4步。

这个过程只遍历了一遍数组，而python实现则遍历了两遍数组，所以这个实现可以使用在C语言中以追求极致的性能。

## C语言实现

#+BEGIN_SRC C
#include <stdio.h>

typedef int ElementType;
typedef int compare(ElementType a, ElementType b);

/# 有一个小瑕疵就是中轴位置在移动后还会参与下一次比较
   例如一开始将start位置的值赋给了temp, 但是第二次从头比较的时候它又一次与自己进行了一次比较
   但是更改过后总是让程序显得笨拙, 不知道哪位大侠有好的办法可以实现他
   并且不会降低可读性#/
/# 另一个可以改进的地方就是当end-start<=5的时候可以使用插入排序取代快排, 这样在数据集很小的时候
   可以获得更高的性能
#/
void quiksort(ElementType lst[],int start,int end, compare compare)
{

        int i = start;

        int j = end;
        ElementType temp = lst[i];
        if( start >= end){ return; }

        while(i < j)
        {
                // while(a[j] >= temp && (i<j) )
                while(compare(lst[j], temp)>=0 && (i < j))
                {
                        j--;
                }
                lst[i] = lst[j];
                //while(a[i] <= temp && (i < j))
                while(compare(lst[i], temp)<=0 && (i < j))
                {
                        i++;
                }
                lst[j]= lst[i];
        }
        lst[i] = temp;
        quiksort(lst, start, i-1, compare);
        quiksort(lst, j+1, end, compare);
}

int compareInt(ElementType a, ElementType b)
{
        return a - b;
}

int main()
{
        // test quiksort

        int arr[8] = {6, 1, 5, 4, 8, 3, 7, 2};
        int correct[8] = {1, 2 ,3 ,4 ,5 ,6, 7, 8};

        int i = 0;

        compare # cpr = compareInt;
        quiksort(arr,0,7, cpr);

        for(i=0;i<8;i++)

        {

                if( arr[i] != correct[i])
                {
                        printf("quicksort error!\n");
                        return 1;
                };

        }

        printf("quicksort ok!");

        return 0;

}
#+END_SRC

## python实现与C实现比较
1. python实现非常简洁, 只有10行语句, 可读性非常强, 把快速排序的思维展现了出来
2. C实现更底层, 空间效率和时间效率非常高, 除掉函数堆栈和一些排序索引之类的变量,
只使用了一个辅助空间. 时间上每一次分割也只扫描一遍数据集.

# 希尔排序

## 算法描述

先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）
分别进行直接插入排序，然后依次缩减增量再进行排序，待整个序列中的元素
基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。

## python实现

/shellsort.py/

#+BEGIN_SRC python3 -n
# 使用的增量序列为 Hibbard：{1, 3, ..., 2^e-1}
# e[0] = math.floor(math.log(length, 2))
# 初始增量: h[0] = pow(2, e[0]) - 1

import math
def shellsort(lst):
    length = len(lst)
    e = math.floor(math.log(length, 2))
    while e > 0:
        h = pow(2, e) - 1
        for i in range(h):
            for j in range(i + h, length, h):
                # 插入排序
                k = j
                while lst[k] < lst[k-h] and k > i:
                     lst[k], lst[k-h] = lst[k-h], lst[k]
                     k = k - h
        e -= 1
    return lst

def test_shellsort():
    # lst = [ 9, 4, 3, 10, 7, 13, 2]
    lst = [9, 4, 3, 10, 7, 13, 2]
    lst_copy = lst[:]
    sorted_list = shellsort(lst)
    if sorted_list == sorted(lst_copy):
        print("test shellsort OK!")
    else:
        print("test shellsort failed")

if __name__ == "__main__":
    test_shellsort()
#+END_SRC

## 算法分析
1. 时间复杂度

   时间复杂的下界是$O(n\log^2 n)$, 上界是$O(n^2)$。

2. 空间复杂度

   O(1)

3. 因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，
因此希尔排序在时间效率上比前两种方法有较大提高。

4. 对于Hibbard增量序列，复杂度为$O(n^1.5)$

5. 希尔排序适合规模中等，序列的有序情况不能预测的情形。

# TODO 堆排序

# TODO 基数排序


# 参考资料

1. [[程序设计基础  哈工大][http://www.icourse163.org/course/hit-56001?tid=60001#/info]]

2. [[http://www.cricode.com/3212.html][8大排序算法图文讲解
]]
