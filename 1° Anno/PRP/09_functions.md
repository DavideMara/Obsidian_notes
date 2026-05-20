---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 09 Functions

## 1. Introduction to Functions
In C, all program instructions must be contained within functions. 
*   **Procedural Paradigm**: Each function is designed to perform a specific task.
*   **The `main()` Function**: This is a special function. It is the program's entry point; the first command executed is the first command in `main()`. Execution proceeds sequentially from top to bottom.
*   **Subroutines**: All other functions serve as subroutines to `main()`. They can have any valid identifier name.
*   Every function must be defined exactly once. However, a program can declare and call a function as many times as necessary.

---

## 2. Function Definition
A function definition provides the actual code that the function will execute. It consists of two parts:

1.  **Function Head (Declarator)**: Specifies the function's name, return type, and the types/names of its parameters.
2.  **Function Block**: A compound statement enclosed in `{}` that specifies what the function does.

$$\text{type function\_name (type parameter\_name1, type parameter\_name2, ...) \{ // statements \}}$$

---

## 3. Function Declaration (Prototype)
Before a function can be called, the compiler needs to know its interface. This is provided by the **function declaration** (or prototype).
*   It defines the function's return type and the number and types of its parameters.
*   **Parameter Names**: Identifiers in a prototype are optional. If included, they have *function prototype scope*, meaning they are ignored by the compiler outside the prototype and serve only as documentation/comments.

*   *Examples of Valid Declarations*:
    ```c
    int sum(int a, int b); // With parameter names
    int sum(int, int);     // Without parameter names
    ```

> [!IMPORTANT]
> If a function is defined *before* it is called in the same file, the definition acts as its declaration. Otherwise, you must explicitly declare the prototype at the top of the file before calling it. You cannot have two definitions of a function with the same identifier in the same file.

---

## 4. Returning Values
The return type must always be specified. (In older C standards, if omitted, it defaulted to `int`).

*   **The `return` Statement**: An unconditional jump that ends the execution of the current function, passing control and an evaluated expression back to the caller.
    $$\text{return [expression];}$$
*   The returned expression is converted to the function's specified return type if necessary.
*   A function can contain multiple `return` statements; the first one executed exits the function.
*   **Void Functions**: If the return type is `void`, the function returns no value. You can use `return;` with no expression to exit early, or omit it entirely.
*   **Falling off the end**: If execution reaches the closing brace `}` of a non-void function without encountering a `return` statement, the value returned to the caller is **undefined**. Always use a return statement for non-void functions.

---

## 5. Scope & Variable Allocation
*   **Block Scope**: Identifiers declared within a block (like function bodies) are visible only from their declaration to the end of the block.
    *   *Note*: Since C11, variable declarations do not have to be placed at the very top of a function block.
*   **Parameter Scope**: The parameter names in a function *definition* have block scope and act as local variables within the function body.

### Memory Allocation & Deallocation
*   **Memory Allocation**: Reserving a segment of memory for a variable.
*   **Automatic Variables**: Local variables (and parameters) are allocated automatically when the program flow enters their scope, and are deallocated automatically when the flow exits the scope.

---

## 6. Parameters & Arguments
*   **Actual Parameters (Arguments)**: The expressions/values passed in the function call.
*   **Formal Parameters**: The variables defined in the function head that receive the values.
*   **Pass by Value**: When a function is called, C allocates storage space for the formal parameters and copies the evaluated values of the actual parameters into them. Modifying the formal parameter inside the function does *not* affect the actual parameter in the caller.

---

## 7. The `main()` Function
The `main()` function communicates directly with the host environment (e.g., the OS shell). 
It can be defined in two ways:
1.  `int main(void)`
2.  `int main(int argc, char *argv[])`

### Return Value
*   `main()` returns an `int` passed to the parent process.
*   A return value of `0` generally indicates a **normal exit**.
*   A non-zero return value signals an **abnormal termination**.

### Command-Line Arguments
*   **`argc` (Argument Count)**: Represents the number of string tokens passed from the command line. It includes the program's invocation name itself.
*   **`argv` (Argument Vector)**: An array of pointers to `char` (strings) containing the command-line tokens.
    *   `argv[0]`: The name used to invoke the program.
    *   `argv[1]` to `argv[argc - 1]`: The actual arguments provided by the user.
    *   `argv[argc]`: Guaranteed to be a **null pointer**.

*   *Example Trace*:
    ```bash
    $ ./args one two "and three"
    ```
    *   `argc` = 4
    *   `argv[0]` = `"./args"`
    *   `argv[1]` = `"one"`
    *   `argv[2]` = `"two"`
    *   `argv[3]` = `"and three"`
    *   `argv[4]` = `NULL`

---

## 8. Function Overloading (Not Supported in C)
**Function overloading** is the ability to define multiple functions with the exact same name but different signatures (different number or types of parameters).
*   This is a common feature in Object-Oriented Languages like C++ and Java.
*   **C does NOT support function overloading.** Defining `int min(int x, int y)` and `float min(float x, float y)` in the same C program will result in a compiler error (`conflicting types for 'min'`).

---

## 9. Textbook References
*   **Sections 5.1–5.6**
*   **Section 15.3**
*   **Section 7.4**
