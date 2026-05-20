---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 08 Arrays

## 1. Overview of Arrays
An **array** is an aggregate data structure that contains a sequence of elements of the same type, stored consecutively in a continuous block of memory.

*   An array's type is defined by the **data type of its elements** and the **total number of elements** (e.g., "array of `int`").
*   An array type without a specified length is considered an **incomplete type**. Specifying the size completes the type (e.g., "array of 16 `int` elements").
*   Array elements can be of any object type.

---

## 2. Array Definition & Subscripting

### Definition Syntax
$$\text{type name[ number\_of\_elements ] ;}$$
The `number_of_elements` must be an integer expression with a value **greater than zero**.

*   *Example*: `char buffer[4 * 512];`
    Defines an array of $2048$ elements of type `char`.
*   *Size calculation*: `sizeof(buffer)` evaluates to $2048 \times \text{sizeof(char)} = 2048$ bytes.

### The Subscript Operator (`[]`)
Individual elements are accessed using square brackets:
$$\text{myArray[index]}$$
*   C arrays are **0-indexed**: The first element is at index `0`.
*   If the array contains `len` elements, the last element is located at index `len - 1`.
*   The index expression (right operand of `[]`) must be an **integer type**.

```c
const int a = 4;
long mArray[a];

for (int i = 0; i < a; ++i) {
    mArray[i] = 2 * i;
}
// Memory Layout:
// mArray[0] = 0
// mArray[1] = 2
// mArray[2] = 4
// mArray[3] = 6
```

---

## 3. Variable-Length Arrays (VLAs)
*   **C99**: Introduced the ability to define arrays whose sizes are determined at runtime using non-constant expressions.
*   **C11**: Made VLAs **optional**; some compliant compilers may choose not to support them.
```c
void func(int n) { 
    int vla1[2 * n]; // Variable length array
    int vla2[n];     // Variable length array
    /* ... */ 
}
```
> [!WARNING]
> VLAs cannot be initialized using an initialization list.

---

## 4. Array Initialization
Arrays can be initialized when defined using an **initialization list** (a comma-separated list of values enclosed in braces `{}`).
$$\text{int a[4] = \{ 1, 2, 4, 8 \};}$$
This is equivalent to: `a[0] = 1; a[1] = 2; a[2] = 4; a[3] = 8;`.

### Initialization Rules
1.  **Omitting Size**: If the size of the array is omitted, the compiler sizes the array automatically based on the number of elements in the initialization list:
    `int a[] = { 1, 2, 0, 0 }; // Array size is 4`
2.  **Implicit Zeroing**: If the size in `[]` is larger than the initialization list, C automatically initializes all remaining elements to `0`:
    `int a[4] = { 1, 2 }; // Equivalent to { 1, 2, 0, 0 }`
3.  **Superfluous Initializers**: If there are more initializers than the specified size, the compiler ignores the excess and generates a warning:
    `int a[4] = { 1, 2, 0, 0, 5 }; // Mismatch: 5 is ignored, warning generated`
4.  **Trailing Commas**: A trailing comma inside the braces is ignored by the compiler:
    `int a[] = { 1, 2, 0, 0, }; // Correct, array size remains 4`
5.  **Type Conversion**: If the types of the initializers do not match the element type, they are converted implicitly.

### Designated Initializers (Specific Elements)
You can initialize specific elements by placing the index in brackets `[constant_expression]`.
*   The index must be an **integer constant expression**.

*   *Invalid (non-constant expression)*:
    ```c
    int three = 2;
    int a[4] = { 1, [three] = 1 }; // Compiler Error
    ```
*   *Valid (const expression)*:
    ```c
    const int three = 2;
    int a[4] = { 1, [three] = 1 }; 
    // Elements: a[0] = 1, a[1] = 0, a[2] = 1, a[3] = 0
    ```
*   *Cascading Initializers*:
    `int a[6] = { 1, 2, [3] = 1, 2 };`
    Initializes elements: `a[0] = 1`, `a[1] = 2`, `a[2] = 0`, `a[3] = 1`, `a[4] = 2`, `a[5] = 0`.

### Out-of-Bounds Pitfall
C does not perform bounds checking at compile-time or run-time. Reading or writing past the array length results in undefined behavior or memory corruption.
```c
int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
for (int i = 0; i < 20; i++) {
    printf("Element[%d] = %d\n", i + 1, a[i]); // Elements 11 to 20 read garbage memory
}
```

---

## 5. Arrays as Function Arguments (Pointer Decay)
When an array is passed as an argument to a function, it **decays into a pointer** to its first element. 
*   A parameter declared as `type a[N]` is interpreted by the compiler as `type *a`.
*   Inside the function, the `sizeof` operator returns the size of the pointer (usually 8 bytes on 64-bit systems) rather than the array.

```c
#include <stdio.h>

void fun(int a[3]) { 
    printf("%lu\n", sizeof(a)); // Prints 8 (pointer size), warning generated
    for (int i = 0; i < 3; ++i) {
        a[i] = i; 
    }
}

int main() { 
    int a[3];
    printf("%lu\n", sizeof(a)); // Prints 12 (3 * sizeof(int))
    fun(a);
    return 0;
}
```
*   *Compiler Warning*: `warning: sizeof on array function parameter will return size of 'int *' instead of 'int [3]' [-Wsizeof-array-argument]`

---

## 6. Character Arrays & Strings
A **string** in C is stored as a continuous sequence of characters in a `char` array terminated by the **null character (`\0`)**.

*   **String Length**: The count of characters, excluding the terminating `\0`.
*   **Buffer Requirement**: An array storing a string must always be allocated at least **one character larger** than the string length to accommodate `\0`.

### Initialization
String arrays can be initialized with string literals or character lists:
```c
char str1[30] = "Let's go"; // Implicitly appends \0
char str1[30] = { 'L', 'e', 't', '\'', 's', ' ', 'g', 'o', '\0' }; // Equivalent
```
*   *Array length:* 30. *String length:* 8.
*   *Omitted Length:* If size is omitted, the array size is implicitly $1$ larger than the string length:
    `char str2[] = " to London!"; // String length: 11, Array size: 12`

### Buffer Overflow Warning
If the string literal exceeds the character array bounds, the null terminator is omitted, causing string operations to read past the buffer:
```c
char string[5] = "Jim Morrison"; // Warning: initializer-string too long
printf("%s\n", string);          // Outputs: "Jim M..." followed by garbage memory corruption
```
*   *Correction (null truncation example)*:
    ```c
    char string[14] = { 'J', 'i', 'm', ' ', 'M', '\0', 'o', 'r', 'r', 'i', 's', 'o', 'n', '\0' };
    printf("%s\n", string); // Outputs: "Jim M" (stops printing at the first \0)
    ```

---

## 7. Multidimensional Arrays (Matrices)
A multidimensional array in C is an array whose elements are themselves arrays.
*   Declaring an $n$-dimensional array requires $n$ sets of square brackets:
    `char screen[10][40][80]; // A 3D array consisting of 32,000 elements`
*   The C standard recommends compilers support at least **256** nesting dimensions.

### Matrices (2D Arrays)
Commonly represented as grids with rows and columns:
`float mat[3][5]; // 3 rows, 5 columns (15 total elements)`

```c
for (int row = 0; row < 3; ++row) {
    for (int col = 0; col < 5; ++col) {
        mat[row][col] = row + (float) col / 10.0;
    }
}
// mat[0] points to the first row (array of 5 floats)
```

### Multidimensional Initialization
Multidimensional arrays are stored in memory in **row-major order** (rightmost indices vary fastest).

*   *Fully Nested Braces (Explicit)*:
    ```c
    int a3d[2][2][3] = { 
        { { 1, 0, 0 }, { 4, 0, 0 } }, 
        { { 7, 8, 0 }, { 0, 0, 0 } } 
    };
    ```
*   *Implicit Outer Dimension*: The first dimension size can be omitted if an initialization list is provided:
    `int a3d[][2][3] = { { { 1 }, { 4 } }, { { 7, 8 } } }; // Size is resolved as 2`
*   *Omitted Inner Braces*: Braces can be omitted. The compiler associates initializers in storage sequence order:
    ```c
    int a3d[2][2][3] = { { 1, 0, 0, 4 }, { 7, 8 } }; 
    int a3d[2][2][3] = { 1, 0, 0, 4, 0, 0, 7, 8 }; // Equivalent to explicit layout above
    ```
*   *Designated Initializers*:
    `int a3d[2][2][3] = { 1, [0][1][0] = 4, [1][0][0] = 7, 8 };`

---

## 8. Textbook References
*   **One-Dimensional Arrays**: Sections 6.1–6.5, 6.11
*   **Strings & Character Arrays**: Chapters 8 & 9
