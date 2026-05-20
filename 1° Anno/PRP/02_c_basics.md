---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 02 C Basics

## 1. Comments in C
Comments are used to make programs readable by humans (ourselves now, team members, and future maintainers). They are ignored by the compiler.

### Types of Comments
*   **Block Comments**: Begin with `/*` and end with `*/`.
    *   Can span multiple lines.
    *   Can be placed within a line of code:
        `int x = 4; /* comment */ int y = 10;`
    *   **Nesting block comments is not allowed.** The first `*/` encountered will close the comment block, causing compilation errors for subsequent characters.
*   **Line Comments**: Begin with `//` and end at the next newline character.

### Rules & Pitfalls
*   **Comments inside literals:** Characters `/*` and `//` inside character constants or string literals do not start a comment.
    *   *Example:* `printf("Comments in C begin with /* or //.\n");` contains no comments.
*   **Commenting out code:** Block comments can enclose line comments, making them useful for temporarily disabling blocks of code during debugging.
*   **Pretty Comments:** Boxed comments (e.g., using columns of asterisks) look clean but are hard to maintain because editing the text requires manually realigning the borders.
*   **Bad Commenting:**
    *   *Redundant/Byte-wastage:* Comments that state the obvious (e.g., `i = i + 1; // increment i`).
    *   *Clarification comments:* Explaining overly complex code. Striking a balance is key; complex code should be simplified and made *self-documenting* rather than clarified by comments.
    *   *Code removal:* Leaving commented-out "old" code in the codebase confuses the reader. Commented-out code should only exist during local debugging.

---

## 2. Character Sets
C distinguishes between the characters used to write the program and those processed at runtime.

*   **Source Character Set**: The set of characters permitted in C source files.
*   **Execution Character Set**: The set of characters that can be interpreted and printed by the running program.
*   *Note:* In almost all modern implementations, these two sets are identical.

### Basic C Character Set
*   **Latin alphabet letters:** `A-Z` and `a-z`
*   **Decimal digits:** `0-9`
*   **29 Punctuation marks:** `! " # % & ' ( ) * + , - . / : ; < = > ? [ \ ] ^ _ { | } ~`
*   **Whitespace characters:**
    *   `' '` Space
    *   `'\t'` Horizontal tab
    *   `'\v'` Vertical tab
    *   `'\n'` Newline
    *   `'\f'` Form feed

---

## 3. Identifiers
An **identifier** is a user-defined name given to variables, functions, macros, structures, and other objects.

### Naming Rules
1.  Must only consist of **letters** (`a-z`, `A-Z`), **digits** (`0-9`), and the **underscore** (`_`).
2.  Must **not start with a digit**.
3.  Are **case-sensitive** (e.g., `while` is a keyword, but `While` is a valid identifier).
4.  Must not match any of C's reserved keywords.
5.  Standard library names (e.g., `printf`) should not be redefined as user functions or global variables.
6.  There is no limit on identifier length, but compilers typically only consider the first **31** (for external/linkage) or **63** (for internal/local) characters as significant.

### Reserved Keywords
There are currently **44 reserved keywords** in C (up from 32 in C89) that cannot be used as identifiers:

| C89 Keywords (32) | | | |
| :--- | :--- | :--- | :--- |
| `auto` | `extern` | `short` | `void` |
| `break` | `float` | `signed` | `volatile` |
| `case` | `for` | `sizeof` | `while` |
| `char` | `goto` | `static` | |
| `const` | `if` | `struct` | |
| `continue` | `int` | `switch` | |
| `default` | `long` | `typedef` | |
| `do` | `register` | `union` | |
| `double` | `return` | `unsigned` | |
| `else` | `enum` | | |

| Modern C Keywords (12 added since C99) | | | |
| :--- | :--- | :--- | :--- |
| `inline` | `_Alignas` | `_Complex` | `_Static_assert` |
| `restrict` | `_Alignof` | `_Generic` | `_Thread_local` |
| `_Atomic` | `_Bool` | `_Imaginary` | `_Noreturn` |

### Examples of Identifiers
*   **Valid:** `x`, `dollar`, `While`, `error_handler`, `scale64`
*   **Invalid:** `1st_rank` (starts with a digit), `switch` (reserved keyword), `y/n` (contains `/`), `x-ray` (contains `-`)

### Best Practices
*   Names should convey identity, behavior, and intended use.
*   Avoid unnecessarily long names or misnaming (e.g., use `weekly_pay = hours_worked * pay_rate;` instead of `a = b * c;`).

### Program Example using Identifiers
```c
#include <stdio.h>

int main() {
    int firstNumber, secondNumber, sumOfTwoNumbers;
    
    printf("Enter two integers: ");
    scanf("%d %d", &firstNumber, &secondNumber);
    
    sumOfTwoNumbers = firstNumber + secondNumber;
    printf("%d + %d = %d", firstNumber, secondNumber, sumOfTwoNumbers);
    
    return 0;
}
```

---

## 4. Scope & Shadowing
**Scope** refers to the textual region of a translation unit in which an identifier is visible and can be referenced.

### Types of Scope
*   **File Scope**: Declarations outside all function bodies and parameter blocks. These identifiers are visible anywhere from their point of declaration to the end of the file.
*   **Block Scope**: Declarations inside a block `{}` or function parameter list. Visible only from their point of declaration to the end of the smallest enclosing block.

### Shadowing (Hiding)
*   **Duplicate identifiers within the same scope are illegal** (e.g., declaring `int a;` and `float a;` in the same block causes a compiler error).
*   An identifier can be redefined in a nested/inner block. The inner declaration **shadows (hides)** the outer declaration, making the outer variable inaccessible within the inner block.

### Shadowing Example 1
```c
int main() {
    {
        int x = 10, y = 20;
        {
            printf("x = %d, y = %d\n", x, y); // Outputs: x = 10, y = 20
            {
                int y = 40; // Shadows outer y
                x++;
                y++;
                printf("x = %d, y = %d\n", x, y); // Outputs: x = 11, y = 41
            }
            printf("x = %d, y = %d\n", x, y); // Outputs: x = 11, y = 20 (outer y is restored)
        }
    }
    return 0;
}
```

### Shadowing Example 2
```c
int main() {
    int x = 1, y = 2, z = 3;
    printf("x = %d, y = %d, z = %d\n", x, y, z); // Outputs: x = 1, y = 2, z = 3
    {
        int x = 10;     // Shadows int x = 1
        float y = 20;   // Shadows int y = 2
        printf("x = %d, y = %f, z = %d\n", x, y, z); // Outputs: x = 10, y = 20.000000, z = 3
        {
            int z = 100; // Shadows int z = 3
            printf("x = %d, y = %f, z = %d\n", x, y, z); // Outputs: x = 10, y = 20.000000, z = 100
        }
    }
    return 0;
}
```

### Out-of-Scope Error Example
```c
int main() {
    {
        int x = 10;
    }
    {
        printf("%d", x); // Compiler Error: x is out of scope here
    }
    return 0;
}
```
*   *Compiler Error:* `error: 'x' undeclared (first use in this function)`

---

## 5. Bindings & Scoping Models
A **binding** is the association between an identifier (name) and the actual memory entity it represents.
*   **Binding Time**: The time at which a binding is created or an implementation decision is made.
*   **Static Binding (Static Scoping)**: The scope of a binding is determined statically at compile time based purely on the program text. **C uses static binding.**
*   **Dynamic Binding (Dynamic Scoping)**: The scope is resolved at run time based on the execution call stack. (e.g., Perl's `local` keyword creates dynamic scope, while `my` creates static scope).

### Perl Code: Static vs. Dynamic Scoping Tracing
```perl
$x = 10;

sub f {
    return $x;
}

sub g {
    local $x = 20; # Dynamically scoped binding
    return f();
}

print g()."\n"; # Output: 20
```
> [!NOTE]
> Under **Static Scoping** (like C), calling `f()` would return `10` because `f` cannot resolve the local `$x` inside `g()`.
> Under **Dynamic Scoping** (using Perl's `local`), calling `f()` returns `20` because it resolves `$x` dynamically from the calling context `g()`.

---

## 6. Scope Tracing Exercise
Analyze the following C program to trace how global variables, local variables, and function parameters shadow each other.

```c
#include <stdio.h>

int f1( void );
int f2( int x, int a );

int a; // Global variable (File Scope)

int main() {
    int a, b, c; // Local variables (Block Scope) shadow global a
    
    a = 7;           // Sets local a = 7
    b = f1();        // Sets global a = 12, returns 17. Prints: "12 "
    c = f2( a, b );  // Calls f2(7, 17). Prints: "17 ". Returns 7 * 17 = 119
    
    printf( "%d %d %d\n", a, b, c ); // Prints local values: "7 17 119"
}

int f1( void ) {
    a = 12;          // Refers to Global a (sets it to 12)
    printf( "%d ", a );
    return ( a + 5 ); // Returns 17
}

int f2( int x, int a ) {
    printf( "%d ", a ); // Refers to parameter a (which is 17)
    return ( x * a );   // Returns 7 * 17 = 119
}
```

### Execution Trace & Outputs
1.  `a = 7` sets local `a` to `7`.
2.  `f1()` sets global `a` to `12`, prints `12 `, and returns `17`. Local `b` in `main` is assigned `17`.
3.  `f2(a, b)` passes local `a` (`7`) and `b` (`17`) as arguments. In `f2`, parameter `a` shadowing `x` prints `17 `, and the function returns `7 * 17 = 119`. Local `c` in `main` is assigned `119`.
4.  `main` prints its local `a` (`7`), `b` (`17`), and `c` (`119`).
*   **Final Combined Output:** `12 17 7 17 119`

---

## 7. Book References
*   **Page 46**
*   **Section 5.13**
*   **Page 346**
