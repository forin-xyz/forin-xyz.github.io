#!/usr/bin/env python3

def insertsort(lst):
    length = len(lst)
    for i in range(1, length):
        j = i
        tmp = lst[i]
        while j and tmp < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        if j<i: lst[j] = tmp
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
