## Stack: Sort Stack 
```python
def sort_stack(stack):
    additional_stack = Stack()
 
    while not stack.is_empty():
        temp = stack.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())
```
The `sort_stack` function sorts a given stack of integers in ascending order using only one additional stack. Here's how it works:

1. First, the function creates a new stack called `additional_stack` to hold the sorted elements.

2. Next, the function enters a `while` loop that continues until the original stack is empty. Inside the loop, the function removes the top element from the original stack using the `pop` method and stores it in a temporary variable called `temp`.

3. The function then enters another `while` loop that continues until the `additional_stack` is empty or the top element of `additional_stack` is less than or equal to `temp`. Inside the loop, the function removes the top element from the `additional_stack` using the `pop` method and adds it back to the original stack using the push method.

4. Once the inner `while` loop is exited, the function adds the `temp` variable to the `additional_stack` using the `push` method. This ensures that the `additional_stack` is always sorted in ascending order.

5. Once the outer `while` loop is exited, the function enters another `while` loop that continues until the `additional_stack `is empty. Inside the loop, the function removes the top element from the `additional_stack` using the `pop` method and adds it back to the original stack using the `push` method. This step ensures that the original stack is sorted in ascending order.

6. Finally, the function returns the sorted stack.

**Overall, this implementation has a time complexity of O(n^2), where n is the number of elements in the original stack, because the function performs nested loops to compare all the elements with each other. However, it has the advantage of using only one additional stack, which could be useful in certain situations where memory is limited.**

