#include <stdio.h>
#include <stdlib.h>

/* Rotazione Antioraria 90 gradi con VLA (Variable Length Array) */
void rotate90(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice ruotata

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    printf("Matrice Ruotata %dx%d:\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%3d ", B[i][j]);
        }
        printf("\n");
    }
}

/* Estrazione Seconda Diagonale con Allocazione Dinamica */
int *seconda_diagonale(int n, int m[n][n]) {
    if (n <= 0) return NULL;
    int *diag = malloc(n * sizeof(int));
    if (diag == NULL) return NULL;

    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }
    return diag;
}

/* Generatore Sequenza di Fibonacci su Heap */
int *crea_fib(unsigned int n) {
    if (n == 0) return NULL;
    int *v = malloc(n * sizeof(int));
    if (v == NULL) return NULL;

    for (unsigned int i = 0; i < n; i++) {
        if (i < 2) v[i] = 1;
        else v[i] = v[i - 1] + v[i - 2];
    }
    return v;
}

int main(void) {
    printf("=== Test Matrici VLA e Allocazione Heap ===\n\n");

    // 1. Test Rotazione Matrice
    printf("--- 1. Matrice Originale 2x3 ---\n");
    int M[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%3d ", M[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    rotate90(2, 3, M);

    // 2. Test Seconda Diagonale
    printf("\n--- 2. Seconda Diagonale Matrice 3x3 ---\n");
    int Q[3][3] = {
        {11, 12, 13},
        {21, 22, 23},
        {31, 32, 33}
    };
    int *diag = seconda_diagonale(3, Q);
    if (diag) {
        printf("Elementi seconda diagonale: ");
        for (int i = 0; i < 3; i++) {
            printf("%d ", diag[i]);
        }
        printf("\n");
        free(diag);
    }

    // 3. Test Fibonacci Dinamico
    printf("\n--- 3. Primi 10 Numeri di Fibonacci ---\n");
    int *fib = crea_fib(10);
    if (fib) {
        for (int i = 0; i < 10; i++) {
            printf("F(%d)=%d  ", i + 1, fib[i]);
        }
        printf("\n");
        free(fib);
    }

    return 0;
}
