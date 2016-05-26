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
