---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 15 Memory: Definitions, Duration, and Layout

## 1. Definition vs. Declaration

### Declaration
A **declaration** provides the basic attributes of a symbol (its type and its name) without allocating memory. It simply tells the compiler: *"Dear Compiler, there is a variable/function with the following name and type somewhere in the program."*
*   Often, the compiler only needs a declaration to compile a file, expecting the linker to find the actual definition later.
*   If a symbol is declared but never defined, you will get an "undefined symbol" error at link time.
*   You can have **many** declarations of the same symbol.

### Definition
A **definition** provides all the details of that symbol. 
*   For a function, it provides the actual code block (the function body).
*   For a variable, it tells the compiler: *"Please **allocate memory** for a variable with this name and type now."*
*   **Every definition is also a declaration.**
*   There can be only **one** definition of the same variable or function across the entire program.

```c
int func(); // Declaration only

int main() {
    int x = func(); // x is defined (memory allocated). func() is called.
}

int func() { // Definition (memory for function block allocated)
    int y = 3; // y is defined
    return y;
}
```

---

## 2. Storage Duration and Specifiers
A storage class specifier in a declaration modifies the **storage duration** (lifetime) of an object. The duration can be:
1.  **Automatic**: Created and destroyed automatically based on scope.
2.  **Static**: Created once at program start, destroyed at program termination.
3.  **Dynamic**: Controlled manually by the programmer (Heap).

### The `auto` Specifier
Objects declared with `auto` have automatic storage duration.
*   In ANSI C, local variables within a function have automatic storage duration by default. The `auto` keyword is considered **archaic** and is rarely used.

### The `register` Specifier
A hint to the compiler that the object should be made as quickly accessible as possible, ideally by storing it directly in a **CPU register** rather than in RAM.
*   The compiler may ignore this hint.
*   **Restriction**: You **must not** use the address operator (`&`) on objects declared with the `register` specifier, because registers do not have memory addresses.

### The `static` Specifier
Variables defined with the `static` specifier have **static storage duration**.
*   **Lifetime**: Created as soon as the program starts, and destroyed only when the program ends.
*   **Initialization**: All objects with static storage duration are **automatically initialized to 0** if no explicit initializer is provided (unlike automatic variables, which contain undefined garbage).
*   Global variables automatically have static storage duration.

---

## 3. Scope vs. Storage Duration
These are two distinct concepts:
*   **Scope**: Determines *where* a name can be accessed (visibility).
*   **Storage Duration**: Determines *when* a variable is created and destroyed (lifetime).

### Local Static Variables
A local variable declared as `static` has *block scope* but *static duration*.
*   It is only accessible within the function it was declared in.
*   However, its value **persists** between function calls because it remains in memory forever.

```c
#include <stdio.h>

void f() {
    static int n = 0; // Created once, initialized to 0
    printf("%d ", ++n);
}

int main() {
    for (int i = 0; i < 5; ++i) f(); 
    // Output: 1 2 3 4 5 (value persists)
    // printf("%d", n); -> ERROR: n is out of scope here!
}
```

---

## 4. Memory Layout (RAM Zones)
A running program divides its memory into distinct zones:

1.  **Permanent Area (Data/BSS & Text Segments)**:
    *   Contains instructions, global variables, and `static` variables.
    *   Lifetime: Entire duration of the program.
2.  **The Stack**:
    *   Contains local variables (automatic storage duration) and function call information.
    *   Lifetime: Begins when the definition is encountered, ends at the end of their scope.
3.  **The Heap**:
    *   Dynamic memory (`malloc()`, `free()`).
    *   Lifetime: Fully under the programmer's control.

---

## 5. The Call Stack
The **call stack** (or execution stack/machine stack) is a LIFO (Last In, First Out) data structure that stores information about active subroutines.

*   **Push & Pop**: When a function is called, a new stack frame is *pushed* onto the stack containing its local variables, parameters, and the return address. When the function finishes, the frame is *popped* off.
*   **Memory Addresses**: Parameters and local variables are placed sequentially in the stack memory.

### Stack Overflow
Like the heap, the stack has a limited size. It cannot grow infinitely.
*   **Infinite Recursion**: If functions call each other in an infinite loop (e.g., `f1()` calls `f2()`, which calls `f1()`), new frames are continuously pushed onto the stack.
*   Eventually, the stack grows past its allocated memory limit, resulting in a crash known as a **Segmentation Fault** (specifically, a Stack Overflow).

---

## 6. Textbook & External References
*   **Sections**: 5.12, 5.7
*   **Additional Links**:
    *   [Memoria RAM: Stack vs Heap](https://profrizzo.altervista.org/memoria-ram-stack-vs-heap-memoria-statica-vs-memoria-dinamica/)
