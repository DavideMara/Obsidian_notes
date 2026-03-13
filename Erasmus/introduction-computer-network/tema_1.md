# 1.1 Introduction

## Basic Concepts

* **Network**
    A distributed system that interconnects multiple devices, facilitating communication between them.
* **Communication**
    The transfer of information.
* **Information**
    Technically, this refers to the message itself being transmitted.
    > The **quantity** of information is measured by the **entropy** of the text $\rightarrow$ **number of bits**.

---

## Communication Model

> **[Source System Diagram]**
> *Source System (Source $\to$ Transmitter) $\to$ Transmission System $\to$ Destination System (Receiver $\to$ Destination)*

---

## Transmission & Propagation Mechanics

> **[Space-Time Diagram]**
> *Diagram illustrating transmission delay ($T_x$) vs propagation delay ($R_p$) between point A and B over distance $d$.*

### Key Formulas & Definitions

**1. Transmission Time ($T_x$)**
$$T_x = \frac{L}{V_t}$$
> **Units:** $\frac{[\text{bits}]}{[\text{bits/s}]} = [\text{seconds}]$

**2. Transmission Speed ($V_t$)**
The rate at which information is transmitted onto the link (also known as Bandwidth or Bit Rate).
* **Unit:** bits per second (**bps**)

**3. Propagation Speed ($V_p$)**
The speed at which a signal travels through the transmission medium.
* **Unit:** meters per second (**m/s**)
* **Approximation (Speed of light in medium):**
    $$V_p \approx 2 \cdot 10^8 \text{ m/s}$$

**4. Propagation Delay ($R_p$)**
$$R_p = \frac{d}{V_p}$$
> *Where $d$ is the distance between transmitter and receiver.*

### Total Delay ($T$)
The total latency is the sum of transmission time and propagation delay (ignoring queuing and processing delays for this model):
$$T = T_x + R_p$$

# 1.2 Network Evolution

## 1950-60's

* **Wide Area Networks (WAN)** $\rightarrow$ A type of network that **covers** a large geographical area; typically operated by service providers.
* **Circuit Switching** $\rightarrow$ A switching mechanism that establishes a dedicated physical path through the network nodes for the duration of the communication (e.g., legacy telephone networks).

## 1970's

* **ITU Standards** $\rightarrow$ International Telecommunication Union standardization efforts.

## Packet Switching

* **Definition:** A mechanism in which data is **routed** in sequences, divided into **small units** called **packets**.

> **[Packet Switching Topology]**
> A network graph showing Source **A** connecting to Destinations **B** and **C** via a mesh of intermediate circular nodes.
> * Small rectangular blocks representing **packets** are traveling along the links.
> * Arrows indicate the circular flow and direction of data transmission.
> * **Visual Note:** "Each packet is passed **node to node**" (Store-and-forward mechanism).

### Transmission Speed Example
$$V_t = 100\text{ M} = 10^8 \text{ bits/s}$$
*(Note: This value likely represents a theoretical calculation example rather than historical 1970s speeds).*

## X.25 Protocol

**Date:** 16/09/2025

### Definition
A legacy **packet switching** standard. At every **hop**, the protocol **verifies** the correctness of each **packet**. If necessary, it is retransmitted or forwarded.

* $\rightarrow$ **High Complexity** and **High Monetary Cost**.
* $\rightarrow$ **64 Kbps MAX** (Maximum transmission speed historically).

> **[X.25 Network Topology & Signal]**
> * The nodes are connected in a mesh, illustrating the path of the packets.

---

## Example: Flow Control

**Text:** This network **uses** a mechanism of **flow regulation** (utilizing a **buffer**).

> **[Node Buffering Mechanism]**
> *Diagram illustrating the queue/buffer at a network node.*

---

## 1980's
* **Frame Relay** emerges as a **replacement for X.25** $\rightarrow$ Cheaper and simpler.
* Evolution from **Mainframe systems** to **local networks of workstations**.

## Frame Relay
Designed for **more reliable links** (fiber/digital), implying a lower probability of packet (or frame) loss.

* **SIMPLER**: The intermediate nodes do not perform error recovery $\rightarrow$ the network allows losses (relying on endpoints for recovery).
* Most **redundant information** used for **error control** is eliminated.
    * $\downarrow$
    * **More EFFICIENT and CHEAPER**.
* The "intelligence" of the network is **moved to the end devices**.

---

## 1990's
* Expansion of the Internet leads to the **Distributed computing model (Client/Server)**.
* Introduction of Internet Access via **PSTN/RTB** (modem, cable network, and ADSL). New telecommunication technologies emerge, such as **ATM**.

## ATM (Asynchronous Transfer Mode)
* **Broadband switching mechanism**, often considered an evolution of Frame Relay.
* **No error control** within the core network (handled **END-TO-END**).
* **Cell-based switching** $\rightarrow$ Data is divided into small, **fixed-length packets** (Cells, typically 53 bytes).
* Packets are **fragmented** into sequence cells $\rightarrow$ **High Speed transmission** ($2 \text{ Mbps}$ to $40 \text{ Gbps}$).

### Implementation of **Quality of Service (QoS)**:
* Allows a **constant transmission speed channel** (Virtual Circuit) to be offered, combining packet switching efficiency with circuit switching reliability.

***

## 2000's
* Widespread adoption of **High-speed Home Networks** (Broadband).
    * *Context:* Cable and **ADSL networks**.
* **IEEE 802.11** (Wi-Fi) wireless local area networks become **ubiquitous**.
* **TCP/IP** cements its status as the universal protocol architecture; **Switched Ethernet** dominates **LAN technology**.

---

## Local Area Network (LAN)

> **[Diagram: Topology Evolution]**
> *Left:* Bus topology labeled "10 Mbps / 100 Mbps".
> *Right:* Star topology connected to a central box/switch labeled "TODAY".

* **Communication networks** providing **small coverage** (buildings, campuses).
* Usually owned by the **same entity** (private ownership).
* Allows for **much higher transmission speeds** compared to traditional **WANs**.
* Modern wired networks use switched systems based on **Switches**.
    * Nodes direct each message specifically to the appropriate destination (Unicast) rather than broadcasting collisions (Hubs).

---

## 2010's
* **Increase in transmission speed** and major improvements in signal processing applied to wireless networks (4G/LTE, 5G).
* Return to a largely **centralized computing model**:
    * $\downarrow$
    * **CLOUD COMPUTING**

---

# 1.2 Protocols and Hierarchical Model

## 1.2.1 Overview
* The volume of tasks required to communicate over a network is **enormous**.
* It is **not feasible** to design a **single monolithic program** to handle all tasks.

### Definitions
* **PROTOCOL:** A set of rules governing the exchange of information.
* **PROTOCOL ARCHITECTURE:** The **hierarchical organization** of **multiple protocols** (layers).

## 1.2.2 Key Aspects of a Protocol
Any protocol consists of **3 key aspects**:

1.  **SYNTAX (HOW):** Defines the **format** of the data blocks (headers, fields).
2.  **SEMANTICS (WHAT):** Defines the **meaning** of each section of bits (control information, error handling).
3.  **TIMING (WHEN):** Defines the **sequencing** and speed matching for information exchange.

---

## 1.2.3 Standard Architectures

For global communication, systems must adhere to a compatible set of layers. This necessitated **standardized architectures** that are open and **vendor-neutral**.

The principal models are:

* **OSI Model**: A comprehensive, **7-layer** theoretical reference model.
* **TCP/IP Model**: A practical, **4-layer** (or 5-layer hybrid) model that became the **standard of the Internet**.

---

# 1.3 OSI Reference Model

## 1.3.1 General Concepts

The **Open Systems Interconnection (OSI) Model** is a **conceptual framework** developed by the **ISO** ($\approx 1984$).
It is designed as a **universal, standardized blueprint** for network communication.

* **GOAL $\rightarrow$ INTEROPERABILITY**: Ensuring that **heterogeneous systems** can communicate.
* **NATURE $\rightarrow$ REFERENCE MODEL**: An "ideal" **7-layer architecture** specifying the functions of each layer.
* **LAYERING**: Decomposing network communication into 7 distinct, **manageable layers**.

# Network Layering Concepts

**Layer Functions**:
* Performs a **specific set of functions**.
* Provides **services** to the layer **above**.
* Consumes **services** from the layer **directly below**.
* Communicates logically **peer-to-peer** with the corresponding layer on the remote **device**.

## 1.3.2 The OSI Layers

> **[Diagram: OSI Model Communication]**
> *Two "End Systems" (stacks of 7 layers) communicating via a "Relay System" (stack of 3 layers).*
> *Horizontal dashed arrows indicate logical protocols (Application, Presentation, Session, Transport).*
> *Vertical arrows indicate physical data flow.*

---

# 1.4 TCP/IP Model

This is the **architecture** underpinning the **global Internet**.

* **Model Type**: A **functional model**, **prioritizing pragmatism** over formal academic distinctions.
* **Structure**: Defines precise specifications for the **protocols** at each layer.

## 1.4.1 Layers
While officially 4 layers, it is often taught using a **5-Layer Hybrid Model**:

* **Layer 5**: Application Layer
* **Layer 4**: Transport Layer (End-to-End)
* **Layer 3**: Internet Layer
* **Layer 2**: Network Access / Data Link Layer
* **Layer 1**: Physical Layer

---

## 1.4.2 Description of the Layers

### Layer 1 - Physical
* Defines the **electrical**, **mechanical**, and **functional interfaces** between the device and the transmission medium.
* **Examples:** Ethernet cabling, Wi-Fi radio frequencies.
> **Note:** Standards like Ethernet and Wi-Fi technically span both **Layer 1 (PHY)** and **Layer 2 (MAC)**.

### Layer 2 - Network Access Layer (Data Link)
* Manages **data exchange** within the local network segment.
* Controls the **sending of frames** and utilizes **48-bit MAC addresses** to identify devices on the **same LAN**.
* **Hardware:** **Switches** (Broadcast address: `FF:FF:FF:FF:FF:FF`).

### Layer 3 - Internet Layer
* Provides **routing** of packets across **interconnected networks** (internetworks).
* Uses logical **IP addresses** (**32-bit IPv4** or **128-bit IPv6**) to identify hosts globally.
* **Hardware:** **Routers**.
> **Data Unit (PDU):** Packet or Datagram.

---

### Layer 4 - Transport Layer
* Provides **end-to-end** data exchange between application processes using **Ports**.
* **TCP (Transmission Control Protocol):** **Connection-oriented**, providing **reliable**, **ordered**, and **error-free** delivery with **flow and congestion control**.
* **UDP (User Datagram Protocol):** **Connection-less** and **unreliable** (best-effort; no ordering/flow control).
> **Data Unit (PDU):** Segment (TCP) or Datagram (UDP).

### Layer 5 - Application Layer
* Implements specific **functions** for user applications (HTTP, SMTP, FTP).
* Protocols here handle logic such as **data formatting** and **session management** (incorporating functions of OSI Presentation/Session layers).

---

## 1.4.4 Addressing Schemes

Three distinct levels of addressing are used in the **TCP/IP model**:

1.  **Physical Address (MAC)**
    * Unique **hardware** ID for the network interface.
    * Assigned by the manufacturer (OUI).
2.  **Internet Address (IP)**
    * **Logical address** identifying the host on the internetwork.
    * Equivalent to **NSAP** in the OSI model.
    * Configured via **software** (static) or protocols like **DHCP** (dynamic assignment).
3.  **Port Number** (Transport)
    * Identifies the specific process/application on the host.

## 1.4.5 Types of PDUs in the TCP/IP Model

> **[Diagram: Encapsulation]**
> *Vertical encapsulation showing the addition of headers at each layer.*

* **Application Level**:
    * **Content**: USER DATA.
    * **PDU**: Application byte stream / Message.
* **Transport Level**:
    * **Encapsulation**: `[ TCP Header | USER DATA ]`
    * **PDU**: **Segment**.
    * **Header Fields**: Source/Destination **Port**.
* **Internet Level**:
    * **Encapsulation**: `[ IP Header | TCP Header | USER DATA ]`
    * **PDU**: **Packet** (or Datagram).
    * **Header Fields**: Source/Destination **IP Address** and **Total Length**.
* **Network Interface Level**:
    * **Encapsulation**: `[ Frame Header | IP Header | TCP Header | USER DATA | FCS ]`
    * **PDU**: **FRAME**.
    * **Header Fields**: Source/Destination **MAC Address** and **EtherType**.

