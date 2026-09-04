#include <stdio.h>

// Definizione globale con Linkage Esterno
int contatore_globale = 100;

// Variabile con Linkage Interno (visibile SOLO in questo file)
static int contatore_privato = 500;

// Funzione con Linkage Interno (visibile solo qui)
static void log_interno(void) {
    printf("[aux.c - static] contatore_privato = %d\n", contatore_privato);
}

// Funzione con Linkage Esterno (chiamabile dal main)
void esegui_step(void) {
    contatore_globale += 10;
    contatore_privato += 1;
    log_interno();
}
