---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 19 Modularization and Linkage

This lecture covers the principles of modular programming in C, compilation and linking processes, storage class specifiers, identifier linkage (internal, external, none), and variable declarations vs. definitions (including tentative definitions).

---

## 1. Modular Programming
**Modularization** is a method used to organize large programs into smaller, manageable parts called **modules**. 
Each module has a well-defined **interface** (header file `.h`) that specifies what "services" it provides to other modules (client files), and an **implementation** (source file `.c`) containing the actual code.

### Benefits of Modular Programming
*   **Reusability**: Modules can be reused across different projects.
*   **Encapsulation**: Changing internal implementation details doesn't affect client modules, provided the interface remains unchanged.
*   **Faster Recompilation**: Only modified modules need to be recompiled, saving build time.
*   **Self-Documenting**: Header files act as documentation for how to use the module.
*   **Easier Debugging**: Dependencies are explicit, and modules can be unit-tested in isolation.

---

## 2. Compilation and Linking Processes

A C compiler translates source code into machine code in distinct phases:
1.  **Preprocessor**: Processes `#include` directives, macros, and conditional compilation.
2.  **Compiler**: Translates C code into assembly.
3.  **Assembler**: Generates an **object file** (suffix `.o` or `.obj`) containing machine code for each **translation unit** (a `.c` file and all headers it includes).
4.  **Linker**: Combines separate object files and library functions (e.g., standard library) into a single **executable file**.

```
Source Code                Object Code               Executable
┌────────────┐             ┌────────────┐
│ mainfile.c │ ──[gcc -c]─>│ mainfile.o │ ──────┐
└────────────┘             └────────────┘       │
                                                ├──[Linker]──> [Executable: main]
┌────────────┐             ┌────────────┐       │
│ hellolib.c │ ──[gcc -c]─>│ hellolib.o │ ──────┘
└────────────┘             └────────────┘
```

### Compiling Separately vs. Together
*   **Compiling Together**:
    ```bash
    gcc -o mainfile mainfile.c hellolib.c
    ```
*   **Compiling Separately**:
    ```bash
    gcc -c mainfile.c   # Produces mainfile.o
    ```
    ```bash
    gcc -c hellolib.c   # Produces hellolib.o
    ```
    ```bash
    gcc -o main mainfile.o hellolib.o  # Links them
    ```
    Separate compilation allows writing and compiling one module independently of the other.

---

## 3. Structure of a Module: Headers & Implementations
To share declarations, macros, constants, and types across multiple files, we use header files.

*   **Header File (`.h`)**: Contains only macro definitions, type definitions, and function declarations (prototypes) that client programs are allowed to see and use.
*   **Code File (`.c`)**: Contains function definitions and private variables. 

> [!IMPORTANT]
> A module's `.c` file should always `#include` its own `.h` file. This allows the compiler to verify that the function definitions match the prototypes declared in the header, catching mismatch errors early.

### Example: Hello Library
**`hellolib.h` (Interface)**
```c
#ifndef HELLOLIB_H
#define HELLOLIB_H

void myPrintHello(void);

#endif
```

**`hellolib.c` (Implementation)**
```c
#include <stdio.h>
#include "hellolib.h"

void myPrintHello(void) {
    printf("Hello!\n");
}
```

**`mainfile.c` (Client)**
```c
#include "hellolib.h"

int main() {
    myPrintHello();
    return 0;
}
```

---

## 4. Storage Duration vs. Linkage

A common source of confusion is that storage class specifiers (`auto`, `register`, `static`, `extern`) affect both:
1.  **Storage Duration** (Lifetime of the object - Stack, Heap, or Static zone).
2.  **Linkage** (Scope of the identifier across different files).

> [!NOTE]
> *   **Objects** have storage duration, not linkage.
> *   **Identifiers** (names) have linkage, not storage duration.

### Rules for Specifiers
*   No more than one storage class specifier may appear in a single declaration (e.g., `static extern int a;` is invalid).
*   **Function identifiers** can only use `extern` or `static`.
*   **Function parameters** can only use `register`.
*   **Variable identifiers** can use `auto`, `register`, `static`, or `extern`.

---

## 5. Linkage Types
Linkage determines whether an identifier can be referenced in other translation units.

| Linkage Type | Scope | Applied To |
| :--- | :--- | :--- |
| **External** | Entire program (all files) | Global variables (default) and functions (default or `extern`) |
| **Internal** | Only within the current translation unit | Global variables and functions declared with `static` |
| **No Linkage** | Only within the local block scope | Local variables (default or `static`) and function parameters |

### Example 1: Identifier Linkage
```c
static int c; // Internal linkage (visible only in this file)

int fun(int a, int b) { // fun has external linkage; a and b have no linkage
    int res = a + b;    // res has no linkage
    extern int c;       // refers to the global 'c' (internal linkage)
    
    // Note: In standard C, static local variables must be initialized with constant expressions.
    // The line below is for illustration of 'd' having no linkage (but static storage duration).
    static int d; 
    d = res + c;
    
    return res;
}
```

### Example 2: Detailed Linkage Tracing
```c
int func1(void);          // func1: external linkage
int a;                    // a: external linkage
extern int b;             // b: external linkage
static int c;             // c: internal linkage

static void func2(int d)  // func2: internal linkage; d: no linkage
{
    extern int a;         // a: external linkage (refers to the global 'a')
    int b = 2;            // b: no linkage (local variable, shadows global 'b')
    static int e;         // e: no linkage (local static variable)
    extern int c;         // c: internal linkage (refers to the file-scope static 'c')
}

void func3(void) {        // func3: external linkage
    /* ... */
}
```

---

## 6. Variable Declarations vs. Definitions
*   **Declaration**: Introduces the identifier's name and type to the compiler. You can declare a symbol multiple times.
*   **Definition**: Allocates memory (for variables) or provides the body (for functions). You can define a symbol only once.

```c
extern int a = 10; // Definition: Includes an initializer, allocating storage.
extern double b;   // Declaration: Tells the compiler b exists; defined elsewhere.

void func(int a) {
    extern char c; // Declaration of c (no storage allocated here).
    static short d;// Definition of d.
    float e;       // Definition of e.
}
```

### Tentative Definitions
If a global variable is declared without an initializer and without `extern`, it is a **tentative definition**.
*   If another definition for the same variable exists in the translation unit, the tentative definition behaves as a simple declaration.
*   If no other definition exists, the compiler treats it as a definition initialized to `0`.

```c
#include <stdio.h>

int count;     // Tentative definition (treated as declaration because count = 4 exists)
int count = 4; // Definition

int main(void) {
    printf("count is %i\n", count); // Prints 4
}
```
*Note: Having multiple definitions with initializers (e.g. `int count = 3; int count = 4;`) causes a **redefinition error**.*

---

## 7. Linkage Case Studies (Linker Errors)

### Case 1: Internal Linkage Variable Reference
*   **`main.c`**:
    ```c
    static int count = 5; // Internal linkage
    void write_extern(void);
    int main() { write_extern(); }
    ```
*   **`write.c`**:
    ```c
    #include <stdio.h>
    extern int count; // Expects count with external linkage
    void write_extern(void) { printf("count is %i\n", count); }
    ```
*   **Result**: Linker error! `count` in `main.c` is private to `main.c` due to `static`. The linker cannot resolve `count` in `write.c`.

### Case 2: Internal Linkage Function Reference
*   **`main.c`**:
    ```c
    int count = 5;
    void write_extern(void); // Expects external linkage
    int main() { write_extern(); }
    ```
*   **`write.c`**:
    ```c
    #include <stdio.h>
    extern int count;
    static void write_extern(void) { printf("count is %i\n", count); } // Internal linkage
    ```
*   **Result**: Linker error! `write_extern` is declared `static` in `write.c`, making it invisible to `main.c`.

### Case 3: Proper Linkage Execution
*   **`main.c`**:
    ```c
    int count = 5; // External linkage definition
    void write_extern(void);
    int main() { write_extern(); }
    ```
*   **`write.c`**:
    ```c
    #include <stdio.h>
    extern int count;
    void write_extern(void) { printf("count is %i\n", count); } // External linkage
    ```
*   **Result**: Compilation and linking succeed. Outputs `count is 5`.

---

## 8. Textbook & Slide References
*   **Textbook Sections**: 1.9.2, 5.2, 15.4
*   [Declare vs Define (CProgramming)](https://www.cprogramming.com/declare_vs_define.html)
*   [Linkage in C (GeeksForGeeks)](https://www.geeksforgeeks.org/internal-linkage-external-linkage-c/)
