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
         
