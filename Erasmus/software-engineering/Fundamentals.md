# Fundamentals

# 1. Context and Core Concepts

### Engineering

Engineering exist because people **design and build increasingly complex** artifacts/systems. So an **Engineer** is a person who applies knowledge from one or more branches of science to solve a certain type of **human need** through the **design, construction, or operation** of some artifact or system.

Any engineering discipline is characterized by:

- Advanced knowledge, required to design and build the types of systems that characterize it  (`The difference between technician and engineer` )
- There are 2 “moments”:
    - Understanding the problem first
    - Only then design and build the solution
- To archive good results (quality, time and cost) ,it is necessary to work in an organized and systematic manner.
    - Creativity is necessary (design), but it is not sufficient (`The difference between artist and engineer`)

### Software Engineering

It is the engineering discipline that encompasses:

- **All the aspects of software production** (from specification to maintenance)
- It focuses on **medium and large-scale software systems**
- the work must be done in an efficient, cost effective, and systematic way
- The product must satisfy the requirements of the users who utilize the system

---

# 2. SWEBOK: The Body of Knowledge

The **SWEBOK (Software Engineering Body of Knowledge)** is a document promoted by the IEEE Computer Society that serves as a guide to the current knowledge in Software Engineering.

> it represents a broad **consensus** regarding the contents of discipline
> 

### Why it matters

SWEBOK servers several goals: it promotes consistent worldwide view of software engineering, clarifies its relationship with related fields like Computer Science and Mathematics, and provides a solid base for developing academic curricula and certifications.

### The knowledge Areas

The guide divides the discipline into distinct knowledge areas. 

The core technical phases include: 

- Requirements
- Design
- Construction
- Testing
- Maintenance
- Configuration Management
- Engineering Management
- Process
- Tools & Methods
- Quality

This structure reinforces that software engineering is not just about writing code, but also involves a complete lifecycle of management and quality assurance

---

# 3. Modeling

### The Purpose of Modeling

We create models to **manage complexity**. In large systems, a model helps engineers understand the system by reducing the problem scope, allowing them to focus on one aspect at a time

- **Note→** Modeling is also crucial for small systems; without it, technical debt accumulates as they grow.
- **Communication →** A formal modeling language acts as a “common vocabulary” for the team

### What is a Model ?

A model is **not** an exact replica of reality, it is a simplified representation defined by:

1. **Correspondence :** it is based on an original entity
2. **Reduction** : it includes **only** elements relevant to a specific purpose;
3. **Substitution** : it can stand in for the real system for that specific purpose

![image.png](Fundamentals/image.png)

> **Example: The London Underground**
> 
> - **1926 Map:** Geographically accurate. Showed real distances.
> - **Beck's Map (>1932):** Modeled like an electric circuit. It abandoned geography to focus on **connectivity**.
> - **The Lesson:** Beck **reduced** the reality to serve a specific purpose: navigation. The physical distance didn't matter to the passenger, only the sequence of stops did .

### UML (Unified Modeling Language)

UML is the industry standard. It uses **Structure Diagrams** (static parts like Classes) and **Behavior Diagrams** (dynamic parts like Activity or Sequence diagrams)

It includes **OCL (Object Constraint Language)** because graphical boxes and arrows sometimes aren’t enough, so you need formal logic constraints

![image.png](<images/Fundamentals/image 1.png>)

---

# 4. Lifecycle and Methodology

### **IMPORTANT DISTINCTION**

- Lifecycle : A reference framework that tells you what processes occur (Analysis, Design, Testing …)
- Methodology : The specific set of procedures, tools and rules that tell you **how** to execute those processes

## Common Lifecycle Models

### 1. Waterfall Model (Cascada)

A rigid, linear approach where each phase must finish before the next starts.

![image.png](<images/Fundamentals/image 2.png>)

- **Best for:** Systems where requirements are stable and well-understood
- **Weakness:** Going back to change things is very expensive

### 2. Iterative Incremental Model

Flexible. You define the core Requirements and Architecture upfront, but detail the rest in cycles (iterations)

![image.png](<images/Fundamentals/image 3.png>)

- **Best for**: Project needing prototypes (like UI heavy apps) or partial deployment

### 3. Spiral Model

The primary focus here is **Risk Management**

- **Process :** Before building, the team analyzes risks and proposes alternatives (like prototypes)
- **The Loop**: Determine objectives -> Analyze Risk → Develop/Verify → Plan next phase

![image.png](<images/Fundamentals/image 4.png>)

---

# 5. Development Methodologies

### Plan-Driven (Heavyweight)

- **Example:** RUP (Rational Unified Process)
- **Focus:** Predictability, comprehensive documentation, and strict phases (Inception, Elaboration, Construction, Transition)

### Agile Methodologies

- **Example:** XP, Scrim
- **Philosophy**: Based on the **Agile Manifesto**. It values individuals over tools, working software over documentation, collaboration over contracts, and **responding to change** over following a plan

> **Focus: The Scrum Framework**
Scrum structures work into short cycles called **Sprints** (1-4 weeks).
> 
> - **Roles:** Product Owner (defines "what"), Scrum Master (manages process), Team (does the work).
> - **Artifacts:** Product Backlog (wishlist), Sprint Backlog (current to-do
**The Power of MDA:** You use **transformation rules** to automatically generate code from the higher-level models.

![image.png](<images/Fundamentals/image 6.png>)