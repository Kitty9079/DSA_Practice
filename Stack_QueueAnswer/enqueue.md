 # Queue Using Stacks: Enqueue

 ```python
 def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
```
This code implements the `enqueue` method for a queue that is implemented using two stacks. The purpose of the enqueue method is to add an element to the back of the queue.

Here's how the code works:



1. First, the code checks if `stack1` has any elements in it. If `stack1` is not empty, the code enters a `while` loop.

2. Inside the `while` loop, the code `pops` elements from `stack1` one at a time and `appends` them to `stack2`. This is done so that we can add the new element to the bottom of `stack1`.

3. Once all elements have been transferred from `stack1` to `stack2`, the code `appends` the new element value to the bottom of `stack1`.

4. Finally, the code enters another `while` loop to transfer all the elements from `stack2` back to `stack1` in their original order. This ensures that the queue is maintained in a First-In-First-Out (FIFO) ordering.