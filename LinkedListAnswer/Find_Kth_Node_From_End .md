## LL: Find Kth Node From End

```python
def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow
```

Let's dive into a detailed explanation of the `find_kth_from_end function`. This function is designed to retrieve the kth node from the end of a linked list.

For this example, let's consider a linked list with the nodes:

`1 → 2 → 3 → 4 → 5 → 6 → 7 → 8`

If we want to find the 3rd node from the end (i.e., k = 3), this node will be 6.



**Method Walkthrough:**

`def find_kth_from_end(ll, k):`


**Initialize two pointers, slow and fast, at the head of the linked list:**

`slow = fast = ll.head `<br>
Both pointers start at the head of the linked list. We'll advance the fast pointer first to create a gap of k nodes between slow and fast.

**Move the fast pointer k nodes ahead:**

`for _ in range(k):`<br>
This loop will advance the fast pointer k nodes forward, thereby creating a gap of k nodes between slow and fast.



**Check if we've gone beyond the end of the list:**
```python
    if fast is None:
        return None
```
If, while moving the fast pointer k steps, we find that fast becomes None, it means that the linked list has fewer than k nodes. Therefore, the kth node from the end doesn't exist, so we `return None`.



**Continue moving both pointers until the fast pointer reaches the end:**
```python
while fast:
    slow = slow.next
    fast = fast.next
```

At this stage, we continue moving both pointers at the same speed. By the time the fast pointer reaches the end of the list, the slow pointer will have advanced by the length of the list minus k nodes. This positions the slow pointer at the kth node from the end.



**Illustrative Steps for the list `1 → 2 → 3 → 4 → 5 → 6 → 7 → 8` and `k = 3`:**

- Both `slow` and `fast` start at node 1.

- We first advance the `fast` pointer 3 nodes ahead. After this step, `slow` is still at node 1, and fast is at node 4.

- Now, we move **both pointers at the same speed**. When fast reaches node 8 (the last node), slow is at node 5.

- The while loop will run one more time which will leave `slow` pointing to the 6 node which is the 3rd node from the end.



- **Return the node** where the `slow` pointer is located:
```python
return slow
```
At this point, the slow pointer is pointing to the kth node from the end. We return this node.



**Conclusion:** The find_kth_from_end function uses the two-pointer technique to efficiently find the kth node from the end of a linked list. By first positioning the fast pointer k nodes ahead of the slow pointer and then moving both pointers at the same speed, we ensure that when the fast pointer reaches the end, the slow pointer is at the desired kth node from the end. In our example, the function would return node 6 as the 3rd node from the end.