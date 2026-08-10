---
tags:
  - ProceduralProgramming
  - ExamPrep
  - LinkedLists
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#16-linked-lists]] | [[PRP_Complete_Notes#18-linked-lists-globals-and-implementations]]

# 🔗 Tipologia 3: Gestione di Liste Concatenate Dinamiche (`struct Node`)

Questa tipologia di esercizio (presente in tutti i testi d'esame con punteggio da 6 punti) richiede di scrivere una funzione in C per la manipolazione di liste semplicemente concatenate basate su una struttura `struct Node`.

---

## 📐 Teoria e Requisiti Fondamentali (`PRP_Complete_Notes.md`)

I riferimenti teorici principali nelle note si trovano in **[[PRP_Complete_Notes#16-linked-lists]]** e **[[PRP_Complete_Notes#18-linked-lists-globals-and-implementations]]**.

### Struttura Nodo Standard:
```c
struct Node {
    int info;
    struct Node* pNext;
};
```

### Principi Tassativi per l'Esame:
1. **Gestione dei Casi Limite (Edge Cases):**
   - Lista vuota (`pFirst == NULL` o parametri `NULL`).
   - Modifica del primo elemento (testa della lista).
   - Elemento non presente / Posizione fuori dai limiti della lista.
2. **Allocazione e Deallocazione:**
   - Se l'esercizio richiede di **creare una nuova lista**: verificare sempre se `malloc()` restituisce `NULL` per evitare dereferenziazione di puntatori nulli.
   - Se l'esercizio richiede di **cancellare un nodo**: salvare il puntatore al nodo da eliminare in una variabile temporanea (`tmp`) prima di ricollegare i puntatori, ed eseguire `free(tmp)`.
   - Se l'esercizio vieta espressamente `malloc`/`free` (es. "solo modifica dei collegamenti"): **NON** chiamare `malloc` né `free`, ma ristrutturare unicamente i puntatori `pNext`.
3. **Puntatori Globali vs Locali:**
   - Prestare attenzione se il testo specifica che la lista inizia da un puntatore globale (es. `struct Node* pFirst;`) oppure se la funzione riceve il puntatore alla testa come parametro.

---

## 📝 Schemi e Algoritmi Ricorrenti

### Schema 1: Scorrimento Sicuro con Due Puntatori (`prev` e `curr`)
Utile per cancellazione o inserimento:
```c
struct Node *prev = NULL, *curr = pFirst;
while (curr != NULL && /* condizione */) {
    prev = curr;
    curr = curr->pNext;
}
```

### Schema 2: Costruzione o Partizionamento con `head` e `tail`
Utile per creare nuove liste o riordinare senza deallocare:
```c
struct Node *head = NULL, *tail = NULL;
// Per aggiungere un nodo 'curr' in coda alla nuova lista:
if (head == NULL) {
    head = tail = curr;
} else {
    tail->pNext = curr;
    tail = curr;
}
tail->pNext = NULL;
```

---

## 📑 Soluzioni Complete degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 3 Giugno 2026 (Riordinamento In-Place senza Allocazioni)
**Testo:** Definire una funzione `sposta_dispari_in_testa()` (senza parametri) che riordina la lista spostando in testa tutti i nodi con campo `info` dispari, preservando l'ordine relativo sia dei nodi dispari sia dei nodi pari (i pari restano in coda, nel loro ordine originale). La funzione non deve allocare né deallocare nodi: deve solo modificare i collegamenti. Supporre il puntatore iniziale globale `pFirst`.

**Codice Soluzione:**
```c
void sposta_dispari_in_testa(void) {
    struct Node *dispH = NULL, *dispT = NULL; /* Sottolista nodi dispari */
    struct Node *pariH = NULL, *pariT = NULL; /* Sottolista nodi pari */
    struct Node *curr = pFirst;

    while (curr != NULL) {
        struct Node *next = curr->pNext; /* Salva il successore */
        curr->pNext = NULL;              /* Stacca il nodo corrente */

        if (curr->info % 2 != 0) {       /* NODO DISPARI: accoda a dispari */
            if (dispH == NULL) {
                dispH = dispT = curr;
            } else {
                dispT->pNext = curr;
                dispT = curr;
            }
        } else {                         /* NODO PARI: accoda a pari */
            if (pariH == NULL) {
                pariH = pariT = curr;
            } else {
                pariT->pNext = curr;
                pariT = curr;
            }
        }
        curr = next;
    }

    /* Concatena le due sottoliste: prima i dispari, poi i pari */
    if (dispH == NULL) {
        pFirst = pariH; /* Nessun elemento dispari trovato */
    } else {
        pFirst = dispH;
        dispT->pNext = pariH; /* Collega i pari in coda ai dispari */
    }
}
```

---

### 📌 Caso 2: Esame 22 Giugno 2026 (Cancellazione per Posizione 1-Indexed)
**Testo:** Definire una funzione `canc_elem(int pos)` che prende come parametro un valore intero rappresentante la posizione del nodo da eliminare (partendo da 1 per la testa). Gestire opportunamente i casi in cui `pos` non sia valida o la lista sia vuota. Usare il puntatore globale `pFirst`.

**Codice Soluzione:**
```c
#include <stdlib.h>

void canc_elem(int pos) {
    /* Controlli di validità e lista vuota */
    if (pos < 1 || pFirst == NULL) {
        return;
    }

    /* Caso speciale: eliminazione del primo nodo (testa) */
    if (pos == 1) {
        struct Node *tmp = pFirst;
        pFirst = pFirst->pNext;
        free(tmp);
        return;
    }

    /* Avanza prev fino al nodo in posizione (pos - 1) */
    struct Node *prev = pFirst;
    for (int k = 1; k < pos - 1 && prev != NULL; k++) {
        prev = prev->pNext;
    }

    /* Se la posizione pos non esiste nella lista */
    if (prev == NULL || prev->pNext == NULL) {
        return;
    }

    /* Ricollega i puntatori e dealloca il nodo target */
    struct Node *target = prev->pNext;
    prev->pNext = target->pNext;
    free(target);
}
```

---

### 📌 Caso 3: Esame 15 Gennaio 2026 (Cancellazione Condizionale in Posizione Fissa)
**Testo:** Definire una funzione `cancella_se_3_posizione(int x)` che cancella l'elemento della lista in 3ª posizione se il suo campo `info` non è divisibile per `x`. Supporre puntatore globale `pFirst`.

**Codice Soluzione:**
```c
#include <stdlib.h>

void cancella_se_3_posizione(int x) {
    /* La lista deve contenere almeno 3 nodi per poter valutare la 3ª posizione */
    if (pFirst == NULL || pFirst->pNext == NULL || pFirst->pNext->pNext == NULL) {
        return;
    }

    struct Node *prev = pFirst->pNext; /* Punta al 2° nodo */
    struct Node *curr = prev->pNext;  /* Punta al 3° nodo */

    /* Verifica la divisibilità del valore info per x */
    if (curr->info % x != 0) {
        prev->pNext = curr->pNext; /* Salta il 3° nodo */
        free(curr);                /* Dealloca la memoria del 3° nodo */
    }
}
```

---

### 📌 Caso 4: Esame 13 Febbraio 2026 (Creazione di una Nuova Lista Alternata)
**Testo:** Definire una funzione `alternate` che prende in input due puntatori a liste di elementi (`l1`, `l2`) e restituisce una nuova lista i cui elementi siano presi alternativamente dalle due originali: `elem1_l1, elem1_l2, elem2_l1, elem2_l2, ...`. Gestire i possibili errori di allocazione.

**Codice Soluzione:**
```c
#include <stdlib.h>

struct Node* alternate(struct Node* l1, struct Node* l2) {
    struct Node* head = NULL;
    struct Node* tail = NULL;

    while (l1 != NULL && l2 != NULL) {
        /* 1. Alloca nuovo nodo da l1 */
        struct Node* n1 = (struct Node*)malloc(sizeof(struct Node));
        if (n1 == NULL) return NULL; // Gestione errore allocazione
        n1->info = l1->info;
        n1->pNext = NULL;

        if (head == NULL) {
            head = tail = n1;
        } else {
            tail->pNext = n1;
            tail = n1;
        }

        /* 2. Alloca nuovo nodo da l2 */
        struct Node* n2 = (struct Node*)malloc(sizeof(struct Node));
        if (n2 == NULL) return NULL; // Gestione errore allocazione
        n2->info = l2->info;
        n2->pNext = NULL;

        tail->pNext = n2;
        tail = n2;

        /* Avanza entrambi i puntatori */
        l1 = l1->pNext;
        l2 = l2->pNext;
    }

    /* Gestione dei nodi rimanenti se una lista è più lunga dell'altra */
    struct Node* rem = (l1 != NULL) ? l1 : l2;
    while (rem != NULL) {
        struct Node* nRem = (struct Node*)malloc(sizeof(struct Node));
        if (nRem == NULL) return NULL;
        nRem->info = rem->info;
        nRem->pNext = NULL;

        if (head == NULL) {
            head = tail = nRem;
        } else {
            tail->pNext = nRem;
            tail = nRem;
        }
        rem = rem->pNext;
    }

    return head;
}
```

---

## 💡 Checklist per l'Esame

- [ ] Ho controllato il caso di lista vuota (`NULL`)?
- [ ] Ho salvato il nodo da deallocare prima di modificare `pNext` ed eseguito `free()`?
- [ ] Se ho fatto `malloc()`, ho verificato se il ritorno è `NULL`?
- [ ] Se l'esercizio vietava l'allocazione, ho modificato unicamente i collegamenti `pNext`?
