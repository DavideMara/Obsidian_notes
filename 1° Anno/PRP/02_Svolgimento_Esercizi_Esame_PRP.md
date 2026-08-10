---
tags:
  - ProceduralProgramming
  - ExamPrep
  - Solutions
  - ExamExercises
---
◀️ *Torna all'Indice Generale:* [[00_Index_Programmazione_Procedurale]]

# 📝 Guida Definitiva: Svolgimento Completo degli Esercizi d'Esame — PRP
---
## 🔀 Tipologia 1: Conversioni di Tipo Implicite (Esercizi Svolti)

### 📌 Caso 1.1: Esame 3 Giugno 2026 (Esercizio 1)
**Codice di Partenza:**
```c
unsigned int h2(long int p) {
    return p + 'g' - 'a'; // Riga 2
}
int h1(unsigned int p) {
    float c = 'n'; // Riga 6
    return h2((p + c) - 'b'); // Riga 7
}
int main(void) {
    unsigned short x = -7L; // Riga 11
    double b = h1(x); // Riga 12
    printf("%f \n", b);
}
```

**1. Elenco Completo delle Conversioni Implicite:**
* **Linea 11:** `-7L` (di tipo `long int`) convertito a `unsigned short`. Valore: $-7 + 65536 = 65529$.
* **Linea 12:** `x` (di tipo `unsigned short`) convertito a `unsigned int` (parametro formale `p` di `h1`). Valore: $65529$.
* **Linea 6:** `'n'` (costante di tipo `int`, ASCII 110) convertito a `float` per inizializzare `c`.
* **Linea 7:** `p` (di tipo `unsigned int`) convertito a `float` per effettuare la somma `p + c`.
* **Linea 7:** `'b'` (costante di tipo `int`, ASCII 98) convertito a `float` per la sottrazione `(p + c) - 'b'`.
* **Linea 7:** L'espressione `(p + c) - 'b'` (di tipo `float`) convertita a `long int` (parametro formale `p` di `h2`).
* **Linea 2:** `'g'` e `'a'` (costanti `int`) convertite a `long int` per l'espressione `p + 'g' - 'a'`.
* **Linea 2:** Il risultato di `p + 'g' - 'a'` (di tipo `long int`) convertito a `unsigned int` (tipo di ritorno di `h2`).
* **Linea 7:** Valore di ritorno di `h2` (di tipo `unsigned int`) convertito a `int` (tipo di ritorno di `h1`).
* **Linea 12:** Valore di ritorno di `h1` (di tipo `int`) convertito a `double` (per l'assegnazione a `b`).

**2. Calcolo Valore Finale e Precisione:**
* `x = -7L` $\rightarrow$ `unsigned short` = $65529$.
* In `h1`: `p = 65529U`. `c = 110.0f`.
* `(p + c) - 'b'` = $(65529 + 110.0) - 98.0 = 65639.0 - 98.0 = 65541.0f$.
* In `h2`: `p = 65541L`. `'g' - 'a'` = $103 - 97 = 6$.
* `return 65541 + 6` = $65547$.
* `h2` ritorna `65547U` $\rightarrow$ `h1` ritorna `65547` (int) $\rightarrow$ `b` riceve `65547.0` (double).
* **Valutazione Precisione:** Il valore $65547$ ha 5 cifre significative. Un `double` rappresenta fino a 15-17 cifre significative, quindi è possibile rappresentare il valore **esattamente** senza alcuna perdita di precisione.

---

### 📌 Caso 1.2: Esame 15 Gennaio 2026 (Esercizio 1)
**Codice di Partenza:**
```c
long int g2(unsigned long p) {
    return p + 'e' - 'a'; // Riga 2
}
int g1(int p) {
    char c = 'k'; // Riga 6
    return g2(p + c - 'd'); // Riga 7
}
int main(void) {
    unsigned short x = -5L; // Riga 11
    double b = g1(x); // Riga 12
    printf("%f \n", b);
}
```

**1. Elenco Completo delle Conversioni Implicite:**
* **Linea 11:** `-5L` (tipo `long int`) convertito a `unsigned short`. Valore: $-5 + 65536 = 65531$.
* **Linea 12:** `x` (tipo `unsigned short`) convertito a `int` (parametro formale `p` di `g1`). Valore: $65531$.
* **Linea 6:** `'k'` (tipo `int`, ASCII 107) convertito a `char` (assegnazione a `c`).
* **Linea 7:** `c` (tipo `char`) convertito a `int` (promozione intera in `p + c`).
* **Linea 7:** Risultato di `(p + c - 'd')` (tipo `int`) convertito a `unsigned long` (parametro formale `p` di `g2`).
* **Linea 2:** `'e'` e `'a'` (tipo `int`) convertiti a `unsigned long` (Regola 1: `unsigned long` domina su `int`).
* **Linea 2:** Risultato dell'espressione `p + 'e' - 'a'` (tipo `unsigned long`) convertito a `long int` (ritorno di `g2`).
* **Linea 7:** Valore di ritorno di `g2` (tipo `long int`) convertito a `int` (ritorno di `g1`).
* **Linea 12:** Valore di ritorno di `g1` (tipo `int`) convertito a `double` (assegnazione a `b`).

**2. Calcolo Valore Finale:**
* `x` a linea 11: $-5 + 65536 = 65531$.
* In `g1`: `p = 65531`. `'k' - 'd'` = $107 - 100 = 7$. `p + c - 'd'` = $65531 + 7 = 65538$.
* In `g2`: `p = 65538UL`. `'e' - 'a'` = $101 - 97 = 4$. `return 65538 + 4 = 65542`.
* `b` riceve `65542.0`. 5 cifre significative $\rightarrow$ perfettamente rappresentabile in `double`.

---

### 📌 Caso 1.3: Esame 13 Febbraio 2026 & 30 Gennaio 2026 (Analisi Regole)

#### Esame 13 Febbraio 2026 (Esercizio 1)
```c
int x = 0;
unsigned int limit = 200U;
long n = 30L;
x = limit * n; // Riga 4
```
* **Risposta Corretta:** Si applica la **Regola 2** delle conversioni aritmetiche implicite:
  L'operando `n` ha tipo con segno (`long`) con grado di conversione strettamente più elevato di `limit` (`unsigned int`). Su architetture 64-bit dove `long` è 8 byte, `long` può rappresentare tutti i valori di `unsigned int` (4 byte), quindi `limit` viene convertito a `long` (**Regola 2a**). La moltiplicazione viene eseguita in `long` e il risultato viene infine convertito a `int` per l'assegnazione a `x`.

#### Esame 30 Gennaio 2026 (Esercizio 4)
```c
int i = -1;
unsigned int limit = 200U;
if (i < limit) // Riga 4
    printf("%d", i);
```
* **Risposta Corretta:** Si applica la **Regola 1** delle conversioni aritmetiche implicite:
  Uno degli operandi è `unsigned int` (`limit`), con grado maggiore o uguale a `int` (`i`). L'operando `i` (valore `-1`) viene convertito a `unsigned int` diventando `4294967295U`. La condizione `4294967295U < 200U` risulta **falsa**.

---

## 🔄 Tipologia 2: Tracing di Codice C e Cicli (Esercizi Svolti)

### 📌 Caso 2.1: Esame 3 Giugno 2026 (Esercizio 2)
**Codice:**
```c
int a = 0x1E & 073;
printf("%d\n", a);
while (a % 2 == 0 ? (a >>= 1, a) : (a += 3, 1)) {
    printf("%d\n", a);
    if (a == 6 || a-- == 10) {
        a *= 2;
        break;
    }
    a -= 1;
}
printf("a: %d\n", a);
```

**Tracciamento Passo-Passo:**
1. **Inizializzazione:**
   - `0x1E` = $30 = 00011110_2$.
   - `073` = $59 = 00111011_2$.
   - `a = 30 & 59 = 26` (`00011010_2`).
   - **Stampa 1:** `26`

2. **Trace Table Ciclo `while`:**

| Iterazione | `a` iniziale | Test `while` Condizionale | `a` dopo test | Stampa Corpo | Test `if` & Cortocircuito | Operazioni successive | `a` fine iterazione |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- | :---: |
| **1** | 26 | `26 % 2 == 0` (VERO) $\rightarrow$ `(a >>= 1, a)` | 13 | **`13`** | `13 == 6` (F), `13-- == 10` (F, `a` diventa 12) | `a -= 1` | 11 |
| **2** | 11 | `11 % 2 == 0` (FALSO) $\rightarrow$ `(a += 3, 1)` | 14 | **`14`** | `14 == 6` (F), `14-- == 10` (F, `a` diventa 13) | `a -= 1` | 12 |
| **3** | 12 | `12 % 2 == 0` (VERO) $\rightarrow$ `(a >>= 1, a)` | 6 | **`6`** | `6 == 6` (VERO! Cortocircuito: `a-- == 10` ignorato) | `a *= 2` (12), `break` | 12 (uscita) |

3. **Stampa Finale:** `a: 12`

**Output Finale a Schermo:**
```text
26
13
14
6
a: 12
```

---

### 📌 Caso 2.2: Esame 15 Gennaio 2026 (Esercizio 2)
**Codice:**
```c
int a = 025 + 0x1A;
printf("%d\n", a);
while (a % 2 ? --a : (a >>= 1, 1)) {
    printf("%d\n", a);
    if (a == 3 || a-- == 4) {
        a <<= 1;
        break;
    }
    a /= 2;
}
printf("a: %d\n", a);
```

**Tracciamento Passo-Passo:**
1. **Inizializzazione:** `025` = $21$, `0x1A` = $26$. `a = 21 + 26 = 47`. **Stampa 1:** `47`.
2. **Trace Table:**
   - **Iter 1:** `47 % 2` (VERO) $\rightarrow$ `--a` ($a=46$). **Stampa 2:** `46`. `if(46==3 || 46--==4)` (FALSO, $a=45$). `a /= 2` ($a=22$).
   - **Iter 2:** `22 % 2` (FALSO) $\rightarrow$ `(a >>= 1, 1)` ($a=11$). **Stampa 3:** `11`. `if(11==3 || 11--==4)` (FALSO, $a=10$). `a /= 2` ($a=5$).
   - **Iter 3:** `5 % 2` (VERO) $\rightarrow$ `--a` ($a=4$). **Stampa 4:** `4`. `if(4==3 || 4--==4)` (VERO su secondo termine! Poi $a$ diventa 3). Corpo `if`: `a <<= 1` ($a=6$), `break`.

**Output Finale a Schermo:**
```text
47
46
11
4
a: 6
```

---

### 📌 Caso 2.3: Esame 30 Gennaio 2026 (Esercizio 5 - Undefined Behavior)
**Codice:**
```c
int a= 0x1b, i= 3, *b= &a;
for (int *p= &i; (a-=1) ? (*p++, --a) : ((*p)+=2, a); *p++) {
    a= (a - i);
    printf("%d %d OK\n", a, *p);
    if (a <= 0) {
        a= 1;
        continue;
    }
}
printf("%d %p\n", a, ((short*)b) + 1);
```
* **Analisi Trap:** Il puntatore `p` parte puntando a `i`. Ma l'incremento del ciclo `for` esegue `*p++` (sposta il puntatore `p` alla locazione di memoria successiva).
* Dopo il primo passo, `p` accede a memoria fuori dall'oggetto d'origine (**Undefined Behavior**).
* **Output Teorico Atteso all'Esame:**
```text
22 _ OK
17 _ OK
12 _ OK
7 _ OK
2 _ OK
0 0x7ffee439a000
```

---

## 🔗 Tipologia 3: Liste Concatenate Dinamiche (Esercizi Svolti)

### 📌 Caso 3.1: Esame 3 Giugno 2026 (Riordinamento In-Place senza Allocazioni)
**Testo:** Definire `sposta_dispari_in_testa()` (senza parametri) che riordina la lista spostando in testa tutti i nodi con `info` dispari, preservando l'ordine relativo. Nessuna allocazione/deallocazione (`malloc`/`free`). Usare il puntatore globale `pFirst`.

**Codice Soluzione:**
```c
void sposta_dispari_in_testa(void) {
    struct Node *dispH = NULL, *dispT = NULL; /* Sottolista dispari */
    struct Node *pariH = NULL, *pariT = NULL; /* Sottolista pari */
    struct Node *curr = pFirst;

    while (curr != NULL) {
        struct Node *next = curr->pNext; /* Salva il successore */
        curr->pNext = NULL;              /* Stacca il nodo corrente */

        if (curr->info % 2 != 0) {       /* NODO DISPARI */
            if (dispH == NULL) {
                dispH = dispT = curr;
            } else {
                dispT->pNext = curr;
                dispT = curr;
            }
        } else {                         /* NODO PARI */
            if (pariH == NULL) {
                pariH = pariT = curr;
            } else {
                pariT->pNext = curr;
                pariT = curr;
            }
        }
        curr = next;
    }

    /* Concatena dispari -> pari */
    if (dispH == NULL) {
        pFirst = pariH;
    } else {
        pFirst = dispH;
        dispT->pNext = pariH;
    }
}
```

---

### 📌 Caso 3.2: Esame 22 Giugno 2026 (Cancellazione per Posizione 1-Indexed)
**Testo:** Definire `canc_elem(int pos)` che elimina il nodo in posizione `pos` (1-indexed). Gestire casi limite e deallocare con `free()`. Usare `pFirst`.

**Codice Soluzione:**
```c
#include <stdlib.h>

void canc_elem(int pos) {
    if (pos < 1 || pFirst == NULL) return;

    /* Eliminazione della testa */
    if (pos == 1) {
        struct Node *tmp = pFirst;
        pFirst = pFirst->pNext;
        free(tmp);
        return;
    }

    /* Avanzamento fino alla posizione (pos - 1) */
    struct Node *prev = pFirst;
    for (int k = 1; k < pos - 1 && prev != NULL; k++) {
        prev = prev->pNext;
    }

    if (prev == NULL || prev->pNext == NULL) return; /* Posizione non esistente */

    struct Node *target = prev->pNext;
    prev->pNext = target->pNext;
    free(target);
}
```

---

### 📌 Caso 3.3: Esame 15 Gennaio 2026 (Cancellazione Condizionale 3° Nodo)
**Testo:** Definire `cancella_se_3_posizione(int x)` che elimina il 3° nodo se `info % x != 0`. Usare `pFirst`.

**Codice Soluzione:**
```c
#include <stdlib.h>

void cancella_se_3_posizione(int x) {
    if (pFirst == NULL || pFirst->pNext == NULL || pFirst->pNext->pNext == NULL) {
        return;
    }

    struct Node *prev = pFirst->pNext; /* 2° nodo */
    struct Node *curr = prev->pNext;  /* 3° nodo */

    if (curr->info % x != 0) {
        prev->pNext = curr->pNext;
        free(curr);
    }
}
```

---

### 📌 Caso 3.4: Esame 13 Febbraio 2026 (Creazione Nuova Lista Alternata)
**Testo:** Definire `alternate(l1, l2)` che alloca e restituisce una nuova lista prendendo elementi alternativamente da `l1` e `l2`.

**Codice Soluzione:**
```c
#include <stdlib.h>

struct Node* alternate(struct Node* l1, struct Node* l2) {
    struct Node *head = NULL, *tail = NULL;

    while (l1 != NULL && l2 != NULL) {
        /* Nodo da l1 */
        struct Node* n1 = (struct Node*)malloc(sizeof(struct Node));
        if (n1 == NULL) return NULL;
        n1->info = l1->info; n1->pNext = NULL;
        if (head == NULL) head = tail = n1;
        else { tail->pNext = n1; tail = n1; }

        /* Nodo da l2 */
        struct Node* n2 = (struct Node*)malloc(sizeof(struct Node));
        if (n2 == NULL) return NULL;
        n2->info = l2->info; n2->pNext = NULL;
        tail->pNext = n2; tail = n2;

        l1 = l1->pNext; l2 = l2->pNext;
    }

    struct Node* rem = (l1 != NULL) ? l1 : l2;
    while (rem != NULL) {
        struct Node* nRem = (struct Node*)malloc(sizeof(struct Node));
        if (nRem == NULL) return NULL;
        nRem->info = rem->info; nRem->pNext = NULL;
        if (head == NULL) head = tail = nRem;
        else { tail->pNext = nRem; tail = nRem; }
        rem = rem->pNext;
    }

    return head;
}
```

---

## 📊 Tipologia 4: Matrici e Array Bidimensionali (Esercizi Svolti)

### 📌 Caso 4.1: Esame 13 Febbraio 2026 (Rotazione Matrice 90° Anti-Oraria)
**Testo:** Scrivere `rotate90(int m, int n, int A[m][n])` che crea e stampa la matrice $n \times m$ ruotata di 90° in senso antiorario.

**Formula Indici:** $B[n - 1 - j][i] = A[i][j]$.

**Codice Soluzione:**
```c
#include <stdio.h>

void rotate90(int m, int n, int A[m][n]) {
    int B[n][m];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```

---

### 📌 Caso 4.2: Esame 30 Gennaio 2026 (Estrazione Diagonale Secondaria)
**Testo:** Scrivere `seconda_diagonale(int n, int m[n][n])` che restituisce un array dinamico allocato con `malloc` contenente gli elementi della diagonale secondaria.

**Formula Indici:** `m[i][n - 1 - i]`.

**Codice Soluzione:**
```c
#include <stdlib.h>

int *seconda_diagonale(int n, int m[n][n]) {
    if (n <= 0) return NULL;

    int *diag = (int*)malloc(n * sizeof(int));
    if (diag == NULL) return NULL;

    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }

    return diag;
}
```

---

## 🧠 Tipologia 5: Mappa di Memoria, Puntatori e Little-Endian (7 Punti - Esercizi Svolti)

### 📌 Caso 5.1: Esame 3 Giugno 2026 (Esercizio 5 - 7 Punti)
**Dati:** `long long a[3] = {2048, -3, LLONG_MIN + 768};` `short *p = (short*)a; char *q = (char*)a;`
Modifiche: `p[1]=4098`, `p[3]=4093`, `*(q+15)=73`, `p[9]=16385`.

**Mappa di Memoria Byte per Byte (Little-Endian):**
* Byte 0-1 (`p[0]`): $2048 = 0x0800 \rightarrow$ Byte 0 = `0x00`, Byte 1 = `0x08`.
* Byte 2-3 (`p[1]`): $4098 = 0x1002 \rightarrow$ Byte 2 = `0x02`, Byte 3 = `0x10`.
* Byte 4-5 (`p[2]`): `0x0000`.
* Byte 6-7 (`p[3]`): $4093 = 0x0FFD \rightarrow$ Byte 6 = `0xFD`, Byte 7 = `0x0F`.
* Byte 8-15 (`a[1]`): $-3 \rightarrow$ `p[4]` = $-3$, `p[5]` = $-1$, `p[6]` = $-1$, `p[7]` ha `q[15]=73` ($0x49$) $\rightarrow p[7] = 18943$.
* Byte 16-23 (`a[2]`): `p[8]` = $768$, `p[9]` = $16385$ ($0x4001$), `p[10]` = $0$, `p[11]` = $-32768$.

**Valutazione delle Affermazioni:**
1. **A. `(*(p + 7) - p[8]) % 2`**
   - $(18943 - 768) \% 2 = 18175 \% 2 = 1 \rightarrow$ **VERA (1)**.
2. **B. `(((int)(p + 11) - (int)(a + 2)) + q[18]) % 7`**
   - $(22 - 16) + 1 = 6 + 1 = 7$. $7 \% 7 = 0 \rightarrow$ **FALSA (0)**.
3. **C. `((&p[9] - &p[2]) + p[8]) % 2`**
   - $(9 - 2) + 768 = 7 + 768 = 775$. $775 \% 2 = 1 \rightarrow$ **VERA (1)**.

---

### 📌 Caso 5.2: Esame 22 Giugno 2026 (Esercizio 5 - 7 Punti)
**Dati:** `int a[4] = {5+2*32, INT_MIN + 21, [2]=65540, 262144/2+99};` `short *p = (short*)a; char *q = (char*)a;`
Modifiche: `*(q+3)=-1; *((short int*)&q[5])=257;`

**Valutazione Affermazioni:**
1. **A. `((&a[4] - a) + p[5]) % 2`** $\rightarrow (4 + 1) \% 2 = 1 \rightarrow$ **VERA (1)**.
2. **B. `(((int)(a + 2) - (int)&q[2]) + q[14]) % 2`** $\rightarrow (6 + 2) \% 2 = 0 \rightarrow$ **FALSA (0)**.
3. **C. `((q[12] >> 4) | q[4]) >= 35`** $\rightarrow (6 \ | \ 21) = 23 \ge 35 \rightarrow$ **FALSA (23)**.

---

## 📚 Tipologia 6: Teoria C, Linkage, Zone Memoria e Pipeline GCC (Esercizi Svolti)

### 📌 Caso 6.1: Esame 15 Gennaio 2026 (Linkage e Definizioni)
**Identificatori ed Analisi:**
```c
typedef long int interol;
interol a = 2;                             // Linea 2: Definito, Linkage Esterno
interol a;                                 // Linea 3: Dichiarazione, Linkage Esterno
interol a;                                 // Linea 4: Dichiarazione, Linkage Esterno
extern int b;                              // Linea 5: Dichiarato, Linkage Esterno
static int c = 1;                          // Linea 6: Definito, Linkage Interno
extern long int cfun(float, float);       // Linea 7: Dichiarato, Linkage Esterno

static int *my_func(int d) {              // Linea 9: Definito, Linkage Interno; d: Definito, No Linkage
    static double e = 4.2;                // Linea 10: Definito, No Linkage (Durata Statica)
    double *f = &e;                        // Linea 11: Definito, No Linkage (Durata Automatica)
    int q;                                 // Linea 12: Definito, No Linkage (Durata Automatica)
    extern int c;                          // Linea 13: Dichiarato, Linkage Interno (riferisce riga 6)
}
```

---

### 📌 Caso 6.2: Esame 22 Giugno 2026 (Errori di Linker vs Compilatore)
1. `gcc -c stampa.c`: **Nessun errore di linker** (flag `-c` arresta la pipeline all'assemblatore).
2. `gcc -o prog calc.c`: **ERRORE DI LINKER** (`undefined reference to logga`).
3. `gcc -o stampa stampa.c`: **ERRORE DI LINKER** (`undefined reference to main`).
4. `gcc -c calc.c`: **Nessun errore di linker** (flag `-c`).
5. `gcc calc.c stampa.c -o prog`: **Nessun errore** (linking completato con successo).

---

### 📌 Caso 6.3: Esame 3 Giugno 2026 (Programma C Minimale con Zone di Memoria)
```c
#include <stdio.h>
#include <stdlib.h>

int g_inited = 5;          /* Data Segment (Globale Inizializzata) */
int g_uninited;            /* BSS Segment (Globale Non Inizializzata) */

int main(void) {           /* Text / Code Segment (Istruzioni macchina) */
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
* `main`: **Text Segment**.
* `g_inited` e `s_var`: **Data Segment**.
* `g_uninited`: **BSS Segment**.
* `stack_var` e `heap_ptr`: **Stack**.
* `*heap_ptr`: **Heap**.

---

### 📌 Caso 6.4: Esame 30 Gennaio 2026 (Gestione Memoria Dinamica)
1. *"Le funzioni `malloc()` e `calloc()` restituiscono la quantità di byte allocati."* $\rightarrow$ **FALSO** (restituiscono un puntatore `void*` o `NULL`).
2. *"C'è un errore in: `int a; int *p = &a; free(p);`"* $\rightarrow$ **VERO** (`free()` si applica solo a puntatori dall'Heap).
3. *"`malloc()` alloca memoria ed inizializza i byte a 0."* $\rightarrow$ **FALSO** (memoria non inizializzata; è `calloc()` che azzera).
4. *"`calloc(5,3)` e `malloc(15)` allocano la stessa quantità di memoria."* $\rightarrow$ **VERO** ($15$ byte totali).
