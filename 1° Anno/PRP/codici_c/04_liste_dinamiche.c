#include <stdio.h>
#include <stdlib.h>

struct Node {
    int info;
    struct Node *pNext;
};

// Variabile globale per gli algoritmi d'esame che la usano (es. canc_elem, sposta_dispari_in_testa, inserisci_ordinato)
struct Node *pFirst = NULL;

struct Node* crea_nodo(int val) {
    struct Node *n = malloc(sizeof(struct Node));
    if (!n) {
        perror("malloc fallita");
        exit(EXIT_FAILURE);
    }
    n->info = val;
    n->pNext = NULL;
    return n;
}

void stampa_lista(const char *label, struct Node *head) {
    printf("%s: ", label);
    if (!head) {
        printf("(vuota)\n");
        return;
    }
    struct Node *curr = head;
    while (curr) {
        printf("[%d] -> ", curr->info);
        curr = curr->pNext;
    }
    printf("NULL\n");
}

void libera_lista(struct Node **head_ref) {
    struct Node *curr = *head_ref;
    while (curr) {
        struct Node *tmp = curr->pNext;
        free(curr);
        curr = tmp;
    }
    *head_ref = NULL;
}

/* ==========================================================
 * Algoritmo 1: Fusione Alternata di Due Liste (alternate)
 * ========================================================== */
struct Node* alternate(struct Node *l1, struct Node *l2) {
    struct Node *head = NULL;
    struct Node *tail = NULL;

    while (l1 != NULL && l2 != NULL) {
        // Alloca e inserisce nodo da l1
        struct Node *n1 = malloc(sizeof(struct Node));
        if (n1 == NULL) return NULL;
        n1->info = l1->info;
        n1->pNext = NULL;
        if (head == NULL) head = tail = n1;
        else { tail->pNext = n1; tail = n1; }

        // Alloca e inserisce nodo da l2
        struct Node *n2 = malloc(sizeof(struct Node));
        if (n2 == NULL) return NULL;
        n2->info = l2->info;
        n2->pNext = NULL;
        tail->pNext = n2;
        tail = n2;

        l1 = l1->pNext;
        l2 = l2->pNext;
    }
    return head;
}

/* ==========================================================
 * Algoritmo 2: Cancellazione di un Elemento per Posizione 1-based
 * ========================================================== */
void canc_elem(int pos) {
    if (pos < 1 || pFirst == NULL)
        return;

    // Caso 1: Cancellazione in testa (posizione 1)
    if (pos == 1) {
        struct Node *tmp = pFirst;
        pFirst = pFirst->pNext;
        free(tmp);
        return;
    }

    // Caso 2: Avanzamento fino al nodo in posizione pos - 1
    struct Node *prev = pFirst;
    for (int k = 1; k < pos - 1 && prev != NULL; k++) {
        prev = prev->pNext;
    }

    // Posizione non valida (out of bounds)
    if (prev == NULL || prev->pNext == NULL)
        return;

    // Ricollegamento e deallocazione del nodo target
    struct Node *target = prev->pNext;
    prev->pNext = target->pNext;
    free(target);
}

/* ==========================================================
 * Algoritmo 3: Partizione e Spostamento Dispari in Testa
 * ========================================================== */
void sposta_dispari_in_testa(void) {
    struct Node *dispH = NULL, *dispT = NULL; // Lista dispari
    struct Node *pariH = NULL, *pariT = NULL; // Lista pari
    struct Node *curr = pFirst;

    while (curr != NULL) {
        struct Node *next = curr->pNext;
        curr->pNext = NULL; // Stacca il nodo

        if (curr->info % 2 != 0) { // Elemento Dispari
            if (dispH == NULL) dispH = dispT = curr;
            else { dispT->pNext = curr; dispT = curr; }
        } else {                    // Elemento Pari
            if (pariH == NULL) pariH = pariT = curr;
            else { pariT->pNext = curr; pariT = curr; }
        }
        curr = next;
    }

    // Concatenazione delle due sottoliste
    if (dispH == NULL) {
        pFirst = pariH;
    } else {
        pFirst = dispH;
        dispT->pNext = pariH;
    }
}

/* ==========================================================
 * Algoritmo 4: Inserimento Ordinato Crescente
 * ========================================================== */
void inserisci_ordinato(int x) {
    struct Node *nuovo = malloc(sizeof(struct Node));
    if (nuovo == NULL)
        return;
    nuovo->info = x;

    // Caso 1: Lista vuota o inserimento in testa
    if (pFirst == NULL || x <= pFirst->info) {
        nuovo->pNext = pFirst;
        pFirst = nuovo;
        return;
    }

    // Caso 2: Ricerca della posizione intermedia o in coda
    struct Node *prev = pFirst;
    while (prev->pNext != NULL && prev->pNext->info < x) {
        prev = prev->pNext;
    }

    nuovo->pNext = prev->pNext;
    prev->pNext = nuovo;
}

int main(void) {
    printf("=== Test Algoritmi Liste Dinamiche ===\n\n");

    // 1. Test Inserimento Ordinato
    printf("--- 1. Inserimento Ordinato (5, 2, 8, 1, 9, 4) ---\n");
    inserisci_ordinato(5);
    inserisci_ordinato(2);
    inserisci_ordinato(8);
    inserisci_ordinato(1);
    inserisci_ordinato(9);
    inserisci_ordinato(4);
    stampa_lista("pFirst ordinata", pFirst);

    // 2. Test Sposta Dispari in Testa
    printf("\n--- 2. Sposta Dispari in Testa ---\n");
    sposta_dispari_in_testa();
    stampa_lista("pFirst dopo partizione dispari/pari", pFirst);

    // 3. Test Cancellazione Elemento per Posizione
    printf("\n--- 3. Cancellazione Elementi ---\n");
    canc_elem(1); // Cancella la testa
    stampa_lista("Dopo canc_elem(1) [testa]", pFirst);
    canc_elem(3); // Cancella il 3° elemento
    stampa_lista("Dopo canc_elem(3)", pFirst);

    libera_lista(&pFirst);

    // 4. Test Fusione Alternata
    printf("\n--- 4. Fusione Alternata (alternate) ---\n");
    struct Node *l1 = crea_nodo(10);
    l1->pNext = crea_nodo(20);
    l1->pNext->pNext = crea_nodo(30);

    struct Node *l2 = crea_nodo(100);
    l2->pNext = crea_nodo(200);
    l2->pNext->pNext = crea_nodo(300);

    stampa_lista("Lista L1", l1);
    stampa_lista("Lista L2", l2);

    struct Node *fusa = alternate(l1, l2);
    stampa_lista("Lista Fusa Alternata", fusa);

    libera_lista(&l1);
    libera_lista(&l2);
    libera_lista(&fusa);

    printf("\nFine esecuzione con deallocazione completata.\n");
    return 0;
}
