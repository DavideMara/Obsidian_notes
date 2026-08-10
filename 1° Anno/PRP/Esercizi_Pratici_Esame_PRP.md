---
tags:
  - ProceduralProgramming
  - ExamPrep
  - PracticeExercises
---
◀️ *Torna al Master Index:* [[01_Guida_Tipologie_Esami_PRP]] | *Note Teoriche:* [[PRP_Complete_Notes]]

# 🧪 Esercizi d'Esame Pratici da Svolgere (Mock Exam & Practice Set)

Questo file contiene una selezione di **esercizi pratici inediti ma modellati esattamente sul formato delle prove d'esame PRP**. 

Mettiti alla prova risolvendo gli esercizi su un foglio di carta (foglio protocollo), poi espandi le sezioni **"Soluzione e Spiegazione"** per verificare il tuo operato!

---

## 🏋️ Simulazione 1: Prova d'Esame Completa (31 Punti)

---

### Esercizio 1: Conversioni di Tipo Implicite (6 punti)

Analizzare il seguente codice C:

```c
long int f2(unsigned long p) {
    return p + 'f' - 'a'; // Linea 2
}

int f1(int p) {
    char c = 'm'; // Linea 6
    return f2(p + c - 'c'); // Linea 7
}

int main(void) {
    unsigned short x = -8L; // Linea 11
    double b = f1(x); // Linea 12
    printf("%f\n", b);
    return 0;
}
```

**Quesiti:**
1. Elencare tutte le conversioni di tipo implicite riga per riga (da ... a ...).
2. Sapendo che `'a'` vale 97 in ASCII e `USHRT_MAX = 65535`, scrivere il valore finale della variabile `b`.
3. Spiegare se il valore finale `b` è rappresentato esattamente in memoria dal tipo `double` o se vi è perdita di precisione.

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 1</b></summary>

#### 1. Elenco Conversioni Implicite:
- **Linea 11:** `-8L` (di tipo `long int`) convertito a `unsigned short`. Valore: $-8 + 65536 = 65528$.
- **Linea 12:** `x` (di tipo `unsigned short`) convertito a `int` (parametro formale `p` di `f1`). Valore: $65528$.
- **Linea 6:** `'m'` (costante di tipo `int`, ASCII 109) convertita a `char` (assegnazione a `c`).
- **Linea 7:** `c` (di tipo `char`) convertito a `int` per la somma `p + c` (promozione intera).
- **Linea 7:** Risultato di `(p + c - 'c')` (di tipo `int`) convertito a `unsigned long` (parametro `p` di `f2`).
- **Linea 2:** `'f'` e `'a'` (costanti di tipo `int`) convertite a `unsigned long` (Regola 1: `unsigned long` domina).
- **Linea 2:** Risultato dell'espressione `p + 'f' - 'a'` (di tipo `unsigned long`) convertito a `long int` (ritorno di `f2`).
- **Linea 7:** Valore di ritorno di `f2` (di tipo `long int`) convertito a `int` (ritorno di `f1`).
- **Linea 12:** Valore di ritorno di `f1` (di tipo `int`) convertito a `double` (assegnazione a `b`).

#### 2. Calcolo Valore Finale:
- `x` a linea 11: $-8 + 65536 = 65528$.
- In `f1`: `p = 65528`. `'m' - 'c'` = $109 - 99 = 10$. `p + c - 'c'` = $65528 + 10 = 65538$.
- In `f2`: `p = 65538UL`. `'f' - 'a'` = $102 - 97 = 5$. `return 65538 + 5 = 65543`.
- `b` riceve `65543.0`.

#### 3. Precisione:
Il valore $65543$ possiede 5 cifre significative. Poiché un tipo `double` (IEEE 754 a 64 bit) può rappresentare fino a 15-17 cifre decimali significative, il valore è **rappresentato esattamente** senza alcuna perdita di precisione.
</details>

---

### Esercizio 2: Tracing di Codice e Precedenza Operatori (6 punti)

Scrivere cosa stampa a schermo il seguente programma C motivando i passaggi:

```c
#include <stdio.h>

int main(void) {
    int a = 0x17 & 055;
    printf("%d\n", a);
    while (a % 2 == 0 ? (a >>= 1, a) : (a += 5, 1)) {
        printf("%d\n", a);
        if (a == 8 || a-- == 12) {
            a *= 2;
            break;
        }
        a -= 2;
    }
    printf("a: %d\n", a);
    return 0;
}
```

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 2</b></summary>

#### Tracciamento Passo-Passo:
1. **Inizializzazione:**
   - `0x17` = $23 = 00010111_2$.
   - `055` (ottale) = $5 \times 8 + 5 = 45 = 00101101_2$.
   - `a = 23 & 45`:
     ```text
       00010111 (23)
     & 00101101 (45)
     --------------
       00000101 (5)
     ```
   - **Stampa 1:** `5`

2. **Ciclo `while`:**
   - **Iterazione 1:**
     - Test `while`: `a % 2 == 0` ($5 \% 2 == 0$, FALSO).
     - Raggio FALSO del ternario: `(a += 5, 1)`. `a += 5` $\rightarrow a = 10$. Restituisce `1` (VERO).
     - **Stampa 2:** `10`
     - Test `if`: `a == 8` (FALSO). `a-- == 12` ($10 == 12$, FALSO, poi `a` diventa `9`).
     - Esegue `a -= 2` $\rightarrow a = 7$.
   - **Iterazione 2:**
     - Test `while`: `a % 2 == 0` ($7 \% 2 == 0$, FALSO).
     - Raggio FALSO: `(a += 5, 1)`. `a += 5` $\rightarrow a = 12$. Restituisce `1` (VERO).
     - **Stampa 3:** `12`
     - Test `if`: `a == 8` (FALSO). `a-- == 12` ($12 == 12$, VERO! Poi `a` diventa `11`).
     - Esegue corpo `if`: `a *= 2` $\rightarrow a = 11 \times 2 = 22$.
     - `break`: esce dal ciclo `while`.

3. **Stampa Finale:**
   - **Stampa 4:** `a: 22`

#### Output Finale Stampato:
```text
5
10
12
a: 22
```
</details>

---

### Esercizio 3: Gestione Liste Concatenate Dinamiche (6 punti)

Data la struttura nodo:
```c
struct Node {
    int info;
    struct Node* pNext;
};
```
Definire una funzione C `sposta_pari_in_testa()` (senza parametri) che riordina la lista spostando in testa tutti i nodi aventi campo `info` **pari**, mantenendo l'ordine relativo originale sia tra i nodi pari che tra i nodi dispari (i dispari finiscono in coda).

**Vincoli Tassativi:**
- La funzione **non deve allocare né deallocare nodi** (vietato usare `malloc` o `free`).
- Deve modificare unicamente i collegamenti dei puntatori `pNext`.
- Supporre un puntatore globale `pFirst` che punta alla testa della lista.

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 3</b></summary>

```c
#include <stddef.h>

extern struct Node* pFirst;

void sposta_pari_in_testa(void) {
    struct Node *pariH = NULL, *pariT = NULL;   /* Sottolista nodi pari */
    struct Node *dispH = NULL, *dispT = NULL;   /* Sottolista nodi dispari */
    struct Node *curr = pFirst;

    while (curr != NULL) {
        struct Node *next = curr->pNext;  /* Salva il successore */
        curr->pNext = NULL;               /* Stacca il nodo corrente */

        if (curr->info % 2 == 0) {        /* NODO PARI: in coda ai pari */
            if (pariH == NULL) {
                pariH = pariT = curr;
            } else {
                pariT->pNext = curr;
                pariT = curr;
            }
        } else {                          /* NODO DISPARI: in coda ai dispari */
            if (dispH == NULL) {
                dispH = dispT = curr;
            } else {
                dispT->pNext = curr;
                dispT = curr;
            }
        }
        curr = next;
    }

    /* Riconcatena le due liste: prima i pari, poi i dispari */
    if (pariH == NULL) {
        pFirst = dispH; /* Nessun nodo pari */
    } else {
        pFirst = pariH;
        pariT->pNext = dispH; /* Attacca i dispari in coda ai pari */
    }
}
```
</details>

---

### Esercizio 4: Matrici Bidimensionali (5 punti)

Definire una funzione C `ruota90_orario()` che riceve in input una matrice di dimensione $m \times n$ di interi, ne crea una nuova $n \times m$ corrispondente a una **rotazione in senso orario di 90 gradi** e la stampa a schermo (senza restituirla al chiamante).

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 4</b></summary>

#### Mappa Indici per Rotazione Oraria 90°:
- Matrice originale $A$ di dimensione $m \times n$ ($i \in [0, m-1], j \in [0, n-1]$).
- Matrice ruotata $B$ di dimensione $n \times m$.
- Formula di trasformazione: $B[j][m - 1 - i] = A[i][j]$.

```c
#include <stdio.h>

void ruota90_orario(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice VLA ruotata

    // Esegue la rotazione in senso orario
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[j][m - 1 - i] = A[i][j];
        }
    }

    // Stampa la matrice ruotata
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```
</details>

---

### Esercizio 5: Mappa di Memoria, Puntatori e Little-Endian (7 punti)

Dati i seguenti dati:
- `long long a[3] = {1024, -2, LLONG_MIN + 512};`
- `short int *p = (short*) a; char *q = (char*) a;`
- Modifiche eseguite: `p[1] = 2048; p[3] = 4096; *(q+15) = 42; p[9] = 8193;`

Sapendo che `long long` = 8 byte, `short` = 2 byte, `char` = 1 byte in Little-Endian e complemento a 2:

1. Disegnare la mappa di memoria byte per byte.
2. Determina se ciascuna delle seguenti 3 affermazioni è **VERA** o **FALSA** motivando la risposta:
   - **A.** `(*(p + 3) - p[1]) % 2`
   - **B.** `(((int)(p + 9) - (int)(a + 2)) + q[18]) % 2`
   - **C.** `((&p[8] - &p[3]) + p[0]) % 2`

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 5</b></summary>

#### 1. Mappa di Memoria:
- `p[0]` (byte 0-1): $1024 = 0x0400$.
- `p[1]` (byte 2-3): sovrascritto con $2048 = 0x0800$.
- `p[2]` (byte 4-5): $0$.
- `p[3]` (byte 6-7): sovrascritto con $4096 = 0x1000$.
- `p[4]` (byte 8-9): parte di `-2` $\rightarrow -2 = 0xFFFE$.
- `p[5]` (byte 10-11): $-1 = 0xFFFF$.
- `p[6]` (byte 12-13): $-1 = 0xFFFF$.
- `p[7]` (byte 14-15): `*(q+15) = 42`. Il byte 15 diventa $42 = 0x2A$. `p[7]` diventa `0x2AFF` ($10975$).
- `p[8]` (byte 16-17): $512 = 0x0200$.
- `p[9]` (byte 18-19): sovrascritto con $8193 = 8192 + 1 = 0x2001$.

#### 2. Valutazione Affermazioni:

- **A. `(*(p + 3) - p[1]) % 2`**
  - `*(p + 3)` = `p[3]` = $4096$.
  - `p[1]` = $2048$.
  - Differenza: $4096 - 2048 = 2048$.
  - Modulo: $2048 \% 2 = 0$.
  - **Risultato A: FALSA (valore 0)**.

- **B. `(((int)(p + 9) - (int)(a + 2)) + q[18]) % 2`**
  - `(int)(p + 9)` sta al byte offset $9 \times 2 = 18$.
  - `(int)(a + 2)` sta al byte offset $2 \times 8 = 16$.
  - Differenza in byte: $18 - 16 = 2$.
  - `q[18]` corrisponde al LSB di `p[9]` ($8193 = 0x2001 \rightarrow$ LSB = $1$).
  - Somma: $2 + 1 = 3$.
  - Modulo: $3 \% 2 = 1$.
  - **Risultato B: VERA (valore 1)**.

- **C. `((&p[8] - &p[3]) + p[0]) % 2`**
  - `&p[8] - &p[3]` = differenza di elementi `short*` = $8 - 3 = 5$.
  - `p[0]` = $1024$.
  - Somma: $5 + 1024 = 1029$.
  - Modulo: $1029 \% 2 = 1$.
  - **Risultato C: VERA (valore 1)**.
</details>

---

### Esercizio 6: Teoria C, Linkage e Zone di Memoria (4 punti)

1. Spiegare perché il comando `gcc -c modulo.c` **non può generare un errore di linker** del tipo `undefined reference to main`.
2. Considerare la dichiarazione `static int x = 10;` all'interno di una funzione C. Specificare la sua **durata di memorizzazione (storage duration)**, il suo **scope** e il suo **linkage**.

<details>
<summary>🔍 <b>Soluzione e Spiegazione Esercizio 6</b></summary>

#### Risposte:
1. L'opzione `-c` dice a `gcc` di eseguire unicamente la preelaborazione, la compilazione e l'assemblaggio, fermandosi alla produzione del file oggetto `.o`. La fase finale di **linking** (gestita da `ld`) viene **saltata**, pertanto non viene effettuata la risoluzione dei simboli né la ricerca della funzione d'ingresso `main()`.
2. Per `static int x = 10;` definita dentro una funzione:
   - **Durata di memorizzazione:** **Statica** (l'oggetto viene creato all'avvio del programma nel Data Segment e persiste per tutta l'esecuzione).
   - **Scope:** **Locale / di Blocco** (è visibile solo all'interno della funzione in cui è dichiarata).
   - **Linkage:** **Nessun Linkage (No Linkage)** (non può essere riferita fuori dal blocco).
</details>

---

## 💡 Come Continuare ad Esercitarsi
- Consulta il Master Index [[01_Guida_Tipologie_Esami_PRP]] per ripassare le guide teoriche dedicate.
- Rivedi le note teoriche complete in [[PRP_Complete_Notes]].
