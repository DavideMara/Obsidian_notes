---
tags:
  - ProceduralProgramming
type: Elaborato
---
The **type casting** is a fundamental operation inside C that enables the modification of variables's **data type** to another.
## 1. Impicit Type Casting

Also called **Automatic type coveresion**, is performed by the compiler without any intervention from the programmer.
The compiler follows a rule set called **Integer Promotion** and the **Usual Arithmetic Conversions** to ensure the operation makes sense.
### The "Promotion" Rule
The compiler generally converts the "smaller" type to the "larger" type to prevent data loss. This is often called **Widening**.

- **Logic:** `char` → `short` → `int` → `unsigned int` → `long` → `float` → `double`
- **Example:**
```c
int a = 10;
float b = 5.5;
float result = a + b; // 'a' is implicitly promoted to float before addition
```

> [!warning] Precision Loss
> While implicit casting usually "widens" data, it can occur during assignment in a way that causes "narrowing " wihtout a warning
> `int i = 3.99; // The compiler implicitly casts 3.99 to 3` 


## 2. Explicit Type Casting 

Is a manual conversion performed by the programmer using the **cast operator**. This is  essentially you telling the compiler that "you are forcing" this bit pattern into this type.

```c
int total_marks = 450;
int max_marks = 500;

// Incorrect: result will be 0.000000 because 450/500 = 0 in integer math
float percentage = total_marks / max_marks; 

// Correct: Explicitly cast one operand to float
float percentage = (float)total_marks / max_marks;
```

## 3. Comparison

| **Feature**      | **Implicit Casting**             | **Explicit Casting**                     |
| ---------------- | -------------------------------- | ---------------------------------------- |
| **Performed by** | Compiler automatically           | Programmer manually                      |
| **Direction**    | Usually "Lower" to "Higher" type | Any type to any compatible type          |
| **Safety**       | Generally safe (Widening)        | Potentially risky (Narrowing/Truncation) |
| **Syntax**       | None                             | `(type)` operator                        |
## 4. Pointer Casting

Pointer casting allows you to treat a memory address as a different type
```c
int n = 65;
int *p = &n;
char *c = (char*)p; // Explicitly casting int* to char*

printf("%c", *c); // Outputs 'A' (ASCII 65)
```
In the example, the cast tells the compiler to read only  **1 byte** at that address instead of the usual **4 bytes** for an integer. This is the foundation of how `void*` pointers work in functions like `malloc()` 