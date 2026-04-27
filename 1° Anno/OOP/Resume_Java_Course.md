---
tags:
  - OOP
---
# 0. Introduction 

On some languages like C the programming is **structurated**, so a problem is broke down into simpler subproblems, that are then divided in subprograms (top-down method).
When we talk about the OOP we build an application on simpler **objects**, those are designed using classes, built and then used. To design an **object**, you must specify its properties (attributes or fields) and it's functionality (methods or functions).

> [!IMPORTANT] The 3 pillars of the OOP
> - **Inheritance**--> you can reuse an existing project and modify it
> - **Encapsulation**--> code reuse, abstraction, error containment
> - **Polymorphism**--> each Object behaves differently depending on the context and the value

# 1. The Java Language

The Java environment include on both a compiler and an interpreter (Java Runtime Environment,  JRE).

![[Pasted image 20260401173524.png]]

Through the compiler, the Java Source code it's converted into bytecode, which consist of pseudo-instruction in a platform-indipendet, artificial language. The Interpreters translate the bytecode into an executable file specific to the OS on which the bytecode runs  (WIndows, Linux, Mac). This allows a balance between speed and portability.

# 2. Object Oriented Programming with Java

A class is a generic model of a set of objects with similar characteristics. 
An object is a specific instance of a class.
The attributes (properties and fields) describe the state, the are represented by object's fields. The are also class fields.

#### How to create an Object ?

```java
Motocicletta m; // declaration (creation of a variable m of type Motocicletta(m is 4 byte))
m = new Motocicletta(); // instance (creation a new Motocicletta)
m.marca = "Guzzi 1000"; // inizialization 
m.colore = "rossa"; // inizialization ( insert a new property to the empty variable m)
m.mostra; // take the method "mostra" and the returned values are assigned to m 
```

#### How to create an Object with a Constructure? 
The constructor basically does 2 things:
-  instantiates the object and returns its address
-  what the programmer wants --> usually instantiates the object

