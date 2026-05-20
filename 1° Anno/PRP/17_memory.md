---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 17 Memory: Storage Classes, Zones, and the Call Stack

## 1. Definition vs. Declaration

* **Declaration**: Tells the compiler that a symbol (variable or function) exists, along with its name and type. You can have multiple declarations.
  * *Variable declaration*: *"There is a variable with the following name and type in the program."*
  * *Function declaration*: A prototype (e.g. `int func();`) without a body.
* **Definition**: Allocates memory for a variable or provides the actual body for a function. Since every definition is also a declaration, it declares the symbol as well. There can only be one definition per symbol.
  * *Variable definition*: Tells the compiler to allocate memory for the variable now.
  * *Function definition*: Provides the function body.

### Examples

**Example 1 — Function declaration vs variable definition:**
```c
int func(); // func is declared
int main() {
    int x = func(); // x is defined
}
```

**Example 2 — Global variable definition:**
```c
int x; // x is defined (memory allocated)
int main() {
    x = 3;
}
```

**Example 3 — Local variable definition:**
```c
int func() {
    int x = 3; // x is defined
}
```
*Note: Since a definition is also a declaration, the symbols are also declared at their definition.*

---

## 2. Storage Classes and Specifiers

A **storage class specifier** modifies the **storage duration** (lifetime) of an object. There are three possible durations:

1. **Automatic**: Created and destroyed automatically based on scope.
2. **Static**: Created once at program start, destroyed at program termination.
3. **Dynamic**: Controlled manually by the programmer (heap).

### The `auto` Specifier
Objects declared with `auto` have automatic storage duration. In ANSI C, local variables within a function have automatic storage duration by default — the `auto` keyword is considered **archaic** and rarely used.

```c
int main(void) {
    int a;
    {
        int count;
        auto int month; // Archaic: local auto storage class specifier
    }
    a++;
}
```

### The `register` Specifier
A hint to the compiler that the object should be stored in a **CPU register** for fast access.
*   The compiler may ignore this hint.
*   **Restriction**: You **must not** use the address operator (`&`) on `register` variables, since registers have no memory address.

```c
{
    register int miles;       // OK: hint to use a register
}

{
    register int miles;
    int *p = &miles;          // ERROR: cannot take address of a register variable
}
```

### The `static` Specifier
Variables defined with `static` have **static storage duration**.
*   **Lifetime**: Created when the program starts, destroyed only when the program ends.
*   **Initialization**: Automatically initialized to `0` if no explicit initializer is provided (unlike automatic variables, which contain garbage).
*   Global variables automatically have static storage duration.

```c
int x = 0;          // Global: static storage duration by default
int main() { x = 3; }

int main() {
    static int x = 3;   // Local, but with static storage duration
}
```

---

## 3. Scope vs. Storage Duration

These are two **distinct** concepts:
*   **Scope**: Determines *where* a name can be accessed (visibility).
*   **Storage Duration**: Determines *when* a variable is created and destroyed (lifetime).

| | Scope | Storage Duration |
|---|---|---|
| Local variable | Block (function/loop/...) | Automatic (destroyed at end of scope) |
| `static` local variable | Block | Static (persists for the whole program) |
| Global variable | File (from declaration onward) | Static |

### Key Rules
*   A variable being **forever in memory** does not mean it is always accessible — it is only accessible **within its scope**.
*   Automatic variables are **re-created** every time execution enters their scope.
*   Static local variables **retain their value** between function calls.

### Examples

**Example 1 — Scope of local vs. global variables:**
```c
// Local variable: block scope, automatic storage duration
void f() { int i; i = 1; }   // OK: in scope
void g() { i = 2; }           // ERROR: i not in scope

// Global variable: file scope, static storage duration
int i;
void f() { i = 1; }           // OK
void g() { i = 2; }           // OK: still in scope
```

**Example 2 — Automatic vs. static in a loop:**
```c
for (int i = 0; i < 5; ++i) {
    int n = 0;
    printf("%d ", ++n);
}
// prints: 1 1 1 1 1  (automatic: re-created each iteration)

for (int i = 0; i < 5; ++i) {
    static int n = 0;
    printf("%d ", ++n);
}
// prints: 1 2 3 4 5  (static: value persists)
```

**Example 3 — Static local is out of scope outside its block:**
```c
for (int i = 0; i < 5; ++i) {
    static int n = 0;
    printf("%d ", ++n);
}
printf("%d ", n);   // ERROR: n is out of scope here
```

**Example 4 — Static local inside a function:**
```c
#include <stdio.h>
void func(void);
int count = 10;   // global: static storage

int main() {
    while (count--) func();
}

void func(void) {
    static int i = 5;   // initialized only once
    i++;
    printf("i is %d and count is %d\n", i, count);
}
// Output:
// i is 6 and count is 9
// i is 7 and count is 8
// ...
// i is 15 and count is 0
```

**Example 5 — Local static is not visible outside its block:**
```c
#include <stdio.h>
void func(void);
int count = 10;

int main() {
    while (count--) func();
    i++; // ERROR: i is static but not visible in main
}

void func(void) {
    static int i = 5;
    i++;
    printf("i is %d and count is %d\n", i, count);
}
// Compilation fails: error: use of undeclared identifier 'i'
```

**Example 6 — Global variable must be declared before use:**
```c
#include <stdio.h>
void func(void);

int main() {
    while (count--) func(); // ERROR: count is not declared yet
}

int count = 10; // Declared too late for main
void func(void) {
    static int i = 5;
    i++;
    printf("i is %d and count is %d\n", i, count);
}
// Compilation fails: error: use of undeclared identifier 'count'
```

---

## 4. Static Storage: Initialization

All objects with **static storage duration** are **initialized to 0 automatically**.  
Objects with **automatic storage duration** are **not** initialized — their value is undefined.

```c
int main() {
    static int a;   // initialized to 0
}

int main() {
    int a;          // NOT initialized — value is undefined (garbage)
}
```

> **Best practice**: Always initialize variables explicitly, especially those with automatic storage duration.

---

## 5. Different Memory Zones (RAM Layout)

A running program divides its RAM into distinct zones:

| Zone | Contents | Lifetime |
|---|---|---|
| **Permanent Area** (Data/BSS & Text) | Global variables, `static` variables, instructions | Entire program |
| **Stack** | Local variables, function parameters, return addresses | Scope-based (automatic) |
| **Heap** | Dynamically allocated memory (`malloc`/`free`) | Programmer-controlled |

### Characteristics
*   **Permanent Area**: Variables with static storage duration — created at program start, destroyed at program end.
*   **Stack**: Variables with automatic storage duration — created when their definition is encountered, destroyed at the end of their scope.
*   **Heap**: Allocation begins with `malloc()`, deallocation with `free()`.

### Example — Stack vs. Heap allocation:
```c
int main() {
    int a1[3];                              // Stack: local array
    int *a2 = (int*) malloc(3 * sizeof(int)); // Heap: dynamic array
}
// a2 is a pointer on the stack; the array data lives in the heap
```

### Example — Mixing static, stack, and heap:
```c
#include <stdio.h>
int size = 5;  // global (static storage)

void fun(int *b, int n) {
    for (int i = 0; i < n; ++i) {
        static int c = 0;   // static: persists across calls
        b[i] = ++c;
    }
}

int main() {
    int *a = (int*) malloc(sizeof(int) * size);
    fun(a, size);   // a = {1, 2, 3, 4, 5}
    fun(a, size);   // a = {6, 7, 8, 9, 10}  (c continues from 5)
    free(a);        // Always free heap memory!
}
```

---

## 6. The Call Stack

The **call stack** (also known as execution stack, program stack, run-time stack, or machine stack) is a **LIFO** (Last In, First Out) data structure that stores information about active subroutines.

### Stack Operations
*   **Push**: When a function is called, a new **stack frame** is pushed onto the stack, containing:
    *   Local variables
    *   Function parameters
    *   The return address
*   **Pop**: When the function returns, its frame is popped off the stack.

### Memory Address Layout
Parameters and local variables are placed sequentially in stack memory:

```c
int fun(int p1, int p2, int p3) {
    int res = 0;
    res = p1 + p2 + p3;
    return res;
}
int main() {
    int a = 4, b = 5, c = 7;
    a = fun(a, b, c);
}
// Stack layout (bottom to top): a, b, c | p1, p2, p3, return address, res
```

### Example — Function calls and the stack:
```c
#include <stdio.h>
void f2() { int c; puts("bye f2"); }
void f1() { int b = 0; f2(); puts("bye f1"); }
int main() { int a = 0; f1(); puts("bye main"); }
// Output:
// bye f2
// bye f1
// bye main
// Stack frames: a → b → c (pushed), then c → b → a (popped)
```

---

## 7. Stack Overflow

Like the heap, the stack has a **limited size** and cannot grow infinitely.

*   If functions call each other recursively without a base case (e.g., `f1()` calls `f2()` which calls `f1()` …), new frames are continuously pushed.
*   Eventually the stack exceeds its memory limit → **Segmentation Fault** (Stack Overflow).

```c
void f2() { int c; f1(); puts("bye f2"); }
void f1() { int b = 0; f2(); puts("bye f1"); }
int main() { int a = 0; f1(); puts("bye main"); }
// Result: Segmentation fault: 11  (infinite mutual recursion)
```

---

## 8. Textbook & External References
*   **Sections**: 5.12, 5.7
*   **Additional Links**:
    *   [Memoria RAM: Stack vs Heap](https://profrizzo.altervista.org/memoria-ram-stack-vs-heap-memoria-statica-vs-memoria-dinamica/)
    *   [Allocazione dinamica della memoria](https://www.riochierego.it/docs/10Allocazione_dinamica_della_memoria.pdf)
    *   [shorturl.at/fknPY](https://shorturl.at/fknPY)
