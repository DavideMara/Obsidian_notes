---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 10 Pointers

## 1. Concept of Pointers
A **pointer** is a variable whose value is the direct memory address of another variable or function.
*   A pointer represents both the **address** and the **type** of an object.
*   If an object has type `T`, a pointer to that object has the derived type **"pointer to `T`"** (written as `T*`).

### Declaration Syntax
$$\text{type * [type-qualifier-list] name [= initializer] ;}$$
*   *Example:* `float x, *ptr;` (declares a float `x` and a pointer to a float `ptr`).

---

## 2. Address & Indirection Operators

### The Address Operator (`&`)
Yields the memory address of its operand.
*   The operand must have an addressable location in memory (it must be an **lvalue** and not a bit-field).
*   *Example*:
    ```c
    float x, *ptr;
    ptr = &x;       // OK: ptr now holds the address of x
    ptr = &(x + 1); // ERROR: (x + 1) is an rvalue, it has no addressable location
    ```

### The Indirection (Dereferencing) Operator (`*`)
Accesses the actual object located at the address held by the pointer.
*   The operand must be of a pointer type.
*   If `ptr` is a pointer, `*ptr` acts as an lvalue representing the referenced object.
*   *Example*:
    ```c
    float x, *ptr = &x;
    *ptr = 1.7; // Modifies the value of x to 1.7
    ++(*ptr);   // Increments the value of x by 1
    ```
> [!NOTE]
> The unary indirection operator `*` has higher precedence than the binary multiplication operator `*`. The expression `*ptr1 * *ptr2` evaluates to `(*ptr1) * (*ptr2)`.

---

## 3. Lvalues and Pointers Quiz
Consider the code: `int a = 3; int *p = &a;`
*   Is `a` an lvalue? **Yes** (designates an object in memory).
*   Is `p` an lvalue? **Yes** (the pointer variable itself is an object).
*   Is `*p` an lvalue? **Yes** (dereferencing yields the object `a`).
*   Is `&a` an lvalue? **No** (it yields the address value itself, which is an rvalue).

---

## 4. Null Pointers and `void` Pointers

### Null Pointers
A null pointer constant is an integer constant expression with the value `0`.
*   The macro **`NULL`** is defined in `<stdlib.h>`.
*   A null pointer is guaranteed to be unequal to any valid pointer to an actual object or function.
*   *Dereferencing NULL:* Attempting to access memory via a null pointer (e.g., `int *p = NULL; *p = 6;`) causes a **Segmentation Fault** and crashes the program.

### Void Pointers (`void*`)
Used as an **all-purpose pointer type**.
*   A `void*` can store the address of *any* object type, but it forgets the type of the object.
*   Because the compiler does not know the type (or size) of the object being pointed to, **you cannot directly dereference a `void*`**.
*   You must **explicitly cast** the void pointer back to an appropriate object pointer before dereferencing:
    ```c
    void *pA = NULL;
    int p = 10;
    pA = &p;
    printf("%d", *((int*) pA)); // Cast to int* before dereferencing
    ```

---

## 5. Printing Pointers and Sizes
*   **Printing Addresses**: Use the `%p` format specifier in `printf()`.
    `printf("Address of p: %p\n", p);`
*   **Pointer Size**: The amount of memory occupied by a pointer variable itself is determined by the system architecture (e.g., 8 bytes on a 64-bit OS), **regardless of the type of object it points to**. `sizeof(int*)` and `sizeof(double*)` are the same.

---

## 6. Pointers to Pointers
Since a pointer is itself an object stored in memory, it has an address, meaning another pointer can point to it. This requires chaining asterisks:
```c
char c = 'A';
char *cPtr = &c;
char **cPtrPtr = &cPtr; // Pointer to a pointer to a char
```
*   `*cPtrPtr` yields the pointer `cPtr`.
*   `**cPtrPtr` yields the character `c` (`'A'`).

---

## 7. Pointer Arithmetic & Arrays
When adding or subtracting integers to/from a pointer, the compiler **automatically scales** the operation by the size of the referenced object (`sizeof(type)`).

### Allowable Operations
1.  **Addition/Subtraction of an Integer**: `p1 + n` points to the memory location $n$ elements away (e.g., `a[i+n]`).
    *   If `dPtr` points to an `int` array, `dPtr + 1` advances the memory address by `sizeof(int)` (usually 4 bytes).
2.  **Pointer Subtraction**: `p2 - p1` yields the **number of array elements** between the two pointers.
    *   The result is of type `ptrdiff_t` (defined in `<stddef.h>`), usually an `int`.
3.  **Pointer Comparison**: Relational operators (`<`, `>`, `==`) can compare pointers. `p1 < p2` is true if `p2` points to a higher memory address (a subsequent array element).

### Arrays and Pointers Equivalence
In C, the name of an array is implicitly converted into a pointer to its first element. "Arrays do not exist in C: they are just pointers."
*   `a + i` is equivalent to the address `&a[i]`.
*   `*(a + i)` is exactly equivalent to accessing `a[i]`.

---

## 8. Const Pointers vs. Pointers to Const
The `const` qualifier's placement dictates whether the pointer address itself is locked, or if the underlying object is locked.

### Constant Pointers
The pointer's stored address cannot be changed, but the object it points to *can* be modified.
*   **Declaration**: `type *const name;`
    ```c
    int var = 1, var2 = 2;
    int *const c_ptr = &var; 
    *c_ptr = 123;    // OK: the object var is modified
    c_ptr = &var2;   // ERROR: the pointer address cannot be changed
    ```

### Pointers to Const (Read-Only Pointers)
The pointer can change its address to point to other objects, but you *cannot modify* the object through this pointer.
*   **Declaration**: `const type *name;`
    ```c
    int var = 1;
    const int *ptr_to_const;
    ptr_to_const = &var;    // OK: pointer address can be reassigned
    *ptr_to_const = 77;     // ERROR: cannot modify the object through a read-only pointer
    ```
> [!TIP]
> **Implicit Conversions**: You can safely assign a standard pointer to a `pointer-to-const` (upgrading safety).
> **Explicit Conversions**: Converting a `pointer-to-const` back into a standard pointer requires an explicit cast `(int*)`. This is dangerous if the underlying variable was originally declared as a true `const`, as modifying it will cause undefined behavior.

---

## 9. Textbook References
*   **Sections**: 7.1-7.3, 7.5, 7.8, 7.9, 7.10
