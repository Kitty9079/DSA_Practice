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


**Solution**  for LL: Find Middle Node *[here](./LinkedListAnswer/find_middle_node.md)*

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

**Solution**  for LL: Has Loop *[here](./LinkedListAnswer/Has_Loop.md)*
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
**Solution**  for LL: Find Kth Node From End  *[here](./LinkedListAnswer/Find_Kth_Node_From_End%20.md)*
_________________________________________________

**4. LL: Partition List (  Interview Question)**<br>

Implement the `partition_list` member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

**Note:  This linked list class does NOT have a tail which will make this method easier to implement.**

The original relative order of the nodes should be preserved.



**Details:**

The function `partition_list` takes an integer`x`as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., `head` is `null`), the function should return immediately without making any changes.



**Example 1:**

**Input:**

Linked List: `3 -> 8 -> 5 -> 10 -> 2 -> 1`<br> 

x: `5`

**Process:**

Values less than 5: `3`, `2`, `1`

Values greater than or equal to 5: `8`, `5`, `10`

**Output:**

Linked List: `3 -> 2 -> 1 -> 8 -> 5 -> 10`





**Example 2:**

**Input:**

Linked List: `1 -> 4 -> 3 -> 2 -> 5 -> 2`<br> 

x: `3`

**Process:**

Values less than 3: `1`, `2`, `2`

Values greater than or equal to 3: `4`, `3`, `5`

**Output:**

Linked List: `1 -> 2 -> 2 -> 4 -> 3 -> 5`





**Tips:**

While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.

Use dummy nodes to simplify the handling of the heads of these chains.

After processing the entire list, connect the two chains to get the desired arrangement.



**Note:**

**The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.**

**You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' next pointers may be changed.)**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

        



#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      
```

**Solution**  for LL: Partition List  *[here](./LinkedListAnswer/Partition_List.md)*
__________________________

**5. LL: Remove Duplicates ( ** Interview Question)**<br>

You are given a singly linked list that contains integer values, where some of these values may be duplicated.

**Note: this linked list class does NOT have a `tail` which will make this method easier to implement.**

Your task is to implement a method called `remove_duplicates()` within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the `remove_duplicates()` method in two different ways:

1. **Using a Set** - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

1. **Without using a Set** - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.

Here is the method signature you need to implement:

```def remove_duplicates(self):```


**Example:**

Input:

LinkedList: `1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5`

Output:

LinkedList: `1 -> 2 -> 3 -> 4 -> 5`

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    #   +===================================================+
    #   |                  WRITE YOUR CODE HERE             |
    #   | Description:                                      |
    #   | - This method removes all nodes with duplicate    |
    #   |   values from the linked list.                    |
    #   | - It keeps track of seen values with a set.       |
    #   | - If a value is repeated, it is skipped over by   |
    #   |   changing the 'next' pointer of the previous     |
    #   |   node, effectively removing the duplicate.       |
    #   | - The list's length is adjusted for each removed  |
    #   |   duplicate.                                      |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We maintain a 'previous' node as a reference    |
    #   |   to re-link the list when skipping duplicates.   |
    #   | - The 'current' node iterates through the list.   |
    #   | - The 'values' set holds unique items seen so far.|
    #   +===================================================+

            
            


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0   # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])
```
**Solution**  for LL: Partition List  *[here](./LinkedListAnswer/Partition_List.md)*
__________________________

**6. Binary to Decimal ( ** Interview Question)**

Your task is to implement the `binary_to_decimal` method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.

The `binary_to_decimal` method should start from the head of the linked list and use each node's value to calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:

To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power equivalent to the position of the digit, counting from right to left starting from 0, and all the results are summed together to get the decimal number.

The binary_to_decimal method should return this calculated decimal number.



**Examples**

Consider the binary number 101. If this number is represented as a linked list, the head of the linked list will contain the digit 1, the next node will contain 0, and the last node will contain 1. When we apply the binary_to_decimal method on this linked list, the method should return the number 5, which is the decimal equivalent of binary 101.

Similarly, for a linked list representing the binary number 1101, the binary_to_decimal method should return the number 13.

Here's how you can create these linked lists and call the binary_to_decimal method:
```python

# Create a linked list for binary number 101
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 5
 
# Create a linked list for binary number 1101
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  
# Output: 13
```

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    # WRITE BINARY_TO_DECIMAL METHOD HERE #
    #                                     #
    #                                     #
    #                                     #
    #                                     #
    #######################################




# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 6
    print("Test case 1 passed, returned: ", result)
except AssertionError:
    print("Test case 1 failed, returned: ", result)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned: ", result)
except AssertionError:
    print("Test case 2 failed, returned: ", result)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned: ", result)
except AssertionError:
    print("Test case 3 failed, returned: ", result)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned: ", result)
except AssertionError:
    print("Test case 4 failed, returned: ", result)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned: ", result)
except AssertionError:
    print("Test case 5 failed, returned: ", result)
    
 
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 passed, returned:  6
    Test case 2 passed, returned:  8
    Test case 3 passed, returned:  0
    Test case 4 passed, returned:  1
    Test case 5 passed, returned:  13
"""

```


**Solution**  for LL: binary_to_decimal *[here](./LinkedListAnswer/binary_to_decimal.md)*

_____________________________________________________

**7. LL: Reverse Between ( ** Interview Question)**

You are given a singly linked list and two integers `start_index` and `end_index`.

Your task is to write a method `reverse_between` within the LinkedList class that reverses the nodes of the linked list from `start_index` to  `end_index` (inclusive using 0-based indexing) in one pass and in-place.

**Note: the Linked List does not have a `tail` which will make the implementation easier.**

**Assumption**: You can assume that start_index and end_index are not out of bounds.



**Input**

- The method `reverse_between` takes two integer inputs `start_index` and `end_index`.

- The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



**Output**

The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.

If the linked list is empty or has only one node, the method should `return None`.



**Example**

Suppose the linked list is `1 -> 2 -> 3 -> 4 -> 5`, and `start_index = 2` and `end_index = 4`. Then, the method should modify the linked list to `1 -> 2 -> 5 -> 4 -> 3`.



**Constraints**

The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).


```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
```


**Solution**  for LL: Reverse Between *[here](./LinkedListAnswer/reversed_between.md)*

_____________________________________________________
<br>
