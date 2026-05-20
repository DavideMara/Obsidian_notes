---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 11 Dynamic Memory Management

## 1. Why Dynamic Memory?
When writing a program, you often cannot predict how much data it will need to process, or the amount of data may vary widely. 
*   **Static/Automatic Allocation**: Fixed at compile-time (or function-entry time), which can waste memory if the allocated space is too large, or crash if it is too small.
*   **Dynamic Memory (The Heap)**: Allows the programmer to manually decide when to allocate memory, exactly how much to allocate at runtime, and when to destroy it.
    *   This ensures efficient resource use.
    *   The program doesn't need to be rewritten to handle larger datasets on systems with more available memory.

---

## 2. Standard Memory Functions (`<stdlib.h>`)
The C standard library provides four primary functions for dynamic memory management. They all operate on bytes and use `size_t` (an unsigned integer type representing sizes in bytes, usually returned by `sizeof`).

### Allocating Memory
1.  **`malloc( size_t size )`**
    *   Reserves a contiguous memory block of at least `size` bytes.
    *   The contents of the newly allocated memory are **undetermined** (they contain garbage values).
    *   *Example:* `int *p = (int*) malloc(sizeof(int) * 10);`
2.  **`calloc( size_t count, size_t size )`**
    *   Reserves a block of memory large enough to hold an array of `count` elements, each of `size` bytes.
    *   **Initializes every byte of the memory to `0`.**
    *   *Example:* `int *q = (int*) calloc(3, sizeof(int));`

**Characteristics of Allocation:**
*   Both functions return a `void *` (a typeless pointer) to the lowest byte address of the block.
*   The compiler implicitly (or explicitly via a cast) converts the `void *` to the target pointer type, determining how the memory contents are interpreted.
*   **Memory Exhaustion**: If the requested memory is not available, these functions return a **null pointer (`NULL`)**. *Always check for `NULL` before using the pointer!*
*   The physical arrangement of blocks in the heap from successive calls is unspecified.

### Resizing and Releasing Memory
1.  **`free( void *ptr )`**
    *   Releases a dynamically allocated memory block back to the OS.
    *   You only pass the starting address (`ptr`). The memory management system internally tracks the size of each allocated block.
    *   Passing a `NULL` pointer has no effect.
    *   It has no return value, so there is no way to test if a call to `free()` was successful.
2.  **`realloc( void *ptr, size_t size )`**
    *   Releases the old block addressed by `ptr` and allocates a new block of `size` bytes, returning its new address.
    *   It preserves the contents of the original memory block up to the size of whichever block is smaller.
    *   If the new block is larger, the values of the additional bytes are unspecified.
    *   If `ptr` is `NULL`, it behaves exactly like `malloc(size)`.
    *   **Failure Handling**: If it fails to allocate the new size, it returns `NULL` and **does not** release the original memory block or alter its contents.

---

## 3. Common Errors and Pitfalls
Because C relies on manual memory management (unlike Java which uses an automatic Garbage Collector), it is highly error-prone.

### Memory Leaks
Occur when a dynamically allocated block is not freed, and the pointer to it is overwritten or goes out of scope.
*   The object becomes unreachable and cannot be deallocated.
*   If repeated, the heap is eventually fully consumed, causing allocation failures or crashes. This is especially critical for long-running programs (e.g., servers).
    ```c
    int* p = (int*) malloc(sizeof(int));
    p = NULL; // Memory leak! The allocated block is now unreachable.
    ```

### Dangling Pointers
Arise during object destruction when memory is freed, but the pointer variable still holds the memory address. The pointer now points to deallocated memory.
*   *Solution*: Always assign `NULL` to the pointer immediately after freeing it.
    ```c
    free(message);
    message = NULL; // Prevents dangling pointer usage
    ```

### Segmentation Faults & Undefined Behavior
Your program is only allowed to touch memory that belongs to it. Touching restricted memory causes a crash (Segmentation Fault). Common causes include:
*   **Double Free**: Calling `free()` twice on the same pointer (`free(str1); free(str1);`).
*   **Dereferencing NULL**: Trying to read or write to a null pointer.
    ```c
    int* p = NULL;
    int c = 3 + *p; // Segmentation fault!
    ```
*   **Freeing Non-Heap Memory**: Calling `free()` on an address that was not obtained from `malloc/calloc/realloc` (e.g., a local variable on the stack).
    ```c
    int m = 100;
    int *p1 = &m;
    free(p1); // ERROR: free can only be called on memory allocated in the heap
    ```
*   **Uninitialized Pointers**: Dereferencing a pointer that hasn't been assigned an address.
    ```c
    int *p1;
    int n = *p1; // ERROR: p1 is uninitialized garbage, points anywhere
    ```

### Postfix `++` Precedence
Be careful when applying pointer arithmetic and dereferencing together:
*   `*p1++` is parsed as `*(p1++)` because postfix `++` has higher precedence than the dereference operator `*`. It yields the value pointed to by `p1`, and then increments the pointer.

---

## 4. Textbook References
*   **Section 12.3**
