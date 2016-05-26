def splitlist(lst):
    pi, lst = lst[0], lst[1:]
    gt = [v for v in lst if v > pi ]
    lt = [v for v in lst if v <= pi]
    return lt, pi, gt

def quicksort(lst):
    if len(lst) < 2:
        return lst
    lt, pi, gt = splitlist(lst)
    return quicksort(lt) + [pi] + quicksort(gt)

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
