---
tags:
  - ProceduralProgramming
  - ExamPrep
  - CTheory
  - Linkage
  - MemoryZones
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#15-memory-definitions-duration-and-layout]] | [[PRP_Complete_Notes#17-memory-storage-classes-zones-and-the-call-stack]] | [[PRP_Complete_Notes#19-modularization-and-linkage]] | [[PRP_Complete_Notes#20-gcc-compilation-steps-and-gdb-debugging]]

# 📚 Tipologia 6: Teoria C, Linkage, Zone di Memoria e Pipeline di Compilazione

Questa tipologia di esercizio (presente in tutti i testi d'esame con punteggio da 3 a 6 punti) pone domande teoriche precise o richiede di scrivere codice minimale per dimostrare la comprensione dell'architettura di esecuzione del C.

---

## 📐 Teoria e Concetti Chiave (`PRP_Complete_Notes.md`)

I riferimenti teorici principali nelle note si trovano in:
* **[[PRP_Complete_Notes#15-memory-definitions-duration-and-layout]]**
* **[[PRP_Complete_Notes#17-memory-storage-classes-zones-and-the-call-stack]]**
* **[[PRP_Complete_Notes#19-modularization-and-linkage]]**
* **[[PRP_Complete_Notes#20-gcc-compilation-steps-and-gdb-debugging]]**

---

### 1. Fasi della Pipeline di Compilazione GCC
L'invocazione di `gcc` esegue in sequenza quattro strumenti:
$$\text{Sorgente (.c)} \xrightarrow{\text{Preprocessore (cpp)}} \text{.i} \xrightarrow{\text{Compilatore (cc1)}} \text{Assembler (.s)} \xrightarrow{\text{Assemblatore (as)}} \text{Oggetto (.o)} \xrightarrow{\text{Linker (ld)}} \text{Eseguibile}$$

1. **Preprocessore (`cpp`):** Espande le direttive (`#include`, `#define`, `#ifdef`), rimuove i commenti.
2. **Compilatore (`cc1`):** Traduce il C preelaborato in codice Assembly. Effettua il controllo sintattico e semantico.
3. **Assemblatore (`as`):** Traduce il codice Assembly in codice macchina oggetto (`.o`).
4. **Linker (`ld`):** Risolve i simboli esterni e unisce più file oggetto (`.o`) e librerie in un unico file eseguibile.

> [!NOTE]
> L'opzione `gcc -c` blocca l'esecuzione dopo la fase di assemblaggio, producendo il file oggetto `.o` senza invocare il **Linker**. Di conseguenza, `gcc -c` **non genera mai errori di linker** (es. `undefined reference to main`).

---

### 2. Linkage, Scope e Storage Duration
* **Dichiarazione vs Definizione:**
  - **Dichiarazione:** Informa il compilatore del nome e del tipo di un simbolo, senza allocare memoria (es. `extern int b;`, prototipo di funzione `void foo();`).
  - **Definizione:** Riserva effettivamente lo spazio in memoria per la variabile o fornisce il corpo della funzione (es. `int a = 2;`).
  - **Tentative Declaration (Dichiarazione Tentativa):** In C, una variabile globale senza specificatore `extern` e senza inizializzazione (es. `int a;` a livello di file) è una dichiarazione tentativa che diventa definizione se non ve ne sono altre.
* **Tipi di Linkage:**
  - **Esterno (External Linkage):** Il simbolo è visibile in tutti i file oggetto del progetto (variabili globali non `static`, funzioni non `static`).
  - **Interno (Internal Linkage):** Il simbolo è visibile solo all'interno del singolo file translation unit (`static` a livello di file globale).
  - **Nessun Linkage (No Linkage):** Il simbolo è locale a un blocco o funzione (variabili locali, parametri di funzione, `static` locali).
* **Durata di Memorizzazione (Storage Duration):**
  - **Statica:** Esiste per tutta la durata dell'esecuzione del programma (variabili globali, `static` locali).
  - **Automatica:** Creata all'ingresso del blocco/funzione e distrutta all'uscita (variabili locali, parametri).
  - **Dinamica:** Gestita manualmente dal programmatore tramite `malloc()`/`free()` nell'Heap.

---

### 3. Le 5 Zone di Memoria di un Programma C
1. **Text / Code Segment:** Contiene le istruzioni in codice macchina eseguibile. Read-only.
2. **Data Segment (Inizializzato):** Contiene variabili globali e `static` con inizializzazione esplicita diversa da zero.
3. **BSS Segment (Uninitialized Data):** Contiene variabili globali e `static` non inizializzate (azzerate all'avvio dal loader).
4. **Heap:** Zona per l'allocazione dinamica gestita a runtime via `malloc()`, `calloc()`, `realloc()`, `free()`. Cresce verso indirizzi alti.
5. **Stack:** Contiene i frame di attivazione delle funzioni (variabili locali, parametri formali, indirizzi di ritorno). Cresce verso indirizzi bassi.

---

## 📑 Soluzioni Complete degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 15 Gennaio 2026 (Analisi Linkage e Definizioni)
**Testo:** Per ogni identificatore di variabile e funzione scrivere se è definito o dichiarato, e il suo linkage.

```c
typedef long int interol;
interol a = 2;                             // Linea 2
interol a;                                 // Linea 3
interol a;                                 // Linea 4
extern int b;                              // Linea 5
static int c = 1;                          // Linea 6
extern long int cfun(float, float);       // Linea 7

static int *my_func(int d) {              // Linea 9
    static double e = 4.2;                // Linea 10
    double *f = &e;                        // Linea 11
    int q;                                 // Linea 12
    extern int c;                          // Linea 13
}
```

**Soluzione Svolta:**
- **Linea 2 (`interol a = 2`):** **Definito**, Linkage **Esterno**.
- **Linea 3 (`interol a`):** Dichiarazione tentativa (rimane **Dichiarazione** poiché `a` è già definita alla linea 2), Linkage **Esterno**.
- **Linea 4 (`interol a`):** Dichiarazione tentativa (rimane **Dichiarazione**), Linkage **Esterno**.
- **Linea 5 (`extern int b`):** **Dichiarto**, Linkage **Esterno**.
- **Linea 6 (`static int c = 1`):** **Definito**, Linkage **Interno**.
- **Linea 7 (`cfun`):** **Dichiarto**, Linkage **Esterno**.
- **Linea 9 (`my_func`):** **Definito**, Linkage **Interno**.
- **Linea 9 (`d`):** **Definito**, **No Linkage** (parametro di funzione, durata automatica).
- **Linea 10 (`e`):** **Definito**, **No Linkage** (locale statico, durata statica).
- **Linea 11 (`f`):** **Definito**, **No Linkage** (variabile locale, durata automatica).
- **Linea 12 (`q`):** **Definito**, **No Linkage** (variabile locale, durata automatica).
- **Linea 13 (`extern int c`):** **Dichiarto**, Linkage **Interno** (riferisce la definizione con linkage interno alla linea 6).

---

### 📌 Caso 2: Esame 22 Giugno 2026 (Errori di Linker vs Compilatore)
**Testo:** Dire quali invocazioni `gcc` provocano errore a causa del **linker** (e perché):
1. `gcc -c stampa.c`
2. `gcc -o prog calc.c`
3. `gcc -o stampa stampa.c`
4. `gcc -c calc.c`
5. `gcc calc.c stampa.c -o prog`

**Soluzione Svolta:**
1. `gcc -c stampa.c`: **Nessun errore di linker**. Il flag `-c` compila soltanto e produce `stampa.o`. Il linker non viene invocato.
2. `gcc -o prog calc.c`: **ERRORE DI LINKER**. La funzione `logga` invocata in `calc.c` non è definita nel file (errore: `undefined reference to logga`).
3. `gcc -o stampa stampa.c`: **ERRORE DI LINKER**. Manca la definizione della funzione `main()` e della variabile `totale` (errore: `undefined reference to main`).
4. `gcc -c calc.c`: **Nessun errore di linker**. Flag `-c` interrompe prima del linking.
5. `gcc calc.c stampa.c -o prog`: **Nessun errore**. Tutti i simboli si risolvono con successo.

---

### 📌 Caso 3: Esame 3 Giugno 2026 (Programma Minimale con Zone di Memoria)
**Testo:** Scrivere un programma minimale compilabile senza errori, avente un oggetto memorizzato in ciascuna zona di memoria vista a lezione. Descrivere la zona di ogni oggetto.

**Codice Soluzione:**
```c
#include <stdio.h>
#include <stdlib.h>

int g_inited = 5;          /* Data Segment (Globale Inizializzata) */
int g_uninited;            /* BSS Segment (Globale Non Inizializzata) */

int main(void) {
    int stack_var = 10;    /* Stack (Variabile locale automatica) */
    static int s_var = 7;  /* Data Segment (Static locale inizializzata) */
    
    int *heap_ptr = (int*)malloc(sizeof(int)); /* Heap (Memoria allocata dinamicamente) */
    if (heap_ptr != NULL) {
        *heap_ptr = 20;
        free(heap_ptr);
    }
    
    return 0;
}
```

**Descrizione Zone:**
* `main`: Il codice eseguibile delle istruzioni risiede nel **Text/Code Segment**.
* `g_inited` e `s_var`: Risiedono nel **Data Segment** (durata statica, valore iniziale esplicito).
* `g_uninited`: Risiede nel **BSS Segment** (durata statica, inizializzata a 0 di default).
* `stack_var` e `heap_ptr`: Risiedono nello **Stack** (variabili locali all'attivazione di `main`).
* `*heap_ptr` (la memoria puntata): Risiede nell'**Heap** (allocata via `malloc`).

---

### 📌 Caso 4: Esame 30 Gennaio 2026 (Gestione Memoria Dinamica - Vero/Falso)
1. *"Le funzioni `malloc()` e `calloc()` restituiscono la quantità di byte allocati."* $\rightarrow$ **FALSO**. Restituiscono un puntatore generico `void*` all'indirizzo di memoria allocato (o `NULL` se falliscono).
2. *"C'è un errore in: `int a; int *p = &a; free(p);`"* $\rightarrow$ **VERO**. `free()` deve essere chiamata **solo** su puntatori restituiti da `malloc`/`calloc`/`realloc`. Chiamarla su un indirizzo dello Stack causa undefined behavior / crash.
3. *"`malloc()` alloca la memoria ed inizializza tutti i byte a 0."* $\rightarrow$ **FALSO**. `malloc()` lascia la memoria **non inizializzata** (contiene valori spazzatura). È `calloc()` che azzera i byte.
4. *"`calloc(5,3)` e `malloc(15)` allocano la stessa quantità di byte in memoria."* $\rightarrow$ **VERO**. Entrambe allocano $5 \times 3 = 15$ byte totali.

---

## 💡 Checklist per l'Esame

- [ ] Ho verificato se il comando `gcc` contiene l'opzione `-c` (che impedisce errori di linker)?
- [ ] Ho distinto la variabile locale puntatore (`stack`) dalla blocco puntato allocato con `malloc` (`heap`)?
- [ ] Ho ricordato che una variabile `static` locale ha durata **statica** ma scope **locale** (no linkage)?
