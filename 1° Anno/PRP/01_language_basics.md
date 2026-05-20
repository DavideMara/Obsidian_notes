---
tags:
  - ProceduralProgramming
  - LectureNotes
---
# 01 Language Basics

## Introduction to Programming Languages
- A **formal language** that specifies a set of instructions to produce various outputs.
- Used to create programs implementing specific algorithms.
- **High-level languages**: Closer to human language, further from machine language.

## C Programming Language
- **Imperative**: The programmer instructs the machine on how to change its state (e.g., `a = a + 1;`).
- **Procedural**: Instructions are grouped into functions.
- **History**:
    - Developed by **Dennis Ritchie** in the 1970s at AT&T Bell Labs.
    - Purpose: Implement the Unix operating system.
    - Ancestors: BCPL and B.
    - Standardized description by Kernighan and Ritchie in 1978.
- **Characteristics**:
    - Source code portability.
    - "Close to the machine" operation.
    - High efficiency and fast execution (compiled).
    - Direct access to memory.
    - Small core language; functionality like I/O and memory management is provided by the **Standard Library** (e.g., `stdio.h`).

## Compilation vs. Interpretation
- **Compiler**: Translates high-level source program into an equivalent target program (assembly/machine language) *before* execution.
    - Hallmarks: Thorough analysis and nontrivial transformation.
    - Example: `gcc`.
- **Interpreter**: Stays around during execution, implementing a virtual machine that executes the high-level language directly.
    - Example: Python.

## C Development Life Cycle
1. **Edit Code**
2. **Compile-time**: Using `gcc`. Errors detected here are **Syntax Errors** (e.g., missing `;`).
3. **Run-time**: Executing the program. Errors here include **Runtime Errors** (e.g., Segmentation Fault).
4. **Test & Debug**: "Testing shows the presence, not the absence of bugs" (Dijkstra).

## Standards

- **K&R C** (1972/1978)
- **ANSI C / C89** (1989)
- **ISO C / C90** (1990)
- **C99** (1999)
- **C11** (2011) - Use `gcc file.c -std=c11`
- **C18** (2018)
