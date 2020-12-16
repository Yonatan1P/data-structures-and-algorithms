def merge_sort(arr):
    arr_length = len(arr)
    if arr_length > 1:
        middle = arr_length//2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)

        merge_sort(right)

        merge(left,right,arr)

def merge(left,right,arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
