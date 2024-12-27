## Stack and Queue Interview Question

**1. Stack: Implement Stack Using a List ( ** Interview Question)**<br>

In the Stack: Intro video we discussed how stacks are commonly implemented using a list instead of a linked list.

Create a constructor for Class `Stack` that implements a new stack with an empty list called `stack_list`.

```python
# answer
class Stack:
    def __init__(self):
        self.stack_list = []
#here
```


_____________________________________________________
<br>

**2. Stack: Push for Stack That Uses List ( ** Interview Question)**<br>

Add a method to `push` a value onto the Stack implementation that we began in the last Coding Exercise.

**Remember: This Stack implementation uses a list instead of a linked list.**
```python
class Stack:
    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

# answer
    def push(self, value):
        self.stack_list.append(value)
# here
```
_____________________________________________________
<br>

**3. Stack: Pop for Stack That Uses List  ( ** Interview Question)**<br>

Add a method to `pop` a value from the Stack implementation that we began in the last two Coding Exercises.

**Remember: This Stack implementation uses a list instead of a linked list.**

```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)
# answer
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
# here      
            
            
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1
    
    Popped node:
    3
    
    Stack after pop():
    2
    1
 
"""

```
_____________________________________________________
<br>

**4.Stack: is_balance_parenthesis  ( ** Interview Question)**<br>

Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of `parentheses` as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

**Function name:**<br>
`is_balanced_parentheses`

**Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.**


This will use the Stack class we created in these coding exercises:
```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
#                                             #
#    This is a separate function that is      #
#    not a method within the Stack class.     #
#    Indent all the way to the left.          #
#                                             #
###############################################




def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()
```
**Solution**  for Stack: Pop for Stack That Uses List *[here](./Stack_QueueAnswer/parenthesis_balance.md)*

_____________________________________________________
<br>

**5.Stack: Reverse String  ( ** Interview Question)**<br>
The `reverse_string` function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.


```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
#########################################




my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
```
**Solution**  for Stack: Reverse String *[here](./Stack_QueueAnswer/reveresed_string.md)*

_____________________________________________________
<br>

**6. Stack: Sort Stack   ( ** Interview Question)**<br>
The `sort_stack` function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the `pop`, `push`, `peek`, and `is_empty` methods of the Stack object.

**Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.**

The function should perform the following tasks:

1. Create a new instance of the Stack class called `sorted_stack`.

2. While the input stack is not empty, perform the following:

    - Pop the top element from the input stack and store it in a variable `temp`.

    - While the `sorted_stack` is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.

    - Push the `temp` variable onto the sorted_stack.

3. Once the input stack is empty, transfer the elements back from `sorted_stack` to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.

```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
```
**Solution**  for Stack: Sort Stack *[here](./Stack_QueueAnswer/sort_stack.md)*

_____________________________________________________
<br>

**7. Queue Using Stacks: Enqueue   ( ** Interview Question)**<br>

You are given a class `MyQueue` which implements a queue using two stacks. Your task is to implement the `enqueue` method which should add an element to the back of the queue.

To achieve this, you can use the two stacks `stack1` and `stack2`. Initially, all elements are stored in stack1 and `stack2` is empty. In order to add an element to the back of the queue, you need to first transfer all elements from `stack1` to `stack2` using a loop that pops each element from `stack1` and pushes it onto stack2.

Once all elements have been transferred to `stack2`, push the new element onto `stack1`. Finally, transfer all elements from `stack2` back to `stack1` in the same way as before, so that the queue maintains its ordering.

Your implementation should satisfy the following constraints:



- The method signature should be `def enqueue(self, value)`.

- The method should add the element value to the back of the queue.

```python
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    # WRITE ENQUEUE MEHTOD HERE #
    #                           #
    #                           #
    #                           #
    #                           #
    #############################

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
```
**Solution**  for  Queue Using Stacks: Enqueue *[here](./Stack_QueueAnswer/enqueue.md)*
_____________________________________________________
<br>

**8. Queue Using Stacks: Dequeue ( ** Interview Question)**<br>

You have been tasked with implementing a queue data structure using two stacks in Python, and you need to write the `dequeue` method.

The `dequeue` method should `remove` and `return` the `first` element in the queue.
```python
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    # WRITE DEQUEUE MEHTOD HERE #
    #                           #
    #                           #
    #                           #
    #                           #
    #############################

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Enqueue another value
q.enqueue(4)

# Output the front of the queue again
print("Front of the queue:", q.peek())

# Dequeue all remaining values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

# Dequeue from an empty queue and check if it returns None
print("Dequeued value from empty queue:", q.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Dequeued value: 1
    Dequeued value: 2
    Front of the queue: 3
    Dequeued value: 3
    Dequeued value: 4
    Is the queue empty? True
    Dequeued value from empty queue: None
    
"""
```
**Solution**  for  Queue Using Stacks: Dequeue  *[here](./Stack_QueueAnswer/dequeue.md)*
_____________________________________________________
<br>
