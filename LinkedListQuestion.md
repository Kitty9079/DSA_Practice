## LinkedList Interview Question

**1. LL: Find Middle Node ( ** Interview Question)**

Implement the `find_middle_node` method for the LinkedList class.

**Note: this `LinkedList` implementation does not have a `length `member variable.**

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

- The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

- The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.

- The method should only traverse the linked list once.  In other words, you can only use one loop.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ###################################### 




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""

```


**Solution**  for LL: Find Middle Node *[here](./find_middle_node.md)*

_____________________________________________________
<br>

**2. LL: Has Loop ( \*\* Interview Question\*\*)**<br>
Write a method called `has_loop` that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.

This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

1. The method should follow these guidelines:
Create two pointers, slow and fast, both initially pointing to the head of the linked list.

2. Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

3. If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

4. If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.

If your Linked List contains a loop, it indicates a flaw in its implementation. This situation can manifest in several ways:

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # WRITE HAS_LOOP METHOD HERE #
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    
    
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True

```

**Solution**  for LL: Has Loop *[here](./Has_Loop.md)*
_________________________________________________
<br>

**3. LL: Find Kth Node From End ( ** Interview Question) ( \*\* Interview Question)**<br>

Implement the `find_kth_from_end` function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list **WITHOUT USING LENGTH**.

Given this LinkedList:

`1 -> 2 -> 3 -> 4`

If `k=1` then return the first node from the end (the last node) which contains the value of `4`.

If `k=2` then return the second node from the end which contains the value of `3`, etc.

If the index is out of bounds, the program should `return None`.

The `find_kth_from_end` function should follow these requirements:

1. The function should utilize `two pointers`, slow and fast, initialized to the head of the linked list.

2. The `fast` pointer should `move k nodes` ahead in the list.

3. If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

4. The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

5. The function should `return the slow pointer`, which will be at the k-th position from the end of the list.



**This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the LEFT.**

```python 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
#                                             #
###############################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
```
**Solution**  for LL: Find Kth Node From End  *[here](./Find_Kth_Node_From_End%20.md)*
_________________________________________________


