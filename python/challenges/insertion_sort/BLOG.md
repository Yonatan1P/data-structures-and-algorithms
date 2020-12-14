# SELECTION SORT
## What is selection sorting?
Have you ever played cards, and while you hold a bunch of cards in your hands, you got to search through and scan for cards and think which ones will be useful for you to play. Our minds can do this very quickly, but as the level of sorting complexity grows, so does the time and energy it takes to do that. Good thing we have logical computers that can do that job for us!

This article is going to go into the step by step break down of how a programmer would communicate to the computer to sort a list of number from least to greatest. To do this, we need look at an array, lets take [8,4,23,42,16,15] for example. If I asked you to list those numbers in order from least to greatest, you would know exactly what to do in a few seconds. But a computer would be able to take that same amount of time to sort through an array of a million numbers if we tell it how to do so.

## Psuedo Code
```
sert_sort(list):
    for index in range(1, len(list)):
        index_position = index
        temporary_position = list[index]

        while index_position > 0 and temporary_position < list[index_position - 1]:
            list[index_position] = list[index_position - 1]
            index_position -= 1
        list[index_position] = temporary_position
    return list

if __name__ == "__main__":
    sortify = insert_sort([8, 4, 23, 42, 16, 15])
    print(sortify)


# returns [4, 8, 15, 16, 23, 42]
```
## Expectations

Say you were given an array of numbers like in the psuedo code above. You would want to go through the list of values and replace the previous index value with the current index value if they previous is greater than the current. You keep going through the array until all the numbers are in the correct position, meaning that the order is from least to greatest.

Input: [8,4,23,42,16,15]

Expected Output: [4,8,15,16,23,42]

## First Round Through

In a 0 based index, start at index 1 and compare it to index 0.

Input: [8,4,23,42,16,15]

Value of Index 0 = 8

Value of Index 1 = 4

Because 4 is less than 8, it needs to switch places

Now our output array looks like this: [4,8,23,42,16,15]

## Second Round

We finished with the 4 and the 8 and now we move on to compare the next 2 index values, index 1 to index 2

Again, out array is currently: [4,8,23,42,16,15]

So our index 1 = 8, and our index 2 = 23.

Now 8 is less than 23, so no changes need to be made, our output array remiains the same and we move on to the next index

## Third Round

Once again, we index 2 is 23 while index 3 is 42.

These numbers are already in the correct position because 23 is less than 42.

## Fourth Round
Current array: [4,8,23,42,16,15]

At this point, we are at index 3 (value = 42) and index 4 (value = 16).

You can clearly see with your eyes that we need to move our current index 4 (16), to be between the 8 and the 23 (which makes it the nex index 2 value). But to make this happen, we need to go through our loop 2 times to make the comparison as long as the current and previous values need to flip.

The first round through, our current index is 4, and our previous index is 3. We compare those values of 16 to 42 and see that 16 is indeed less than 42. This means that we must switch their places and make the next comparison.

So in this intermediate step, we have a current array of: [4,8,23,16,42,15]

Now we want to compare the new current index of 3 (value = 16), to its previous index value of 2 (value =23).
Once again we find that 16 is less than 23, and thus we must switch their positions and make the comparison once more.

The current array becomes: [4,8,16,23,42,15]

At this point, we know we are done moving our 16 around using our human logic, but the computer still doesn't know that.
It will check the while statement once again to see if the current value, which is still 16, is less than the previous value of 8. In this case the numbers are already in the correct order and we can move on to the final comparison.

## Fifth Round

The array now looks like this: [4,8,16,23,42,15] and we know we are almost done.

We are now on the index 5 and comparing it to the previous index of 4.

Index 5= 15

Index 4 = 42

The current and previous index pass the while condition and switch positions, and the while condition continues to be met until the 15 has switched places with the 16. At that final condition, the while loop condition will not be met, so the for loop will have reached the limit of its range, and the final array will be returned.

Final Array: [4,8,15,16,23,42]

## Conclusions

Although this process may seem slower, more laborious, or simple, it can be used as a tool to help you in many more ways than you may understand at the moment. But this powerful concept can turn tedious work into thin air, and sort out all your problems.
