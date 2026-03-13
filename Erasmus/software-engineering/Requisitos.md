# REQUIREMENTS

## 1. FUNDAMENTAL CONCEPTS
* **Definition:** A requirement is a property software must exhibit to solve a specific problem.
* **Economic Impact:**
    * Accounts for 10-15% of total project costs.
    * Errors here are critical: fixing a requirement error in production can cost up to 100 times more than fixing a code error.
* **The Domain Gap:**
    * **User/Client:** Operates in the "Problem Domain" (describes needs without technical precision).
    * **Developer:** Operates in the "Solution Domain" (translates needs into features).
    * **Risk:** Ambiguity and vague requests often lead to a disconnect between intent and interpretation.

## 2. TYPES OF REQUIREMENTS
* **Categorization by Focus:**
    * **Product Requirements:** What is developed (e.g., enrollment criteria).
    * **Process Requirements:** How it is developed (e.g., using Scrum or Java).
* **Functional vs. Non-Functional:**
    * **Functional Requirements:** Define capabilities and behaviors (what the system *does*). Can be high-level goals or detailed sub-functions.
    * **Non-Functional Requirements (NFRs):** Define constraints and quality attributes (how the system *performs*). Critical for safety and economic stability.

## 3. QUALITY ATTRIBUTES (ISO 25010)
NFRs are often categorized by the ISO 25010 standard. They often conflict (e.g., Security vs. Usability), requiring trade-offs.
* **Performance Efficiency:** Response times, throughput.
* **Portability:** Compatibility with different OS/environments.
* **Security:** Encryption, data protection.
* **Reliability:** Availability and uptime.
* **Usability:** Accessibility and ease of use.

## 4. THE ENGINEERING PROCESS
The process is iterative, cyclical, and dominated by human factors.

1.  **Elicitation (Capture):**
    * Gathering requirements from stakeholders and the environment.
    * Techniques: Interviews, prototyping, observation, scenarios.
2.  **Analysis & Negotiation:**
    * Classifying requirements and resolving conflicts/ambiguities.
    * Modeling the system (Use Cases, DFDs) and negotiating feasibility.
3.  **Specification:**
    * Creating the Software Requirements Specification (SRS).
    * Serves as the formal agreement; must be complete and verifiable (e.g., IEEE 830 standard).
4.  **Validation:**
    * Confirming requirements match actual user needs.
    * Techniques: Formal inspections, checklists, acceptance testing.

## 5. REQUIREMENTS MANAGEMENT
* **Volatility:** Requirements are unstable; >50% may change due to business/tech shifts.
* **Traceability:** The ability to track a requirement's lifecycle to manage change impact.
    * *Backward Traceability:* Links to origin/source.
    * *Forward Traceability:* Links to design/code entities.