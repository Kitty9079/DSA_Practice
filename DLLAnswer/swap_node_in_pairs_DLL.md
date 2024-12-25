## DLL: Swap Nodes in Pairs

```python
def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
    
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            second_node.prev = previous_node
            first_node.prev = second_node
    
            if first_node.next:
                first_node.next.prev = first_node
    
            self.head = first_node.next
            previous_node = first_node
    
        self.head = dummy_node.next
    
        if self.head:
            self.head.prev = None

```

In this function, the goal is to swap every two adjacent nodes in the doubly linked list.

Given a doubly linked list like:

`1 <-> 2 <-> 3 <-> 4`

After performing the swap_pairs operation, it should look like:

`2 <-> 1 <-> 4 <-> 3`



**Method Walkthrough:**

`def swap_pairs(self):`


**Initialize a dummy node and connect it to head for easier manipulation:**
```python
dummy_node = Node(0)
dummy_node.next = self.head
```

This dummy node simplifies the swapping process, especially at the beginning of the list. We link the dummy's next to the head.



**Set up the previous pointer:**
```python
previous_node = dummy_node
```

`previous_node` pointer always points to the node just before the first node in the pair we're about to swap.



**Iterate through the list as long as there are at least two nodes left to swap:**
```python
while self.head and self.head.next:
```

**Assign the two nodes to be swapped to first_node and second_node:**
```python
first_node = self.head
second_node = self.head.next
```

**Swapping logic:**
a. **Point previousNode's next to second_node:**
```
previous_node.next = second_node
```
previous_node should point to the second node of the pair after swapping.



b. **Link the end of our swapped pair to the rest of the list:**

first_node.next = second_node.next
This ensures that after swapping, the list remains intact.



c. **Make the actual swap by reversing their next pointers:**

second_node.next = first_node


**Update the previous pointers for a doubly linked list:**

a. **Link the prev pointer of second_node:**

second_node.prev = previous_node


b. **Update the prev pointer for the first_node:**

first_node.prev = second_node


c. **Ensure that the node after our swapped pair has its prev updated:**
```python
if first_node.next:
    first_node.next.prev = first_node
```

Move the head pointer two nodes ahead for the next iteration:
```python
self.head = first_node.next
```

This is essential since we've swapped the current pair and need to move to the next pair.



**Update the previous_node pointer to point to the first_node after the swap:**
```python
previous_node = first_node
```
As we move on to the next pair, our previous pointer should move two nodes ahead, but since we've swapped them, it now needs to point to what was originally the first node of our pair.



**Finally, reset the head of the list:**
```python
self.head = dummy_node.next
```

Once we've swapped all possible pairs, we adjust our head to point to the node following our dummy node.



**Ensure the new head's previous pointer is None:**
```python
if self.head:
    self.head.prev = None
```
After all swaps, it's crucial to reset the prev pointer of the head to ensure the integrity of the doubly linked list.



**Conclusion: The swap_pairs function effectively swaps adjacent nodes in pairs for a doubly linked list. By employing a dummy node, we simplify the task of swapping, especially at the beginning of the list. After all operations, we ensure the head is correctly placed, and the previous pointers are updated to retain the doubly linked list's structure. In our given example, the nodes of `1 <-> 2 <-> 3 <-> 4` get swapped to become `2 <-> 1 <-> 4 <-> 3`.**