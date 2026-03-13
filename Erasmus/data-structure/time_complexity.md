---
tags:
  - appunti
  - DataStructure
  - Erasmus
---
◀️ *Back to:* [[00_Index_Data_Structure_Erasmus]]

--- 

# Topic: Detailed Time Complexity Analysis ⏱

Time complexity analysis determines how an algorithm's running time ($T(n)$) grows with the input size ($n$). We use **Big O Notation** ($\mathbf{O}$) to express the *worst-case* growth rate.


## 1\. Rules for Iterative (Non-Recursive) Code

The goal is to count the highest order of operations in the code block as $n$ approaches infinity.

### 1.1. Simplification and Dominance

When calculating $T(n)$, always simplify by ignoring **constants** and **lower-order terms**.

| Rule              | Example Function $T(n)$    | Big O Complexity $O(f(n))$ | Rationale                                              |
| :---------------- | :------------------------- | :------------------------- | :----------------------------------------------------- |
| **Sum Rule**      | $T(n) = n^2 + 5n + 10$     | $\mathbf{O(n^2)}$          | $n^2$ grows much faster than $5n$ or $10$.             |
| **Constant Rule** | $T(n) = 3n^2$              | $\mathbf{O(n^2)}$          | The constant factor (3) is discarded.                  |
| **Combined**      | $T(n) = 2 + 5000 + \log n$ | $\mathbf{O(\log n)}$       | $\log n$ is the dominant term (all others are $O(1)$). |

### 1.2. Analysis of Control Structures

#### A. Sequential Statements (Addition Rule)

Code blocks executed one after the other. The total complexity is the complexity of the **most time-consuming** block.

```java
// Block A: O(n)
for (int i = 0; i < n; i++) { 
    System.out.println("A"); 
}

// Block B: O(n^2)
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        System.out.println("B");
    }
}

// T(n) = O(n) + O(n^2) = O(n^2)
```

#### B. Loops (Multiplication Rule)

The complexity inside the loop is multiplied by the number of iterations.

1.  **Linear Loop $\mathbf{O(n)}$:** Iterates proportional to $n$.

    ```java
    for (int i = 0; i < n; i++) { // Runs n times
        // Constant work O(1) inside
    }
    // T(n) = n * O(1) = O(n)
    ```

2.  **Quadratic Loop $\mathbf{O(n^2)}$ (Nested):**

    ```java
    for (int i = 0; i < n; i++) {       // Outer loop: n times
        for (int j = 0; j < n; j++) {   // Inner loop: n times
            // O(1) work
        }
    }
    // T(n) = n * n * O(1) = O(n^2)
    ```

3.  **Logarithmic Loop $\mathbf{O(\log n)}$:** The loop control variable is multiplied or divided by a constant factor.

    ```java
    for (int i = 1; i < n; i = i * 2) { // i doubles in each iteration
        // O(1) work
    }
    // The loop terminates when 2^k = n, so k = log2(n). T(n) = O(log n)
    ```

-----

## 2\. Analysis of Recursive Code (Recurrence Relations)

Analyzing recursive functions requires setting up a **Recurrence Relation** $T(n)$ and solving it. The most practical way for an exam is often the **Master Theorem**.

### 2.1. The Recurrence Relation Form

$$T(n) = a T(n/b) + f(n)$$

  * $a$: Number of recursive calls.
  * $b$: Factor by which input size is reduced ($n/b$).
  * $f(n)$: Cost of non-recursive work (e.g., merging, splitting, setup) done in the function call.

### 2.2. Examples Solved with the Master Theorem

The Master Theorem compares the cost of the work at the root and internal nodes, $f(n)$, against the cost of the leaves, $n^{\log_b a}$.

| Example Algorithm          | Recurrence $T(n)$          | Parameters | $n^{\log_b a}$           | Master Theorem Case                              | Complexity $O(f(n))$   |
| :------------------------- | :------------------------- | :--------- | :----------------------- | :----------------------------------------------- | :--------------------- |
| **Binary Search**          | $T(n) = 1 T(n/2) + O(1)$   | $a=1, b=2$ | $n^{\log_2 1} = n^0 = 1$ | **Case 1**: $f(n)=O(1)$ is equal to $n^0$.       | $\mathbf{O(\log n)}$   |
| **Merge Sort**             | $T(n) = 2 T(n/2) + O(n)$   | $a=2, b=2$ | $n^{\log_2 2} = n^1 = n$ | **Case 2**: $f(n)=O(n)$ is equal to $n^1$.       | $\mathbf{O(n \log n)}$ |
| **$T(n) = 4T(n/2) + n^3$** | $T(n) = 4 T(n/2) + O(n^3)$ | $a=4, b=2$ | $n^{\log_2 4} = n^2$     | **Case 3**: $f(n)=O(n^3)$ is greater than $n^2$. | $\mathbf{O(n^3)}$      |

### 2.3. Linear Recurrences (The Exception)

For recurrences like $T(n) = T(n-1) + O(1)$, where the problem size is reduced by an **additive constant** (not multiplicative), the Master Theorem doesn't apply.

| Example Algorithm         | Recurrence $T(n)$               | Solution (Expansion)                     | Complexity $O(f(n))$ |
| :------------------------ | :------------------------------ | :--------------------------------------- | :------------------- |
| **Recursive Factorial**   | $T(n) = T(n-1) + O(1)$          | $1 + 1 + ... + 1$ (n times)              | $\mathbf{O(n)}$      |
| **Inefficient Fibonacci** | $T(n) = T(n-1) + T(n-2) + O(1)$ | The number of calls grows exponentially. | $\mathbf{O(2^n)}$    |

-----

## 3\. Practical Complexity in Data Structures

In your exam, you must analyze the complexity of basic ADT operations based on their implementation.

| ADT Operation            | Array Implementation        | Linked List Implementation                  | Logic/Reason                                                                     |
| :----------------------- | :-------------------------- | :------------------------------------------ | :------------------------------------------------------------------------------- |
| **List Access `get(i)`** | $\mathbf{O(1)}$             | $\mathbf{O(n)}$                             | Array: Direct index access. List: Must traverse $i$ nodes.                       |
| **Stack `push()`**       | $\mathbf{O(1)}$ (Amortized) | $\mathbf{O(1)}$                             | Both: Operation happens at one end (top/end) with a single pointer/index update. |
| **Queue `dequeue()`**    | $\mathbf{O(1)}$ (Circular)  | $\mathbf{O(1)}$                             | Both: Operation happens at the front with a single pointer/index update.         |
| **List Insert (Middle)** | $\mathbf{O(n)}$             | $\mathbf{O(1)}$ (If previous node is known) | Array: Must shift $n/2$ elements. List: Only pointer reassignment is needed.     |

**Amortized $\mathbf{O(1)}$:** An operation is $\mathbf{O(1)}$ *on average*, even if occasional operations (like array resizing) are $\mathbf{O(n)}$. Since resizing happens very rarely, the total cost spread over all operations remains constant.