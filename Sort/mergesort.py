
def merge_sort1(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2    #Finding the mid of the array
        left_half = a_list[:mid]  # Dividing the array elements
        right_half = a_list[mid:]  # into 2 halves

        merge_sort(left_half)   # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = 0
        j = 0
        k = 0
        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
           # print('Main merge a_list[{}] is {}'.format(k-1, a_list[k - 1]))

        # copying the remaining sorted elements
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
           # print('Left merge a_list[{}] is {}'.format(k-1, a_list[k-1]))

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
           # print('Right merge a_list[{}] is {}'.format(k-1, a_list[k-1]))
    print("Merging", a_list)
    print('-'*40)


def merge_sort(a_list):
    print("Splitting: ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # merge
        i = 0
        j = 0
        k = 0  # record the current index

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

        print("Merging:", a_list)




if __name__ == "__main__":
    #alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #alist = [1, 3, 5, 7, 2, 4, 6, 8]
    alist = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
    print(len(alist))
    merge_sort(alist)
    print(alist)