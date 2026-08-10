---
tags:
  - ProceduralProgramming
  - ExamPrep
  - Matrices
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#08-arrays]] | [[PRP_Complete_Notes#11-dynamic-memory-management]]

# 📊 Tipologia 4: Matrici e Array Bidimensionali (VLA e Memoria Dinamica)

Questa tipologia di esercizio (presente negli esami con punteggio da 5 a 6 punti) richiede di scrivere funzioni C per la manipolazione di matrici bidimensionali (Variable Length Arrays - VLA introduibili da C99, o matrici allocati dinamicamente).

---

## 📐 Teoria e Regole di Riferimento (`PRP_Complete_Notes.md`)

I riferimenti teorici principali nelle note si trovano in **[[PRP_Complete_Notes#08-arrays]]** e **[[PRP_Complete_Notes#11-dynamic-memory-management]]**.

### 1. Variable Length Arrays (VLA)
Dallo standard C99, è possibile passare matrici multidimensionali con dimensioni variabili formalizzate come parametri antecedenti:
```c
void manipola_matrice(int m, int n, int A[m][n]);
```
* **Impostazione degli Indici:** In C, la memoria per le matrici bidimensionali è allocata in ordine **Row-Major** (riga per riga contigua in memoria).
* L'elemento alla riga `i` e colonna `j` di una matrice $m \times n$ è `A[i][j]`.

### 2. Diagonali di una Matrice Quadrata $n \times n$
* **Diagonale Principale:** Gli elementi dove l'indice di riga è uguale all'indice di colonna: `A[i][i]` per $i = 0, \dots, n-1$.
* **Diagonale Secondaria:** Gli elementi dove la somma degli indici è $n - 1$: `A[i][n - 1 - i]` per $i = 0, \dots, n-1$.

---

## 📑 Soluzioni Complete degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 13 Febbraio 2026 (Rotazione Matrice 90° Anti-Oraria)
**Testo:** Definire una funzione `rotate90()` che prenda in input una matrice di dimensione $m \times n$, e ne crei una $n \times m$ che corrisponde a una rotazione in senso **antiorario** di 90 gradi. La funzione stampa la matrice risultato, ma non la ritorna al chiamante.

**Analisi Indici per Rotazione Antioraria 90°:**
- Matrice sorgente $A$ di dimensione $m \times n$ (riga $i \in [0, m-1]$, colonna $j \in [0, n-1]$).
- Matrice ruotata $B$ di dimensione $n \times m$.
- L'elemento $A[i][j]$ finisce nella riga $n - 1 - j$ e colonna $i$ di $B$:
  $$B[n - 1 - j][i] = A[i][j]$$

**Codice Soluzione:**
```c
#include <stdio.h>

void rotate90(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice ruotata (VLA)

    // Esegui la rotazione antioraria
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    // Stampa la matrice risultato
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```

---

### 📌 Caso 2: Esame 30 Gennaio 2026 (Estrazione Diagonale Secondaria)
**Testo:** Scrivere una funzione che prende una matrice $n \times n$ di valori `int` come parametro e restituisce un array allocato dinamicamente contenente tutti gli elementi sulla **seconda diagonale**.

**Codice Soluzione:**
```c
#include <stdlib.h>

int *seconda_diagonale(int n, int m[n][n]) {
    // Controllo parametri
    if (n <= 0) {
        return NULL;
    }

    // Allocazione dinamica array per contenere n elementi
    int *diag = malloc(n * sizeof(int));
    if (diag == NULL) {
        return NULL; // Errore di allocazione
    }

    // Copia degli elementi della diagonale secondaria
    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }

    return diag;
}
```

---

## 💡 Checklist per l'Esame

- [ ] Ho posizionato i parametri di dimensione ($m, n$) **prima** della matrice nella lista dei parametri della funzione?
- [ ] Ho verificato che l'allocazione con `malloc()` ritorni un puntatore non `NULL`?
- [ ] Ho azzeccato la formula della mappa indici (es. `n - 1 - j` per la rotazione, `n - 1 - i` per la diagonale secondaria)?
