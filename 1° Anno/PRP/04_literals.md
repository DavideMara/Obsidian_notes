---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 04 Literals

## 1. Concept of Literals
A **literal** is a source code token that denotes a fixed value. C supports four primary kinds of literals:
1.  **Integer Constants**
2.  **Floating-Point Constants**
3.  **Character Constants**
4.  **String Literals**

A literal’s specific data type is determined implicitly by its value and its notation (prefixes, suffixes, and formats).

---

## 2. Integer Constants
Integer constants can be expressed in decimal, octal, or hexadecimal systems. The notation used is indicated by the prefix of the constant.

### Notation Types
*   **Decimal Constants**: Begin with a non-zero digit.
    *   *Example:* `512`
*   **Octal Constants (Base 8)**: Begin with a leading zero `0` and use digits `0–7`.
    *   *Example:* `047`
    *   *Conversion:* $$047_8 = (4 \times 8^1) + (7 \times 8^0) = 32 + 7 = 39_{10}$$
*   **Hexadecimal Constants (Base 16)**: Begin with the prefix `0x` or `0X` and use digits `0–9` and `a–f` / `A–F` (case-insensitive).
    *   *Example:* `0xff` (or `0Xff`, `0xFF`, `0XFF`)
    *   *Conversion:* $$0\text{xFF}_{16} = (15 \times 16^1) + (15 \times 16^0) = 240 + 15 = 255_{10}$$

### Type Assignment Rules
By default, the compiler assigns an integer constant the type `int`. If the value is too large to fit in an `int`, the compiler assigns it the first type in the following hierarchy that is large enough to represent it:
$$\text{int} \rightarrow \text{long} \rightarrow \text{long long}$$

*   *Example:* On systems where a `short` is 2 bytes (max: $32,767$), the decimal constant `50000` is implicitly given the type `int` because it exceeds the maximum value of a signed short.

### Explicit Type Suffixes
You can explicitly force the type of an integer constant by appending suffixes (case-insensitive, e.g., `l` or `L`):

| Suffix | Forced Type | Example |
| :--- | :--- | :--- |
| `U` / `u` | `unsigned int` | `512U` |
| `L` / `l` | `long` | `0Xf0fL` |
| `UL` / `ul` | `unsigned long` | `7UL` |
| `LL` / `ll` | `long long` | `0777ll` |
| `ULL` / `ull` | `unsigned long long` | `123uLL` |

```c
int a = 512U;   // unsigned int literal assigned to int
int b = 1LL;    // long long literal assigned to int
int c = 7UL;    // unsigned long literal assigned to int
```

---

## 3. Floating-Point Constants
Floating-point constants represent real numbers and can be written in decimal or hexadecimal formats.

### Decimal Formatting Rules
*   Must contain a decimal point.
*   The decimal point can be the first or last character (e.g., `10.` and `.234` are permissible).
*   **Scientific Notation (E-Notation)**: The value can be multiplied by a power of 10 using the exponent indicator `e` or `E`.
    *   `2.34E5` represents $2.34 \times 10^5$
    *   `67e-12` represents $67.0 \times 10^{-12}$
    *   `.234E6` represents $0.234 \times 10^6$

> [!WARNING]
> A number written without a decimal point or an exponent (e.g., `10`) is treated by the compiler as an **integer constant**, not a floating-point constant.

### Default & Explicit Floating-Point Types
*   **Default Type**: Floating-point constants are treated as **`double`** by default.
*   **Forcing `float`**: Append the suffix `F` or `f` (e.g., `1.23f`).
*   **Forcing `long double`**: Append the suffix `L` or `l` (e.g., `2.5L`).

---

## 4. Character Constants
A character constant consists of a single character enclosed in single quotation marks (e.g., `'a'`, `'0'`, `'*'`).

*   **Standard characters**: `'a'`, `'0'`, `'*'`
*   **Escape characters**: Special sequences are used to represent non-printable characters or characters with syntactic meaning (e.g., `'\''`, `'\\'`, `'\n'`).

> [!IMPORTANT]
> In C, character constants (e.g., `'a'`) have the type **`int`**, not `char`.

### Escape Sequences Table

| Escape Sequence | Character Value | Action on Output Device |
| :--- | :--- | :--- |
| `\'` | Single quotation mark (`'`) | Prints `'` |
| `\"` | Double quotation mark (`"`) | Prints `"` |
| `\?` | Question mark (`?`) | Prints `?` |
| `\\` | Backslash character (`\`) | Prints `\` |
| `\a` | Alert / Bell | Generates an audible beep or visual signal |
| `\b` | Backspace | Moves cursor back one character |
| `\f` | Form Feed | Moves cursor to the next page |
| `\n` | Newline / Line Feed | Moves cursor to the beginning of the next line |
| `\r` | Carriage Return | Moves cursor to the beginning of the current line |

---

## 5. String Literals
A string literal consists of a sequence of characters and escape sequences enclosed in double quotation marks.

*   *Example:* `"Hello world!\n"`
*   String literals can contain any characters from the source character set.

### Representation in Memory
*   A string literal is represented in memory as a **static array of `char`**.
*   It contains the ASCII character codes of the string followed by a terminating **null character (`\0`)** to mark the end of the string.
*   An **empty string literal (`""`)** occupies exactly **1 byte** in memory (holding only the `\0` terminator).

### Code Example
```c
#include <stdio.h>

int main() {
    char helloWorld[128] = "Hello World!\n"; // String stored in char array
    printf("Print the string: %s\n", helloWorld);
    return 0;
}
```

---

## 6. Book References
*   **Section 15.6**
*   **Page 339**
*   **Page 46, Section 9.10**
