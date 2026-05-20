---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 06 Expressions & Operators

## 1. Expressions & Side Effects

### Expressions
An **expression** consists of a sequence of constants (literals), identifiers, and operators that the program evaluates to obtain a value, produce side effects, or both.
*   A single constant, a string literal, or a variable identifier is in itself an expression.

### Side Effects
An expression is said to have a **side effect** if it modifies some state outside its local environment (i.e., it has an observable interaction with the memory or the outside world besides returning a value).

*   *Example (Value only)*:
    ```c
    if (a == 5) { /* ... */ } // Evaluates comparison, returns 0 or 1. No side effects.
    ```
*   *Example (Value + Side Effect)*:
    ```c
    if (a = 5) { /* ... */ }  // Assigns 5 to a (side effect), and evaluates to 5.
                              // WARNING: This is a common logic error when testing conditions.
    ```

### Type of an Expression
Every expression has an associated type determined by the resulting value of its evaluation. If the expression yields no value, its type is `void`.

*   *Examples (assuming `a` is of type `int`)*:

| Expression | Evaluated Type | Notes |
| :--- | :--- | :--- |
| `'\n'` | `int` | Character constants are typed as integers in C |
| `a + 1` | `int` | Standard integer addition |
| `a + 1.0` | `double` | Implicitly promoted via usual arithmetic conversions |
| `a < 77.7` | `int` | Comparative relations evaluate to `0` or `1` (`int`) |
| `"A string literal."`| `char *` | Array of characters decay to a pointer |
| `abort()` | `void` | Function returns no value |
| `sqrt(2.0)` | `double` | Function returns a double precision float |

---

## 2. Lvalues & Rvalues

### Lvalues (Left Values)
An **lvalue** is an expression that designates a specific object in memory. 
*   The simplest example is a variable name.
*   The "l" originally stood for "left" because an lvalue can appear on the **left side of an assignment operator** (but it can also appear on the right).
    $$\text{leftExpression (lvalue)} = \text{rightExpression (rvalue/lvalue)}$$
*   **Modifiable Lvalues**: Lvalues whose values can be changed in memory. Lvalues declared as `const` are **non-modifiable lvalues**. You cannot assign to them after definition.
    ```c
    int a = 1;
    const int b = 2; // b is a non-modifiable lvalue
    b = 20;          // Compiler Error: b is const-qualified
    ```
*   **Constant Initialization**: Const variables must be assigned a value immediately when defined.
    *   *Correct:* `const double pi = 3.14;`
    *   *Incorrect:* `const double pi; pi = 3.14; // Error`

### Rvalues (Right Values)
An **rvalue** represents a value without designating a specific memory object.
*   An rvalue can only appear on the **right side of an assignment operator**.
*   *Examples:* Constants, expressions like `a + 1`, character constants `'c'`.
    *   `7 = a;` or `a + 1 = 8;` are **compilation errors** because `7` and `a + 1` are rvalues.

### Variable Representation in Memory
Variables are modifiable lvalues. They act as named containers of values in memory.

*   *Example:* `int a = 7; int b = 256;` (assuming 4-byte integers on a little-endian system):

```text
Address     Memory Bytes (Reversed bit order representation)
0           [0000 0000]
...
2700 (a)    [1110 0000] [0000 0000] [0000 0000] [0000 0000] (recursively 7)
2704 (b)    [0000 0000] [1000 0000] [0000 0000] [0000 0000] (recursively 256)
```

---

## 3. Operator Precedence & Associativity
When an expression contains multiple operators, their evaluation is resolved using precedence and associativity rules.

*   **Precedence**: Determines which operator groups its operands first (e.g., `*` has higher precedence than `-`).
    *   `a - b * c` is parsed as `a - (b * c)`
    *   Parentheses override precedence: `(a - b) * c`
*   **Associativity**: Determines the grouping order (left-to-right or right-to-left) when consecutive operators share the same precedence.
    *   *Left-to-Right (e.g., division):* `a / b / c` $\rightarrow$ `(a / b) / c`
    *   *Right-to-Left (e.g., assignment):* `a = b = c` $\rightarrow$ `a = (b = c)`

### Precedence & Associativity Table

| Precedence | Operators | Associativity | Description |
| :--- | :--- | :--- | :--- |
| **1** | `[]` `()` `.` `->` `++` `--` `(type){list}` | Left to right | Postfix operators |
| **2** | `++` `--` `!` `~` `+` `-` `*` `&` `sizeof` | Right to left | Unary operators |
| **3** | `(type_name)` | Right to left | Explicit cast operator |
| **4** | `*` `/` `%` | Left to right | Multiplicative operators |
| **5** | `+` `-` | Left to right | Additive operators |
| **6** | `<<` `>>` | Left to right | Shift operators |
| **7** | `<` `<=` `>` `>=` | Left to right | Relational operators |
| **8** | `==` `!=` | Left to right | Equality operators |
| **9** | `&` | Left to right | Bitwise AND |
| **10** | `^` | Left to right | Bitwise XOR |
| **11** | `\|` | Left to right | Bitwise OR |
| **12** | `&&` | Left to right | Logical AND |
| **13** | `\|\|` | Left to right | Logical OR |
| **14** | `?:` | Right to left | Conditional ternary operator |
| **15** | `=` `+=` `-=` `*=` `/=` `%=` `&=` `^=` `\|=` `<<=` `>>=` | Right to left | Assignment operators |
| **16** | `,` | Left to right | Comma operator |

> [!NOTE]
> *   Postfix increment/decrement (`x++`) has higher precedence than prefix (`++x`).
> *   The tokens `+`, `-`, `*`, and `&` have dual meanings (unary vs binary). Unary versions have higher precedence.

---

## 4. Operator Categories

### Arithmetic Operators
*   **Binary**: `*`, `/`, `%`, `+`, `-`
*   **Unary**: `+` (sign), `-` (negation)
*   **Modulo (`%`)** requires **integer operands**.
*   **Integer Division**: Division between two integers truncates the fractional part (returns an integer).
    *   *Example with `short n = -5`*:
        *   `8 / n` $\rightarrow$ Evaluates to `8 / -5 = -1` (after integer promotion).
        *   `8.0 / n` $\rightarrow$ Evaluates to `8.0 / -5.0 = -1.6` (since `8.0` is `double`).
        *   `8.0 % n` $\rightarrow$ **Compiler Error** (modulo requires integers).
*   **Modulo Signs**: The sign of the modulo result matches the **left operand (numerator)**.
    *   `5 % 3 = 2`
    *   `-5 % 3 = -2`

### Assignment Operators
*   **Simple Assignment (`=`)**: Stores the right operand value in the left operand (must be a modifiable lvalue).
*   **Compound Assignment**: `x op= y` (e.g. `x += y`) is equivalent to `x = x op (y)`.
*   An assignment expression evaluates to the value assigned, but the expression itself is **not an lvalue**.
    *   `c = (b = a);` $\rightarrow$ Valid. Assigns `a` to `b`, then assigns the result (`6`) to `c`.
    *   `(c = b) = a;` $\rightarrow$ **Compiler Error**. The expression `c = b` is an rvalue and cannot be assigned to.

### Increment & Decrement Operators
*   **Postfix (`x++` / `x--`)**: Evaluates to the current value of `x`, then increments/decrements `x` as a side effect.
*   **Prefix (`++x` / `--x`)**: Increments/decrements `x` first, then evaluates to the new value.
    *   `int a = 3, b = 4; a = b++;` results in `a = 4` and `b = 5` (two side effects: one on `b`, one on `a`).

### Comparative Operators
*   **Relational**: `<`, `<=`, `>`, `>=`
*   **Equality**: `==`, `!=`
*   Always evaluate to type `int` (returning `1` for true, `0` for false).
*   Equality operators have **lower precedence** than relational operators.
    *   `a < b != b < c` is equivalent to `(a < b) != (b < c)`.

### Logical Operators
*   `&&` (AND), `||` (OR), `!` (NOT).
*   `0` is false; any other value is true. They return `int` (`1` or `0`).
*   **Short-Circuit Evaluation**: Evaluation is guaranteed left-to-right. Evaluation stops as soon as the result is determined.
    *   `&&` evaluates the right operand **only if** the left operand is non-zero (true).
    *   `||` evaluates the right operand **only if** the left operand is zero (false).
    ```c
    int a = 1, b = 0, c;
    c = a || ++b; // a is 1 (true), so ++b is skipped. b remains 0.
    c = b && ++a; // b is 0 (false), so ++a is skipped. a remains 1.
    ```

### Bitwise Operators
*   Used to manipulate individual bits:
    *   `&` (AND), `|` (OR), `^` (XOR), `~` (NOT / one's complement).
    *   *Example:* `a &= 0xFF;` clears all bits in `a` except the lowest 8 bits.
*   **Processor vs. Memory Endianness**:
    *   Values in memory are saved in little-endian.
    *   In the processor, they are translated to big-endian for calculations.
    *   The result is stored back to memory in little-endian.

### Shift Operators
*   `<<` (shift left), `>>` (shift right).
*   `x << y` is equivalent to $x \times 2^y$. `x >> y` is equivalent to $x / 2^y$.
*   Operands must be integers. The right operand (shift count) must **not be negative** and must be **less than the bit width** of the promoted left operand.

---

## 5. Sequence Points
A **sequence point** is a step in execution where it is guaranteed that all side effects of previous evaluations are complete, and no side effects of subsequent evaluations have occurred.

> [!CAUTION]
> **Variable Modification Rule**: You must not modify the same variable more than once between two consecutive sequence points. Doing so results in **undefined behavior**.
> *   *Undefined:* `i = i++;` (two unsequenced modifications of `i`)
> *   *Defined:* `int i = i++;` (permissible because it is an initialization, not an assignment).

### Location of Sequence Points
1.  At the end of a full statement (marked by a semicolon `;`).
2.  After evaluating all function arguments in a call, before entering the function.
3.  At the end of controlling expressions in `if`, `while`, `for`, and `return` statements.
4.  After the evaluation of the first operand of these operators: `&&`, `||`, `?:` (ternary), and `,` (comma).

### Sequence Point Examples
*   `++i < 100 ? f(i++) : (i = 0)` $\rightarrow$ **Permissible**: The ternary operator `?` introduces a sequence point after the condition, separating `++i` from `i++` or `i = 0`.
*   `a++ && a++` $\rightarrow$ **Permissible**: `&&` introduces a sequence point after the first operand.
*   `a++ + b++` $\rightarrow$ **Permissible**: Modifies different variables, so ordering does not cause collision.

---

## 6. Tracing Exercises

```c
#include <stdio.h>

int main() {
    int i = 0;
    int k = i++, j = i++;
    printf("%d %d %d\n", k, j, i); // Outputs: 0 1 2
    
    int l = 0;
    int m = ++l, n = ++l;
    printf("%d %d %d\n", m, n, l); // Outputs: 1 2 2
    
    int q;
    q = ++q; // WARNING: undefined behavior (unsequenced modification)
    printf("%d\n", q);
    
    return 0;
}
```

### Trace 1: `k = i++, j = i++`
1.  The comma operator `,` separates declarations and introduces a sequence point.
2.  `k = i++` assigns `0` (current `i`) to `k`, then increments `i` to `1`.
3.  The sequence point occurs.
4.  `j = i++` assigns `1` (current `i`) to `j`, then increments `i` to `2`.
5.  **Output:** `k = 0, j = 1, i = 2`.

### Trace 2: `m = ++l, n = ++l`
1.  `m = ++l` increments `l` to `1`, then assigns `1` to `m`.
2.  Sequence point occurs.
3.  `n = ++l` increments `l` to `2`, then assigns `2` to `n`.
4.  **Output:** `m = 1, n = 2, l = 2`.

### Trace 3: `q = ++q`
*   No sequence point separates the prefix increment `++q` and the assignment `=`.
*   The compiler issues a warning: `warning: multiple unsequenced modifications to 'q' [-Wunsequenced]`. The result is undefined.

---

## 7. Book & External References
*   **Textbook**: Sections 2.5, 2.6, 3.11, 3.12, 4.9, 4.10, 7.7, 10.9. Appendix A. Pages 77, 87, 135, 243.
*   **MSDN Side Effects**: [Microsoft](https://learn.microsoft.com/it-it/cpp/c-language/side-effects?view=msvc-170)
*   **MSDN Sequence Points**: [Microsoft](https://learn.microsoft.com/it-it/cpp/c-language/c-sequence-points?view=msvc-170)
