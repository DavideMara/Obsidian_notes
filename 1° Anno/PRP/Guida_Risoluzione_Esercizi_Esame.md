---
tags:
  - ProceduralProgramming
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]] 

#  Prep Esercizi d'Esame (PRP)
##  Mappa degli Argomenti d'Esame

1. [[#1. Conversioni di Tipo Implicite ed Esplicite]] *(Es. 1 / 4 di ogni prova)*
2. [[#2. Mappe di Memoria, Endianness, Complemento a Due e Puntatori]] *(Es. 5 / 7 da 6-7 punti)*
3. [[#3. Tracing di Codice: Operatori, Sequenziamento, Sequence Points]] *(Es. 2 / 4 / 5)*
4. [[#4. Dichiarazioni, Definizioni, Linkage e Scope]] *(Es. 4 del 15 Gennaio)*
5. [[#5. Gestione Dinamica della Memoria (Heap) e Fasi del Compilatore GCC]] *(Es. 1, 2, 3 del 30 Gennaio)*
6. [[#6. Strutture Dati Dinamiche: Liste Collegate]] *(Es. 2 / 3 di scrittura codice)*
7. [[#7. Matrici e VLA (Variable-Length Arrays)]] *(Es. 3 / 6 di matrici 2D)*

---

# 1. Conversioni di Tipo Implicite ed Esplicite

### 🔹 Teoria e Regole di Conversione

#### A. Integer Promotion (Promozione ad Intero)
- Qualsiasi tipo con rango inferiore a `int` (`_Bool`, `char`, `signed char`, `unsigned char`, `short`, `unsigned short`) in un'espressione aritmetica o logica viene automaticamente promosso a:
  - `int` (se `int` può rappresentare tutti i valori del tipo originale);
  - `unsigned int` (altrimenti).
- **Attenzione ai caratteri:** In C, i letterali carattere come `'a'`, `'e'`, `'k'` hanno tipo `int` (valore ASCII: `'a'` = 97, `'b'` = 98, ..., `'k'` = 107).

#### B. Gerarchia di Conversione (Conversion Rank)
$$\text{\_Bool} < \text{char} < \text{short} < \text{int} < \text{long} < \text{long long} < \text{float} < \text{double} < \text{long double}$$

#### C. Usual Arithmetic Conversions (Conversioni Aritmetiche Usuali)
Applicate agli operandi di operatori binari aritmetici (`+`, `-`, `*`, `/`, `%`) e di confronto (`<`, `<=`, `>`, `>=`, `==`, `!=`):
1. **Regola Floating-Point:** Se uno degli operandi è un tipo a virgola mobile, l'altro viene promosso al tipo floating-point di rango più alto.
2. **Regola 1 (Unsigned Dominance):** Se un operando ha tipo `unsigned TipoT` il cui rango è $\ge$ al rango dell'altro operando, l'altro operando è convertito a `unsigned TipoT`.
   - *Esempio tipico d'esame:* `int i = -1; unsigned int limit = 200U; if (i < limit)` $\implies$ `i` è convertito a `unsigned int` (valore $4.294.967.295$), rendendo la condizione **FALSA**.
3. **Regola 2 (Signed Dominance / Fallback):** Se l'operando con rango maggiore ha tipo `signed TipoT`:
   - Se `signed TipoT` può rappresentare **tutti** i valori del tipo dell'altro operando, l'altro operando viene convertito a `signed TipoT`.
   - Se **non** può rappresentarli tutti, entrambi gli operandi vengono convertiti a `unsigned TipoT`.
   - *Esempio tipico d'esame:* `unsigned int limit = 200U; long n = 30L; limit * n` $\implies$ su sistemi a 64 bit (`long` a 64 bit può contenere tutti i valori di `unsigned int` a 32 bit), `limit` viene convertito a `signed long`.

#### D. Wrap-around Modulare per Tipi Unsigned
L'assegnazione di un valore negativo $-v$ a un tipo `unsigned` a $N$ bit applica l'aritmetica modulo $2^N$:
$$\text{valore} = 2^N - v = (\text{UINT\_MAX} + 1) - v$$
- `unsigned short x = -5L;` (16 bit $\implies 2^{16} = 65536$): $\text{valore} = 65536 - 5 = 65531$.
- `int b = -1U;` (32 bit $\implies 2^{32} = 4294967296$): `-1U` vale $4294967295$, assegnato a `int b` memorizza $-1$ in complemento a 2.

#### E. Analisi di Precisione (Float vs Double)
- **`float` (IEEE 754 a 32 bit):** Mantissa a 24 bit $\implies \approx 6\text{--}7$ cifre decimali significative ($2^{24} \approx 16.777.216$). Se un calcolo intero supera $16.777.216$ (es. `UINT_MAX`), un `float` perde precisione per troncamento/arrotondamento.
- **`double` (IEEE 754 a 64 bit):** Mantissa a 53 bit $\implies \approx 15\text{--}17$ cifre decimali significative ($2^{53} \approx 9 \times 10^{15}$). Numeri come $65542$ (5 cifre) sono **esattamente rappresentabili** senza perdita di precisione.

---

# 2. Mappe di Memoria, Endianness, Complemento a Due e Puntatori

### 🔹 Dimensioni Standard dei Tipi
- `char`: 1 byte (8 bit)
- `short` / `short int`: 2 byte (16 bit)
- `int`: 4 byte (32 bit)
- `long long`: 8 byte (64 bit)

### 🔹 Rappresentazione Binaria e Complemento a Due
1. **Numeri Positivi:** Conversione diretta in binario su $N$ bit.
   - $1536 = 1024 + 512 = 2^{10} + 2^9 = \texttt{00000110 00000000}_2 = \texttt{0x0600}$.
2. **Numeri Negativi (Complemento a Due a $N$ bit):**
   - Rappresenta il valore assoluto in binario.
   - Inverti tutti i bit ($\sim$) e aggiungi $1$.
   - *Esempio (-2 su 8 byte / 64 bit):* `0x0000000000000002` $\to$ `0xFFFFFFFFFFFFFFFD` $+ 1 =$ `0xFFFFFFFFFFFFFFFE` (tutti bit a 1 eccetto il bit 0 che vale 0).
   - *Esempio (-67 su 4 byte / 32 bit):* $67 = \texttt{0x00000043} \to \sim 67 + 1 = \texttt{0xFFFFFFBD}$.
3. **Costanti Limite Note:**
   - `INT_MAX` (32 bit): `0x7FFFFFFF` (0 seguito da 31 uni)
   - `INT_MIN` (32 bit): `0x80000000` (1 seguito da 31 zeri, valore $-2^{31}$)
   - `(INT_MAX + INT_MIN) + 1`: `0x7FFFFFFF + 0x80000000 + 1 = (-1) + 1 = 0`.
   - `LLONG_MIN` (64 bit): `0x8000000000000000` (valore $-2^{63}$).
   - `LLONG_MIN + 512`: byte meno significativi = $\texttt{0x0200}$, byte più significativo = $\texttt{0x80}$.

### 🔹 Disposizione in Memoria Little-Endian
Il **Byte meno significativo (LSB)** risiede all'**indirizzo più basso**.
*Esempio:* `short val = 0x1234;`
- Byte 0 (indirizzo basso): `0x34`
- Byte 1 (indirizzo alto): `0x12`

### 🔹 Algoritmo di Risoluzione per la Mappa di Memoria
1. **Traccia la colonna dei byte:** Disegna una tabella verticale partendo dall'indice di byte 0 in alto fino a $N-1$ in basso.
2. **Inizializza l'array:** Riempi i byte con i valori dell'inizializzatore (ricordando di convertire in esadecimale/binario e memorizzare in Little-Endian).
3. **Applica le modifiche sequenziali dei puntatori:**
   - Calcola l'indirizzo esatto in byte:
     $$\text{Offset Byte} = \text{Indice} \times \text{sizeof}(*\text{puntatore})$$
     - `short *p = (short*)a; p[1] = 4098;` $\implies$ modifica i byte $1 \times 2 = 2$ e $3$.
     - `char *q = (char*)a; *(q+15) = 73;` $\implies$ modifica il byte 15.
     - `p[4] += 2048;` $\implies$ legge il valore a 16 bit ai byte 8-9, somma 2048 e riscrive in Little-Endian.
     - `q[19] = ~q[19];` $\implies$ inverte i bit del byte 19.
4. **Verifica delle Asserzioni:**
   - **Sottrazione tra puntatori:** `&p[9] - &p[2]` conta quanti elementi di tipo `short` ci sono tra i due puntatori: $9 - 2 = 7$.
   - **Casting ad intero per differenza indirizzi:** `(int)(p+11) - (int)(a+2)` calcola la differenza in **byte** tra l'indirizzo del byte $11 \times 2 = 22$ e l'indirizzo del byte $2 \times 8 = 16 \implies 22 - 16 = 6$.
   - **Accesso reinterpretato con dereferenziazione:** `*((long long*)(&p[1]))` legge 8 byte consecutivi a partire dal byte 2.

---

# 3. Tracing di Codice: Operatori, Sequenziamento, Sequence Points

### 🔹 Regole di Valutazione delle Espressioni
1. **Basi Numeriche nei Letterali:**
   - `0...` (zero iniziale) $\implies$ **Ottale (Base 8)**: `025` $= 2 \times 8 + 5 = 21$.
   - `0x...` $\implies$ **Esadecimale (Base 16)**: `0x1A` $= 1 \times 16 + 10 = 26$; `0xae` $= 10 \times 16 + 14 = 174$.
2. **Operatore Virgola (`,`)**:
   - Ha la **priorità più bassa** di tutti gli operatori C.
   - Valuta gli operandi da sinistra a destra; produce come risultato il valore dell'operando destro.
   - Introduce un **Sequence Point** tra la valutazione dell'operando sinistro e quello destro.
3. **Operatori Logici di Cortocircuito (`&&`, `||`)**:
   - `A && B`: se `A == 0`, `B` non viene valutato.
   - `A || B`: se `A != 0`, `B` non viene valutato.
   - Introducono un Sequence Point dopo `A`.
4. **Operatore Ternario (`cond ? exp1 : exp2`)**:
   - Introduce un Sequence Point dopo `cond`.
   - Viene eseguito esclusivamente il ramo selezionato.
5. **Warning "Multiple Unsequenced Modifications":**
   - Modificare una variabile due volte tra due sequence point consecutivi provoca **Undefined Behavior**:
     - ❌ `a = a++;` (genera warning / UB)
     - ❌ `a++ + a++;` (genera warning / UB)
     - ✅ `a = 2, a++;` (operatore virgola separa le modifiche con un sequence point $\implies$ NO warning).
     - ✅ `a++ && a++;` (operatore `&&` separa con un sequence point $\implies$ NO warning).
     - ✅ `a++ ? a++ : a++;` (operatore `?:` separa con sequence point $\implies$ NO warning).

---

# 4. Dichiarazioni, Definizioni, Linkage e Scope

Per ogni identificatore occorre stabilire se è **Dichiarato** o **Definito** e determinare il tipo di **Linkage**:

| Costrutto C | Definito / Dichiarato | Tipo di Linkage | Note / Spiegazione |
| :--- | :--- | :--- | :--- |
| `typedef long int interol;` | Definizione di tipo | **Nessun linkage** | Introduce un alias, non alloca spazio di memoria. |
| `interol a = 2;` (globale) | **Definito** | **Esterno** | Alloca memoria e inizializza la variabile globale. |
| `interol a;` (globale ripetuta) | **Dichiarato** | **Esterno** | Tentativo di definizione (*tentative definition*) che si risolve in dichiarazione poiché `a` è già definita. |
| `extern int b;` (globale, senza init) | **Dichiarato** | **Esterno** | Riferimento a una variabile definita in un'altra unità di traduzione. |
| `static int c = 1;` (globale) | **Definito** | **Interno** | Visibile solo all'interno del file sorgente corrente. |
| `extern long int cfun(float, float);` | **Dichiarato** | **Esterno** | Prototipo di funzione. |
| `static int *my_func(int d) { ... }` | **Definito** | **Interno** | Funzione con linkage interno (`static`). |
| Parametro formale `int d` | **Definito** | **Nessun linkage** | Variabile locale allocata nello stack frame. |
| `static double e = 4.2;` (locale) | **Definito** | **Nessun linkage** | Variabile locale con durata statica (segmento dati). |
| `double *f = &e;` (locale) | **Definito** | **Nessun linkage** | Puntatore locale sullo stack. |
| `extern int c;` (locale dentro blocco) | **Dichiarato** | **Interno** (se `c` è già `static` nel file) / **Esterno** | Riferimento alla variabile `c` visibile a livello di file. |

---

# 5. Gestione Dinamica della Memoria (Heap) e Fasi del Compilatore GCC


### 🔹 Funzioni della Memoria Dinamica
1. **`malloc(size_t size)`**:
   - Alloca un blocco contiguo di `size` byte.
   - I byte **non vengono azzerati** (contengono dati casuali).
   - Ritorna `void*` (indirizzo iniziale) o `NULL` in caso di fallimento.
2. **`calloc(size_t num, size_t size)`**:
   - Alloca `num * size` byte e **inizializza tutti i bit a 0**.
   - `calloc(5, 3)` e `malloc(15)` allocano la medesima quantità totale di byte (15 byte).
3. **`realloc(void *ptr, size_t new_size)`**:
   - Prende **due parametri**: puntatore al blocco esistente e nuova dimensione in byte.
   - Ritorna `void*` (può essere lo stesso indirizzo o un nuovo indirizzo se il blocco è stato rilocato; ritorna `NULL`/0 se non c'è memoria sufficiente).
4. **`free(void *ptr)`**:
   - Libera la memoria allocata precedentemente su Heap.
   - ⚠️ **Errore grave:** Passare a `free()` l'indirizzo di una variabile allocata sullo stack (es. `int a; int *p = &a; free(p);`) provoca un crash/errore a runtime.

### 🔹 Le 4 Fasi del Compilatore GCC (in ordine di esecuzione)
$$\text{Preprocessore (cpp)} \longrightarrow \text{Compilatore (cc1)} \longrightarrow \text{Assembler (as)} \longrightarrow \text{Linker (ld)}$$

1. **Preprocessore (`cpp`):** Elabora direttive con `#` (`#include`, `#define`, `#ifdef`), espande le macro e rimuove i commenti.
2. **Compilatore (`cc1`):** Traduce il codice C preprocessato in codice Assembly (`.s`). Effettua il controllo sintattico e semantico.
3. **Assembler (`as`):** Traduce il codice Assembly in codice macchina/oggetto rilocabile binario (`.o`).
4. **Linker (`ld`):** Risolve i riferimenti a simboli esterni e funzioni di libreria, producendo il file eseguibile finale.

---

# 6. Strutture Dati Dinamiche: Liste Collegate

### 🔹 Struttura Base del Nodo
```c
struct Node {
    int info;
    struct Node *pNext;
};
```

### 🔹 Pattern 1: Cancellazione Condizionale con Puntatore Globale
```c
void cancella_se_3_posizione(int x) {
    struct Node *prev, *curr;
    
    /* 1. Controllo preliminare: la lista deve avere almeno 3 nodi */
    if (pFirst == NULL || pFirst->pNext == NULL || pFirst->pNext->pNext == NULL)
        return;
        
    /* 2. Posizionamento: prev punta al secondo nodo, curr al terzo nodo */
    prev = pFirst->pNext;
    curr = prev->pNext;
    
    /* 3. Verifica condizione e ricollegamento */
    if (curr->info % x != 0) {
        prev->pNext = curr->pNext; // Salta il terzo nodo
        free(curr);                 // Dealloca la memoria
    }
}
```

### 🔹 Pattern 2: Costruzione / Fusione di Nuova Lista (Inserimento in Coda $O(1)$)
```c
struct Node* alternate(struct Node *l1, struct Node *l2) {
    struct Node *head = NULL;
    struct Node *tail = NULL;

    while (l1 != NULL && l2 != NULL) {
        // --- Allocazione nodo da l1 ---
        struct Node *n1 = malloc(sizeof(struct Node));
        if (n1 == NULL) return NULL; // Controllo obbligatorio
        n1->info = l1->info;
        n1->pNext = NULL;

        if (head == NULL) {
            head = tail = n1;
        } else {
            tail->pNext = n1;
            tail = n1;
        }

        // --- Allocazione nodo da l2 ---
        struct Node *n2 = malloc(sizeof(struct Node));
        if (n2 == NULL) return NULL;
        n2->info = l2->info;
        n2->pNext = NULL;

        tail->pNext = n2;
        tail = n2;

        // Avanzamento delle liste di input
        l1 = l1->pNext;
        l2 = l2->pNext;
    }
    return head;
}
```

---

# 7. Matrici e VLA (Variable-Length Arrays)

### 🔹 Pattern 1: Estrazione Diagonale Secondaria con Allocazione Dinamica
In una matrice quadrata $n \times n$, gli elementi della diagonale secondaria hanno indici $(i, n - 1 - i)$ con $0 \le i < n$:
```c
int *seconda_diagonale(int n, int m[n][n]) {
    if (n <= 0) return NULL;
    
    int *diag = malloc(n * sizeof(int));
    if (diag == NULL) return NULL;
    
    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }
    return diag;
}
```

### 🔹 Pattern 2: Rotazione Matrice Antioraria di 90°
Una matrice $A$ di dimensione $m \times n$ (righe $\times$ colonne) ruotata in senso antiorario produce una matrice $B$ di dimensione $n \times m$:
$$\text{Elemento } A[i][j] \longrightarrow B[n - 1 - j][i]$$
```c
void rotate90(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice ruotata
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    // Stampa del risultato
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```
