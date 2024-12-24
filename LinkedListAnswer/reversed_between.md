## LL: Reverse Between ( ** Interview Question)
<br>

```python
 def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
    
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        for i in range(start_index):
            previous_node = previous_node.next
    
        current_node = previous_node.next
    
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        self.head = dummy_node.next
```
Given the list:
`1 → 2 → 3 → 4 → 5.`

Our goal with 0-based indexing: Reverse nodes between indices 1 and 3 (inclusive) to get the result:
`1 → 4 → 3 → 2 → 5`.



**Detailed Walkthrough:**

**Preliminary Steps:**

1. Check if the list is empty or has only one node:
```python
if self.length <= 1:
    return
```

It's pointless to reverse if there's only one or no nodes.

2. Create a dummy node:
```python
dummy_node = Node(0)
dummy_node.next = self.head
```

This dummy node simplifies our code, especially if we need to reverse from the start of the list.

**Preparation:**

3. Navigate to the Preceding Node:

     Move to the node right before where the reversal starts.
```python
previous_node = dummy_node
for i in range(start_index):
    previous_node = previous_node.next
```

Here, if we're reversing from index 1 onwards, prev will point to node 1 (index 0).

4. Set current to the node at position m:
```python
current_node = previous_node.next
```

currentNode now points to the node at the index of 1, where our reversal starts.

**The Core Loop:**

5. Reverse nodes between start_index and end_index:
```python
for i in range(end_index - start_index):
    node_to_move = current_node.next
    current_node.next = node_to_move.next
    node_to_move.next = previous_node.next
    previous_node.next = node_to_move
```

Using our example, where we reverse nodes at indices 1 through 3:



**First iteration (Reversing node at index 2, i.e., node 3):**

- node_to_move will first point to node 3.

- Node 2 (current_node) will then point to node 4.

- Node 3 (node_to_move) will point to node 2.

- Node 1 (previous_node) points to node 3.

Result: `1 → 3 → 2 → 4 → 5`.



**Second iteration (Reversing node at index 3, i.e., node 4):**

- node_to_move will next point to node 4.

-Node 2 (current_node) will then point to node 5.

- Node 4 (node_to_move) will point to node 3.

- Node 1 (previous_node) points to node 4.

Result: `1 → 4 → 3 → 2 → 5`.
This is our desired reversed sequence!

**Finalization:**

6. Reset the head:
```python
self.head = dummy_node.next
```

This ensures the head now correctly points to the new start of the list if the reversal included the original first node.

Visualizing this with diagrams on paper or on a board is usually very helpful. Consider each node as a box and each pointer as an arrow. Move the boxes around as you progress through the code, and redraw the arrows according to where the pointers point.



