---
tags:
  - oop
aliases:
  - Java Basics
  - Java Crash Course
---

# ☕ Java Fundamentals Basic Guide

## 1. Anatomy of Java
In Java, **everything** is an object. There are no standalone functions or variables; everything must live inside a `class`.
- The **Class** is the file/blueprint.
- The **Main Method** is the exact starting line of the program.

```java
public class Main { 
    // The entry point of your program
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

## 2. Variables & Memory Space
Java is statically typed, meaning you must declare what type of data a variable holds before using it.
### Primitives (Stored in Stack Memory)
These hold the actual value.
```java
int age = 20;            // Whole numbers
double price = 19.99;    // Decimals
boolean isStudent = true;// true/false
char grade = 'A';        // Single quotes for chars
```

### Reference Types (Stored in Heap Memory)
These hold a memory address (pointer) to the object, not the object itself.
```java
String name = "Alice";   // Double quotes for Strings
Scanner sc = new Scanner(System.in); 
int[] numbers = {1, 2, 3}; // Arrays are objects too!
```

## 3. Passing Variables 
> [!IMPORTANT]
> Java is STRICTLY Pass-by-Value. When you pass a variable to a method, Java makes a copy of the value.
> - **For Primitives:** It copies the actual number. Changing it inside the method does not affect the original.
> - **For Objects:** It copies the memory address. Because both the original and the copy point to the exact same house in memory, modifying the object inside the method will affect the original.

```java
public void updateData(int number, int[] array) {
    number = 50;       // Does NOT change the original integer
    array[0] = 99;     // DOES change the original array!
}
```

## 4. Control Flow
How we tell the program to make decisions and repeat tasks.

### Conditionals
```java
if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else {
    System.out.println("C");
}
```
*Note: NEVER use `==` to compare Strings. Always use `string1.equals(string2)`.*

### Loops
```java
// FOR LOOP: When you know how many times to repeat
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// WHILE LOOP: When you repeat until a condition is false
int count = 0;
while (count < 5) {
    count++;
}

// FOR-EACH LOOP: Best for iterating through arrays/lists
String[] names = {"Bob", "Alice"};
for (String n : names) {
    System.out.println(n);
}
```

## 5. Object-Oriented Programming (OOP) Paradigms
The core philosophy of Java. You model your code after real-world things.

### The 4 Pillars of OOP
- **Encapsulation:** Hiding data. Use `private` for variables and `public` for getters/setters so outside code can't break your object.
- **Inheritance:** Classes taking traits from other classes (using `extends`). Promotes code reuse. (e.g., `Dog extends Animal`).
- **Polymorphism:** "Many forms." A child class can override a parent's method to do something specific.
- **Abstraction:** Hiding complex implementation details and only showing the essential features (using abstract classes or interfaces).

### Class Construction Example
```java
public class Student {
    // 1. Encapsulated Attributes
    private String name;
    private int id;

    // 2. Constructor (Runs when 'new Student()' is called)
    public Student(String name, int id) {
        this.name = name; // 'this' refers to the object's attribute
        this.id = id;
    }

    // 3. Methods (Behaviors)
    public void study() {
        System.out.println(this.name + " is studying.");
    }

    // 4. Getters/Setters
    public String getName() { return this.name; }
}
```

## 6. Arrays vs. ArrayLists
Standard arrays have a fixed size. If you need a list that can grow and shrink dynamically, use `ArrayList`.

```java
// Array (Fixed Size)
int[] fixedScores = new int[5];
fixedScores[0] = 100;

// ArrayList (Dynamic Size)
import java.util.ArrayList;

ArrayList<String> dynamicList = new ArrayList<>();
dynamicList.add("Apple");
dynamicList.add("Banana");
dynamicList.remove(0); // Removes "Apple"
int size = dynamicList.size(); // Returns 1
```
*Note: ArrayLists cannot store primitives directly. You must use Wrapper classes like `Integer` instead of `int`, or `Double` instead of `double`.*

## 7. Static vs. Instance
- **Instance Variables/Methods:** Belong to a specific object. You need `new` to use them. (e.g., `myCar.drive()`)
- **Static Variables/Methods:** Belong to the Class itself. Shared across all objects. You call them directly from the class name. (e.g., `Math.max(10, 20)`)

## 8. Common Pitfalls
- **NullPointerException:** You declared an object but forgot to initialize it with `new`. It's pointing to nothing.
- **ArrayIndexOutOfBoundsException:** You tried to access index 5 in an array that only has 5 items (Indexes go from 0 to 4).
- **Scanner skipping inputs:** If you use `sc.nextInt()` and then immediately use `sc.nextLine()`, the `nextLine()` will consume the leftover "Enter" key press. Add a blank `sc.nextLine();` in between to clear the buffer.