**LL: Has Loop ( \*\* Interview Question\*\*)**<br>
```python
def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

Let's break down the `has_loop` function to understand how it detects a cycle (or loop) in a linked list. This method makes use of Floyd's cycle-finding algorithm, often referred to as the "tortoise and the hare" technique.

For the sake of visualization, imagine a linked list that has a loop in it, like this:

```
1 → 2 → 3 → 4 
          ↗ ↓
        6 ← 5
```

In this example, nodes 4, 5, and 6 form a loop.

**1. Initialize two pointers, `slow` (the tortoise) and `fast `(the hare):**
```
slow = self.head
fast = self.head
```
Both pointers start at the head of the linked list. The idea is to move the `slow` pointer one step at a time while moving the `fast` pointer two steps at a time.



**2. Traverse the linked list:**

while `fast is not None and fast.next is not None:`
This loop ensures we continue as long as `fast` and the node after `fast` (fast.next) are not None. This is similar to the logic we used in the `find_middle_node` function and serves to prevent potential errors by ensuring we don't access nonexistent nodes.



**3. Move the slow pointer one node and the fast pointer two nodes:**
```python
    slow = slow.next
    fast = fast.next.next
```
For each iteration of the loop, `slow` moves one step, and `fast` moves two steps.



**4. Check if the slow pointer meets the fast pointer:**
```python
    if slow == fast:
        return True
```
This is the crucial step. If there's a loop in the linked list, the fast pointer (which moves twice as quickly) will eventually catch up to the slow pointer inside the loop. When they meet (point to the same node), we've found a loop, and the function returns `True`.



Illustrative Steps for `1 → 2 → 3 → 4 → 5 → 6` (with loop from 6 to 4):

- Both `slow` and `fast` start at node 1.

- After the first iteration, `slow` is at node 2, and `fast` is at node 3.

- In the next iteration, `slow` moves to node 3, and `fast `jumps to node 5.

- Following that, `slow` reaches node 4, while `fast` is now at node 6.

- As we continue, `slow` will be at node 5, and `fast`, having moved two steps, will loop back and land on node 4.

- Eventually, as we iterate further, both pointers will meet inside the loop, confirming its presence.



**5. Return False if no loop is found:**

```python 
return False
```
If the loop completes without the two pointers meeting, it indicates there's no loop in the list, so the function `returns False`.



**Conclusion**: The `has_loop` method efficiently determines if a linked list contains a cycle or loop. By advancing one pointer at double the speed of the other, and checking if they ever meet, we can identify loops without needing to use any additional memory or mark visited nodes. If they meet, there's a loop. If they don't, the list has no loops.