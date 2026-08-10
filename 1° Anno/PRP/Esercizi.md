
### Esercizio 1 - prova Esame 
```c
double f(float a) {
    // 5. ESECUZIONE DELLA FUNZIONE
    // Il parametro 'a' locale vale 3.0f.
    // Conversione implicita (sottrazione): la costante '1' (int) diventa '1.0f' (float).
    // Calcolo: 3.0f - 1.0f = 2.0f.
    // Conversione implicita (ritorno): '2.0f' (float) diventa '2.0' (double).
    return (a - 1);
}

int main(void) {
    // 1. INIZIALIZZAZIONE DI 'a'
    // Conversione implicita: 3LL (long long int) -> 3 (unsigned int).
    unsigned a = 3LL;          // Valore in memoria: a = 3

    // 2. INIZIALIZZAZIONE DI 'b'
    // L'espressione '-1U' vale 4294967295 (unsigned int).
    // Conversione implicita: 4294967295 (unsigned int) -> -1 (int, in complemento a 2).
    int b = -1U;               // Valore in memoria: b = -1

    // 3 e 4. OPERATORE TERNARIO E ASSEGNAMENTO A 'c'
    // Valutazione condizione (b < a): per confrontarli, 'b' (int) viene promosso 
    // a 'unsigned int'. Il valore -1 diventa 4294967295.
    // Il confronto è: 4294967295 < 3, che è FALSO.
    // L'operatore ternario restituisce il ramo falso: 'a' (che vale 3, unsigned int).
    // Conversione implicita (parametro): 3 (unsigned) -> 3.0f (float) per la funzione f.
    // La funzione f(3.0f) restituisce 2.0 (double).
    // Conversione implicita (assegnamento): 2.0 (double) -> 2.0f (float).
    float c = f((b < a) ? b : a); // Valore in memoria: c = 2.0f

    // 6. CALCOLO FINALE DI 'd'
    // 'UINT_MAX' vale 4294967295.
    // Conversione implicita: UINT_MAX (unsigned int) -> float.
    // PERDITA DI PRECISIONE: 4294967295 necessita di 32 bit esatti, ma il float 
    // ha solo 24 bit di mantissa. Viene arrotondato al valore: 4294967296.0f (2^32).
    //
    // Somma (+ c): 4294967296.0f + 2.0f.
    // ASSORBIMENTO: A 2^32, i float saltano di 256 in 256. Aggiungere 2.0 non 
    // modifica il valore. Rimane 4294967296.0f.
    // 
    // Sottrazione (- 7):
    // Conversione implicita: 7 (int) -> 7.0f (float).
    // ASSORBIMENTO: Sottrarre 7.0f viene ugualmente assorbito dalla limitata precisione.
    float d = UINT_MAX + c - 7;   // Valore finale effettivo calcolato: d = 4294967296.0f
}
```