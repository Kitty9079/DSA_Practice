## Stack: Reversed String
```python
def reverse_string(string):
    stack = Stack()
    reversed_string = ""
 
    for char in string:
        stack.push(char)
 
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    return reversed_string
```
The `reverse_string()` function uses a stack to reverse a string. The string is iterated over, and each character is added to the stack. After the stack is filled with all of the characters from the string, the stack is emptied and each character is added to the reversed_string variable. This creates a new string that is the reverse of the original.

This approach works by using the `Last-In-First-Out (LIFO) `property of a stack. The first character in the string is the last character to be added to the stack, and the last character in the string is the first character to be removed from the stack. Therefore, reversing the order of the characters is simply a matter of pushing them onto the stack in the opposite order and then popping them off again in that order.