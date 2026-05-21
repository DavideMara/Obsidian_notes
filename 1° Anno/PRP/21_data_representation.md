---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 21 Data Representation & Computer Arithmetic (C Context)

This note serves as a general guide and cheatsheet for numerical base conversions, integer representations (Sign-Magnitude and Two's Complement), endianness, representability ranges, binary arithmetic, and floating-point systems in the C language.

---

## 1. Numeral Systems & C Literals

### C Integer Literal Prefixes
In C, the base of an integer literal is determined by its prefix:
*   **Decimal (Base 10)**: No prefix (e.g., `156`). Uses digits `0-9`.
*   **Octal (Base 8)**: Prefix `0` (e.g., `0234`). Uses digits `0-7`.
*   **Hexadecimal (Base 16)**: Prefix `0x` or `0X` (e.g., `0x9C`). Uses digits `0-9` and `A-F` (case-insensitive).
*   **Binary (Base 2)**: Prefix `0b` or `0B` (C23 standard, common compiler extension). Uses `0-1`.

> [!CAUTION]
> **Octal Literal Trap:** Any integer literal starting with a leading `0` is interpreted as octal. Therefore, literals like `0128` or `079` are **invalid** and cause compile-time syntax errors because `8` and `9` are not valid octal digits.

---

### Conversion Methods

#### 1. Decimal to Base $B$ (Repeated Division)
Divide the decimal integer by $B$ repeatedly, recording the remainders from bottom to top (Least Significant Digit to Most Significant Digit).
*   *Example: Convert $156_{10}$ to Hexadecimal (Base 16):*
    *   $156 \div 16 = 9$ remainder **`12`** (`C`)
    *   $9 \div 16 = 0$ remainder **`9`**
    *   **Result:** `0x9C`
*   *Example: Convert $156_{10}$ to Octal (Base 8):*
    *   $156 \div 8 = 19$ remainder **`4`**
    *   $19 \div 8 = 2$ remainder **`3`**
    *   $2 \div 8 = 0$ remainder **`2`**
    *   **Result:** `0234`

#### 2. Base $B$ to Decimal (Positional Sum)
Sum the digits multiplied by their positional weight $B^i$:
$$\text{Value} = \sum d_i \times B^i$$
*   *Example: Convert hex literal `0x2F3` to decimal:*
    *   $d_2 = 2$, $d_1 = 15$, $d_0 = 3$
    *   $\text{Value} = (2 \times 16^2) + (15 \times 16^1) + (3 \times 16^0) = 512 + 240 + 3 = 755_{10}$

#### 3. Power-of-2 Shortcuts (Binary $\leftrightarrow$ Hex / Octal)
Group bits starting from the right (pad with leading zeros if necessary):
*   **Binary to Hexadecimal**: Group in chunks of **4 bits** ($16 = 2^4$).
    *   `0b11010111` $\rightarrow$ `1101 0111` $\rightarrow$ `D` `7` $\rightarrow$ `0xD7`
*   **Binary to Octal**: Group in chunks of **3 bits** ($8 = 2^3$).
    *   `0b11010111` $\rightarrow$ `011 010 111` $\rightarrow$ `3` `2` `7` $\rightarrow$ `0327`

---

## 2. Sign-Magnitude Representation (Modulo e Segno)
A signed representation where the sign and the value are strictly separated.

### Layout for $N$ Bits
*   **Most Significant Bit (MSB)**: Sign bit (`0` = positive, `1` = negative).
*   **Remaining $N-1$ bits**: Magnitude (absolute value in standard binary).

```
MSB (Sign)                    Magnitude
[ 0 / 1 ]  [ b_{N-2} ] ... [ b_1 ] [ b_0 ]
```

### Key Operations & Rules
*   **Negation ($-x$):** Flip/toggle only the sign bit (MSB).
*   **Representable Range:** $[-(2^{N-1} - 1), \ +(2^{N-1} - 1)]$
    *   For 8 bits ($N=8$): $[-127, \ 127]$
*   **Zero Representation:** Double zero exists: $+0$ (`0000 0000`) and $-0$ (`1000 0000`).

*   *Example (8-bit):*
    *   $+42_{10} \rightarrow$ Sign `0`, Magnitude $42$ (`0101010`) $\rightarrow$ `0010 1010`
    *   $-42_{10} \rightarrow$ Sign `1`, Magnitude $42$ (`0101010`) $\rightarrow$ `1010 1010`
    *   Negation of `1010 1010` ($-42$) is `0010 1010` ($+42$).

---

## 3. Two's Complement Representation (Complemento a Due)
The standard signed integer representation in modern systems (mandated in C23).

### Layout & Concept
The MSB has a negative weight:
$$\text{Value} = -d_{N-1} 2^{N-1} + \sum_{i=0}^{N-2} d_i 2^i$$

### Key Operations & Rules
*   **Representable Range:** $[-2^{N-1}, \ +(2^{N-1} - 1)]$
    *   For 8 bits ($N=8$): $[-128, \ 127]$
*   **Zero Representation:** Single zero: `0000 0000`.
*   **Negation ($-x$):** Flip all bits (One's Complement) and add $1$.
    *   *Example: Negate $+42_{10}$ (`0010 1010`):*
        1.  Invert bits: `1101 0101`
        2.  Add 1: `1101 0110` (represents $-42_{10}$)

> [!WARNING]
> **Negation Limit:** The minimum negative value (e.g., `1000 0000` = $-128$ in 8-bit) cannot be negated because its positive counterpart ($+128$) is out of range. Applying the inversion rule wraps it back to itself.

### Decoding Binary to Decimal

#### Method A: Direct Weight Expansion (Fastest)
Add the positional weights directly, treating the MSB weight as negative:
*   *Example: Convert `1101 0110` to decimal:*
    $$\text{Value} = -2^7 + 2^6 + 2^4 + 2^2 + 2^1 = -128 + 64 + 16 + 4 + 2 = -42_{10}$$

#### Method B: Negate-and-Convert
If the MSB is `1` (negative):
1.  Apply the negation rule (invert bits, add 1) to find its positive magnitude.
2.  Convert that magnitude to decimal.
3.  Prepend a minus sign.

---

## 4. Endianness (Byte-Level vs. Bit-Level)

### Byte-Level Endianness
Defines the storage order of multi-byte variables in memory addresses:
*   **Big-Endian**: Most Significant Byte (MSB) stored at the lowest address.
*   **Little-Endian**: Least Significant Byte (LSB) stored at the lowest address.

*   *Visual Example:* Storing `0x12345678` (4 bytes: `12`, `34`, `56`, `78`) at address `0x1000`:

| Address | Big-Endian Byte | Little-Endian Byte |
| :--- | :--- | :--- |
| `0x1000` | `0x12` (MSB) | `0x78` (LSB) |
| `0x1001` | `0x34` | `0x56` |
| `0x1002` | `0x56` | `0x34` |
| `0x1003` | `0x78` (LSB) | `0x12` (MSB) |

---

### Bit-Level Endianness (Bit Reversal)
In some networking protocols, serial hardware, or academic exercises, "Little Endian" is used to describe reversing the **entire bit sequence** of a word.
*   **Big Endian (Standard/MSB first)**: Bit order is $b_{N-1} \dots b_0$ (read left-to-right).
*   **Little Endian (Bit-Reversed/LSB first)**: Bit order is $b_0 \dots b_{N-1}$ (read right-to-left).

*   *Example: Write $-10_{10}$ in 6-bit two's complement in both formats:*
    1.  $+10_{10} = 001010_2$
    2.  Negate: Invert $\rightarrow$ `110101` $\xrightarrow{+1}$ `110110`
    3.  **Big-Endian (Standard)**: `110110` (MSB leftmost)
    4.  **Little-Endian (Bit-Reversed)**: `011011` (LSB leftmost)

---

## 5. Summary of Representability Ranges
To find the representable limits for a word size of $N$ bits:

| System | Minimum Value | Maximum Value | Example (8-bit) |
| :--- | :--- | :--- | :--- |
| **Unsigned** | $0$ | $2^N - 1$ | $0$ to $255$ |
| **Sign-Magnitude** | $-(2^{N-1} - 1)$ | $+(2^{N-1} - 1)$ | $-127$ to $+127$ |
| **Two's Complement** | $-2^{N-1}$ | $+(2^{N-1} - 1)$ | $-128$ to $+127$ |

---

## 6. Binary Arithmetic & Signed Overflow

### Addition Rules
Addition is done column-by-column, carrying over values:
*   $0 + 0 = 0$
*   $0 + 1 = 1$
*   $1 + 1 = 0 \text{ (carry 1)}$
*   $1 + 1 + 1 = 1 \text{ (carry 1)}$

### Subtraction Rule
In C, subtraction `A - B` is executed at hardware level as addition of the negation: `A + (-B)`. Discard any carry-out bit beyond the word size in Two's Complement.

---

### Signed Overflow Detection
Signed overflow occurs when the mathematical result of an operation exceeds the range limits of the representation. 

*   **Logic Rule:** If you add two numbers of the **same sign** and get a result with the **opposite sign**, an overflow occurred.
    *   $\text{Positive} + \text{Positive} = \text{Negative}$ $\rightarrow$ **Overflow**
    *   $\text{Negative} + \text{Negative} = \text{Positive}$ $\rightarrow$ **Overflow**
*   **Hardware Rule:** Overflow occurs if the **carry-in** to the MSB is different from the **carry-out** of the MSB.

#### Walkthrough: Overflow vs. Normal Addition (8-bit Signed)

*   **Case A (Normal - No Overflow):** `45 + 12`
    ```
      0010 1101 (45)
    + 0000 1100 (12)
    -----------
      0011 1001 (57) -> Both inputs positive, result positive. Correct.
    ```

*   **Case B (Positive Overflow):** `120 + 10`
    ```
      0111 1000 (120)
    + 0000 1010 (10)
    -----------
      1000 0010 (-126 in Two's Complement)
    ```
    *   *Analysis:* Added two positive numbers, got a negative result (MSB is `1`). The true value ($130$) exceeds the max limit $+127$.

*   **Case C (Negative Overflow):** `-100 + (-40)`
    *   $-100 = 10011100_2$, \ $-40 = 11011000_2$
    ```
      1001 1100 (-100)
    + 1101 1000 (-40)
    -----------
    1 0111 0100 (+116 in Two's Complement)
    ```
    *   *Analysis:* Discarding the carry-out, the 8-bit result is positive (MSB is `0`). Added two negative numbers, got a positive result. The true value ($-140$) is below the min limit $-128$.

---

## 7. Floating-Point Representations

### IEEE 754 Standard Formats
Real numbers are formatted in scientific notation:
$$\text{Value} = (-1)^{\text{Sign}} \times (1.\text{Fraction}) \times 2^{\text{Exponent} - \text{Bias}}$$

*   **Single Precision (32-bit)**: 1 sign bit, 8 exponent bits, 23 fraction bits. $\text{Bias} = 127$.
*   **Double Precision (64-bit)**: 1 sign bit, 11 exponent bits, 52 fraction bits. $\text{Bias} = 1023$.

---

### Hexadecimal Floating-Point Literals (C99)
C99 allows exact binary float specification:
*   **Syntax:** `0x` + hex significand + `p`/`P` + base-2 exponent in decimal.
*   *Example:* `0x1.8p2` $\rightarrow (1 + 8/16) \times 2^2 = 1.5 \times 4 = 6.0_{10}$
*   *Example:* `0x1.0p-1` $\rightarrow 1.0 \times 2^{-1} = 0.5_{10}$

---

### Recipe for Decoding Custom / Simplified Floating-Point Formats
In academic exercises, you may encounter simplified floating-point formats. They are typically calculated using:
$$\text{Value} = (-1)^s \times c \times 2^q$$
Where $s$ is the sign bit, $c$ is the mantissa, and $q$ is the exponent.

To decode these formats, follow this checklist:

#### Step 1: Identify Field Boundaries
Read the formatting instructions to identify the size and position of:
*   Sign bit ($s$)
*   Exponent bits ($q$)
*   Mantissa bits ($c$)

#### Step 2: Handle Endianness (Bit Reversal)
If the format specifications state that a field is **Little Endian** at the bit level, **reverse the bit sequence** of that field before decoding it.
*   *Example:* If exponent bits are `1000` and specified as Little Endian, reverse them to `0001`.

#### Step 3: Decode Fields Based on their Encoding
Translate the exponent ($q$) and mantissa ($c$) based on their encoding system (e.g., Two's Complement, Sign-Magnitude, or Biased Exponent).
*   *Example:* If `0001` is encoded in Sign-Magnitude: MSB is `0` (positive), magnitude is `001` ($1$), so value is $+1$.
*   *Example:* If `1001` is encoded in Sign-Magnitude: MSB is `1` (negative), magnitude is `001` ($1$), so value is $-1$.

#### Step 4: Calculate the Decimal Value
Plug the decoded values into the formula $(-1)^s \times c \times 2^q$.
*   *Example:* If $s=1$, $c=12$, $q=1$:
    $$\text{Value} = (-1)^1 \times 12 \times 2^1 = -24$$
