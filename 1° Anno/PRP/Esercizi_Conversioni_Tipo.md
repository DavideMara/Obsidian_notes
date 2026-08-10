---
tags:
  - ProceduralProgramming
  - ExamPrep
  - TypeConversions
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#05-type-conversions]]

# 🔀 Tipologia 1: Conversioni di Tipo Implicite e Promozione Aritmetica

Questa tipologia di esercizio (presente in quasi tutti i testi d'esame con punteggio da 3 a 6 punti) richiede di analizzare un frammento di codice C ed elencare **tutte le conversioni di tipo implicite** riga per riga, specificando il tipo di partenza e di arrivo (`da ... a ...`), la regola applicata e calcolando il valore finale della variabile di output verificando eventuali perdite di precisione.

---

## 📐 Teoria e Regole di Riferimento (`PRP_Complete_Notes.md`)

I riferimenti teorici principali nelle note si trovano in **[[PRP_Complete_Notes#05-type-conversions]]** e **[[PRP_Complete_Notes#21-data-representation--computer-arithmetic-c-context]]**.

### 1. Integer Promotions (Promozioni Intere)
Tutti i tipi interi con grado di conversione inferiore a `int` (`char`, `signed char`, `unsigned char`, `short`, `unsigned short`) usati in un'espressione vengono promossi a:
* **`int`**: se `int` è in grado di rappresentare tutti i valori del tipo originale.
* **`unsigned int`**: altrimenti (raro sulle architetture a 32/64 bit dove `int` è 4 byte e `short` è 2 byte).

### 2. Conversioni Intere Implicite nei Calcoli Operandi (Usual Arithmetic Conversions)
Quando due operandi interi di tipo diverso partecipano a un'operazione binaria:
* **Regola 1 (Unsigned domina per grado $\ge$):**
  Se l'operando $x$ ha tipo `unsigned TipoT` il cui grado di conversione è $\ge$ a quello dell'altro operando $y$, allora l'altro operando $y$ viene convertito ad `unsigned TipoT`.
  * *Esempio:* `int i = -1; unsigned int limit = 200U; if (i < limit)` $\rightarrow$ `i` viene convertito da `int` a `unsigned int`. `-1` in `unsigned int` (32 bit) diventa $2^{32} - 1 = 4294967295$, quindi `-1 < 200U` risulta **FALSO**.
* **Regola 2 (Signed con grado più elevato):**
  Se $x$ ha tipo `signed TipoT` con grado di conversione strettamente maggiore dell'operando $y$ (`unsigned TipoU`):
  * Se `signed TipoT` può rappresentare tutti i valori di `unsigned TipoU`, allora $y$ viene convertito a `signed TipoT`.
  * Altrimenti, entrambi gli operandi vengono convertiti a `unsigned TipoT`.

### 3. Conversioni Floating-Point e Miste
* **Caratteri in Espressioni:** Le costanti carattere (es. `'a'`, `'g'`, `'n'`) hanno tipo `int` in C.
* **Conversioni Miste Integro-Reali:** Se uno degli operandi è `double`, l'altro viene convertito a `double`. Se uno è `float`, l'altro viene convertito a `float`.
* **Assegnazione / Ritorno da Funzione:** Il valore restituito o assegnato viene sempre convertito al tipo della variabile ricevente o della firma della funzione.

### 4. Precisione e Rappresentabilità
* **`float` (IEEE 754 Single Precision):** 32 bit, 24 bit di mantissa $\approx$ **6-7 cifre decimali significative**.
* **`double` (IEEE 754 Double Precision):** 64 bit, 53 bit di mantissa $\approx$ **15-17 cifre decimali significative**.
* **Unsigned Overflow/Wrap-around:** Gli interi `unsigned` lavorano in modulo $2^N$. Ad esempio, assegnare un valore negativo ad un `unsigned short` a 16 bit computa: $\text{valore} + 2^{16} = \text{valore} + 65536$.

---

## 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

1. **Identifica il tipo di ciascuna costante e variabile:**
   - Litera intero semplice (es. `3`): `int`.
   - Literal con suffisso: `3L` $\rightarrow$ `long int`, `3LL` $\rightarrow$ `long long int`, `200U` $\rightarrow$ `unsigned int`.
   - Costante carattere (es. `'a'`): `int`.
   - Inizializzazione negativa di unsigned (es. `unsigned short x = -7L;`): esegui la conversione da `long int` a `unsigned short` applicando la riduzione modulo $65536$.
2. **Traccia le chiamate di funzione e le espressioni nell'ordine di esecuzione:**
   - Analizza la riga di assegnazione in `main`.
   - Segui i parametri passati alla funzione chiamante (conversione da argomento attuale a parametro formale).
   - Analizza ogni riga interna alla funzione (promozioni, calcoli intermedi, conversioni verso floating point).
   - Analizza il valore di ritorno (`return`) convertito al tipo di ritorno dichiarato.
3. **Calcola il valore numerico esatto passo dopo passo:**
   - Applica il wrap-around unsigned se negativo.
   - Esegui le somme/sottrazioni tra codici ASCII (es. `'g' - 'a' = 103 - 97 = 6`).
4. **Verifica la precisione finale:**
   - Confronta il numero di cifre significative del risultato finale con la capacità del tipo di destinazione (`float` vs `double`).

---

## 📑 Analisi degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 3 Giugno 2026 (Esercizio 1)
**Codice:**
```c
unsigned int h2(long int p) {
    return p + 'g' - 'a'; // Riga 2
}
int h1(unsigned int p) {
    float c = 'n'; // Riga 6
    return h2((p + c) - 'b'); // Riga 7
}
int main(void) {
    unsigned short x = -7L; // Riga 11
    double b = h1(x); // Riga 12
    printf("%f \n", b);
}
```

**Soluzione Svolta:**
1. **Elenco Conversioni Implicite:**
   - **Linea 11:** `-7L` (di tipo `long int`) convertito a `unsigned short`. Valore: $-7 + 65536 = 65529$.
   - **Linea 12:** `x` (di tipo `unsigned short`) convertito a `unsigned int` (parametro formale `p` di `h1`). Valore: $65529$.
   - **Linea 6:** `'n'` (costante di tipo `int`, ASCII 110) convertito a `float` per inizializzare `c`.
   - **Linea 7:** `p` (di tipo `unsigned int`) convertito a `float` per effettuare la somma `p + c`.
   - **Linea 7:** `'b'` (costante di tipo `int`, ASCII 98) convertito a `float` per la sottrazione `(p + c) - 'b'`.
   - **Linea 7:** L'espressione `(p + c) - 'b'` (di tipo `float`) convertita a `long int` (parametro formale `p` di `h2`).
   - **Linea 2:** `'g'` e `'a'` (costanti `int`) convertite a `long int` per l'espressione `p + 'g' - 'a'`.
   - **Linea 2:** Il risultato di `p + 'g' - 'a'` (di tipo `long int`) convertito a `unsigned int` (tipo di ritorno di `h2`).
   - **Linea 7:** Valore di ritorno di `h2` (di tipo `unsigned int`) convertito a `int` (tipo di ritorno di `h1`).
   - **Linea 12:** Valore di ritorno di `h1` (di tipo `int`) convertito a `double` (per l'assegnazione a `b`).

2. **Calcolo Valore Finale e Precisione:**
   - `x = -7L` $\rightarrow$ `unsigned short` = $65529$.
   - In `h1`: `p = 65529U`. `c = 110.0f`.
   - `(p + c) - 'b'` = $(65529 + 110.0) - 98.0 = 65639.0 - 98.0 = 65541.0f$.
   - In `h2`: `p = 65541L`. `'g' - 'a'` = $103 - 97 = 6$.
   - `return 65541 + 6` = $65547$.
   - `h2` ritorna `65547U` $\rightarrow$ `h1` ritorna `65547` (int) $\rightarrow$ `b` riceve `65547.0` (double).
   - **Valutazione Precisione:** Il valore $65547$ ha 5 cifre significative. Un `double` rappresenta fino a 15-17 cifre significative, quindi è possibile rappresentare il valore **esattamente** senza alcuna perdita di precisione.

---

### 📌 Caso 2: Esame 15 Gennaio 2026 (Esercizio 1)
**Codice:**
```c
long int g2(unsigned long p) {
    return p + 'e' - 'a'; // Riga 2
}
int g1(int p) {
    char c = 'k'; // Riga 6
    return g2(p + c - 'd'); // Riga 7
}
int main(void) {
    unsigned short x = -5L; // Riga 11
    double b = g1(x); // Riga 12
    printf("%f \n", b);
}
```

**Soluzione Svolta:**
1. **Elenco Conversioni Implicite:**
   - **Linea 11:** `-5L` (tipo `long int`) convertito a `unsigned short`. Valore: $-5 + 65536 = 65531$.
   - **Linea 12:** `x` (tipo `unsigned short`) convertito a `int` (parametro formale `p` di `g1`). Valore: $65531$.
   - **Linea 6:** `'k'` (tipo `int`, ASCII 107) convertito a `char` (assegnazione a `c`).
   - **Linea 7:** `c` (tipo `char`) convertito a `int` (promozione intera in `p + c`).
   - **Linea 7:** Risultato di `(p + c - 'd')` (tipo `int`) convertito a `unsigned long` (parametro formale `p` di `g2`).
   - **Linea 2:** `'e'` e `'a'` (tipo `int`) convertiti a `unsigned long` (Regola 1: `unsigned long` domina su `int`).
   - **Linea 2:** Risultato dell'espressione `p + 'e' - 'a'` (tipo `unsigned long`) convertito a `long int` (ritorno di `g2`).
   - **Linea 7:** Valore di ritorno di `g2` (tipo `long int`) convertito a `int` (ritorno di `g1`).
   - **Linea 12:** Valore di ritorno di `g1` (tipo `int`) convertito a `double` (assegnazione a `b`).

2. **Calcolo Valore Finale e Precisione:**
   - `x` a linea 11: $-5 + 65536 = 65531$.
   - In `g1`: `p = 65531`. `'k' - 'd'` = $107 - 100 = 7$. `p + c - 'd'` = $65531 + 7 = 65538$.
   - In `g2`: `p = 65538UL`. `'e' - 'a'` = $101 - 97 = 4$. `return 65538 + 4 = 65542`.
   - `b` riceve `65542.0`. 5 cifre significative $\rightarrow$ perfettamente rappresentabile in `double`.

---

### 📌 Caso 3: Esame 13 Febbraio 2026 & 30 Gennaio 2026 (Spiegazione Regole)

#### Esame 13 Febbraio 2026 (Esercizio 1)
```c
int x = 0;
unsigned int limit = 200U;
long n = 30L;
x = limit * n; // Riga 4
```
* **Domanda:** Descrivere la regola di conversione applicata alla linea 4.
* **Risposta Corretta:** Si applica la **Regola 2** delle conversioni aritmetiche implicite tra interi:
  Se l'operando $n$ ha tipo con segno (`long`) con grado di conversione strettamente più elevato dell'altro operando `limit` (`unsigned int`), l'operando `limit` viene convertito al tipo con segno `long` *solo se* questo tipo è in grado di rappresentare tutti i valori di `unsigned int` (cosa vera su architetture a 64 bit dove `long` è 8 byte e `unsigned int` è 4 byte). Di conseguenza, `limit` viene convertito da `unsigned int` a `long`, la moltiplicazione viene eseguita in `long` e il risultato viene infine convertito a `int` per l'assegnazione a `x`.

#### Esame 30 Gennaio 2026 (Esercizio 4)
```c
int i = -1;
unsigned int limit = 200U;
if (i < limit) // Riga 4
    printf("%d", i);
```
* **Domanda:** Descrivere la regola di conversione applicata alla linea 4.
* **Risposta Corretta:** Si applica la **Regola 1** delle conversioni aritmetiche implicite tra interi:
  Se in un'espressione binaria uno degli operandi è di tipo `unsigned TipoT` (`limit`, `unsigned int`) il cui grado di conversione è maggiore o uguale a quello dell'altro operando (`i`, `int`), l'altro operando viene convertito ad `unsigned TipoT`. Alla linea 4, l'operando `i` (`int`, valore `-1`) viene convertito a `unsigned int` diventando `4294967295U`. La condizione `4294967295U < 200U` risulta falsa.

---

## 💡 Checklist per l'Esame

- [ ] Ho indicato sia il tipo di **partenza** che quello di **arrivo** per ogni conversione?
- [ ] Ho considerato la promozione da `char`/`short` a `int` prima dei calcoli?
- [ ] Ho ricordato che le costanti carattere come `'a'` sono di tipo `int`?
- [ ] Ho applicato il wrap-around per le assegnazioni negative a tipi `unsigned`?
- [ ] Ho giustificato se il valore finale floating-point è esatto contandone le cifre significative?
