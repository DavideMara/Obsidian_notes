---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 16 Linked Lists

## 1. Why Linked Lists?
To understand linked lists, we must first look at the limitations of arrays:
*   **Fixed Size**: Array dimensions must be known in advance (or allocated to a fixed size dynamically).
*   **Contiguous Memory**: Arrays require a single, unbroken block of memory, which can be hard to find for very large datasets.
*   **Complex Insertions/Deletions**: Inserting or deleting an element in the middle of an array requires shifting all subsequent elements, which is computationally expensive.

**Advantages of Linked Lists:**
*   **Dynamic Size**: The list can grow or shrink exactly as needed during runtime.
*   **Scattered Memory**: Nodes can be allocated anywhere in the heap; they do not need to be contiguous.
*   **Fast Insertions/Deletions**: Adding or removing a node only requires updating a few pointers, without shifting other elements.

---

## 2. What is a Linked List?
A linked list is a collection of **nodes**. Each node is an independent structure that contains:
1.  **Data fields**: To store the actual information (e.g., an `int`, `char`, or another `struct`).
2.  **Link fields**: Pointers that hold the memory address of the next node(s) in the sequence.

### Representation of a Node
Using a self-referential structure, we can define a node for a singly linked list:
```c
typedef struct Node Node;

struct Node {
    int info;       // Data field
    Node *pNext;    // Link field (pointer to the next Node)
};
```

---

## 3. Allocation and Initialization
Nodes are created dynamically in the **heap** using `malloc()`.

```c
#include <stdlib.h>

int main() {
    // 1. Allocate memory in the heap
    Node *p = (Node*) malloc(sizeof(Node));
    
    // 2. Initialize the node
    p->info = 3;
    p->pNext = NULL; // NULL indicates the end of the list
    
    return 0;
}
```

### Side Structures (List Pointers)
To manage a linked list, you typically maintain:
*   `Node *pFirst;` (or `head`): A pointer to the very first element of the list.
*   `Node *pLast;` (or `tail`): An optional pointer to the last element. Keeping track of the tail makes adding nodes to the end of the list much faster.

---

## 4. Common Operations (Singly Linked List)

### 1. Print (List Scan)
To traverse a list, we use a temporary scanning pointer. We follow the `pNext` links until we reach `NULL`.
```c
void print_list(Node *pFirst) {
    if (pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    
    Node *pScan = pFirst;
    do {
        printf("Info: %d\n", pScan->info);
        pScan = pScan->pNext; // Move to the next node
    } while (pScan != NULL);
}
```

### 2. Head Insertion
Adding a new node at the very beginning of the list.
```c
void head_insertion(Node **pFirst) {
    Node *pNew = (Node*) malloc(sizeof(Node));
    scanf("%d", &(pNew->info));
    pNew->pNext = NULL;
    
    if (*pFirst == NULL) {
        *pFirst = pNew; // The list was empty
    } else {
        pNew->pNext = *pFirst; // The old first node becomes the second
        *pFirst = pNew;        // The new node becomes the first
    }
}
```

### 3. Head Deletion
Removing the first node from the list and freeing its memory.
```c
void head_deletion(Node **pFirst) {
    if (*pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    // Remember the second node
    Node *temp = (*pFirst)->pNext; 
    
    // Free the old first node
    free(*pFirst); 
    
    // The second node is now the first
    *pFirst = temp; 
}
```

### 4. Tail Insertion
If you maintain a `pLast` pointer, tail insertion is highly efficient.
```c
void tail_insertion(Node **pFirst, Node **pLast) {
    Node *pNew = (Node*) malloc(sizeof(Node));
    scanf("%d", &(pNew->info));
    pNew->pNext = NULL;
    
    if (*pFirst == NULL) {
        *pFirst = pNew;
        *pLast = pNew;
    } else {
        (*pLast)->pNext = pNew; // The old last node points to the new one
        *pLast = pNew;          // The new node becomes the last
    }
}
```

### 5. Tail Deletion
To delete the last node in a singly linked list, you must scan the entire list to find the **second-to-last** node (`pPrev`), so you can update its `pNext` to `NULL`.
*   If the list has only 1 element, you simply free it and set `pFirst = NULL`.
*   Otherwise, iterate until `pScan->pNext == pLast`. Then:
    ```c
    free(pLast);
    pPrev->pNext = NULL;
    pLast = pPrev;
    ```

### 6. Deletion at a Given Position
To delete a node in the middle (e.g., the one containing value `key`):
1.  Scan the list to find the node *before* the target (`pScan`).
2.  `temp = pScan->pNext->pNext;` (the node *after* the target).
3.  `free(pScan->pNext);` (delete the target).
4.  `pScan->pNext = temp;` (bridge the gap).

---

## 5. Different Kinds of Lists
1.  **Singly Linked List**: Each node points to the next. The last node points to `NULL`.
2.  **Circular Singly Linked List**: The last node points back to the first node instead of `NULL`.
3.  **Doubly Linked List**: Each node contains *two* pointers: one pointing to the `next` node, and one pointing to the `previous` node. This makes reverse traversal and targeted deletions much easier.
4.  **Circular Doubly Linked List**: A doubly linked list where the tail links forward to the head, and the head links backward to the tail.

---

## 6. Textbook References
*   **Sections**: 12.2, 12.4
