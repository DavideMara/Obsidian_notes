---
tags:
  - ProceduralProgramming
  - ExamPrep
  - Summary
---
◀️ *Torna all'Indice Generale:* [[00_Index_Programmazione_Procedurale]] | *Note di Riferimento:* [[PRP_Complete_Notes]]

# 🎯 Guida Definitiva alle Tipologie di Esercizi d'Esame — PRP (Programmazione Procedurale)

Questa guida raccoglie, analizza e scompone **ogni singola tipologia di esercizio** presente nella raccolta delle prove d'esame ufficiali (13 Febbraio, 15 Gennaio, 22 Giugno, 30 Gennaio, 3 Giugno, Prova 1).

Ogni sezione fa riferimento diretto alle **note teoriche complete** (`PRP_Complete_Notes.md`) e fornisce schemi risolutivi passo-passo con tutti gli esercizi degli esami svolti nel dettaglio.

---

## 🗺️ Mappa delle Tipologie d'Esame

| Tipologia | Descrizione Esercizio | Punteggio Tipico | File Guida Dedicato | Sezioni Note Riferimento |
| :--- | :--- | :---: | :--- | :--- |
| **Tipologia 1** | Conversioni di Tipo Implicite, Regole & Promozione Aritmetica | 3 - 6 punti | [[Esercizi_Conversioni_Tipo]] | [[PRP_Complete_Notes#05-type-conversions]] |
| **Tipologia 2** | Tracing di Codice, Cicli, Operatori Bitwise & Precedenze | 6 punti | [[Esercizi_Tracing_Output]] | [[PRP_Complete_Notes#06-expressions--operators]] |
| **Tipologia 3** | Gestione Liste Concatenate Dinamiche (`struct Node`) | 6 punti | [[Esercizi_Liste_Concatenate]] | [[PRP_Complete_Notes#16-linked-lists]] |
| **Tipologia 4** | Matrici e Array Bidimensionali (VLA, Diagonali, Rotazioni) | 5 - 6 punti | [[Esercizi_Matrici_Array]] | [[PRP_Complete_Notes#08-arrays]] |
| **Tipologia 5** | Mappa di Memoria, Puntatori, Cast, Little-Endian & Bitwise | **7 punti** | [[Esercizi_Mappa_Memoria_Puntatori]] | [[PRP_Complete_Notes#21-data-representation--computer-arithmetic-c-context]] |
| **Tipologia 6** | Teoria C, Linkage, Zone di Memoria & Pipeline GCC | 3 - 5 punti | [[Esercizi_Teoria_Linkage_Memoria]] | [[PRP_Complete_Notes#15-memory-definitions-duration-and-layout]] |

---

## 🚀 Esercizi Pratici e Simulazioni d'Esame
- Per metterti alla prova con una simulazione d'esame completa e verificare i tuoi risultati con soluzioni dettagliate, consulta: **[[Esercizi_Pratici_Esame_PRP]]**.

---

## 📚 Indice Dettagliato delle Guide

### 1. 🔀 [[Esercizi_Conversioni_Tipo]]
* **Cosa contiene:** Analisi completa delle conversioni da tipo A a tipo B (promozioni intere, Regola 1 Unsigned vs Signed, Regola 2, conversioni a `float`/`double`, calcolo esattezza cifre significative).
* **Prove svolte:** 13 Febbraio (linea 4), 15 Gennaio (funzioni `g1`, `g2`), 3 Giugno (funzioni `h1`, `h2`), 30 Gennaio (linea 4), Prova 1 (funzione `f`).

### 2. 🔄 [[Esercizi_Tracing_Output]]
* **Cosa contiene:** Tecnica di tracciamento tabella iterazioni, gestione cortocircuiti (`&&`, `||`), operatore virgola `,`, operatore ternario `?:`, shift bitwise (`<<`, `>>`), costanti ottali (`073`) ed esadecimali (`0x1E`).
* **Prove svolte:** 13 Febbraio (`while` con ternario), 15 Gennaio (`025 + 0x1A`), 22 Giugno (`goto`), 30 Gennaio (for con `*p++` out of bounds / Undefined Behavior), 3 Giugno (`0x1E & 073`), Prova 1 (`0xfb`).

### 3. 🔗 [[Esercizi_Liste_Concatenate]]
* **Cosa contiene:** Implementazione di funzioni su liste `struct Node` senza memory leak o segmentation fault. Gestione casi limite (`pFirst == NULL`, rimozione testa, elementi non trovati).
* **Prove svolte:**
  - `sposta_dispari_in_testa()` (3 Giugno - 6pt): Riordinamento in-place senza allocazioni.
  - `canc_elem(int pos)` (22 Giugno - 6pt): Cancellazione per posizione 1-indexed.
  - `cancella_se_3_posizione(int x)` (15 Gennaio - 6pt): Cancellazione condizionale 3° nodo.
  - `alternate(l1, l2)` (13 Febbraio - 6pt): Allocazione e alternanza di due liste.

### 4. 📊 [[Esercizi_Matrici_Array]]
* **Cosa contiene:** Manipolazione di matrici bidimensionali VLA (Variable Length Arrays) e allocazione dinamica di array per diagonali o trasformazioni geometriche.
* **Prove svolte:**
  - `rotate90(int m, int n, int A[m][n])` (13 Febbraio - 5pt): Rotazione antioraria 90°.
  - `seconda_diagonale(int n, int m[n][n])` (30 Gennaio - 5pt): Estrazione dinamica diagonale secondaria.

### 5. 🧠 [[Esercizi_Mappa_Memoria_Puntatori]]
* **Cosa contiene:** Costruzione passo-passo della tabella di memoria byte per byte (architettura Little-Endian e Complemento a Due). Dimostrazione e calcolo di affermazioni (A, B, C) con aritmetica dei puntatori (`&p[9] - &p[2]`), differenza in byte `(int)(p+11) - (int)(a+2)` e bitwise (`~`, `&`, `|`, `% 2`).
* **Prove svolte:** Svolgimento dettagliato delle mappe di memoria a 7 punti di tutti gli appelli d'esame.

### 6. 📚 [[Esercizi_Teoria_Linkage_Memoria]]
* **Cosa contiene:**
  - **Linkage e Scope:** Identificazione di Dichiarazione vs Definizione, linkage esterno/interno/no linkage, durata statica/automatica/dinamica.
  - **GCC & Linker:** Analisi errori in compilazione vs linking (`gcc -c` vs `gcc -o`).
  - **Zone di Memoria:** Programma C minimale contenente oggetti in Text, Data, BSS, Stack, Heap.
  - **Memory Management:** Funzionamento e trabocchetti di `malloc()`, `calloc()`, `realloc()`, `free()`.

---

## 💡 Consigli Strategici per l'Esame

1. **Gestione del Tempo:** L'esercizio da 7 punti (Mappa di Memoria - Tipologia 5) richiede attenzione ai dettagli ma segue una procedura rigida. Dedicagli 20-25 minuti all'inizio.
2. **Foglio Protocollo e Brutta:** Scrivi sempre le tabelle di tracciamento (Trace Tables) in brutta prima di ricopiare la soluzione.
3. **Attenzione alle Trappole Frequenti:**
   - Negazione bitwise `~` (ribalta tutti i bit) vs negazione logica `!` (restituisce 0 o 1).
   - Cortocircuito dell'operatore `||` (se il primo valore è vero, il secondo NON viene eseguito).
   - Invocazione di `free()` solo su puntatori restituiti da `malloc`/`calloc`/`realloc`.
   - `gcc -c` non invoca mai il linker, quindi non produce mai errori di `undefined reference`.
