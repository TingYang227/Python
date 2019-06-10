def selection_sort(alist):
    for fill_slot in range(len(alist)-1, 0, -1):
        pos_max = 0
        for location in range(1, fill_slot+1):
            if alist[location] > alist[pos_max]:
                pos_max = location

        # put the largest element to the last (the position of fill_slot)
        temp = alist[fill_slot]
        alist[fill_slot] = alist[pos_max]
        alist[pos_max] = temp

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)