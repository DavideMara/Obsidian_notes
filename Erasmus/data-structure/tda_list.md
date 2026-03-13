---
tags:
  - DataStructure
  - appunti
  - Erasmus
---
◀️ *Back to:* [[00_Index_Data_Structure_Erasmus]]

--- 

# TDA Lista (List Abstract Data Type) 

The **List ADT** defines a linear collection of elements where each element has a position relative to the others. Key operations include insertion, deletion, accessing elements by position, and checking size.

-----

## 3.2. Implementación de listas basada en array (Array-Based List)

This implementation uses a contiguous block of memory (a Java array) to store the list elements.

### Key Features:

  * **Structure:** A fixed-size array, typically managed dynamically (e.g., resizing when full).
  * **Time Complexity (Big O):**

| Operation | Complexity | Note |
| :--- | :--- | :--- |
| **Access/Get** (by index) | $\mathbf{O(1)}$ | Direct memory lookup. |
| **Insert/Delete** (at end) | $\mathbf{O(1)}$ | No shifting required. |
| **Insert/Delete** (at middle/start) | $\mathbf{O(n)}$ | Requires shifting all subsequent elements. |
| **Resize** (when array is full) | $\mathbf{O(n)}$ | Must copy all $n$ elements to a new, larger array. |

### Java Example (`ArrayList` Concept):

```java
public class ArrayList<E> {
    private E[] data;
    private int size; // Current number of elements

    // O(1) access
    public E get(int index) {
        return data[index]; // Direct access
    }

    // O(n) insertion at the beginning
    public void addFirst(E element) {
        // Shift all existing elements to the right
        for (int i = size - 1; i >= 0; i--) { 
            data[i + 1] = data[i]; // O(n) operation
        }
        data[0] = element;
        size++;
    }
}
```

-----

## 3.3. Pointers / 3.4. Singly Linked Lists

In Java we use **references** (pointers managed by the JVM). A **Singly Linked List (SLL)** uses these references.

### Key Features (SLL):

  * **Structure:** A sequence of **nodes (cells)**, where each node contains the data element and a **single reference** (pointer) to the next node in the sequence.
  * **Head:** A reference to the first node.
  * **Tail:** (Often tracked) A reference to the last node.

### Time Complexity (Big O) - SLL:

| Operation | Complexity | Note |
| :--- | :--- | :--- |
| **Access/Get** (by index) | $\mathbf{O(n)}$ | Must traverse from the head. |
| **Insert/Delete** (at head) | $\mathbf{O(1)}$ | Simple pointer reassignment. |
| **Insert/Delete** (at end, no tail) | $\mathbf{O(n)}$ | Must traverse to the last node. |
| **Insert/Delete** (at middle/end, with tail) | $\mathbf{O(1)}$ | If the position *before* the insertion/deletion point is known. |

### Java Example (SLL Node Structure):

```java
// Inner class representing a "cell" or "node"
private static class Node<E> {
    private E element;  // The data
    private Node<E> next; // The reference (pointer) to the next node

    public Node(E e, Node<E> n) {
        element = e;
        next = n;
    }
}

// O(1) insertion at the head
public void addFirst(E element) {
    // Create new node, pointing to the current head
    head = new Node<>(element, head); // O(1) operation
    size++;
}
```

-----

## 3.5. Implementación de listas mediante celdas doblemente enlazadas (Doubly Linked Lists - DLL)

The **Doubly Linked List (DLL)** improves SLL by including a second pointer.

### Key Features (DLL):

  * **Structure:** Each node contains the data, a reference to the **next** node, and a reference to the **previous** node.
  * **Advantages:** Allows for bidirectional traversal (forward and backward). Makes deleting a node much easier if only the node itself is known.

### Time Complexity (Big O) - DLL:

The complexity remains generally the same as SLL, but specific operations become more efficient:

| Operation | Complexity | Note |
| :--- | :--- | :--- |
| **Access/Get** (by index) | $\mathbf{O(n)}$ | Still requires traversal. |
| **Insert/Delete** (at head/tail) | $\mathbf{O(1)}$ | Simple pointer reassignment (faster with a tail pointer). |
| **Delete a known node** | $\mathbf{O(1)}$ | Can update `prev` and `next` pointers immediately. |

-----

## 3.6. Comparación (incompleta, falta iterador)

| Feature | Array-Based List | Singly/Doubly Linked List |
| :--- | :--- | :--- |
| **Memory** | Contiguous, less overhead. | Non-contiguous, higher overhead (extra pointers). |
| **Access (by index)** | $\mathbf{O(1)}$ (Excellent) | $\mathbf{O(n)}$ (Poor) |
| **Insertion/Deletion (Middle)** | $\mathbf{O(n)}$ (Poor, requires shifting) | $\mathbf{O(1)}$ (Excellent, if node position is known) |
| **Dynamic Resizing** | Required, $\mathbf{O(n)}$ cost. | Not required, automatically handles size. |
| **Locality of Reference** | High (better cache performance). | Low (nodes are scattered). |

-----

## 3.7. Iterators

An **Iterator** is an object that provides a standard way to access and traverse the elements of a collection sequentially without exposing its underlying structure (array, linked nodes, etc.).

### Key Iterator Methods (Java `Iterator<E>` interface):

1.  `boolean hasNext()`: Returns `true` if there are more elements to iterate over.
2.  `E next()`: Returns the next element in the iteration and advances the iterator.
3.  `void remove()`: Removes the last element returned by `next()` (optional operation).

-----

## 3.8. Iterator in array-based lists / 3.9. Iterator in linked-cell-based lists

Implementing an iterator is different for array-based vs. linked lists, but the **interface** and **time complexity of traversal** remain the same.

| Implementation Type | Internal State of Iterator | `hasNext()`/`next()` Complexity |
| :--- | :--- | :--- |
| **Array-Based** | An integer index (`int cursor`). | $\mathbf{O(1)}$ (Index increment is instant). |
| **Linked-Based** | A node reference (`Node<E> current`). | $\mathbf{O(1)}$ (Reference update is instant). |

**Note:** While `next()` is $\mathbf{O(1)}$, the **total traversal** of the entire list using an iterator is $\mathbf{O(n)}$ for both.

### Java Example (Iterator Concept - Linked List):

```java
// Inside the LinkedList class:
private class ListIterator implements Iterator<E> {
    private Node<E> current = head; // Start at the head

    public boolean hasNext() {
        return current != null; // Checks if the current node is valid
    }

    public E next() {
        if (!hasNext()) throw new NoSuchElementException();
        E element = current.element; // Get the current element
        current = current.next;    // Advance the pointer to the next node (O(1))
        return element;
    }
}
```

-----

## 3.10. Cursor Implementation

The **Cursor Implementation** is a memory management technique, usually used in languages like C/C++ or older systems, to simulate linked lists using **arrays** when native pointers are unavailable or too costly.

  * **Structure:** Uses an array of "nodes," where each element in the array has fields for the `data` and the integer `index` of the next node.
  * **Concept:** The "pointer" is just an array index (a *cursor*).
  * **Time Complexity:** Generally $\mathbf{O(n)}$ for insertions/deletions/access, similar to a traditional linked list, but with $\mathbf{O(1)}$ memory overhead per node (no memory fragmentation).

-----

## 3.11. Comparación de las implementaciones (Summary)

| Implementation | Index Access | Insertion/Deletion (Middle) | Memory Use | Best For... |
| :--- | :--- | :--- | :--- | :--- |
| **Array-Based (Contiguous)** | $\mathbf{O(1)}$ | $\mathbf{O(n)}$ | Memory efficiency, high locality. | Frequent lookups, few modifications. |
| **Singly/Doubly Linked** | $\mathbf{O(n)}$ | $\mathbf{O(1)}$ (If position known) | Memory overhead (pointers), low locality. | Frequent insertions/deletions, sequential access. |
| **Cursor-Based** | $\mathbf{O(n)}$ | $\mathbf{O(1)}$ (If position known) | Efficient fixed memory allocation. | Environments without dynamic memory management. |

-----

## 3.12. Listas en “Java Collections Framework” 

The Java Collections Framework (JCF) provides robust, optimized implementations of the List ADT.

| JCF Class | Implementation Type | Key Features |
| :--- | :--- | :--- |
| **`ArrayList`** | **Array-Based** | Best for random access (`get(i)` is O(1)). Dynamic resizing occurs automatically. |
| **`LinkedList`** | **Doubly Linked List** | Best for frequent insertions/deletions at the ends or middle (if iterator is used). |
| **`Vector`** | Array-Based | Legacy class, similar to `ArrayList` but synchronized (thread-safe, but slower). |

**Practical Tip:** Always default to using `ArrayList` unless you have a specific requirement for high-volume insertions/deletions in the middle of the list, in which case `LinkedList` is better.