def insertion_sort(alist):
    for index in range(1, len(alist)):

        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1

        # insert current_value in this position
        alist[position] = current_value

    return alist

alist = [1, 4, 2, 3, 69 ,23,123,21,4]
print(insertion_sort(alist))

