---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 05 Type Conversions

## 1. Overview of Type Conversions
In C, operands of different types can be combined in a single operation. When types are mismatched, the compiler automatically attempts to convert them to a uniform type before performing the operation.

```c
double dVar = 2.5; 
dVar = dVar * 3;          // 3 (int) is implicitly converted to double
if (dVar < 10L) { ... }   // 10L (long) is implicitly converted to double
```

---

## 2. Implicit vs. Explicit Conversions

### Implicit Conversions
The compiler provides automatic conversions in three scenarios:
1.  When operands in an expression have mismatched types.
2.  When a function argument’s type does not match the parameter type in the function's prototype.
3.  During variable initializations or assignments.

If a necessary conversion is impossible, the compiler issues an **error message**. In cases of potential data loss, it may issue a **warning message**.

### Explicit Conversions (Casts)
You can force a value to convert to another type using the unary cast operator:

$$\text{(type\_name) expression}$$

```c
int sum = 10, count = 3;
double mean = (double) sum / count; // Output: 3.3333
```
*   *How it works*: `sum` is explicitly cast to `double`. The compiler then implicitly promotes the divisor `count` to `double` before executing the division.
*   *Best Practice*: Always use explicit casts when there is a risk of losing information. This makes the conversion intentional and suppresses compiler warnings.

---

## 3. Hierarchy of Types (Conversion Rank)
Implicit conversions are governed by the type's **conversion rank**.

### Integer Ranks
*   Every unsigned integer type has a different conversion rank.
*   A wider integer type has a higher rank than a narrower one.
*   Each signed type has the same rank as its corresponding unsigned type.
*   Standard integer ranks (lowest to highest):
    $$\text{\_Bool} < \text{char} < \text{short} < \text{int} < \text{long} < \text{long long}$$
*   **Enumerations (`enum`)** have the same rank as `int`.

### Floating-Point Ranks
*   Rank order (lowest to highest):
    $$\text{float} < \text{double} < \text{long double}$$
*   **Real vs. Integer**: The lowest-ranked floating-point type (`float`) has a **higher rank than any integer type**.

---

## 4. Integer Promotion
To optimize execution, CPU arithmetic operations are performed on at least **4 bytes (32 bits)**.
*   Any value whose type ranks lower than `int` (such as `char`, `_Bool`, `short`) can be used where an `int` or `unsigned int` is expected.
*   The compiler automatically applies **integer promotion**:
    *   The lower-ranked operand is promoted to `int` if `int` is capable of representing all values of its original type.
    *   If `int` is not sufficient, it is promoted to `unsigned int`.

### Preventing Overflow Example
```c
#include <stdio.h> 

int main() {
    char a = 30, b = 40, c = 10;
    char d = (a * b) / c;
    printf("%d ", d); // Outputs: 120
    return 0;
}
```
> [!NOTE]
> Signed `char` can only hold values from $-128$ to $127$. The multiplication $30 \times 40 = 1200$ would overflow a `char`. 
> However, because `a` and `b` are promoted to `int` before multiplication, the calculation succeeds without overflow. The result (`120`) is then safely cast back and assigned to the `char d`.

---

## 5. Usual Arithmetic Conversions
Usual arithmetic conversions are implicit conversions automatically applied to operands of different arithmetic types for most binary operators:
*   **Arithmetic operators with two operands:** `*`, `/`, `%`, `+`, `-`
*   **Relational and equality operators:** `<`, `<=`, `>`, `>=`, `==`, `!=`

### Rules of Application

#### 1. Floating-Point Rule
If either operand has a floating-point type, the operand with the lower conversion rank is converted to the type of the higher-rank operand. Real types are only converted to real types.

#### 2. Integer Rules
If both operands are integers, **integer promotion** is first performed on both. If their types still differ, the following rules apply:
*   **Rule 1 (Unsigned Dominance)**: If one operand has an `unsigned` type $T$ whose conversion rank is at least as high as that of the other operand's type, the other operand is converted to `unsigned T`.
*   **Rule 2 (Signed Dominance / Fallback)**: If the operand with the higher rank has a `signed` type $T$, the other operand is converted to `signed T` *only if* `signed T` can represent all values of the other operand's type.
    *   If `signed T` *cannot* represent all values, both operands are converted to the unsigned type corresponding to `signed T` (`unsigned T`).

---

## 6. Tracing Scenarios (Usual Arithmetic Conversions)

```c
int x = 0;
int i = -1; 
unsigned int limit = 200U; 
long n = 30L; 

if ( i < limit ) 
    x = limit * n;

printf("%d\n", x); // Outputs: 0
```

### Trace 1: `i < limit` (Governed by Rule 1)
1.  `i` is a signed `int` (value `-1`). `limit` is an `unsigned int` (value `200`).
2.  Both types have the same rank. Since `limit` is unsigned, **Rule 1** applies.
3.  The signed `int i` (`-1`) is converted to `unsigned int`.
4.  In 32-bit two's complement, `-1` is represented as `11111111 11111111 11111111 11111111`. Interpreted as unsigned, this represents `4,294,967,295`.
5.  The comparison becomes: `4,294,967,295 < 200`, which is **false**.
6.  The body of the `if` is skipped, and `x` remains `0`.

### Trace 2: `limit * n` (Governed by Rule 2)
1.  `limit` is `unsigned int` (32-bit). `n` is `long` (32-bit on 32-bit compilers).
2.  `long` (signed) has a higher rank than `unsigned int`.
3.  We test if signed `long` can represent the entire range of `unsigned int` ($0$ to $4,294,967,295$).
    *   A 32-bit signed `long` only goes up to $2,147,483,647$.
4.  Since it cannot represent all values of `unsigned int`, **Rule 2** dictates that *both* operands are converted to **`unsigned long`** (the unsigned equivalent of `long`).

---

## 7. Specific Conversion Behaviors

### Conversions to Unsigned Integer Types
*   If the value is within the range of the target unsigned type ($0$ to $U_{\text{type\_MAX}}$), the value is preserved.
*   If the value lies outside the range, the target type's modulo arithmetic is applied: $(U_{\text{type\_MAX}} + 1)$ is added or subtracted repeatedly until the value fits.
    *   *Example:*
        ```c
        unsigned short n = 1000;
        n = -1; // -1 is outside the range [0, USHRT_MAX]
        ```
        $$-1 + (\text{USHRT\_MAX} + 1) = \text{USHRT\_MAX}$$
        Thus, `n` is assigned the value `USHRT_MAX` (e.g., `65535`).

### Conversions between Float and Integer
*   **Floating-point to Integer**: The fractional part is discarded (truncated).
    *   If the remaining integer value exceeds the range of the target integer type, the behavior is **undefined**.
    *   *Example:*
        ```c
        double x = 2.9;
        unsigned long n = x; // n is assigned 2 (fractional part lost)
        ```
*   **Integer to Floating-point**: If the integer value cannot be represented exactly in the floating-point type's precision (e.g., converting a large `long` to `float` which has only 6 digits of precision), the value is rounded to the next lower or next higher representable value.
    *   *Example:*
        ```c
        float r_var = 16777217;
        double l_var = 16777217;
        // rounding error (l_var - r_var) is 1.00
        // r_var is 16777216.00
        ```

### Conversions between Floating-Point Types
*   **Lower to Higher Precision** (e.g., `float` $\rightarrow$ `double`): The value is exactly preserved.
*   **Higher to Lower Precision** (e.g., `double` $\rightarrow$ `float`):
    *   If the value exceeds the target range, the result is **undefined**.
    *   If the value is within range but cannot be represented exactly, it is rounded to the next smaller or next larger representable value.

---

## 8. Assignments & Functions Tracing
The compiler performs implicit conversion in assignments, function calls, and returns:

```c
#include <math.h> // Declares: double sqrt( double ); 

int i = 7; 
float x = 0.5f; 

i = x;          // x (0.5) is converted from float to int -> i becomes 0 (truncated)
x += 2.5;       // x is promoted to double for addition with 2.5 (double). 
                // The sum (2.5) is converted to float to be assigned back to x.

x = sqrt(i);    // i (0) is converted from int to double as argument. 
                // sqrt returns double, which is converted to float for assignment to x.

long my_func() { 
    return 0;   // The integer constant 0 is implicitly converted to long
} 
```

---

## 9. References
*   **Textbook**: Nothing directly covered in the textbook.
*   **W3Schools C Type Conversion**: [W3Schools](https://www.w3schools.com/c/c_type_conversion.php)
*   **Guru99 C Type Casting**: [Guru99](https://www.guru99.com/c-type-casting.html)
*   **O'Reilly C in a Nutshell Chapter 4**: [C in a Nutshell](https://www.oreilly.com/library/view/c-in-a/0596006977/ch04.html)
