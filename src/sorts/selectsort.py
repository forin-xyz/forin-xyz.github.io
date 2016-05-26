def imin(lst, start=0, end=None):
    """
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
