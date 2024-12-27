## Stack: Parentheses Balanced 

```python
def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()
```
or
```python
def is_balanced_parentheses(string):
    stack = Stack()
    
    for char in string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
```


The function creates a new stack using the `Stack()` class, and then iterates through each character in the input string using a for loop.

For each character, the function checks if it is an opening parenthesis, represented by the `(`character. If it is an opening parenthesis, the function pushes it onto the stack using the push method of the stack.

If the character is a closing parenthesis, represented by the `)` character, the function checks if the stack is empty or if the top of the stack, which is the most recent opening parenthesis that has not been closed, is not an opening parenthesis. If either of these conditions is true, the function returns False because the parentheses are not balanced.

If the top of the stack is an opening parenthesis, the function pops it from the stack using the pop method of the stack. The function continues iterating through the input string until all characters have been processed.

After processing all the characters, the function returns True if the stack is empty, which indicates that all opening parentheses have been matched with a closing parenthesis, and False otherwise.



**Big O:**

**Time Complexity**

The for loop iterates through each character in parentheses, making it O(n).

The stack.push() and stack.pop() operations are O(1).

Combining these, the overall time complexity is O(n).



**Space Complexity**

In the worst case, the stack could store all opening parentheses, making it O(n).

