## LL: Binary_to_decimal ( ** Interview Question)
<br>

```python
def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num
```
Given the linked list: `1 → 0 → 1 → 0`

This represents the binary number `1010`, where the head of the list is the most significant bit (MSB) and the tail is the least significant bit (LSB).

**Method Walkthrough:**
```python
def binary_to_decimal(self):
```

**Initialize the decimal number:**
```python
num = 0
```

Here, num will store our resulting decimal number. We initialize it to 0.



**Start at the head of the linked list:**
```python
current = self.head
```

This current pointer will help us traverse the linked list from the start (MSB) to the end (LSB).



**Traverse the linked list:**
```python
while current:
```
This loop runs as long as we have nodes left in the linked list.



**Convert the binary number to decimal:**
```python
    num = num * 2 + current.value
```

**For every node we encounter, we:**

- Multiply the current `num` by `2`. This shifts our binary number left, preparing it for the next bit. It's analogous to multiplying by `10` in decimal arithmetic.

- Add the value of the current node (0 or 1) to `num`.



**Illustrative Steps for 1010:**

Starting with `num` as `0`.

First node (MSB) is `1`. So, num = `0 * 2 + 1` which makes num equal to `1`.

Move to the next node, which is `0`. Now, `num = 1 * 2 + 0` which makes `num` equal to `2`.

The next node is `1`. So, `num = 2 * 2 + 1 `which results in `num` becoming `5`.

The last node (LSB) is `0`. Thus, num = `5 * 2 + 0 `which makes `num` equal to `10`.

Consequently, the binary number 1010 converts to the decimal number 10.



**Proceed to the next node:**
```python
    current = current.next
```
This line shifts our attention to the next node in the linked list.



**Return the decimal number:**
```python
return num
```
After processing all the bits in our binary number (i.e., all the nodes in our linked list), we can return our decimal result stored in num.


**Conclusion:**

The process for converting binary to decimal using a linked list reflects standard binary conversion rules. We work from the MSB (head of the linked list) to the LSB (tail), doubling our current result and adding the next bit at every step. This method ensures that each binary bit contributes the correct power of 2 to our final decimal result. In our example, 1010 rightly converts to 10.

