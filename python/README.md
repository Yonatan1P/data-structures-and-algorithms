# Data Structures and Algorithms
Code Fellows 401 d15 Python with JB Tellez
## In Challenges Folder
challenge-01:
![array-reverse](./assets/challenge1Whiteboard.png)

challenge-02:
![array-shift](./assets/challenge2-whiteboard.png)

challenge-03:
![array-binary-search](./assets/challenge3-whiteboard.png)

### Challenge 5
A linked list was created, with the ability to insert into and read out the entirety of the list.
#### Challenge
One major challenge was not being able to link the tests to the data_structures folder. Another major challenge was understanding how to add a node to the head, rather than to the end as appending methods in previous problems. Another annoying challenge I faced was an inability to properly use f strings to do what I wanted to do. I solved the issue with a roundabout concatonation method.
### Approach and Efficiency
First I tried to follow the demo in lecture, because the professors explanation of the linked list is better than any alternative explanation. It seemed clear enough to follow. As I got stuck, I asked my peers if they had ideas for my bugs. When I got frustrated I left the computer.
### API
There are 2 class of objects, Node and LinkedList
The LinkedList objects have a dunder init method which creates an empty LinkedList.

Then there is an insert method which replaces the head with a new Node object that has an input value and its next node property is the previous head.
Then there is an includes method which scans through the LinkedList object, starting at the head, and matches the queried value to existing node values while node values actually exist.
Finally, there is a dunder string method which prints out all the node values inside of a string with arrows point from one node to the next.
## In Data-Structures Folder
