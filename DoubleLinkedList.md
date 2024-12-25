## Double LinkedList Interview Question

**1. DLL: Swap First and Last ( ** Interview Question)**<br>

Swap the values of the first and last node

Method name:
    `swap_first_last`

**Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE SWAP_FIRST_LAST METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    
    
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""
```
**Solution**  DLL: Swap First and Last *[here](./DLLAnswer/swap_first_last.md)*

_____________________________________________________
<br>

**2. DLL: Reverse ( ** Interview Question)**<br>

Create a new method called `reverse` that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and **change the direction of the pointers** between the nodes so that they point in the opposite direction.

Do not change the `value` of any of the nodes.

Once you've done this for all nodes, you'll also need to update the `head` and `tail` pointers to reflect the new order of the nodes.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    ## WRITE REVERSE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""
```

**Solution**  DLL: Reversed *[here](./DLLAnswer/reverse_DLL.md)*

_____________________________________________________
<br>

**3. DLL: Palindrome Checker ( ** Interview Question)**<br>
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values `[1, 2, 3, 2, 1]`, then the method should `return True`, since the list is a palindrome.

If the list contains the values `[1, 2, 3, 4, 5]`, then the method should `return False`, since the list is not a palindrome.

Method name:
`is_palindrome`
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE IS_PALINDROME METHOD HERE #
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""
```
**Solution**  DLL: is_palindrome *[here](./DLLAnswer/is_palindrome_DLL.md)*

_____________________________________________________
<br>

**4. DLL: Swap Nodes in Pairs  ( ** Interview Question)**<br>

You are given a doubly linked list.

Implement a method called `swap_pairs` within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

**Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.**

Example:

`1 <-> 2 <-> 3 <-> 4` should become `2 <-> 1 <-> 4 <-> 3`

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem **WITHOUT MODIFYING THE VALUES** in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    # WRITE SWAP_PAIRS METHOD HERE #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
```

**Solution**  DLL: Swap Nodes in Pairs *[here](./DLLAnswer/is_palindrome_DLL.md)*

_____________________________________________________
<br>
