#include <stdio.h>

/* Esercizio Flusso di Controllo e Sequence Points (13 Febbraio 2026) */
void test_flusso_esame(void) {
    printf("=== Test Flusso di Controllo d'Esame ===\n");
    int a = 0xa; // 10 in decimale

    while (a > 8 ? (a--, (a > 7 ? a-- : a)) : a--, a--) {
        if (a + 2 >= 07) { // 07 ottale = 7 decimale
            printf("HERE %d\n", a);
            a != 1; // Istruzione senza effetto
            continue;
            break;  // Irraggiungibile
            printf("NO MORE OK\n");
        }
        printf("EXIT\n");
    }

    // Sequence point al cortocircuito di &&
    a = a++ && a++;
    a += 0xae; // 0xae = 174 decimale
    printf("Valore finale di a: %d\n\n", a);
}

void test_short_circuit(void) {
    printf("=== Test Cortocircuito Logico && e || ===\n");
    int x = 0;
    int y = 5;

    // x e' 0 (falso), quindi ++y NON viene valutato
    if (x && ++y) {
        printf("Non entrera' qui\n");
    }
    printf("Dopo x && ++y: x=%d, y=%d (y e' rimasto 5!)\n", x, y);

    // y e' 5 (vero), quindi ++x NON viene valutato con ||
    if (y || ++x) {
        printf("Entrato nel ramo OR\n");
    }
    printf("Dopo y || ++x: x=%d, y=%d (x e' rimasto 0!)\n\n", x, y);
}

int main(void) {
    test_flusso_esame();
    test_short_circuit();
    return 0;
}
