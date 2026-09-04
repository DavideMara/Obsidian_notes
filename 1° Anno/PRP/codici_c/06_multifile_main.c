#include <stdio.h>

// Dichiarazione di variabile definita in aux.c
extern int contatore_globale;

// Prototipo di funzione definita in aux.c
extern void esegui_step(void);

// Variabile con Linkage Interno (nessun conflitto con contatore_privato in aux.c!)
static int contatore_privato = 1;

int main(void) {
    printf("=== Test Multi-file & Linkage ===\n");
    printf("[main.c] contatore_globale = %d\n", contatore_globale);
    printf("[main.c] contatore_privato (static) = %d\n\n", contatore_privato);

    printf("Chiamata a esegui_step() in aux.c:\n");
    esegui_step();

    printf("\nDopo esegui_step:\n");
    printf("[main.c] contatore_globale = %d\n", contatore_globale);
    printf("[main.c] contatore_privato (static di main) = %d\n", contatore_privato);

    return 0;
}
