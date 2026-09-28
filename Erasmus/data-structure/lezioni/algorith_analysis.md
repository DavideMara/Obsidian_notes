---
tags:
  - DataStructure
  - appunti
  - Erasmus
---
◀️ *Back to:* [[00_Index_Data_Structure_Erasmus]]

--- 
# Asymptotic Analysis Foundation

## 2.1 What is an algorithm
**Definition** -> A step-by-step procedure to solve a problems or perform a computation

**Key Properties**
   
    Input: Has well-defined inputs.

    Output: Produces well-defined outputs.

    Definiteness: Each step is clear and unambiguous.

    Finiteness: It terminates after a finite number of steps.

    Effectiveness: Each step is basic enough to be performed.

## 2.2 Efficiency 
Efficiency is measured in terms of:
    **Time Complexity** : How the running time increases with the input size (n).
    **Time Complexity** : How much memory the algorithm uses relative to the input size.
We focus on the **grown rate** of the time/space required, not the actual clock time

## 2.3 Asyntotic notation (Big-O Notation)
We use Big O notation (O) to describe the Worst-Case running time's growth rate as input size (n) goes to infinity.
| Notation | Name | Meaning | Example Runtime |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Time is independent of the input size. | Accessing an array element. |
| **O(log n)** | Logarithmic | Time grows very slowly as **n** increases. | Binary Search. |
| **O(n)** | Linear | Time grows proportionally to **n**. | Simple loop (e.g., iterating an array). |
| **O(n log n)** | Linearithmic | Time grows a bit faster than linear. | Efficient sorts (MergeSort, QuickSort avg). |
| **O(n²)** | Quadratic | Time grows proportionally to the square of **n**. | Nested loops. |
| **O(2ⁿ)** | Exponential | Time doubles with each addition to the input. Becomes slow very fast. | Recursive Fibonacci (naive implementation). |

## 2.4 Calculating Temporal Complexity (iterative Examples)
We calculate complexity by counting basic operations and keeping only the **dominant term** (the one that grows fastest)

### Example: O(1) - Constant Time
The running time doesn't depend on the size of the array (n)

```java
// O(1) example: Accessing or basic arithmetic
public int getFirstElement(int[] arr) {
    if (arr.length == 0) return -1; // Single operation: O(1)
    return arr[0]; 
}
```
### Example: O(n) - Linear Time
The loop runs exactly ***n*** times, so the operations inside are executed ***n***
```java 
// O(n) example: Single loop
public int sumArray(int[] arr) {
    int sum = 0; // O(1)
    
    // Loop runs n times (where n = arr.length)
    for (int i = 0; i < arr.length; i++) { 
        sum += arr[i]; // O(1) operation
    }
    
    // Total: O(1) + O(n * 1) = O(n)
    return sum;
}
```
### Example O(n^2) - Quadratic Time
This uses the Multiplication Rule (Nested Loops). The inner loop runs ***n*** times for every iteration of the outer loop, which also runs ***n*** times ***(n⋅n=n^2)***
```java
// O(n^2) example: Nested loops
public void printPairs(int[] arr) {
    // Outer loop runs n times
    for (int i = 0; i < arr.length; i++) { 
        // Inner loop runs n times for EACH outer iteration
        for (int j = 0; j < arr.length; j++) { 
            System.out.println(arr[i] + ", " + arr[j]); // O(1)
        }
    }
    // Total: O(n * n) = O(n^2)
}
``` 
## Example O(log n) - Logarithmic Time
The key is that the input is **halved** (or divided by a constant factor) in each iteration

```java
// O(log n) example: Dividing the problem size
public void logExample(int n) {
    int i = 1; 
    // The loop variable 'i' is multiplied by 2, so it doubles each time.
    // The number of iterations is log base 2 of n.
    while (i < n) { 
        System.out.println(i);
        i = i * 2; // Problem size is reduced exponentially
    }
    // Total: O(log n)
}
```
## 2.5 Calculating Temporal Complexity of Simple Recursive Algorithms
We analyze recursive complexity using a **Recurrence Relation** of the form ***T(n)=aT(n/b)+f(n)***

### Example O(log n) - Binary Search
**Recurrence**: *T(n)=1⋅T(n/2)+O(1)*

    a=1 (one recursive call)

    b=2 (input is halved)

    f(n)=O(1) (constant work: comparison, addition, return)
**Master Theorem Case 1** applies: *n^(log2​)1=n0=1*. Since f(n)=1, the solution is *O(log n)*.
```java
//Recursive Binary Search
public int binarySearch(int[] arr, int target, int low, int high) {
    if (low > high) { // Base Case: O(1)
        return -1;
    }
    
    int mid = low + (high - low) / 2; // O(1)
    
    if (arr[mid] == target) { // O(1)
        return mid;
    } else if (arr[mid] < target) {
        // Recursive Call: T(n/2)
        return binarySearch(arr, target, mid + 1, high); 
    } else {
        // Recursive Call: T(n/2)
        return binarySearch(arr, target, low, mid - 1);
    }
}
```

### Example O(n) - Linear Recursion / Factorial
**Recurrence**: *T(n)=1⋅T(n−1)+O(1)*
>    The problem size is reduced by 1(n-1), not divided
>    The function is called *n* times before hitting the base case, and each call does *O(1)* work 

This is a new paragraph of regular text, which means the blockquote has ended.
```java
//Recursive Factorial
public int factorial(int n) {
    if (n <= 1) { // Base Case: O(1)
        return 1;
    }
    // Recursive Call: T(n-1) + O(1)
    return n * factorial(n - 1); 
}
```
### Example O(2^n) - Exponential Recursion - Fibonacci 
**Recurrence**: *T(n)=2⋅T(n−1)+O(1)*

>The input size is reduced by 1, but it makes two recursive calls.
>The number of calls doubles with each step (without memoization).

**Solution**: *O(2^n)*.
```java
//Recursive Fibonacci (inefficient)
public int fibonacci(int n) {
    if (n <= 1) { // Base Case: O(1)
        return n;
    }
    // Two recursive calls: 2 * T(n-1) + O(1)
    return fibonacci(n - 1) + fibonacci(n - 2); 
}

```
---
◀️ *Back to:* [[00_Index_Data_Structure_Erasmus]]
