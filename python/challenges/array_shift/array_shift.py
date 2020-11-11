array=[1,2,4,5,6,7,8] #the input array
insert=3 # the number that we want insert
if len(array)%2==0: # if the array is even
    spotToInsert=len(array)/2 #this is the middle index
else: # else if the array is odd
    spotToInsert=round(len(array)/2 + 1) # this is the middle index
firstHalf=[] # empty array for the first half of the input
secondHalf=[] # emptry array for the second half of the input
for num in array: # for every value in the input array
  if num<=spotToInsert: # if the index is still in the first half
    firstHalf += [num] # add the current number to the first array
  elif num>spotToInsert: # if the index is past the middle
    secondHalf += [num] # insert the current number into the second array

answer = firstHalf + [insert] + secondHalf # concatonate the 2 halves with the insert in the middle
print(answer) # print the answer
