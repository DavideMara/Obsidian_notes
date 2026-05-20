---
tags:
  - ProceduralProgramming
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 20 GCC Compilation Steps and GDB Debugging

This lecture details the internal steps performed by the GCC compiler chain (preprocessing, compilation, assembly, and linking) and provides an introduction to debugging C programs with GDB.

---

## 1. The Four Steps of GCC Compilation
When you run `gcc -o program file.c`, GCC coordinates four distinct tools behind the scenes:

```
Source (.c) ──► [ Preprocessor ] ──► Preprocessed (.i)
                                            │
                                            ▼
               Assembly (.s)   ◄─── [ Compiler ]
                     │
                     ▼
                [ Assembler ]  ──► Object Code (.o)
                                         │
                                         ▼
Executable ◄──── [ Linker ]    ◄── Other .o files & Libraries
```

---

## 2. Preprocessing (`cpp`)
The C preprocessor is a **macro processor** that transforms the source code before actual compilation.

### Key Facilities
1.  **Header File Inclusion**: Replaces `#include` directives with the literal content of the referenced files.
2.  **Macro Expansion**: Replaces macro names with their defined text fragments (e.g., `#define ARRAY_SIZE 100`).
3.  **Conditional Compilation**: Includes or excludes blocks of code using directives like `#if`, `#ifdef`, `#ifndef`, `#else`, and `#endif`.

### Header File Search Paths
*   **Angle Brackets (`#include <filename.h>`)**: Used for C standard library headers. The preprocessor searches in system include directories (e.g., `/usr/include` or `/usr/local/include` on Unix systems).
*   **Double Quotes (`#include "filename.h"`)**: Used for program-specific headers. The preprocessor searches the current directory containing the source files first. If not found, it falls back to the system include directories.
*   **Explicit Path**: If the filename contains a path (e.g., `"../headers/myproject.h"`), the preprocessor looks *only* in that directory.

### Macro Rules
*   **Constant Definitions**: `#define PI 3.141593`
*   **No Recursion**: Macro expansion cannot be recursive. For example:
    ```c
    #define A (A / 8) // The inner A will not be expanded again, avoiding infinite loops.
    ```

### Saving Preprocessor Output
By default, preprocessor output is temporary. You can inspect it by running GCC with the `-E` option, which halts compilation after preprocessing:
```bash
gcc -E -o mylibrary.i mylibrary.c
```

---

## 3. Compilation (`cc1`)
The compiler translates preprocessed C code (`.i`) into **assembly language** (`.s`), which matches the target CPU architecture.

### Saving Assembly Output
Use the `-S` option to stop GCC after generating the assembly files:
```bash
gcc -S file.c   # Produces file.s
```

### Assembly Example
For a simple program:
```c
int main() {
   int a = 5;
   a++;
}
```

The generated x86_64 assembly (macOS version shown below) looks like:
```assembly
.section        __TEXT,__text,regular,pure_instructions
.macosx_version_min 10, 11
.globl   _main
.align   4, 0x90
_main:
        .cfi_startproc
        pushq   %rbp
        movq    %rsp, %rbp
        xorl    %eax, %eax
        movl    $5, -4(%rbp)       # int a = 5; (stores 5 in stack memory)
        movl    -4(%rbp), %ecx     # Load a into register %ecx
        addl    $1, %ecx           # Increment %ecx
        movl    %ecx, -4(%rbp)     # Store result back into a
        popq    %rbp
        retq
        .cfi_endproc
```

---

## 4. Assembly (`as`)
The assembler translates assembly language (`.s`) into binary **machine code** (also known as instruction codes).

### Output: Object Files (`.o` or `.obj`)
An object file contains:
*   Machine code instructions.
*   A **symbol table** listing functions and global variables defined in the file that have external linkage, allowing the linker to find them.

### Compiling Without Linking
To produce an object file without linking, compile with the `-c` flag:
```bash
gcc -c mylibrary.c   # Produces mylibrary.o
```

---

## 5. Linking (`ld`)
The linker joins multiple binary object files (`.o`) and library files into a single **executable file**.

### Tasks of the Linker
1.  **Resolve Symbolic References**: Replaces references to external symbols (functions and variables) with their final memory locations.
2.  **Include Library Code**: Integrates the binary code for standard library functions (like `printf` or `sqrt`) referenced in the program.

---

## 6. Debugging with GDB (GNU Debugger)
GDB is a symbolic, command-line debugger that lets you inspect what is happening inside a C program during execution.

### Compiling with Debug Symbols
To use GDB, you must instruct the compiler to include debugging information and the symbol table in the executable by using the `-g` option:
```bash
gcc -g -o test test.c
```

### Essential GDB Commands
| Command | Short | Description |
| :--- | :--- | :--- |
| `list` | `l` | Lists 10 lines of source code (type `l` again to list the next 10). |
| `break [line/func]` | `b` | Sets a breakpoint at a specific line or function (e.g., `b 7` or `b main`). |
| `run` | `r` | Starts program execution. |
| `next` | `n` | Executes the next statement. If it contains a function call, it **steps over** it. |
| `step` | `s` | Executes the next statement. If it contains a function call, it **steps into** it. |
| `print [expr]` | `p` | Prints the value of a variable or expression (e.g., `p i` or `p a[i]`). |
| `continue` | `c` | Continues execution until the next breakpoint or program end. |
| `info breakpoints` | | Lists all active breakpoints and how many times they have been hit. |
| `delete [num]` | `d` | Deletes breakpoint number `num`. |
| `quit` | `q` | Exits GDB. |

---

## 7. GDB Debugging Case Study: Array Out-of-Bounds
Consider the following program with a bug:

```c
#include <stdio.h>

int main() {
    int a[] = {6, 5, 4, 3, 2};
    // Bug: The condition checks elements up to a[5] (out of bounds)
    for (int i = 0; i < sizeof(a) / sizeof(int); i++) {
        if (a[i] > a[i+1]) 
            continue;
        puts("Errore");
        break;
    }
    return 0;
}
```

### Identifying the Bug using GDB
1.  **Compile and Run GDB**:
    ```bash
    gcc -g -o test test.c
    gdb test
    ```
2.  **Set Breakpoint and Run**:
    ```gdb
    (gdb) b 7
    Breakpoint 1 at 0x100000ecc: file test.c, line 7.
    (gdb) r
    Starting program: /path/to/test
    Breakpoint 1, main () at test.c:7
    7		for (int i = 0; i < sizeof(a) / sizeof(int); i++) {
    ```
3.  **Step and Print**:
    Use `n` to step through the loop iterations. 
    At iteration `i = 4` (the 5th element of `a` which contains `2`):
    ```gdb
    (gdb) p a[i]
    $2 = 2
    (gdb) p a[i+1]
    $3 = 32767   <-- Out of bounds access! Contains garbage from stack memory.
    (gdb) p i
    $4 = 4
    ```
    Because `a[4] > a[5]` (i.e. `2 > 32767`) evaluates to false, the loop does not hit the `continue` statement. Instead, it reaches line 10, executes `puts("Errore")`, and breaks.

---

## 8. Textbook & References
*   **Sections**: 1.2, 1.4, 1.9.2–1.9.7
*   **Chapter**: 14
*   **Appendix**: G
