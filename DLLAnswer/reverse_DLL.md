## DLL: Swap First and Last

```python
def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head
```


This code is designed to reverse a doubly linked list in-place. Here's a step-by-step explanation:

**Initialization:**

- The method starts by assigning the `temp` variable to the `head` of the list. This variable will be used to traverse the list from the beginning to the end.

**Traversal and Swapping Pointers:**

- The code enters a while loop that continues as long as `temp is not None`. This condition ensures that the loop goes through every node in the list.

- Inside the loop, for each node that `temp` points to, the prev and next pointers are swapped. This operation reverses the direction of the links for each node.

- `temp.prev, temp.next = temp.next, temp.prev` effectively changes the direction of the pointers. For example, if a node N points forward to N+1 (next) and backward to N-1 (prev), after this line, it will point forward to N-1 and backward to N+1.

- After swapping the pointers of the current node, `temp` is updated to `temp.prev`, which, due to the swap, now points to the next node in the original sequence. This update moves the traversal forward through the list, even though it seemingly moves to the prev node due to the reversed pointers.

**Final Adjustment:**

- After the loop completes, meaning temp has reached beyond the end of the list (temp is None), the head and tail of the list are swapped.

- This swapping of `self.head` and `self.tail` is necessary because, by reversing the direction of each node's pointers, what was originally the head of the list (the starting point) is now at the end position, and what was the tail (the end point) is now at the start. Swapping these pointers ensures that the list's head and tail properties correctly represent the new start and end of the reversed list.

**In summary, this code methodically reverses the direction of a doubly linked list by swapping the forward and backward pointers of each node and then adjusting the head and tail pointers of the list to reflect the reversed order.**

