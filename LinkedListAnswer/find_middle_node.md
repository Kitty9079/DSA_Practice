## LL: Find Middle Node ( ** Interview Question)

```python 
def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

```

For this example, let's consider a linked list with the nodes:<br>
`1 → 2 → 3 → 4 → 5.`



Method Walkthrough: `find_middle_node`

`def find_middle_node(self):`


**1. Initialize two pointers, slow and fast:**


`slow = self.head`<br>
`fast = self.head`

Here, both pointers start at the head of the linked list. The idea is that `slow` will move one node at a time, while `fast` will move two nodes. By the time fast reaches the end, `slow` will be at the middle.



**2. Traverse the linked list:**

`while fast is not None and fast.next is not None:`<br>
This loop ensures that we continue as long as `fast` and the node after fast (`fast.next`) are not None. The two conditions are vital:

- The first, `fast is not None`, ensures that we haven't already reached the end of the list.

- The second, `fast.next is not None`, makes sure there's another node to move to, given that fast will be jumping two nodes in the next step. This prevents potential errors.

- This will allow us to find the middle node when there is an even or odd number of nodes.



**3. Move the slow pointer one node and the fast pointer two nodes:**

    slow = slow.next
    fast = fast.next.next


For each iteration of the loop, the `slow` pointer moves one step (or one node) and the `fast` pointer moves two steps (or two nodes).



Illustrative Steps for `1 → 2 → 3 → 4 → 5`:

- Both `slow` and `fast` start at node 1.

- After the first iteration, `slow` moves to node 2, and `fast` moves to node 3.

- In the second iteration, `slow` moves to node 3, and `fast` jumps to node 5.

- On the next attempt to iterate, since `fast.next` is None (there's no node after node 5), the loop stops.

- The `slow` pointer is now pointing to node 3, which is the middle of our list.



**4. Return the node the slow pointer is currently at:**

`return slow`


Once the loop exits, the slow pointer is either pointing to the middle node of the list (for odd-length lists) or the first of the two middle nodes (for even-length lists).



***Conclusion:*** The `find_middle_node` method efficiently locates the middle of a linked list by using a `two-pointer technique`. The `slow` pointer moves at half the speed of the `fast` pointer. By the time the `fast` pointer has traveled the full length of the list, the `slow` pointer has traveled half the length, landing it in the middle. In our example, the middle of `1 → 2 → 3 → 4 → 5` is node 3, and the method will return this node.