## LL: Remove Duplicates ( ** Interview Question)
<br>

```python
def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next

```
Let's break down the `remove_duplicates` function.

This function aims to remove any duplicate nodes from a linked list. For instance, if you have a linked list:

`3 → 5 → 3 → 7 → 8 → 5 → 9`

After removing duplicates, it should look like:

`3 → 5 → 7 → 8 → 9`

**Method Walkthrough:**
```python
def remove_duplicates(self):
```

**Initialize a set to store unique values:**
```python
values = set()
```

We're using a set (`values`) because checking membership in a set is typically O(1), making it efficient for this operation. As we traverse the list, we'll add each encountered node's value to this set.



**Setup initial pointers:**
```python
previous = None
current = self.head
```

The `current` pointer will traverse through the list, while `previous` will keep track of the last unique node.

**Iterate through the list to remove duplicates:**
```python
while current:
```
This loop will traverse each node in the linked list.



**Check if the current node's value is in our set of seen values:**
```python
if current.value in values:
```

If this condition is true, it means we've seen this value before, and therefore, the current node is a duplicate.



**Remove the current node from the list:**
```python
    previous.next = current.next
    self.length -= 1
```
If the current node's value is a duplicate, we'll bypass it by pointing the next attribute of the previous node directly to current.next, effectively skipping over the current node. We then decrement the length of the linked list since we've removed a node.

**Otherwise, if the value is unique (not seen before):**
```python
else:
    values.add(current.value)
    previous = current
```
If we haven't seen the current value before, we add it to our set (values) and move the previous pointer to point at the current node since it's unique.



**Move to the next node:**
```python
    current = current.next
```
We update the current pointer to move on to the next node in the list for further processing.



**Conclusion: The remove_duplicates method efficiently iterates through the linked list, maintaining a set of seen values. If a value is repeated, the node containing that value gets removed from the list. By the end of the function, all duplicate nodes in the linked list will have been removed. In our example, repeated nodes with values 3 and 5 are removed, leaving us with a linked list of unique values: `3 → 5 → 7 → 8 → 9`.**

