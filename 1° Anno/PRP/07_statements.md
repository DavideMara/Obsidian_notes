---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 07 Statements

## 1. Concept of Statements
A **statement** specifies one or more actions for the program to perform, such as assigning a value to a variable, passing control to a function, or jumping to another statement.
*   Statements are executed sequentially in the order they appear, except when flow control statements alter execution.
*   Syntactically, a statement is created by appending a semicolon to an expression:
    $$\text{[expression] ;}$$
*   *Examples*:
    *   `a + 3` is an expression.
    *   `a + 3;` is a statement.
    *   `if (a + 3;) { ... }` $\rightarrow$ **Compiler Error** (the semicolon inside parentheses is syntactically invalid because C expects an expression here, not a statement).
    *   `int a = 3; a = a + 2` $\rightarrow$ **Compiler Error** (missing semicolon at the end of the statement).

### Imperative vs. Declarative Programming
*   **Imperative Programming**: A paradigm where the programmer uses statements that explicitly change the program's state. C is an imperative and procedural language.
*   **Declarative Programming**: A paradigm that expresses the logic of a computation without describing its control flow. It aims to minimize or eliminate side effects by describing *what* the program must accomplish rather than *how* to accomplish it (e.g., Prolog-like logic rules).

---

## 2. Block Statements (Compound Statements)
A **block statement** groups multiple declarations and statements together inside braces `{}` to form a single statement:
$$\{\quad \text{[list of declarations and statements]} \quad\}$$

*   Block statements are **not** terminated by a semicolon.
*   A block is used wherever the language syntax expects a single statement but the program logic requires multiple.

### Block Statement Caveat Example
If braces are omitted, only the single statement immediately following the `if` condition is treated as conditional:

*   *Braces Omitted (Incorrect Logic)*:
    ```c
    int a = 4;
    if (a < 0)
        printf("%d is less than 0", a); // Conditional
        a = -a;                         // Unconditional (runs anyway)
        printf("a now is %d", a);       // Unconditional (runs anyway)
    // Result: prints "a now is -4"
    ```
*   *With Braces (Correct Logic)*:
    ```c
    int a = 4;
    if (a < 0) {
        printf("%d is less than 0", a); // Conditional block
        a = -a;
        printf("a now is %d", a);
    }
    // Result: prints nothing (correct)
    ```

### Block Scope & Shadows
*   Identifiers declared within a block have **block scope**. They are visible only from their point of declaration to the end of the containing block.
*   A variable declared inside a block hides (shadows) an outer variable of the same name.
```c
{ 
    double result = 0.0, x = 0.0; 
    long status = 0; 
    int limit; 
    ++x; 
    if (status == 0) { // Nested block
        int i = 0; 
        { int k = 3; } // k ceases to exist here
    } // i ceases to exist here
} // result, x, status, limit cease to exist here
```

---

## 3. Definition Statements
Definition statements are used to define variables (allocate them in memory).
*   Variables must have distinct names if they share the same scope:
    *   *Invalid:* `int a = 4; float a = 5;` (inside the same block).
*   Definition statements **cannot be used as expressions**:
    *   *Invalid:* `int a = int b = 3;` (variable declarations do not return values, so they cannot be chained like expressions).

---

## 4. Loops (Iteration Statements)
Loops execute a group of statements (the loop body) repeatedly. The execution is controlled by a **controlling expression** of scalar type (arithmetic or pointer).
*   If the controlling expression evaluates to a non-zero value, it is considered **true** and the loop continues.
*   If it evaluates to `0`, it is considered **false** and the loop terminates.

### 1. While Statement (Top-Driven)
Executes a statement repeatedly as long as the controlling expression is true:
$$\text{while ( expression ) statement}$$
The condition is evaluated *before* entering the loop body. If false initially, the body never runs.
```c
#include <stdio.h>

int main() {
    int a = 10;
    while (a < 20) {
        printf("value of a: %d\n", a);
        a++;
    }
    return 0;
}
```

### 2. For Statement (Top-Driven)
A top-driven loop containing initialization, testing, and updates in its header:
$$\text{for ( [expression1]; [expression2]; [expression3] ) statement}$$
*   `expression1` (Initialization): Evaluated once at the beginning to set up loop counters.
*   `expression2` (Controlling Expression): Evaluated before each iteration. If false, loop ends.
*   `expression3` (Adjustment): Evaluated at the end of each iteration (e.g. increments) before testing `expression2` again.

```c
int a = 0;
int i;
for (i = 0; i < 4; ++i) { // i runs: 0, 1, 2, 3 (exits at 4)
    a = a + 2;
    printf("%d ", a); // Outputs: 2 4 6 8
}
```

#### Omission of Expressions
*   Any of the three expressions in the `for` header can be omitted.
*   `for (;;)` creates an **infinite loop** (omitted conditions default to true).
*   `for (; expression; )` is equivalent to `while (expression)`.
*   All `for` loops can be rewritten as `while` loops and vice versa:
    ```c
    int a = 0, i = 0;
    while (i < 4) {
        a = a + 2;
        ++i;
    }
    ```

#### Scope of Loop Counter (C99)
Since C99, you can declare variables inside the initialization statement of a `for` loop. The counter variable's scope is restricted to the loop body:
```c
for (int i = 0; i < 4; ++i) {
    a = a + 2;
}
// i does not exist here
```

### 3. Do-While Statement (Bottom-Driven)
Executes the loop body first, then evaluates the controlling expression at the bottom:
$$\text{do statement while ( expression ) ;}$$
*   **Guarantees at least one iteration** of the loop body.
```c
#include <stdio.h>

int main() {
    double number, sum = 0;
    do {
        printf("Enter a number: ");
        scanf("%lf", &number);
        sum += number;
    } while (number != 0.0);
    printf("Sum = %.2lf\n", sum);
    return 0;
}
```

---

## 5. Selection Statements
Selection statements branch the program flow depending on the result of an evaluation.

### If Statement
$$\text{if ( expression ) statement1 [ else statement2 ]}$$
*   The `else` clause is optional.
*   The controlling `expression` must be a scalar type.

#### Dangling Else Resolution
In nested if-statements, an `else` clause is always associated with the **nearest preceding `if`** at the same block nesting level that does not have an `else`:
```c
if (n > 0)
    if (n % 2 == 0)
        puts("n is positive and even");
    else // Belongs to the nearest (inner) if
        puts("n is positive and odd");
```
To force an `else` to link to an outer `if`, enclose the inner `if` in braces:
```c
if (n > 0) {
    if (n % 2 == 0)
        puts("n is positive and even");
} else // Belongs to the first (outer) if
    puts("n is negative or zero");
```

---

## 6. Switch Statement
Jumps execution to one of several labels based on the value of an integer expression:
$$\text{switch ( expression ) statement}$$

*   The controlling `expression` must evaluate to an **integer type**.
*   **Fall-through Behavior**: Execution jumps to the matching `case` constant and continues cascading downward through all subsequent cases unless interrupted by a `break;` statement.
*   **Default Label**: executed if no case constants match. At most one `default` label is allowed.

```c
switch (menu()) {
    case 'A': 
        action1(); 
        break; // Exits switch
    case 'B': 
        action2(); 
        break; // Exits switch
    default: 
        putchar('\a'); // Runs if neither matches
}
```

### Fall-through Bug Example
```c
int Grade = 'A';
switch (Grade) {
    case 'A' : printf("Excellent\n"); // Missing break
    case 'B' : printf("Good\n");      // Missing break
    case 'C' : printf("OK\n");        // Missing break
    default  : printf("What is your grade?\n");
}
// Prints: Excellent, Good, OK, What is your grade?
```

### Case Intervals (GCC Extension)
GCC compilers support shorthand range selection inside `switch` cases.
*   *GCC Extension:* `case 1 ... 8:`
*   *Standard C Equivalent:* Stacking individual labels:
    `case 1: case 2: case 3: case 4: case 5: case 6: case 7: case 8:`

*If you need to handle multiple distinct intervals, an `else if` chain should be used instead.*

---

## 7. Unconditional Jumps
Jump statements interrupt sequential execution and continue running at another designated point. Jumps destroy local automatic variables if the jump target lies outside their scope.

C has four unconditional jump statements:
1.  **`break;`**: Exits the innermost enclosing loop or `switch` block.
2.  **`continue;`**: Skips the remaining statements in the current iteration of a loop and moves directly to the loop condition evaluation (or the update step in a `for` loop).
3.  **`return [expression];`**: Terminates the current function and returns the value of the expression to the caller.
4.  **`goto label_name;`**: Transposes execution to the line starting with `label_name:` in the same function.

```c
void calculate(int a) {
    if (a < 1 || a > 5)
        goto here; // Jump to label
    printf("a between 1 and 5!\n");
    return;
    
    here: // Label target
    printf("a is out of range!\n");
    return;
}
```
> [!CAUTION]
> Excessive use of `goto` makes code tangled and hard to read, creating **"Spaghetti Code"**. Avoid using `goto` unless it provides a clear benefit, such as a clean exit from deep, multi-level nested loops. Any program written with `goto` can be restructured to run without it.

---

## 8. Typedef Statements
The `typedef` statement is used to define shorter or more descriptive aliases (synonyms) for existing types.

*   **Syntax**: Except for the `typedef` keyword, the syntax is identical to declaring an object of that type.
```c
typedef unsigned int UINT;                  // UINT is an alias for unsigned int
typedef enum state { DEAD, ALIVE } State;   // State is an alias for the enum

UINT ui = 10;
State s = DEAD;
```

---

## 9. Textbook References
*   **Scope & Context**: Section 5.13
*   **Iteration & Jumps**: Sections 3.4–3.10, 4.1–4.8, 15.9
*   **Type Alias**: Section 10.6
