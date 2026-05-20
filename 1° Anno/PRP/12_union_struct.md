---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 12 Structures and Unions

## 1. Structures (`struct`)
While arrays group data items of the same type, **structures** are user-defined data types that allow you to combine data items of *different* kinds into a single record.
*   For instance, a `Book` record might combine a string `Title`, a string `Author`, and an integer `Book ID`.

### Definition & Syntax
To define a structure, use the `struct` keyword. This creates a new data type.
$$\text{struct [tag\_name] \{ member\_declaration\_list \};}$$
```c
struct Song {
    char title[64];
    char artist[32];
    char composer[32];
    short duration;
    struct Date published;
};
```
*   **Name Spaces**: Structure tags (like `Song`) exist in a distinct namespace, meaning the compiler distinguishes them from variables or functions with the exact same name. Additionally, the member names of each structure form a separate namespace.
*   **Members**: Structure members can be of any complete type, including previously defined structures. They cannot be variable-length arrays.

### Self-Referential Structures
A structure type **cannot** contain an instance of itself as a member (because its definition is incomplete until the closing brace). However, it **can contain a pointer** to its own type. This is commonly used in implementing linked lists:
```c
struct Cell {
    struct Song song;       // Data
    struct Cell *pNext;     // Pointer to the next record (self-referential)
};
```

---

## 2. Structure Objects and `typedef`
Once a structure is defined, you can declare objects of that type.
*   **Direct Declaration**: You must include the `struct` keyword:
    `struct Song song1, song2, *pSong = &song1;`
*   **Using `typedef`**: You can define a one-word alias for the structure type to avoid typing `struct` repeatedly:
    ```c
    typedef struct Song Song_t;
    Song_t song1, song2; // 'Song_t' is synonymous with 'struct Song'
    ```
    *Combined definition and typedef:*
    ```c
    typedef struct S {
        int x;
    } T;
    ```

---

## 3. Operations on Structures

### Accessing Members
There are two operators used to access the fields of a structure. Both have the highest precedence (Level 1) and evaluate left-to-right.
1.  **Dot Operator (`.`)**: Used when working directly with a structure object.
    `song1.duration = 180;`
2.  **Arrow Operator (`->`)**: Used when working with a **pointer** to a structure object. It is a syntactical shortcut.
    `pSong->duration = 180;` is exactly equivalent to `(*pSong).duration = 180;`

### Copying Structures
You can use the assignment operator `=` to copy the entire contents of a structure object to another object of the same type:
```c
struct Books book1, book2;
book2 = book1; // All member values of book1 are copied into book2
```

### Initializing Structures
Structures are initialized using an **initialization list** (comma-separated list of initial values in braces).
*   **Sequential Initialization**: Values associate with members in the order of declaration.
    ```c
    struct Song mySong = { "What It Is", "Aubrey Haynie", "Mark Knopfler", 297, { 26, 9, 2000 } };
    ```
*   **Specific Member Initialization (Designated Initializers)**: You can explicitly target members using a dot `.member` prefix.
    ```c
    Song_t aSong = { .title = "I've Just Seen a Face", .composer = "John Lennon", 127 };
    ```
    *(Note: The `127` automatically initializes the field immediately following `composer`, which is `duration`).*

### Arrays of Structs & Size
*   **Array of Structs**: Handled just like standard arrays: `struct Song library[100];`
*   **Memory Size**: You can evaluate the byte size of a structure object using `sizeof(songVar)`.

---

## 4. Unions (`union`)
A **union** is formally defined similarly to a structure, but it behaves completely differently in memory.
*   While structure members each have their own distinct memory location, **all members of a union share the exact same memory location**.
*   All members start at the same base address.
*   Because they overlap, a union can define many members, but **only one member can contain a valid value at any given time**.

### Definition & Size
$$\text{union [tag\_name] \{ member\_declaration\_list \};}$$
```c
union Data { 
    int i; 
    double x; 
    char str[16]; 
};
```
*   **Size Allocation**: A union is only as big as its **largest member**. In the `Data` example above, `sizeof(union Data)` yields `16` bytes (the size of `char str[16]`).

### Initializing Unions
Like structures, unions use an initialization list. However, **the list can contain only ONE initializer**.
*   By default, a non-designated initializer is associated with the **first member** of the union.
*   You can use designated initializers to initialize a different member:
    ```c
    union Data var1 = { 77 };             // Initializes the integer 'i'
    union Data var2 = { .str = "Mary" };  // Initializes the string 'str'
    ```

### Overwriting Behavior (Data Corruption)
Because members share memory, assigning a value to one member permanently overwrites any value previously assigned to a different member.
```c
union Data data;
data.i = 10;
data.f = 220.5;                          // Overwrites 'i'
strcpy(data.str, "C Programming");       // Overwrites 'f'

printf("data.i : %d\n", data.i);         // Prints garbage (e.g., 1917853763)
printf("data.f : %f\n", data.f);         // Prints garbage (e.g., 41223605...0)
printf("data.str : %s\n", data.str);     // Prints "C Programming"
```

---

## 5. Textbook References
*   **Sections**: 10.1 - 10.8
