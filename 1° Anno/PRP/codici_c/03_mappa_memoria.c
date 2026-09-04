#include <stdio.h>
#include <limits.h>
#include <stdint.h>

void stampa_byte(const char *label, void *ptr, size_t n_bytes) {
    unsigned char *b = (unsigned char *)ptr;
    printf("\n--- Mappa Byte [%s] (%zu bytes) ---\n", label, n_bytes);
    printf("Offset | Hex  | Dec | Binario  | Indirizzo\n");
    printf("-------+------+-----+----------+------------------\n");
    for (size_t i = 0; i < n_bytes; i++) {
        printf("  %2zu   | 0x%02X | %3u | ", i, b[i], b[i]);
        for (int bit = 7; bit >= 0; bit--) {
            printf("%d", (b[i] >> bit) & 1);
        }
        printf(" | %p\n", (void *)&b[i]);
    }
    printf("--------------------------------------------------\n");
}

void test_mappa_1(void) {
    printf("=== Esercizio Mappa di Memoria 1 (8 Luglio 2026) ===\n");
    // a[0] = 131 (0x83), a[1] = INT_MIN + 9, a[2] = 131076, a[3] = 131105
    int a[4] = {3 + 2 * 64, INT_MIN + 9, 131076, 524288 / 4 + 33};
    short int *p = (short *)a;
    char *q = (char *)a;

    printf("Stato iniziale di a: {%d, %d, %d, %d}\n", a[0], a[1], a[2], a[3]);

    // Modifiche
    *(q + 2) = -1;                     // Scrive 0xFF al byte offset 2
    *((short int *)&q[9]) = 513;        // Scrive 513 (0x0201) a offset 9 e 10

    stampa_byte("Array int a[4] dopo modifiche", a, sizeof(a));

    // Valutazione Affermazioni
    int aff_A = ((&a[3] - a) + p[5]) % 2;
    int aff_B = (int)(((intptr_t)(a + 3) - (intptr_t)&q[6]) + q[10]) % 4;
    int aff_C = ((q[12] >> 2) | q[4]) >= 9;

    printf("Affermazione A: ((&a[3] - a) + p[5]) %% 2 = ((3) + %d) %% 2 = %d (Atteso: 1 / VERO)\n", p[5], aff_A);
    printf("Affermazione B: (offset(a+3) - offset(&q[6]) + q[10]) %% 4 = (6 + %d) %% 4 = %d (Atteso: 0 / FALSO)\n", q[10], aff_B);
    printf("Affermazione C: ((q[12] >> 2) | q[4]) >= 9 = ((%d >> 2) | %d) >= 9 -> %d (Atteso: 1 / VERO)\n\n", q[12], q[4], aff_C);
}

void test_mappa_2(void) {
    printf("=== Esercizio Mappa di Memoria 2 (3 Giugno 2026) ===\n");
    long long a[3] = {2048, -3, LLONG_MIN + 768};
    short int *p = (short *)a;
    char *q = (char *)a;

    p[1] = 4098;
    p[3] = 4095 - 2;
    *(q + 15) = 73;
    p[9] = 4096 * 4 + 1;

    stampa_byte("Array long long a[3] dopo modifiche", a, sizeof(a));

    int aff_A = (*(p + 7) - p[8]) % 2;
    int aff_B = (int)(((intptr_t)(p + 11) - (intptr_t)(a + 2)) + q[18]) % 7;
    int aff_C = ((&p[9] - &p[2]) + p[8]) % 2;

    printf("Affermazione A: (*(p + 7) - p[8]) %% 2 = (%d - %d) %% 2 = %d (Atteso: 1 / VERO)\n", *(p + 7), p[8], aff_A);
    printf("Affermazione B: (offset(p+11) - offset(a+2) + q[18]) %% 7 = (6 + %d) %% 7 = %d (Atteso: 0 / FALSO)\n", q[18], aff_B);
    printf("Affermazione C: ((&p[9] - &p[2]) + p[8]) %% 2 = (7 + %d) %% 2 = %d (Atteso: 1 / VERO)\n\n", p[8], aff_C);
}

int main(void) {
    test_mappa_1();
    test_mappa_2();
    return 0;
}
