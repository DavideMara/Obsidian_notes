---
tags:
  - DataStructure
  - Erasmus
  - appunti
---
◀️ *Back to:* [[00_Index_Data_Structure_Erasmus]]

--- 


# Stacks and Queues 
## 4.1. Queue ADT (Cola) 

A **Queue** is a linear structure that adheres to the **FIFO (First-In, First-Out)** principle—the element inserted first is the one removed first (like a queue of people).

| Operation | Description | Time Complexity |
| :--- | :--- | :--- |
| **`enqueue(e)`** | Adds element `e` to the **rear** of the queue. | $\mathbf{O(1)}$ |
| **`dequeue()`** | Removes and returns the element from the **front**. | $\mathbf{O(1)}$ |
| **`first()`** | Returns the element at the front without removing it. | $\mathbf{O(1)}$ |

-----

## 4.2. Implementation of Queues with Circular Array 

This implementation uses a fixed-size array but treats the ends as connected to avoid the slow $\mathbf{O(n)}$ shifting problem.

### Key Features:

  * Uses two integer indices: **`front`** (points to the first element) and **`rear`** (points to where the next element is added).
  * **Wrap-Around Logic:** Indices move using the **modulo operator ($\%$)** to loop from the end of the array back to index 0.

### Complexity and Java Concept:

Both `enqueue` and `dequeue` are $\mathbf{O(1)}$ because they only involve updating pointers (indices) using constant-time arithmetic.

```java
// O(1) Circular Array Logic
// To find the next available index:
int nextIndex = (current_index + 1) % capacity;

// The Queue is full when:
if ((rear + 1) % capacity == front) {
    // Requires O(n) resizing or an exception
}
```

-----

## 4.3. Implementation of Queues with Linked Cells 

This uses a **Singly Linked List (SLL)** with references to both the head and the tail. This is typically the preferred implementation as it handles dynamic size without $\mathbf{O(n)}$ resizing.

### Key Features:

  * **Front:** Managed by the **`head`** reference (where `dequeue` happens).
  * **Rear:** Managed by the **`tail`** reference (where `enqueue` happens).

### Complexity and Java Concept:

| Operation | Implementation | Complexity |
| :--- | :--- | :--- |
| **`enqueue(e)`** | Add a new node at the **tail**. | $\mathbf{O(1)}$ |
| **`dequeue()`** | Remove the node at the **head**. | $\mathbf{O(1)}$ |

```java
// O(1) enqueue: Adding to the tail
public void enqueue(E e) {
    Node<E> newNode = new Node<>(e, null); // New node always points to null
    if (isEmpty()) {
        head = newNode;
    } else {
        tail.next = newNode; // Link the old tail to the new node
    }
    tail = newNode; // Update tail to the new node
    size++;
}
```

-----

## 4.4. Stack ADT (Pila) 

A **Stack** is a linear structure that adheres to the **LIFO (Last-In, First-Out)** principle—the element inserted last is the one removed first (like a stack of books).

| Operation | Description | Time Complexity |
| :--- | :--- | :--- |
| **`push(e)`** | Adds element `e` to the **top** of the stack. | $\mathbf{O(1)}$ |
| **`pop()`** | Removes and returns the element from the **top**. | $\mathbf{O(1)}$ |
| **`top()`** | Returns the element at the top without removing it. | $\mathbf{O(1)}$ |

-----

## 4.5. Implementation of Stacks with Array 

Since access is constrained to one end, an array is highly efficient for a Stack.

### Key Features:

  * Uses an array and a single integer index, **`topIndex`**, pointing to the most recently added element.
  * The "top" of the stack is effectively the end of the array.

### Complexity and Java Concept:

Both `push` and `pop` are $\mathbf{O(1)}$ because they only involve array access and index updates. Resizing is $\mathbf{O(n)}$.

```java
private E[] data;
private int topIndex = -1; 

// O(1) push: Increment index and insert
public void push(E e) {
    // Check and handle array resizing (amortized O(1))
    if (topIndex + 1 == data.length) { 
        // resize (O(n))
    }
    data[++topIndex] = e; // Increment topIndex THEN assign
}

// O(1) pop: Read and decrement index
public E pop() {
    if (topIndex == -1) throw new EmptyStackException();
    return data[topIndex--]; // Read THEN decrement topIndex
}
```

-----

## 4.6. Implementation of Stacks with Linked Cells 

This also uses a **Singly Linked List (SLL)** where the **head** always represents the **top** of the stack.

### Key Features:

  * Only a single **`head`** reference is needed.
  * **`push`** involves inserting the new node at the head.
  * **`pop`** involves removing the head node.

### Complexity and Java Concept:

Both `push` (insert at head) and `pop` (remove at head) are $\mathbf{O(1)}$.

```java
// O(1) push: Insert at the head
public void push(E e) {
    // New node points to the current head, then becomes the new head
    head = new Node<>(e, head); 
    size++;
}

// O(1) pop: Remove at the head
public E pop() {
    if (head == null) throw new EmptyStackException();
    E element = head.element;
    head = head.next; // Head moves to the second node
    size--;
    return element;
}
```

-----

## 4.7. Comparison of Implementations

| TDA | Implementation | Dynamic Size | Push/Enqueue| Pop/Dequeue | Memory/Performance Tradeoff |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Stack** | Array-Based | No (needs resize) | $\mathbf{O(1)}$ (amortized) | $\mathbf{O(1)}$ | Better CPU cache performance (locality). |
| **Stack** | Linked-Based | Yes | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | Higher memory overhead (pointers). |
| **Queue** | Circular Array | No (needs resize) | $\mathbf{O(1)}$ (amortized) | $\mathbf{O(1)}$ | Better CPU cache performance, no shifting cost. |
| **Queue** | Linked-Based | Yes | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | Preferred for dynamic size; uses more memory. |

-----

## 4.8. Stacks and Queues in Java Collections Framework 

The Java Collections Framework (JCF) provides optimized interfaces and concrete classes for these ADTs.

| ADT | JCF Interface | Preferred JCF Class | Key Notes |
| :--- | :--- | :--- | :--- |
| **Queue** | `Queue<E>` | **`ArrayDeque<E>`** or **`LinkedList<E>`** | `ArrayDeque` is generally fastest. `LinkedList` implements `Queue` well (using its O(1) head/tail methods). |
| **Stack** | `Deque<E>` (Double Ended Queue) | **`ArrayDeque<E>`** | The legacy `java.util.Stack` class is synchronous and generally avoided. `ArrayDeque` provides a modern, fast, array-based stack implementation. |

**Note on `ArrayDeque`:** It uses a dynamically resizing circular array, making it efficient for both Stack and Queue operations at both ends ($\mathbf{O(1)}$).