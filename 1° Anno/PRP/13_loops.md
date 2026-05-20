---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 13 Conditional Statements and Loops Examples

## 1. Why Loops are Important
Loops are one of the basic logical structures of computer programming. They allow computers to perform the same task repeatedly. 
*   **When to use them**: Every time you might use the words "each" and "every" in the natural language description of your program's specification, you want a loop.
*   **Infinite Loops**: You can loop forever using `while(1)`.

---

## 2. Common Errors in Logic Conditions

### Assignment vs. Equality
A very common mistake in C is confusing the assignment operator `=` with the equality operator `==`.

*   **Incorrect (Assignment)**:
    ```c
    int x = 1;
    while (x = 1) { // Assigns 1 to x. The result of the expression is 1 (true).
        printf("Insert 1 to continue");
        scanf("%d", &x);
    }
    // This is an infinite loop because (x = 1) is always true.
    ```
*   **Correct (Equality)**:
    ```c
    int x = 1;
    while (x == 1) { // Checks if x is equal to 1.
        printf("Insert 1 to continue");
        scanf("%d", &x);
    }
    ```

Similarly for `if` statements:
*   `if (age = 18)` sets `age` to 18 and evaluates to true (since 18 is non-zero). It will always execute the conditional block.
*   `if (age == 18)` correctly checks if `age` is exactly 18.

### Chaining Relational Operators
In mathematics, you can write $10 < x < 20$. In C, this does not work as expected because relational operators are evaluated left-to-right.

*   **Incorrect**:
    ```c
    int x = 15;
    if (20 > x > 10) { ... }
    ```
    *How C evaluates this:*
    1.  `20 > x` evaluates to `1` (true).
    2.  Then it evaluates `1 > 10`, which is `0` (false).
    The condition fails.

*   **Correct**:
    Use logical operators to combine conditions.
    ```c
    if (x > 10 && x < 20) { ... }
    ```

### Other Common Errors
1.  **Semicolon after `if`**:
    ```c
    if (age >= 18);
        printf("You can drink!\n");
    ```
    The semicolon terminates the `if` statement prematurely. The `printf` is no longer part of the conditional block and will *always* execute.
2.  **`else` with a condition**:
    ```c
    else (a == b) { ... } // ERROR: 'else' cannot have a condition
    ```
    Use `else if (a == b)` instead.
3.  **Missing Block Braces**:
    ```c
    if (age >= 18)
        printf("You can drink!\n");
        printf("Age greater than 18\n"); // This is always printed!
    ```

---

## 3. Pay Attention to Nesting (Dangling Else)
When nesting `if` statements without braces, an `else` is always paired with the closest preceding `if`.
```c
if (x > 10)
    if (x < 20) 
         printf("x is between 10 and 20");
    else
         printf("x is greater than 20");
```
In this case, the `else` is paired with `if (x < 20)`. If you want the `else` to belong to `if (x > 10)`, you **must** use block braces `{}`.

---

## 4. Transforming Loops
Any loop can be transformed into another type of loop.

*   **For Loop**:
    ```c
    int n = 4;
    for (int i = 0; i < n; i++) {
        printf("OK\n");
    }
    ```
*   **While Loop**:
    ```c
    int n = 4;
    int i = 0;
    while (i < n) {
        printf("OK\n");
        i++;
    }
    ```
*   **Do-While Loop**:
    ```c
    int n = 4;
    int i = 0;
    do {
        printf("OK\n");
        i++;
    } while (i < n);
    ```

---

## 5. Arrays and Matrices

### Scanning an Array
```c
int foo[] = {16, 2, 77, 40, 12071}; 
int result = 0; 
for (int n = 0; n < 5; ++n) { 
    result += foo[n]; 
} 
printf("%d", result); // Outputs: 12206
```

### Scanning a Matrix (Nested Loops)
```c
const int width = 5;
const int height = 3; 
int mat[height][width]; 

for (int n = 0; n < height; n++) {
    for (int m = 0; m < width; m++) {
        mat[n][m] = (n + 1) * (m + 1); 
    }
}
```

### Arrays as Arguments of Functions
When the name of an array appears as a function argument, the compiler implicitly converts it into a pointer to the array’s first element.
*   `int name[]` or `int *name` is the same in a function parameter list.
*   **C does not have array variables**. It is really just working with pointers using an alternative syntax.

```c
// Both functions are exactly equivalent
void fun1(int a[], int n) { ... }
void fun2(int *a, int n) { ... }
```

---

## 6. Integer Overflow in Infinite Loops
Consider the following infinite loop:
```c
int i = 1;
while (1) {
    i++;
    if (i < 0) {
        printf("%d\n", i);
        break;
    }
}
```
**Output:** `-2147483648`

**Why? Integer Overflow.**
An `int` in two's complement (32-bit) can hold values up to `2,147,483,647` (`01111111 11111111 11111111 11111111` in binary).
If you add `1` to the maximum positive value, it overflows to the most negative value `-2,147,483,648` (`10000000 00000000 00000000 00000000` in binary). At this point, the condition `i < 0` becomes true, and the loop breaks.
