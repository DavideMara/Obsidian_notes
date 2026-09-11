---
tags:
  - Algoritmi
  - Modulo1
---
*Back to:* [[00_Index_Algoritmi]]

# Modulo 1 - Algoritmi e Strutture Dati

---

## 1. Strutture Dati Lineari

### 1.1 Array
#### Modello Teorico & Operazioni
Un'array

#### Analisi della Complessità
| Operazione                 | Tempo | Spazio Ausiliario | Note / Spiegazione |
| :------------------------- | :---- | :---------------- | :----------------- |
| **Accesso (get/set)**      |       |                   |                    |
| **Inserimento (add)**      |       |                   |                    |
| **Cancellazione (remove)** |       |                   |                    |

### 1.2 Liste Concatenate (Linked Lists)
#### Modello Teorico & Operazioni
#### Pseudocodice
#### Analisi della Complessità
| Operazione | Tempo | Spazio Ausiliario | Note / Spiegazione |
| :--- | :--- | :--- | :--- |
| **Accesso / Ricerca** | | | |
| **Inserimento (Testa / Coda / Intermedio)** | | | |
| **Cancellazione** | | | |

### 1.3 Liste ad Accesso Limitato: Pile (Stack) e Code (Queue)
#### Pile (Stack - LIFO)
##### Modello Teorico & Operazioni (push, pop, top, isEmpty)
##### Implementazione & Complessità

#### Code (Queue - FIFO) e Code Doppie (Deque)
##### Modello Teorico & Operazioni (enqueue, dequeue, isEmpty)
##### Implementazione & Complessità

### Esercizi & Esempi


---

## 2. Studio della Complessità e Notazione Asintotica

### 2.1 Notazioni Asintotiche e Ordini di Grandezza
#### Definizioni Formali ($O$, $\Omega$, $\Theta$, $o$, $\omega$)
#### Proprietà e Relazioni tra Ordini di Grandezza

### 2.2 Costo delle Operazioni di Base e Strutture di Controllo
#### Operazioni Primitive e Assegnamenti
#### Istruzioni Condizionali (if / else)
#### Cicli Iterativi Semplici e Annidati (for, while)

### 2.3 Analisi di Codici Iterativi
#### Modello Teorico & Invarianti di Ciclo
#### Esercizi Svolti & Casi Notevoli


---

## 3. Equazioni di Ricorrenza e Master Theorem

### 3.1 Tecniche di Risoluzione delle Ricorrenze
#### Metodo di Sostituzione (Induzione)
#### Metodo dell'Albero di Ricorsione
#### Metodo per Iterazione (Srotolamento)

### 3.2 Master Theorem (Teorema Esperto)
#### Enunciato Generale e Forma: $T(n) = a T(n/b) + f(n)$
#### I 3 Casi Fondamentali
#### Casi Particolari ed Estensioni

### 3.3 Analisi di Codici Ricorsivi
#### Modello Teorico & Albero delle Chiamate
#### Esercizi Svolti & Casi Notevoli


---

## 4. Paradigma Divide et Impera e Algoritmi di Ricerca

### 4.1 Il Paradigma Divide et Impera
#### Struttura Generale (Divide, Conquer, Combine)

### 4.2 Algoritmi di Ricerca in Vettori
#### Ricerca Lineare vs Ricerca Binaria (Iterativa e Ricorsiva)
#### Ricerca di Prima e Ultima Occorrenza (Cluster di chiavi)
#### Conteggio Occorrenze

### 4.3 Ricerca di Massimo e Minimo
#### Calcolo del Massimo (TrovaMax)
#### Massimo e Secondo Massimo (Algoritmo del Torneo / Prim-Sec)
#### Minimo in Sequenze Unimodali

### 4.4 Ricerca in Matrici
#### Matrici con Righe e Colonne Ordinate

### 4.5 Conteggio delle Inversioni (Counting Inversions)
#### Modello Teorico & Algoritmo Divide et Impera

### 4.6 Tabella di Riepilogo Complessità Ricerche
| Problema / Algoritmo | Caso Migliore | Caso Peggiore | Caso Medio / Stretto | Spazio Ausiliario |
| :--- | :--- | :--- | :--- | :--- |
| **Ricerca Binaria** | | | | |
| **Prima / Ultima Occorrenza** | | | | |
| **Max e Secondo Max** | | | | |
| **Minimo Unimodale** | | | | |
| **Ricerca in Matrici** | | | | |
| **Conteggio Inversioni** | | | | |

### Esercizi & Esempi


---

## 5. Algoritmi di Ordinamento Basati su Confronti

### 5.1 Algoritmi di Ordinamento Incrementali ed Elementari
#### Insertion Sort
##### Pseudocodice
##### Analisi della Complessità
| Caso | Tempo | Spazio Ausiliario |
| :--- | :--- | :--- |
| **Migliore** | | |
| **Peggiore** | | |
| **Medio** | | |

#### Selection Sort / Reiterate Sort
##### Pseudocodice
##### Analisi della Complessità

#### Bubble Sort
##### Pseudocodice
##### Analisi della Complessità & Conteggio Inversioni

### 5.2 Merge Sort e Varianti
#### Merge Sort Standard (2-Way)
##### Pseudocodice (Merge & MergeSort)
##### Analisi della Complessità

#### Varianti: 3-Way MergeSort e Merge-Insertion Sort (Ibrido)
##### Modello Teorico & Pseudocodice
##### Analisi della Complessità

### 5.3 QuickSort
#### QuickSort Standard
##### Pseudocodice
##### Analisi della Complessità (Migliore, Peggiore, Medio)

#### Procedure di Partizione: Lomuto vs Hoare
##### Pseudocodice Lomuto
##### Pseudocodice Hoare

### 5.4 Limite Inferiore all'Ordinamento e Albero di Decisione
#### Teorema del Limite Inferiore per Confronti ($\Omega(n \log n)$)
#### Albero di Decisione: Definizione e Proprietà

### Esercizi & Esempi


---

## 6. Heaps, HeapSort e Code con Priorità

### 6.1 Struttura Dati Heap
#### Definizioni e Proprietà (Max-Heap, Min-Heap, Forma e Ordine)
#### Rappresentazione Vettoriale dell'Albero (Parent, Left, Right)

### 6.2 Operazioni Fondamentali su Heap
#### Max-Heapify (Ripristino Proprietà di Heap)
##### Pseudocodice
##### Complessità

#### Build-Max-Heap (Costruzione dell'Heap)
##### Pseudocodice
##### Analisi della Complessità ($O(n)$)

### 6.3 Algoritmo HeapSort
#### Idea Intuitiva & Pseudocodice
#### Analisi della Complessità
| Caso | Tempo | Spazio Ausiliario |
| :--- | :--- | :--- |
| **Migliore** | | |
| **Peggiore** | | |
| **Medio** | | |

### 6.4 Code con Priorità (Priority Queues)
#### Operazioni: Insert, Maximum / Extract-Max, Increase-Key
#### Analisi della Complessità delle Operazioni

### Esercizi & Esempi


---

## 7. Algoritmi di Ordinamento in Tempo Lineare

### 7.1 Counting Sort
#### Ipotesi, Idea Intuitiva & Proprietà di Stabilità
#### Pseudocodice
#### Analisi della Complessità (Tempo e Spazio Ausiliario)

### 7.2 Radix Sort
#### Idea Intuitiva & Correttezza (Uso di ordinamento stabile)
#### Pseudocodice
#### Analisi della Complessità

### 7.3 Bucket Sort
#### Ipotesi di Distribuzione & Idea Intuitiva
#### Pseudocodice
#### Analisi della Complessità (Caso Medio e Peggiore)

### 7.4 Tabella Comparativa degli Algoritmi di Ordinamento
| Algoritmo | Tempo Migliore | Tempo Peggiore | Tempo Medio | Spazio Ausiliario | Stabile? | In Place? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Insertion Sort** | | | | | | |
| **Selection Sort** | | | | | | |
| **Bubble Sort** | | | | | | |
| **Merge Sort** | | | | | | |
| **QuickSort** | | | | | | |
| **HeapSort** | | | | | | |
| **Counting Sort** | | | | | | |
| **Radix Sort** | | | | | | |
| **Bucket Sort** | | | | | | |

### Esercizi & Esempi


---

## 8. Statistica d'Ordine e Selezione per Rango

### 8.1 Il Problema della Selezione
#### Definizione di $i$-esima Statistica d'Ordine e Rango
#### Minimo e Massimo Simultaneo (Numero minimo di confronti)

### 8.2 Selezione in Tempo Lineare nel Caso Medio: QuickSelect (Randomized-Select)
#### Idea Intuitiva & Pseudocodice
#### Analisi della Complessità (Caso Migliore, Peggiore, Medio)

### 8.3 Selezione in Tempo Lineare nel Caso Peggiore (Mediana delle Mediane / BFPTR)
#### Idea Intuitiva & Suddivisione in Gruppi
#### Analisi della Complessità

### Esercizi & Esempi
