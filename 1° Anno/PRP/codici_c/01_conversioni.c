#include <stdio.h>
#include <limits.h>

/* Esercizio 2 dalla Guida d'Esame */
long int g2(unsigned long p) {
    return p + 'e' - 'a';
}

int g1(int p) {
    char c = 'k';
    return g2(p + c - 'd');
}

void test_esercizio2(void) {
    printf("=== Test Esercizio 2: Conversioni, Wrapping, Promozioni ===\n");
    unsigned short x = -5L; // Wrapping: 65536 - 5 = 65531
    double b = g1(x);
    printf("Valore di x (unsigned short da -5L): %u\n", x);
    printf("Valore finale di b: %f\n\n", b);
}

void test_esercizio3(void) {
    printf("=== Test Esercizio 3: Promozioni e Confronto Signed/Unsigned ===\n");
    int x = 0L, i = -2.5L; // i = -2 (troncamento)
    char a = (char) 70, c = (char) 50;
    char b_val = (char) 70;
    
    // (70 * 70) / 50 -> promozioni a int (4900 / 50 = 98) -> assegna a char
    a = (a * b_val) / c; 
    
    unsigned int limit = 8U;
    long n = 30L;
    
    // Attenzione: i (-2) viene convertito a unsigned int (4294967294U)
    // 4294967294U < 8U e' FALSO!
    if (i < limit) {
        x = limit * n;
        printf("Ramo IF eseguito (inatteso): x = %d\n", x);
    } else {
        printf("Ramo IF NON eseguito perche' (unsigned int)(-2) = %u > %u\n", (unsigned int)i, limit);
    }
    
    printf("Output: a = %d, i = %d\n\n", a, i);
}

int main(void) {
    test_esercizio2();
    test_esercizio3();
    return 0;
}
