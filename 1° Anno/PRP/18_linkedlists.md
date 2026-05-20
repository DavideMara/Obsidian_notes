---
tags:
  - ProceduralProgramming
  - LectureNotes
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]

# 18 Linked Lists: Globals and Implementations

This lecture covers the implementation details of singly linked lists using global tracking pointers, common list operations, and various types of linked list architectures (circular, doubly linked, etc.).

---

## 1. Why Linked Lists?
To understand linked lists, we must first look at the limitations of arrays:
*   **Fixed Size**: Array dimensions must be known in advance (either statically defined or dynamically allocated to a set size).
*   **Contiguous Memory**: Arrays require a single, unbroken block of memory, which can fail if memory is heavily fragmented.
*   **Complex Insertions/Deletions**: Inserting or deleting an element in the middle of an array requires shifting all subsequent elements, which is computationally expensive ($O(n)$).

**Advantages of Linked Lists:**
*   **Dynamic Size**: The list can grow or shrink exactly as needed during runtime.
*   **Scattered Memory**: Nodes can be allocated anywhere in the heap; they do not need to be contiguous.
*   **Fast Insertions/Deletions**: Adding or removing a node only requires updating a few pointers, without shifting other elements ($O(1)$ once the position is found).

---

## 2. Representation of a Node
A linked list is a collection of independent structures called **nodes**. Each node contains:
1.  **Data fields**: The actual information being stored.
2.  **Link fields**: Pointers that hold the memory address of the next node(s) in the sequence.

### Struct Definition
A node can hold multiple data fields of different types:
```c
struct Node {
    int info1;
    char info2;
    struct data info3;
    struct Node* pNext; // Pointer to the next node
};
```

For simplicity, a node with a single integer value is defined as:
```c
typedef struct Node Node;

struct Node {
    int info;
    Node* pNext;
};
```

### Allocation and Initialization in the Heap
Nodes are dynamically allocated in the **heap** using `malloc()`.

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

*Note: The pointer variable `p` resides in the **stack**, pointing to the actual node allocated in the **heap**.*

---

## 3. Side Tracking Structures
To manage the list, we maintain pointers to keep track of its boundaries:
*   `Node* pFirst` (or `head`): Points to the very first node.
*   `Node* pLast` (or `tail`): Points to the last node. (Optional, but highly useful for optimizing tail operations to $O(1)$).

### Example Memory Layout
If we have a list of elements containing the values `10`, `30`, and `5`:

```
Stack:
┌──────────────┐
│ pFirst: 7000 │ ──────┐
└──────────────┘       │
┌──────────────┐       │
│ pLast:  4000 │ ──┐   │
└──────────────┘   │   │
                   │   │
Heap:              ▼   ▼
Address 7000      Address 1000      Address 4000
┌────┬────┐       ┌────┬────┐       ┌────┬────┐
│ 10 │1000│ ────> │ 30 │4000│ ────> │  5 │NULL│
└────┴────┘       └────┴────┘       └────┴────┘
```

---

## 4. Common Operations (Using Global Pointers)
The following implementations assume `pFirst` and `pLast` are global pointers:
```c
Node* pFirst = NULL;
Node* pLast = NULL;
```

### 1. Print (List Scan)
Traverses the list starting from `pFirst` using a scanning pointer `pScan` and prints each node's content until `pScan` becomes `NULL`.
```c
void print_list(Node* pFirst) {
    if (pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    
    Node* pScan = pFirst;
    do {
        printf("Info: %d\n", pScan->info);
        pScan = pScan->pNext; // Move to the next node
    } while (pScan != NULL);
}
```

### 2. Head Insertion
Creates a new node and inserts it at the very beginning of the list.
```c
void head_insertion(void) {
    // 1. Allocate and initialize new node
    Node* pNew = (Node*) malloc(sizeof(Node));
    scanf("%d", &(pNew->info));
    pNew->pNext = NULL;
    
    // 2. Adjust pointers
    if (pFirst == NULL) {
        pFirst = pNew; // If empty, it is the first node
    } else {
        pNew->pNext = pFirst; // Points to the old first node
        pFirst = pNew;        // The new node becomes the first
    }
}
```

### 3. Head Deletion
Deletes the first node and deallocates its memory in the heap.
```c
void head_deletion(void) {
    if (pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    
    // 1. Save pointer to the second node
    Node* temp = pFirst->pNext;
    
    // 2. Free the first node
    free(pFirst);
    
    // 3. Update pFirst
    pFirst = temp;
}
```

### 4. Tail Insertion
Inserts a new node at the end of the list using `pLast`.
```c
void tail_insertion(void) {
    // 1. Create the new node
    Node* pNew = (Node*) malloc(sizeof(Node));
    scanf("%d", &(pNew->info));
    pNew->pNext = NULL;
    
    // 2. Adjust pointers
    if (pFirst == NULL) {
        pFirst = pNew;
        pLast = pNew;
    } else {
        pLast->pNext = pNew; // Old last node points to the new node
        pLast = pNew;        // Update the last pointer
    }
}
```

### 5. Tail Deletion
To delete the last node in a singly linked list, we must scan the entire list to locate the second-to-last node (`pPrev`), so we can set its `pNext` to `NULL` and update `pLast`.
```c
void tail_deletion(void) {
    if (pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    
    Node* pPrev = NULL;
    Node* pScan = pFirst;
    
    if (pScan->pNext == NULL) {
        // List only contains one node
        free(pScan);
        pFirst = NULL;
        pLast = NULL;
    } else {
        // Scan to find the second-to-last node (the one pointing to pLast)
        do {
            if (pScan->pNext == pLast) {
                pPrev = pScan;
                break;
            }
            pScan = pScan->pNext;
        } while (pScan->pNext != NULL);
        
        free(pPrev->pNext); // Free the last node
        pPrev->pNext = NULL;
        pLast = pPrev;      // Update pLast to point to the new last node
    }
}
```

### 6. Deletion at a Given Position (Value Match)
Deletes a node containing a specific `key` value.
```c
void delete_if_equal(int key) {
    if (pFirst == NULL) {
        printf("No node in the list!\n");
        return;
    }
    
    // Case 1: Key is in the first node
    if (pFirst->info == key) {
        Node* temp = pFirst;
        pFirst = pFirst->pNext;
        if (pFirst == NULL) {
            pLast = NULL; // List is now empty
        }
        free(temp);
        return;
    }
    
    // Case 2: Iterate to find node BEFORE the target node
    Node* pScan = pFirst;
    while (pScan->pNext != NULL && pScan->pNext->info != key) {
        pScan = pScan->pNext;
    }
    
    // Node found
    if (pScan->pNext != NULL) {
        Node* temp = pScan->pNext;
        pScan->pNext = temp->pNext; // Bridge the gap
        
        // If we deleted the tail, update pLast
        if (temp == pLast) {
            pLast = pScan;
        }
        free(temp);
    } else {
        printf("Key not found!\n");
    }
}
```

### 7. Homework: Insertion at a Given Position
**Goal**: Insert a new node with value `new_info` after a node containing a specific `key`.
```c
void insert_after(int key, int new_info) {
    Node* pScan = pFirst;
    
    // 1. Scan to locate the node with the key
    while (pScan != NULL && pScan->info != key) {
        pScan = pScan->pNext;
    }
    
    // 2. If node found, insert new node
    if (pScan != NULL) {
        Node* pNew = (Node*) malloc(sizeof(Node));
        pNew->info = new_info;
        pNew->pNext = pScan->pNext; // Connect new node to the rest of the list
        pScan->pNext = pNew;        // Link previous node to new node
        
        // If inserted after the last element, update pLast
        if (pScan == pLast) {
            pLast = pNew;
        }
    } else {
        printf("Node containing key %d not found!\n", key);
    }
}
```

---

## 5. Different Kinds of Lists

### Singly Linked List
Each node contains a pointer to the next node. The last node points to `NULL`.
```
pFirst -> [10 | *] -> [30 | *] -> [5 | NULL]
```

### Circular Singly Linked List
The last node points back to the first node instead of pointing to `NULL`.
```
┌─────────────────────────────────┐
▼                                 │
pFirst -> [10 | *] -> [30 | *] -> [5 | *]
```

### Doubly Linked List
Each node contains **two** pointers: one pointing forward to the next node, and one pointing backward to the previous node. This allows traversal in both directions.
```
         ┌───┐             ┌───┐             ┌───┐
NULL <── │10 │ <─────────> │30 │ <─────────> │ 5 │ ──> NULL
         └───┘             └───┘             └───┘
```

### Circular Doubly Linked List
A doubly linked list where the last node's forward pointer links to the first node, and the first node's backward pointer links to the last node.

---

## 6. Textbook References
*   **Sections**: 12.2, 12.4
