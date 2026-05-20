---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 01 Language Basics

## 1. Programming Languages & Paradigms
A **programming language** is a formal language that specifies a set of instructions used to produce various kinds of output, generally consisting of instructions for a computer to implement specific algorithms.

### Programming Paradigms
Paradigms are ways to classify programming languages based on their design features:
*   **Imperative**: The programmer explicitly instructs the machine on how to change its state.
    *   *Example:* `a = a + 1;`
*   **Procedural**: Derived from structured programming, based on the concept of the *procedure call*. Instructions are grouped into procedures (also known as routines, subroutines, or functions) that contain a series of computational steps.
*   *Other paradigms include:* Object-oriented (e.g., Java), Functional, etc.

> [!NOTE]
> C is both **imperative** and **procedural** because programmers instruct state changes and group these instructions into functions.

---

## 2. Language Levels & The Stack of Interpretation
Languages exist at different levels of abstraction relative to the hardware. As programs grew larger, moving up the stack became necessary to reduce error-prone notation and handle machine dependency.

### The Abstraction Stack (From Top to Bottom)
1.  **High-Level Languages (e.g., C, C++)**: Closer to human language, machine-independent, and abstracted from machine-specific details. Created in the mid-1950s (starting with Fortran, then Lisp and Algol) to avoid rewriting programs for every new machine architecture.
2.  **Assembly Language**: Replaces binary patterns with mnemonic abbreviations (e.g., `movl`, `pushl`, `subl`). Machine-specific.
3.  **Machine Language**: Binary patterns (`1`s and `0`s) directly understood by the hardware.
4.  **Processor**: The physical hardware executing instructions.

---

## 3. Compilation vs. Interpretation
High-level code must be translated so that a processor can run it. There are two primary translation models:

### Compilation (e.g., C, C++)
*   A system program known as a **compiler** translates the high-level source code into an equivalent target program (assembly/machine language) *before* execution.
*   **Hallmarks**: Thorough analysis of source code and nontrivial transformation (the output does not resemble the source).
*   **Flow**:
    $$\text{Source Program} \xrightarrow{\text{Compiler (gcc)}} \text{Target Program (Executable)}$$
    $$\text{Input} \xrightarrow{} \text{Target Program} \xrightarrow{} \text{Output}$$
*   **Error Checking**: Almost all semantic error checking is done at compile time.

### Interpretation (e.g., Python)
*   An **interpreter** remains present in memory during execution. It simulates a virtual machine that executes the high-level instructions directly.
*   **Flow**:
    $$\text{Source Program} + \text{Input} \xrightarrow{\text{Interpreter}} \text{Output}$$
*   **Error Checking**: Most error checking must be performed at run time.

---

## 4. The C Programming Language

### Overview
C is a high-level, general-purpose, procedural programming language developed in the 1970s by Dennis Ritchie at Bell Labs to implement the Unix operating system and utilities.

### Key Characteristics
*   **Source Code Portability**: Code can be recompiled on different hardware platforms with minimal changes.
*   **Close to the Machine**: Operates at a low level when needed, allowing direct access to memory addresses.
*   **Efficiency**: Extremely fast execution because it compiles directly to native machine code.

### Standard Library
The C language proper is small and contains very few hardware-dependent elements (e.g., it lacks built-in statements for file access, dynamic memory management, or input/output).
Instead, these functions are provided by the standard library via header files (e.g., `<stdio.h>`).

### Advantages (Virtues)
*   **Fast**: Compiled language operating close to the hardware.
*   **Portable**: Can run on virtually any platform with a C compiler.
*   **Small**: Simple core language without excess syntax (unlike C++).
*   **Mature**: Extensive documentation, library support, and experienced user base.
*   **Access**: Direct memory manipulation (pointers) and low-level system feature access.

### Challenges
*   **Unsafe**: Easy to cause segmentation faults or corruption via direct memory access and pointers.
*   **Manual Memory Management**: The programmer must allocate and deallocate memory explicitly.
*   **Verbose**: Requires more lines of code compared to scripting languages like Python.

---

## 5. The C++ Programming Language
*   Developed by Bjarne Stroustrup at Bell Labs, starting as "**C with Classes**" in 1983 and officially becoming C++ in 1985.
*   Standardized in 1998 (ISO/IEC 14882:1998).
*   Combines the speed and low-level features of C with support for **Object-Oriented Programming (OOP)** (inspired by Simula).
*   OOP support made C++ the dominant language for GUI-heavy applications in the 1990s.
*   Unlike C, C++ is a massive and highly complex language (with standards spanning hundreds of pages).

---

## 6. Language Standards
Standards prevent vendor fragmentation and ensure compiler compatibility:
*   **K&R C**: 1972 (Created) / 1978 (First informal specification).
*   **ANSI C / C89**: 1989 (First standardized version).
*   **ISO C / C90**: 1990 (Equivalent to C89).
*   **C95**: 1995 (Amendment 1).
*   **C99**: 1999 (Introduced new features).
*   **C11**: 2011 (Standard target). Compile with: `gcc file.c -std=c11`
*   **C18**: 2018 (Bug fixes over C11).

---

## 7. Structure of a C Program
The procedural building blocks of C are **functions**.
*   Functions **cannot** be nested inside each other.
*   Functions contain statements executed **sequentially**.
*   Statements can be grouped into **block statements** (enclosed in `{}`).
*   Every C program must define a `main()` function, which serves as the program's top level of control and entry point.

### Single-File Compilation Example (`mainfile.c`)
```c
#include <stdio.h>

void myPrintHello(); // Function prototype

int main() {
    myPrintHello();
    return(0);
}

void myPrintHello(void) {
    printf("Hello!\n");
    return;
}
```
*   **Compile to custom name:** `gcc -o mainfile mainfile.c` (runs with `./mainfile`)
*   **Default compile:** `gcc mainfile.c` (produces `./a.out`)

### Modular Programming Example
Modular programming is a design technique that separates program functionalities into independent, interchangeable files (modules).

*   `mainfile.c`:
    ```c
    void myPrintHello(void); // Prototype for function in other file

    int main() {
        myPrintHello();
        return(0);
    }
    ```
*   `hello.c`:
    ```c
    #include <stdio.h>

    void myPrintHello(void) {
        printf("Hello!\n");
        return;
    }
    ```
*   **Multi-file Compile:** `gcc -o executable mainfile.c hello.c`

---

## 8. Program Development & Errors
The general program development cycle is:
$$\text{Problem Definition} \rightarrow \text{Problem Analysis} \rightarrow \text{Algorithm Development} \rightarrow \text{Coding} \rightarrow \text{Testing/Debugging} \rightarrow \text{Maintenance}$$

In C, the cycle alternates between **Compile-time** and **Run-time**:
$$\text{Edit Code} \rightarrow \text{Compile (Compile-time)} \rightarrow \text{Test/Execute (Run-time)} \rightarrow \text{Edit Code}$$

### Compile-time Errors
Errors detected by the compiler. These are typically **Syntax Errors** (e.g., missing semicolons or using reserved keywords incorrectly).
*   *Example Code with Error:*
    ```c
    scanf("%d", &b) // Missing semicolon
    while(b != 0) { ... }
    ```
*   *Compiler Output:*
    ```text
    euclid.c:9:20: error: expected ';' after expression
    scanf("%d", &b)
                   ^
                   ;
    1 error generated.
    ```

### Run-time Errors
Errors that occur while the program is executing. These do not prevent compilation but lead to crashes or undefined behavior.
*   *Example (Dereferencing a Null Pointer):*
    ```c
    #include <stdio.h>
    int main() {
        int *a = NULL;
        printf("%d", *a); // Dereferencing NULL
        return 0;
    }
    ```
*   *Terminal Output:*
    ```text
    Segmentation fault: 11
    ```

> [!TIP]
> Debugging requires understanding compiler messages to resolve syntax errors at compile-time and testing the program with diverse inputs to discover logic/runtime errors.
> As Edsger Dijkstra noted: *"Testing shows the presence, not the absence of bugs."*

---

## 9. Full Example: Euclid's GCD Algorithm
This example demonstrates a complete program written in C, compiled to Assembly, and finally stored as Machine Language instructions.

### 1. High-Level C Code
```c
#include <stdio.h>

int main() { 
    int a, b; 
    printf("Enter first positive integer: \n"); 
    scanf("%d", &a); 
    printf("Enter second positive integer: \n"); 
    scanf("%d", &b); 
    
    while(b != 0) { 
        if(a > b) 
            a = a - b; 
        else 
            b = b - a; 
    } 
    
    printf("GCD = %d\n", a); 
    return 0;
}
```

### 2. Equivalent x86 Assembly Code
```assembly
pushl   %ebp
movl    %esp, %ebp
pushl   %ebx
subl    $4, %esp
andl    $-16, %esp
call    getint
movl    %eax, %ebx
call    getint
cmpl    %eax, %ebx
je      C
A:
cmpl    %eax, %ebx
jle     D
subl    %eax, %ebx
B:
cmpl    %eax, %ebx
jne     A
C:
movl    %ebx, (%esp)
call    putint
movl    -4(%ebp), %ebx
leave
ret
D:
subl    %ebx, %eax
jmp     B
```

### 3. Machine Language (Binary Representation)
```text
11001111 11111010 11101101 11111110 00000111 00000000
00000000 00000001 00000011 00000000 00000000 00000000
00000010 00000000 00000000 00000000 00010000 00000000
00000000 00000000 00010000 00000100 00000000 00000000
10000101 00000000 00100000 00000000 00000000 00000000 ...
```

---

## 10. Book References
*   **Section 1.9** (Concepts in 1.9.2–1.9.7 will be reviewed in detail at the end of the course).
*   **Section 2.1–2.3**.

