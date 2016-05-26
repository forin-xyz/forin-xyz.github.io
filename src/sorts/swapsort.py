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
