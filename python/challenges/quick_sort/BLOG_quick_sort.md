# Quick Sort
Welcome to another edition of the Yoni's Sorting Algorthims!

Today we will be discussing the Quick Sort method for sorting an array of values similiar to the merge method in the theme of divide and conqueuer!

There are 3 major components of the quick sort algorithm.
1. The recursive quick sort function which partitions the arr and then calls itself on the left and the right of the partition
2. The partitioner which creates a pivot point, in this case as the right most index. The partitioner then moves the current index value and swaps it with the right most index if the current index is less than or equal to the right.
3. The swap method flips the low and the left position

## Algorithm
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
## Step by step
Take the array [5,4,3,2,1]

left = 0 , right = 4

array[left] = 5 , array[right] = 1

left is currently less than right (0<4)
so we define position as the partition function outcome.
Put a pin in the partition function first round

Partition(arr,left,right)
arr = [5,4,3,2,1] , left = 0 , right = 4

define pivot as array[right] = 1

low = left - 1, so low = -1

for i (left to right)

i = 0 first round

arr[i] = 5 which is greater than the pivot

the if statement is not triggered in the first 4 passes through the for loop.

On the last pass through, the arr[4]=1 which is equal to the pivot of 1

This makes the last index swap with the 0th index. Making the array look like [1,4,3,2,5]

After the for loop is concluded, the partition function will swap the right most index (in this case the 4th index which equals 1) with the low + 1 index which is 1 in this case.

The new array looks like [1,5,3,2,4]
And the partition function returns the low + 1 which again is 1

Now that we can unpin the partition function, we recursively call quick sort once again.
But this time:

arr = [1,4,3,2,5] , left = 0, right = 0

pivot is defined as 1
low is defined as -1

we go back to the for loop at i of 0
the arr[0] is equal to the pivot because they are the same
low increments from -1 to 0
we swap it in place and move onto the next round of the loop

now we have i of 1, and arr[1] = 4, which is greater than the pivot.
It continues to go through until all of the





