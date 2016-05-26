def mergelist(lsta, lstb):
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
