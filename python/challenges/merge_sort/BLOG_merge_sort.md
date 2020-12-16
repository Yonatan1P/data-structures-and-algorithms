# Merge Sort
There are different types of sorting algorithms like insertions sorts. One of those types is the merge sort method. This post will go into the algorithm, code, and a walk through of the step by step process for merge sorting.

In a nutshell, the merge sort method will be taking in an array of numbers sorting that given array in order from least to greatest. It will do this using a recursive divide and conquer method.

## Algorithm
First, we want to find the middle index of our array.

Next we want to recursively call merge_sort on the left half, and then on the right half.

Once the entire array has been cut into pieces, it will be slowly built up and redivided as pieces are merged back together in the proper order.

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
## Code
This code steps through the input array and splits into into halves until the array is split into individual numbers
Once the left side is completely split, the merge method begins to be called and the left and right pieces are added back to the array in their correct order.
```
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
```
## Step-by-step
We start with our original input and split into a left and right.

Then we call merge_sort(left), so we split the left side again. But we call merge_sort(left) yet again.

This continues to happen until the array is split into individual units, and then the merge_sort begins to split the

right sides from smallest array to biggest. Once all the small right pieces are split and merged in order, then we go

off to the original right side and repeat the process all the way through.

The pieces continue to be recombined in the correct order, because the merge sort acts on the assumption that the right

and left halves are already in their own sorted order.

Image from https://www.geeksforgeeks.org/merge-sort/

![Merge-sort](../../assets/Merge-Sort-Tutorial.png)

# Complexity
Time - O(nlogn)

The time complexity grows with each new piece of data, but it does not grow linearly in a 1 to 1 fashion. Rather there is a significant increase in the complexity because for every piece of data, we not only need to split it and compare it, but in the worst case scenario we would need to split it and combine it until the piece was completely on the other side. This would not need to move once for every new position, but it would need to relate to the exponential size of the data because it would move by halves of the data set.

Space - O(n)

We need to store each of the pieces of data temporarily in their own left or right array, and there would be n of those arrays so there would be n pieces of temporary data being used to process this method.
