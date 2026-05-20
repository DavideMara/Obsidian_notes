---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 14 Call By Reference

## 1. Why Pointers?
A **pointer** is a reference to a data object or a function. Pointers are essential in C for several reasons:
*   Defining "call-by-reference" functions to allow functions to modify caller variables.
*   Implementing dynamic data structures such as linked lists and trees.
*   Managing large volumes of data efficiently. Instead of copying massive datasets back and forth, you can simply pass around pointers to the data.
*   Passing large arrays to functions. It is much more economical to pass a pointer to the array's first element than to copy the entire array into the function's scope, even if the data is read-only.

---

## 2. Call by Value vs. Call by Reference

### Call by Value
By default, C passes arguments to functions **by value**. This means the function receives a *copy* of the variable. Any modifications made to the parameter inside the function do not affect the original variable in the calling function.

*   *Example (Call by value)*:
    ```c
    int fun(int b) {        
        return (b + 1); // b is a local copy
    }
    int main() {  
        int a = 3;
        a = fun(a); // a is explicitly updated by the return value
    }
    ```

### Call by Reference
Call by reference is a technique to work on the exact same memory segment from different functions. In C, this is achieved by passing the **memory addresses** (pointers) of the variables instead of their values.

*   *Example (Swapping two variables correctly)*:
    ```c
    #include <stdio.h>

    void swap(int *p, int *q) {
        int tmp = 0; 
        tmp = *p;   // Store the value pointed to by p
        *p = *q;    // Overwrite the value at p with the value at q
        *q = tmp;   // Overwrite the value at q with tmp
    }

    int main(void) {
        int i = 3, j = 5; 
        swap(&i, &j); // Pass memory addresses!
        printf("%d %d\n", i, j); // Outputs: 5 3
        return 0;
    }
    ```
*   *What goes wrong without pointers?*
    If we defined `void swap(int p, int q)`, the function would just swap its own local copies (`p` and `q`). When the function returns, `i` and `j` in `main()` would remain unchanged (`3` and `5`).

---

## 3. Arrays are Passed by Reference
When you pass an array to a function, C automatically passes a pointer to the first element of the array. Therefore, arrays are effectively passed by reference.
*   This is highly efficient. For example, passing a `int a[1000000]` array passes only an 8-byte pointer rather than copying 4,000,000 bytes.
*   Modifying array elements inside the function modifies the original array directly.

```c
void fun(int a[], long int n) {        
    for (int i = 0; i < n; ++i) 
        a[i] = i; // Modifies the original array directly!
}
```

---

## 4. The Problem with Global Variables
Instead of using call-by-reference, one might be tempted to use global variables to share state between functions (e.g., swapping `i` and `j` by declaring them globally).
**This is bad practice.**

### Why you should avoid global variables:
*   **Unmanageable Scope**: Globals force you to keep track of how they are being used throughout the *entire* system.
*   **Team Coordination**: In a collaborative environment, you must coordinate who is creating which global variables to avoid naming conflicts.
*   **Unexpected Behavior**: Localizing algorithm effects (using local variables) reduces bugs and makes the program easier to read and understand.

### When is it reasonable to use global variables?
Only when the entire program is built around a central, large data structure, and access to that data is needed in nearly *every* function.

---

## 5. Pointers to Functions
Functions themselves reside in memory and have addresses. The name of a function acts as a **constant pointer** to the function.

You can declare a pointer variable that points to a function and invoke the function through it:
```c
#include <stdio.h>

int main() {
    // Declare pfunc as a pointer to a function taking a const char* and returning an int
    int (*pfunc)(const char*) = puts; 
    
    // Call the function through the pointer
    (*pfunc)("Any Question?"); 
    return 0;
}
```

---

## 6. Textbook References
*   **Section 7.4**
*   **Section 7.12**
