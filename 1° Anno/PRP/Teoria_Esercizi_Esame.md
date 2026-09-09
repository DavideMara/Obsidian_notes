---
tags:
  - ProceduralProgramming
---
# 1. Conversioni di Tipo Implicite ed Esplicite, Promozioni e Valutazione delle Espressioni

### 🔹 1.1 Grado di Conversione dei Tipi Interi (Ranking C99 §6.3.1.1)
Ogni tipo possiede un grado (*conversion rank*) che stabilisce le priorità nelle conversioni aritmetiche:

* **Gerarchia dei Tipi Interi (dal grado più basso al più alto):**
  $$\text{\_Bool} < \text{char} < \text{short} < \text{int} < \text{long} < \text{long long}$$
  * Un tipo `signed` e il corrispondente `unsigned` hanno lo **stesso grado** (es. $\text{rank}(\text{int}) == \text{rank}(\text{unsigned int})$).
  * `signed char` e `unsigned char` hanno lo stesso grado di `char`.
  * `unsigned short` ha lo stesso grado di `short`.
  * `unsigned long` ha lo stesso grado di `long`.
  * Le enumerazioni (`enum`) hanno lo stesso grado di `int`.

* **Gerarchia dei Tipi Floating Point:**
  $$\text{float} < \text{double} < \text{long double}$$
  * Qualsiasi tipo a virgola mobile (`float`, `double`, `long double`) ha un rango **strettamente superiore a qualunque tipo intero**.

---

### 🔹 1.2 Promozioni Intere (*Integer Promotions* §6.3.1.1)
Prima di qualsiasi operazione aritmetica, logica o bitwise, i tipi più piccoli di `int` (`char`, `signed char`, `unsigned char`, `short`, `unsigned short`, `_Bool`) subiscono **sempre** la promozione a:
1. `int`: se un `int` è in grado di rappresentare tutti i valori del tipo originale.
2. `unsigned int`: se un `int` non può rappresentare tutti i valori (es. `unsigned short` su architetture a 16 bit dove `sizeof(short) == sizeof(int)`).

> 💡 **Esempio:** Nelle espressioni `char a = 70, b = 70; a * b;`, entrambi gli operandi `a` e `b` vengono promossi a `int` prima di eseguire la moltiplicazione. Il risultato intermedio è di tipo `int`.

---

### 🔹 1.3 Conversioni Aritmetiche Consuete (*Usual Arithmetic Conversions* §6.3.1.8)
Quando un operatore binario (`+`, `-`, `*`, `/`, `%`, `<`, `>`, `==`, `&`, `|`, `^`, ecc.) opera su tipi differenti, si applicano le seguenti regole in ordine:

#### 1. Regola Floating Point:
Se almeno un operando è un tipo a virgola mobile:
* Se uno è `long double` $\implies$ l'altro è convertito a `long double`.
* Altrimenti, se uno è `double` $\implies$ l'altro è convertito a `double`.
* Altrimenti, se uno è `float` $\implies$ l'altro è convertito a `float`.

#### 2. Regole tra Tipi Interi (dopo le promozioni intere):
Se entrambi gli operandi sono interi:
* **Stesso Segno:** Se entrambi sono signed o entrambi sono unsigned, l'operando con grado inferiore è convertito al tipo con grado superiore.
* **Segno Diverso - Caso Unsigned $\ge$ Signed (Regola 1 slide):**
  Se l'operando **unsigned** ha grado di conversione **maggiore o uguale** a quello dell'operando signed $\implies$ l'operando con segno viene convertito a **unsigned** del tipo di grado maggiore (o uguale).
  * *Esempio:* `int` e `unsigned int` $\implies$ `int` convertito a `unsigned int`.
  * *Esempio:* `int` e `unsigned long` $\implies$ `int` convertito a `unsigned long`.
* **Segno Diverso - Caso Signed $>$ Unsigned (Regola 2 slide):**
  Se l'operando **signed** ha grado di conversione **strettamente maggiore** dell'operando unsigned:
  * **Sottocaso A:** Se il tipo `signed` può rappresentare **tutti** i valori del tipo `unsigned` $\implies$ l'operando unsigned viene convertito al tipo `signed`.
    * *Esempio su architettura 64-bit:* `long` (64 bit) e `unsigned int` (32 bit). Poiché `long` può contenere tutti i valori di `unsigned int` (da $0$ a $2^{32}-1$), l'`unsigned int` viene convertito a `long`.
  * **Sottocaso B:** Se il tipo `signed` **NON** può rappresentare tutti i valori del tipo `unsigned` (es. entrambi a 32 bit o entrambi a 64 bit) $\implies$ **entrambi** gli operandi sono convertiti al tipo **`unsigned` corrispondente al tipo signed** (es. `unsigned long`).

---

### 🔹 1.4 Conversioni in Assegnamento, Chiamate a Funzione e Return
1. **Assegnamento (`=`):** Il valore a destra viene convertito forzatamente al tipo della variabile a sinistra.
   * Se da tipo più grande a tipo intero più piccolo con segno $\implies$ troncamento dei bit più significativi.
   * Se da floating point a intero $\implies$ troncamento della parte decimale (es. `-2.5L` $\to$ `-2`).
2. **Passaggio di Parametri:** Il valore dell'argomento attuale viene convertito al tipo del parametro formale dichiarato nel prototipo.
3. **Valore di Ritorno (`return`):** Il valore restituito viene convertito al tipo di ritorno dichiarato della funzione.
4. **Operatore Condizionale Ternario (`? :`):** Il secondo e il terzo operando subiscono le *Usual Arithmetic Conversions* per determinare il tipo comune dell'espressione risultante.

---

### 🔹 1.5 Calcolo Numerico del Valore Finale: Wrapping Unsigned e Precisione
* **Wrapping dei Tipi Unsigned (Aritmetica Modulo $2^N$):**
  Nei tipi `unsigned`, l'overflow non è Undefined Behavior, ma è definito per legge dallo standard come aritmetica modulare:
  $$\text{Valore Unsigned} = \text{valore} \pmod{2^N} = \text{valore} \pmod{(\text{UMAX} + 1)}$$
  * Assegnare un numero negativo `-k` a un `unsigned short` (con $\text{USHRT\_MAX} = 65535$):
    $$-k \pmod{65536} = 65536 - k = (\text{USHRT\_MAX} + 1) - k$$
    * `-2L` assegnato a `unsigned short` $\implies 65536 - 2 = 65534$.
    * `-5L` assegnato a `unsigned short` $\implies 65536 - 5 = 65531$.
    * `-7L` assegnato a `unsigned short` $\implies 65536 - 7 = 65529$.
* **Precisione Floating Point e Rappresentabilità:**
  * Un tipo `float` a 32 bit (IEEE 754) ha 24 bit di mantissa $\approx 7$ cifre decimali di precisione.
  * Un tipo `double` a 64 bit ha 53 bit di mantissa $\approx 15\text{--}17$ cifre decimali di precisione.
  * *Domanda d'esame frequente:* "È possibile stabilire il valore esatto della variabile `b`?"
    * Se il risultato intero ha $\le 15$ cifre significative ed è memorizzato in un `double` $\implies$ **Sì, è rappresentabile esattamente**.
    * Se un intero grande (es. `UINT_MAX + c`) supera la precisione di un `float` (che ha solo 7 cifre) $\implies$ si ha perdita di precisione per arrotondamento della mantissa.

---

### 🔹 1.6 Metodologia Risolutiva per l'Esercizio d'Esame sulle Conversioni
Per ogni operazione nel codice, tracciare in ordine:
1. **Cast espliciti:** Segnalare se la conversione è esplicita (es. `(char)70`).
2. **Inizializzazioni e Assegnamenti:** Tracciare la conversione del letterale/valore al tipo della variabile a sinistra.
3. **Promozioni Intere:** Tracciare ogni `char`/`short` promosso a `int` prima di operare.
4. **Operazioni Binarie:** Identificare il tipo di ciascun operando e specificare quale regola si applica (es. da `int` a `unsigned int`, o da `long` a `unsigned long`).
5. **Chiamate e Ritorno di Funzione:** Tracciare argomenti convertiti al tipo del parametro formale e valori restituiti convertiti al tipo di ritorno.
6. **Calcolo Matematico Finale:** Eseguire i calcoli applicando il wrapping modulare unsigned e i codici ASCII indicati (es. `'a' = 97`, `'b' = 98`, ecc.).

---

### 🔹 1.7 Esercizi d'Esame Svolti e Risolti

#### 📌 Esercizio 1 (Esame 13 Febbraio 2026 / 30 Gennaio 2026)
```c
int x = 0;
unsigned int limit = 200U;
long n = 30L;
x = limit * n; // Linea 4
```
* **Descrizione Regola Applicata alla Linea 4:**
  * Si applica la **Regola del Segno Diverso (Signed > Unsigned, Regola 2 slide)**: `n` ha tipo `long` (signed) con grado di conversione superiore a `limit` (`unsigned int`).
  * *Se `long` è a 64 bit:* `long` può rappresentare tutti i valori di `unsigned int` $\implies$ `limit` viene convertito a `long` e l'operazione avviene in `long`. Infine il risultato viene convertito a `int` per assegnamento a `x`.
  * *Se `long` è a 32 bit:* `long` non può rappresentare tutti i valori di `unsigned int` $\implies$ entrambi sono convertiti a `unsigned long`. Il risultato viene poi convertito a `int` per l'assegnamento.

#### 📌 Esercizio 2 (Esame 15 Gennaio 2026)
```c
long int g2(unsigned long p) {
    return p + 'e' - 'a';
}
int g1(int p) {
    char c = 'k';
    return g2(p + c - 'd');
}
int main(void) {
    unsigned short x = -5L;
    double b = g1(x);
    printf("%f\n", b);
}
```
* **Elenco di tutte le conversioni:**
  * Linea 11: `-5L` convertito da `long int` a `unsigned short` (inizializzazione di `x`).
  * Linea 12: `x` convertito da `unsigned short` a `int` (parametro formale `p` di `g1`).
  * Linea 6: `'k'` (letterale carattere, tipo `int`) convertito da `int` a `char`.
  * Linea 7: `c` convertito da `char` a `int` (*Integer Promotion* per `p + c`).
  * Linea 7: `'d'` ha tipo `int`; il risultato dell'espressione `(p + c - 'd')` di tipo `int` viene convertito a `unsigned long` (parametro di `g2`).
  * Linea 2: `'e'` e `'a'` (tipo `int`) convertiti a `unsigned long` per le operazioni con `p` (Regola 1).
  * Linea 2: Risultato di `p + 'e' - 'a'` convertito da `unsigned long` a `long int` (tipo di ritorno di `g2`).
  * Linea 7: Valore di ritorno di `g2` convertito da `long int` a `int` (tipo di ritorno di `g1`).
  * Linea 12: Valore di ritorno di `g1` convertito da `int` a `double` (inizializzazione di `b`).
* **Valore finale esatto di `b`:**
  * `x` vale $-5 + 65536 = 65531$.
  * In `g1`: `c = 'k' = 107`, `'d' = 100` $\implies p + c - 'd' = 65531 + 107 - 100 = 65538$.
  * In `g2`: `'e' = 101`, `'a' = 97` $\implies p + 'e' - 'a' = 65538 + 101 - 97 = 65542$.
  * `b = 65542.0`. Poiché 65542 ha solo 5 cifre significative, è **perfettamente rappresentabile** senza perdita di precisione in un `double` (che garantisce 15 cifre).

#### 📌 Esercizio 3 (Esame 22 Giugno 2026)
```c
int x = 0L, i = -2.5L;
char a = (char) 70, b = (char) 70, c = (char) 50;
a = (a * b) / c;
unsigned int limit = 8U;
long n = 30L;
if (i < limit)
    x = limit * n;
printf("%d %d\n", a, i);
```
* **Conversioni:**
  * Linea 1: `0L` da `long int` a `int`; `-2.5L` da `long double` a `int` (troncamento a `-2`).
  * Linee 2-3: `70` e `50` da `int` a `char` (**esplicite** tramite cast).
  * Linea 4: `a`, `b`, `c` da `char` a `int` (*Integer Promotion*); calcolo `(70 * 70) / 50 = 4900 / 50 = 98` (tipo `int`); risultato `98` convertito da `int` a `char` (assegnato ad `a`).
  * Linea 7: `i` (`-2`) convertito da `int` a `unsigned int` per il confronto con `limit` ($8U$). `-2` diventa $2^{32}-2 = 4294967294U$, quindi la condizione `4294967294U < 8U` è **FALSA**! Il ramo `if` non viene eseguito.
  * Linea 8 (se eseguita): `limit` da `unsigned int` a `unsigned long`, `n` da `long` a `unsigned long`, risultato da `unsigned long` a `int`.
  * **Stampa finale:** `98 -2`.

---

# 2. Dichiarazioni, Definizioni, Linkage e Durata di Memorizzazione

### 🔹 2.1 Dichiarazione vs Definizione
* **Dichiarazione (*Declaration*):** Fa conoscere al compilatore l'esistenza di un identificatore e il suo tipo, senza necessariamente allocare spazio in memoria o fornire il corpo della funzione.
  * `extern int b;` $\implies$ pura dichiarazione di variabile esterna.
  * `int cmp(int x, int y);` $\implies$ dichiarazione (prototipo) di funzione.
* **Definizione (*Definition*):** Alloca effettivamente lo spazio in memoria per una variabile oppure fornisce il corpo del codice per una funzione.
  * `int c = 1;` $\implies$ definizione di variabile con inizializzazione.
  * `int my_func(int d) { ... }` $\implies$ definizione di funzione.
* **Definizione Tentativa (*Tentative Definition* C99 §6.9.2):**
  Una dichiarazione di variabile a livello di file (globale) senza specificatore di classe di memorizzazione (`extern`/`static`) e senza inizializzatore (es. `int a;`).
  * Se nel file è presente una successiva definizione con inizializzatore (`int a = 3;`), le righe precedenti con `int a;` rimangono **dichiarazioni/tentativi**.
  * Se nel file **non** compare alcuna inizializzazione, il compilatore trasforma il tentativo in una **definizione effettiva** inizializzata a 0.

---

### 🔹 2.2 I Tre Tipi di Linkage (Collegamento §6.2.2)
Il *linkage* stabilisce se più dichiarazioni dello stesso nome in contesti diversi si riferiscono alla medesima entità di memoria:

| Tipo di Linkage | Significato | Dove si applica |
| :--- | :--- | :--- |
| **Esterno (*External Linkage*)** | Il simbolo è condiviso e accessibile da **tutti i file sorgente** del programma. Risolto dal Linker (`ld`). | Variabili globali non-static, funzioni non-static (anche prototipi), variabili dichiarate con `extern`. |
| **Interno (*Internal Linkage*)** | Il simbolo è visibile **soltanto all'interno del file sorgente corrente** (Translation Unit). | Variabili globali `static`, funzioni dichiarate/definite come `static`. |
| **Nessun Linkage (*No Linkage*)** | Il simbolo identifica un'entità strettamente locale e unica per il blocco corrente. | Variabili locali automatiche, parametri di funzione, **variabili locali statiche** (pur avendo durata statica, non hanno linkage). |

---

### 🔹 2.3 Durata di Memorizzazione (*Storage Duration* §6.2.4)
1. **Statica (*Static*):** L'oggetto esiste e mantiene il proprio valore per l'intera esecuzione del programma. Allocata nel Segmento Dati / BSS. (Variabili globali e variabili locali `static`).
2. **Automatica (*Automatic*):** L'oggetto viene creato all'ingresso del blocco di codice e distrutto all'uscita. Allocata nello **Stack**. (Variabili locali non-static e parametri formali).
3. **Dinamica (*Dynamic*):** L'oggetto viene allocato e deallocato esplicitamente dal programmatore sull'**Heap** tramite `malloc`, `calloc`, `realloc`, `free`.

---

### 🔹 2.4 Esercizio d'Esame Risolto: Tabella Dichiarazioni e Linkage

#### 📌 Caso Studio (Esame 15 Gennaio 2026):
```c
1  /* file.c */
2  int a;
3  int a;
4  int a;
5  extern int b;
6  static int c = 1;
7  int cfun(int a, int b);
8  
9  static void my_func(int d) {
10     int e = 0;
11     static int f = 1;
12     int *q = &f;
13     extern int c;
14 }
```

| Linea | Identificatore | Definito o Dichiarato? | Linkage | Motivazione |
| :--- | :--- | :--- | :--- | :--- |
| **Linea 2** | `a` | **Definito** (Definizione tentativa) | **Esterno** | Nessun `static`, variabile a livello file senza inizializzatore |
| **Linea 3** | `a` | **Dichiarato** (Tentativo ridondante) | **Esterno** | Ripetizione della dichiarazione di `a` |
| **Linea 4** | `a` | **Dichiarato** (Tentativo ridondante) | **Esterno** | Ripetizione della dichiarazione di `a` |
| **Linea 5** | `b` | **Dichiarato** | **Esterno** | Pura dichiarazione grazie a `extern` |
| **Linea 6** | `c` | **Definito** | **Interno** | Variabile globale marcata `static` con inizializzatore |
| **Linea 7** | `cfun` | **Dichiarato** | **Esterno** | Prototipo di funzione (nessun corpo `{}`) |
| **Linea 9** | `my_func`| **Definito** | **Interno** | Funzione con corpo `{}` marcata `static` |
| **Linea 9** | `d` | **Definito** | **Nessuno (*No Linkage*)** | Parametro formale di funzione |
| **Linea 10**| `e` | **Definito** | **Nessuno (*No Linkage*)** | Variabile locale automatica |
| **Linea 11**| `f` | **Definito** | **Nessuno (*No Linkage*)** | Variabile locale `static` (durata statica, ma nessun linkage) |
| **Linea 12**| `q` | **Definito** | **Nessuno (*No Linkage*)** | Puntatore locale automatico |
| **Linea 13**| `c` | **Dichiarato** | **Interno** | `extern` locale che eredita il linkage interno del `static int c` a riga 6 |

---

# 3. Flusso di Controllo: Precedenze, Sequence Points e Undefined Behavior

### 🔹 3.1 Basi Numeriche
* **Base 8 (Ottale):** Prefisso obbligatorio `0` (cifre 0-7).
  * `07` $= 7$.
  * `021` $= 2 \times 8 + 1 = 17$.
  * `025` $= 2 \times 8 + 5 = 21$.
  * `036` $= 3 \times 8 + 6 = 30$.
  * `073` $= 7 \times 8 + 3 = 59$.
* **Base 16 (Esadecimale):** Prefisso `0x` o `0X`.
  * `0xa` = 10, `0x10` = 16, `0x14` = 20, `0x1A` = 26, `0x1b` = 27, `0x1E` = 30, `0x2d` = 45, `0xae` = 174, `0xfb` = 251.

---

### 🔹 3.2 Tabella Completa delle Precedenze degli Operatori in C

| Precedenza | Operatori | Descrizione | Associatività |
| :---: | :--- | :--- | :---: |
| **1 (Max)** | `()`, `[]`, `->`, `.`, `a++`, `a--` | Postfissi, chiamate, accessi | Da Sinistra a Destra |
| **2** | `++a`, `--a`, `+a`, `-a`, `!`, `~`, `*p`, `&a`, `(type)`, `sizeof` | Unari, prefissi, dereferenziazione, cast | **Da Destra a Sinistra** |
| **3** | `*`, `/`, `%` | Moltiplicativi | Da Sinistra a Destra |
| **4** | `+`, `-` | Additivi | Da Sinistra a Destra |
| **5** | `<<`, `>>` | Shift di bit | Da Sinistra a Destra |
| **6** | `<`, `<=`, `>`, `>=` | Relazionali di confronto | Da Sinistra a Destra |
| **7** | `==`, `!=` | Uguaglianza / Disuguaglianza | Da Sinistra a Destra |
| **8** | `&` | Bitwise AND | Da Sinistra a Destra |
| **9** | `^` | Bitwise XOR | Da Sinistra a Destra |
| **10** | `|` | Bitwise OR | Da Sinistra a Destra |
| **11** | `&&` | AND logico (con cortocircuito) | Da Sinistra a Destra |
| **12** | `||` | OR logico (con cortocircuito) | Da Sinistra a Destra |
| **13** | `? :` | Operatore ternario condizionale | **Da Destra a Sinistra** |
| **14** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, ecc. | Assegnamenti | **Da Destra a Sinistra** |
| **15 (Min)**| `,` | Operatore virgola (*Comma operator*) | Da Sinistra a Destra |

---

### 🔹 3.3 Sequence Points ed Effetti Collaterali (Side Effects)
* **Effetto Collaterale (*Side Effect*):** Qualsiasi modifica permanente dello stato di esecuzione (scrittura in memoria di una variabile, es. `a = 5`, `a++`, `--a`, `*p = 10`).
* **Sequence Point (Punto di Sequenzializzazione):** Un punto nel flusso di esecuzione in cui è **garantito** che tutti gli effetti collaterali delle valutazioni precedenti sono stati completati e nessun effetto collaterale delle valutazioni successive è ancora iniziato.
* **Dove si trovano i Sequence Points in C:**
  1. Alla fine di ogni istruzione completa (il punto e virgola `;`).
  2. All'**operatore virgola (`,`)**: valuta l'operando sinistro, applica gli effetti collaterali, scarta il valore e valuta l'operando destro.
  3. Agli **operatori logici di cortocircuito (`&&`, `||`)**: subito dopo la valutazione del primo operando.
  4. All'**operatore condizionale ternario (`? :`)**: subito dopo la valutazione della condizione.
  5. Prima della chiamata a funzione (dopo la valutazione di tutti gli argomenti).

---

### 🔹 3.4 Multiple Unsequenced Modifications (Undefined Behavior)
> **Regola Fondamentale (§6.5.2):** Tra due sequence point successivi, un oggetto scalare può avere il suo valore memorizzato modificato al massimo **una sola volta**. Inoltre, il valore precedente può essere letto solo per determinare il nuovo valore da memorizzare.

* ❌ `a = a++;` $\implies$ **UB / Compiler Warning** (modifica due volte `a` senza sequence point intermedio).
* ❌ `a++ + a++;` $\implies$ **UB / Compiler Warning** (due modifiche senza sequence point).
* ✅ `a = 2, a++;` $\implies$ **Valido e Sequenziato** (la virgola `,` introduce un sequence point; contiene 2 effetti collaterali distinti).
* ✅ `a++ && a++;` oppure `a++ || a++;` $\implies$ **Valido** (`&&` e `||` introducono un sequence point).
* ✅ `a++ ? a++ : a++;` $\implies$ **Valido** (`?` introduce un sequence point).

#### 📌 Domanda d'Esame: Creazione di Espressioni con Effetti Collaterali
* *Richiesta:* Scrivere un'espressione con 3 effetti collaterali su `a` e 1 su `b` senza warning, e una con 2 su `a` con warning.
* **Soluzione Senza Warning:** `(a++, b++) , (a++, a++)` (i sequence point introdotti da `,` separano ogni singola modifica).
* **Soluzione Con Warning (UB):** `a++ + a++` (due incrementi su `a` tra cui non intercorre alcun sequence point).

---

### 🔹 3.5 Operatori di Cortocircuito e Tracing dell'Output
* `A && B`: Se `A` vale `0` (falso), `B` **non viene valutato** (eventuali `++a` in `B` vengono ignorati).
* `A || B`: Se `A` vale diverso da `0` (vero), `B` **non viene valutato**.
* **Istruzioni senza effetto:** Espressioni come `a != 1;` o `val = val = j;` sono lecite ma non alterano `a` (nel primo caso) o eseguono un normale doppio assegnamento associativo a destra.
* **Accessi Out-of-Bounds nello Stack:** Se un puntatore `p` punta a una variabile locale `i` e viene incrementato (`p++`), qualsiasi accesso `*p` punta a celle dello stack esterne. Nei compiti d'esame va indicato nella stampa con il carattere **`_` (valore indefinito)**.

---

### 🔹 3.6 Esercizio d'Esame Tracciato Passo-Passo (13 Febbraio 2026)
```c
int a = 0xa; // a = 10
while (a > 8 ? (a--, (a > 7 ? a-- : a)) : a--, a--) {
    if (a + 2 >= 07) { // 07 (ottale) = 7
        printf("HERE %d\n", a);
        a != 1; // Nessun effetto!
        continue;
        break;  // Irraggiungibile
        printf("NO MORE OK\n");
    }
    printf("EXIT\n");
}
a = a++ && a++;
a += 0xae; // 0xae = 174
printf("%d\n", a);
```
* **Iterazione 1:** `a = 10`. `10 > 8` è Vero $\implies$ esegue `(a--, (a > 7 ? a-- : a))`:
  * `a--` porta `a` a `9`.
  * `a > 7` ($9 > 7$) è Vero $\implies a--$ porta `a` a `8`. Il blocco ternario ritorna `8`.
  * La virgola valuta l'operando destro: `a--` testa `8` (Vero) e decrementa `a` a `7`.
  * Condizione `if (7 + 2 >= 7)` ($9 \ge 7$) è Vera $\implies$ Stampa: `HERE 7`. `continue` passa all'iterazione successiva.
* **Iterazione 2:** `a = 7`. `7 > 8` è Falso $\implies$ ramo else del ternario: `a--` (diventa 6).
  * La virgola valuta l'operando destro: `a--` testa `6` (Vero) e decrementa `a` a `5`.
  * `if (5 + 2 >= 7)` ($7 \ge 7$) è Vera $\implies$ Stampa: `HERE 5`. `continue`.
* **Iterazione 3:** `a = 5`. `5 > 8` è Falso $\implies a--$ (diventa 4), poi operando destro $a--$ testa `4` (Vero) e porta `a` a `3`.
  * `if (3 + 2 >= 7)` ($5 \ge 7$) è Falsa $\implies$ Stampa: `EXIT`.
* **Iterazione 4:** `a = 3`. `3 > 8` è Falso $\implies a--$ (diventa 2), poi operando destro $a--$ testa `2` (Vero) e porta `a` a `1`.
  * `if (1 + 2 >= 7)` ($3 \ge 7$) è Falsa $\implies$ Stampa: `EXIT`.
* **Iterazione 5:** `a = 1`. `1 > 8` è Falso $\implies a--$ (diventa 0), poi operando destro $a--$ testa `0` (**FALSO**) e porta `a` a `-1`. Il ciclo termina!
* **Istruzione finale:** `a = a++ && a++;` con `a = -1`.
  * Primo `a++`: valuta `-1` (vero) e programma l'incremento (`a` diventa `0` al sequence point di `&&`).
  * Secondo `a++`: valuta `0` (falso) e programma l'incremento (`a` diventa `1`). L'operazione `&&` restituisce `0`.
  * Assegnamento: `a = 0`.
  * `a += 0xae` $\implies a = 0 + 174 = 174$. Stampa: `174`.
* **Output Finale Completo:**
  ```text
  HERE 7
  HERE 5
  EXIT
  EXIT
  174
  ```

---

# 4. Mappa di Memoria, Puntatori Multi-Tipo, Little-Endian, Complemento a Due e Bitwise

Questo è l'esercizio a punteggio più alto dell'esame (7–8 punti). Richiede di ricostruire la disposizione esatta dei byte in memoria, tracciare le modifiche tramite puntatori di diversa dimensione e valutare espressioni aritmetico-logiche.

### 🔹 4.1 Modello di Memoria e Rappresentazione Dati
1. **Dimensioni dei Tipi (Architettura Standard d'Esame):**
   * `char` = 1 Byte (8 bit).
   * `short` / `short int` = 2 Byte (16 bit).
   * `int` = 4 Byte (32 bit).
   * `long long` = 8 Byte (64 bit).
   * Puntatori = 4 Byte (32 bit) o 8 Byte (64 bit).
2. **Architettura Little-Endian:**
   Il **byte meno significativo (LSB)** viene memorizzato all'indirizzo di memoria **più basso** (in cima alla mappa di memoria verticale).
   * Esempio: Il valore `0x00020004` (32 bit) viene memorizzato nei byte consecutivi:
     $$\text{Byte 0 (LSB)} = \text{0x04} \quad | \quad \text{Byte 1} = \text{0x00} \quad | \quad \text{Byte 2} = \text{0x02} \quad | \quad \text{Byte 3 (MSB)} = \text{0x00}$$
3. **Rappresentazione in Complemento a Due:**
   * Numeri negativi: $\text{Valore}(-k) = 2^N - k$.
   * `INT_MIN` $= -2^{31} = \text{0x80000000}$.
   * `INT_MAX` $= 2^{31}-1 = \text{0x7FFFFFFF}$.
   * `LLONG_MIN` $= -2^{63} = \text{0x8000000000000000}$.
   * `LLONG_MAX` $= 2^{63}-1 = \text{0x7FFFFFFFFFFFFFFF}$.
   * `(LLONG_MAX + 1)` in aritmetica a 64 bit genera un overflow che produce esattamente `LLONG_MIN`.

---

### 🔹 4.2 Aritmetica e Algebra dei Puntatori Multi-Granularità
Sia `a` l'indirizzo iniziale dell'array in memoria:
* Se `p` è `short *` (2 byte): `p[k]` accede a 2 byte contigui a partire dall'offset $k \times 2$.
* Se `q` è `char *` (1 byte): `q[k]` accede al singolo byte all'offset $k \times 1$.
* Se `p` è `int *` (4 byte): `p[k]` accede a 4 byte contigui a partire dall'offset $k \times 4$.
* Se `p` è `long long *` (8 byte): `p[k]` accede a 8 byte contigui all'offset $k \times 8$.

> ⚠️ **Differenza Fondamentale tra Sottrazione di Puntatori e Cast a Intero:**
> * `&a[3] - a` $\implies$ Restituisce la distanza in **numero di elementi di tipo `int`**, cioè `3`.
> * `(int)(a + 3) - (int)&q[6]` $\implies$ Converte gli indirizzi in numeri interi (offset in **byte**). Poiché `a+3` si trova al byte $3 \times 4 = 12$ e `&q[6]` al byte 6, la differenza è $12 - 6 = 6$ byte!

---

### 🔹 4.3 Guida alla Decodifica della Sintassi nelle Domande e Asserzioni d'Esame

Nelle asserzioni finali dell'esercizio sulla mappa di memoria, l'errore più comune è confondere:
1. **Il valore memorizzato** in una o più celle.
2. **L'indirizzo di memoria** (la posizione fisica/offset).
3. **La distanza in elementi** (aritmetica dei puntatori).
4. **La distanza fisica in byte** (sottrazione con cast a intero).

Ecco la suddivisione chiara di ogni caso con relative regole di calcolo ed esempi:

---

#### 1️⃣ Accesso ai Valori (Dereferenziazione: cosa c'è scritto dentro la memoria)
Si parla di **valore numerico** quando il puntatore viene dereferenziato con `*` oppure con l'operatore parentesi quadre `[...]` (senza il prefisso `&`).

* **Accesso a 1 Byte (`char *q`):**
  * **Sintassi:** `q[k]` oppure `*(q + k)`
  * **Cosa fa:** Legge il singolo byte situato alla **riga $k$** (offset $+k$ byte).
  * **Esempio:** Se alla riga 4 della mappa abbiamo `0x09`, allora `q[4] = 9`.

* **Accesso a 2 Byte (`short *p`):**
  * **Sintassi:** `p[k]` oppure `*(p + k)`
  * **Cosa fa:** Legge 2 byte contigui a partire dall'offset $2k$. In Little-Endian:
    * La riga **$2k$** contiene il **LSB** (byte meno significativo).
    * La riga **$2k+1$** contiene il **MSB** (byte più significativo).
    * $\text{Valore} = \text{LSB} + (\text{MSB} \times 256) = \text{0xMSB\_LSB}$.
  * **Esempio:** Per $p[5]$, prendiamo riga 10 (`0x02`, LSB) e riga 11 (`0x00`, MSB) $\implies p[5] = \text{0x0002} = 2$.

* **Accesso a 2 Byte con Cast da puntatore a char (`*((short*)&q[k])`):**
  * **Sintassi:** `*((short*)&q[k])`
  * **Cosa fa:** Legge 2 byte consecutivi partendo dall'offset arbitrario $k$ (riga $k$ = LSB, riga $k+1$ = MSB).
  * **Esempio:** `*((short*)&q[9])` con riga 9=`0x01` e riga 10=`0x02` $\implies \text{0x0201} = 513$.

* **Accesso a 4 Byte (`int *` / `int a[]`) o 8 Byte (`long long *` / `long long a[]`):**
  * **Sintassi:** `a[k]` oppure `*(a + k)`
  * **Cosa fa:** Legge l'intero blocco di 4 (o 8) byte a partire dall'offset $k \times \text{sizeof}(a[0])$ ricomposto in Little-Endian.

---

#### 2️⃣ Indirizzi di Memoria e Puntatori (dove si trova la cella)
Si parla di **indirizzo** quando compare l'operatore indirizzo `&` oppure il puntatore/array senza dereferenziazione. Non indica il contenuto della cella, ma la sua **posizione (offset di riga)**.

* **Indirizzo di un singolo byte:**
  * **Sintassi:** `&q[k]` oppure `q + k`
  * **Significato:** Punta alla **riga $k$** (offset $+k$ byte dall'inizio dell'array).
* **Indirizzo di un elemento `short`:**
  * **Sintassi:** `&p[k]` oppure `p + k`
  * **Significato:** Punta alla **riga $2k$** (offset $+2k$ byte dall'inizio dell'array).
* **Indirizzo di un elemento dell'array base `a`:**
  * **Sintassi:** `&a[k]` oppure `a + k`
  * **Significato:** Punta alla **riga $k \times \text{sizeof}(a[0])$** (es. $4k$ per `int`, $8k$ per `long long`).

---

#### 3️⃣ Sottrazione tra Puntatori vs Sottrazione con Cast `(int)` (Trabocchetto Chiave)

> [!WARNING]
> È la distinzione più critica dell'esame: non confondere la distanza in elementi con la distanza in byte!

* **Caso A: Sottrazione tra Puntatori Omogenei (`ptr1 - ptr2`)**
  * **Formula standard C:** `(Indirizzo1 - Indirizzo2) / sizeof(*ptr)`
  * **Risultato:** Restituisce il **numero di elementi/caselle** di quel tipo tra i due puntatori.
  * **Regola pratica:** **NON moltiplicare né contare i byte!** Si fa semplicemente la differenza tra gli indici:
    * `&a[3] - a` $\implies 3 - 0 = \mathbf{3}$ (elementi `int`).
    * `&p[9] - &p[2]` $\implies 9 - 2 = \mathbf{7}$ (elementi `short`).
    * `&q[6] - q` $\implies 6 - 0 = \mathbf{6}$ (elementi `char`).

* **Caso B: Sottrazione con Cast Esplicito a Intero (`(int)ptr1 - (int)ptr2`)**
  * **Significato:** Il cast `(int)` trasforma l'indirizzo in un numero intero puro, corrispondente all'**offset fisico in byte**.
  * **Risultato:** Restituisce la **distanza fisica esatta in singoli BYTE**.
  * **Regola pratica:** Trova l'offset di riga (in byte) del primo puntatore, trova l'offset di riga del secondo e sottrai:
    * `(int)(a + 3) - (int)&q[6]` con `int a[]`:
      * `a + 3` sta al byte $3 \times 4 = 12$.
      * `&q[6]` sta al byte $6$.
      * Risultato $= 12 - 6 = \mathbf{6}$ byte.
    * `(int)(p + 11) - (int)(a + 2)` con `long long a[]` (8 byte) e `short *p` (2 byte):
      * `p + 11` sta al byte $11 \times 2 = 22$.
      * `a + 2` sta al byte $2 \times 8 = 16$.
      * Risultato $= 22 - 16 = \mathbf{6}$ byte.

---

#### 4️⃣ Operazioni Bitwise e Valutazione Finale delle Asserzioni
Nelle espressioni composte (es. `((q[12] >> 2) | q[4]) >= 9` oppure `((&a[3] - a) + p[5]) % 2`):

1. **Isola i singoli blocchi:**
   * Sostituisci prima le distanze tra puntatori o offset in byte con il loro valore numerico.
   * Sostituisci i valori letti dalla mappa (`p[...]`, `q[...]`) con i rispettivi valori interi.
2. **Esegui le operazioni bitwise (`>>`, `<<`, `|`, `&`, `^`, `~`):**
   * Converti i valori decimali in binario a 8 bit.
   * Esegui l'operazione bit a bit e riconverti in decimale.
   * *Esempio:* $q[12] = 33 = \text{00100001b} \implies 33 \gg 2 = 8 = \text{00001000b}$. Poi $8 \mid 9 = 9$.
3. **Calcola l'operatore modulo (`%`):**
   * Calcola la somma/differenza algebrica totale prima di fare il modulo.
   * *Esempio:* $(3 + 2) \% 2 = 5 \% 2 = 1$.
4. **Valuta il test logico (`==`, `>=`, `!=`, ecc.):**
   * Un'asserzione è **VERA** se la condizione matematica è soddisfatta (valore booleano $1$).
   * Un'asserzione è **FALSA** se non è soddisfatta (valore booleano $0$).

---

#### 🧠 Schema Mentale Riassuntivo

```
Domanda: Cosa rappresenta l'espressione?
│
├── C'è '*' oppure '[...]' senza '&'?
│   └── ➔ VALORE memorizzato nella cella (char: 1 byte, short: 2 byte Little-Endian, int: 4 byte)
│
├── C'è '&' oppure il nome del puntatore da solo?
│   └── ➔ INDIRIZZO / OFFSET (posizione fisica nella mappa)
│
├── C'è una sottrazione del tipo 'ptr1 - ptr2' (senza cast)?
│   └── ➔ DISTANZA IN ELEMENTI (differenza tra indici, non contare i byte)
│
└── C'è una sottrazione del tipo '(int)ptr1 - (int)ptr2'?
    └── ➔ DISTANZA FISICA IN BYTE (differenza tra gli offset di riga fisici)
```

---

### 🔹 4.4 Operatori Bitwise Fondamentali
* **Bitwise NOT (`~x`):** Inverte tutti i bit di `x` ($\sim b = 1-b$).
* **Bitwise AND (`a & b`):** 1 solo se entrambi i bit sono 1.
* **Bitwise OR (`a | b`):** 1 se almeno uno dei due bit è 1.
* **Bitwise XOR (`a ^ b`):** 1 se i bit sono discordi.
* **Right Shift (`x >> k`):** Sposta i bit a destra di $k$ posizioni (divisione intera per $2^k$).

---

### 🔹 4.5 Algoritmo Risolutivo a 6 Passi per la Mappa di Memoria

```
  ┌────────────────────────────────────────────────────────┐
  │ 1. Calcola la dimensione totale in byte dell'array     │
  └──────────────────────────┬─────────────────────────────┘
                             ↓
  ┌────────────────────────────────────────────────────────┐
  │ 2. Converti ogni valore iniziale in esadecimale        │
  └──────────────────────────┬─────────────────────────────┘
                             ↓
  ┌────────────────────────────────────────────────────────┐
  │ 3. Disponi i byte in tabella (Little-Endian: LSB alto) │
  └──────────────────────────┬─────────────────────────────┘
                             ↓
  ┌────────────────────────────────────────────────────────┐
  │ 4. Applica in ordine le modifiche (p[i]=.., *(q+k)=..) │
  └──────────────────────────┬─────────────────────────────┘
                             ↓
  ┌────────────────────────────────────────────────────────┐
  │ 5. Mappa gli indirizzi dei puntatori per le domande    │
  └──────────────────────────┬─────────────────────────────┘
                             ↓
  ┌────────────────────────────────────────────────────────┐
  │ 6. Valuta matematicamente le affermazioni A, B, C      │
  └────────────────────────────────────────────────────────┘
```

---

# 5. Compilazione con GCC, Progetti Multi-File, Linkage ed Esecuzione

Questa sezione costituisce la **guida metodologica completa** per risolvere gli esercizi d'esame dedicati a GCC, progetti multi-file, linkage e tracciamento dell'output (come l'**Esercizio 4 della Prova del 1° Settembre 2026**, 8 Luglio 2026, 22 Giugno 2026).

---

### 🔹 5.1 Pipeline di Compilazione GCC e Ruolo dei Flag

Il processo di generazione di un eseguibile in C è composto da 4 fasi sequenziali:

$$\text{Sorgente (.c)} \xrightarrow{\text{1. Preprocessore (cpp) [-E]}} \text{.i} \xrightarrow{\text{2. Compilatore (cc1) [-S]}} \text{Assembly (.s)} \xrightarrow{\text{3. Assembler (as) [-c]}} \text{Oggetto (.o)} \xrightarrow{\text{4. Linker (ld) [-o]}} \text{Eseguibile}$$

| Comando | Fasi Eseguite | File Prodotto | Il Linker viene invocato? | Può dare errori di Linker? |
| :--- | :--- | :---: | :---: | :---: |
| `gcc -E file.c` | Solo Preprocessore | Output a video / `.i` | ❌ No | ❌ **MAI** |
| `gcc -S file.c` | Preprocessore + Compilatore | `file.s` (Assembly) | ❌ No | ❌ **MAI** |
| `gcc -c file.c` | Preprocessore + Compilatore + Assembler | `file.o` (File Oggetto) | ❌ No | ❌ **MAI** |
| `gcc -o prog file.c` | Tutte le 4 fasi (compreso il Linker) | `prog` (Eseguibile) | ✅ **SÌ** | ✅ **SÌ** (se mancano simboli o `main`) |
| `gcc file1.c file2.c -o prog` | Tutte le 4 fasi su entrambi i file | `prog` (Eseguibile) | ✅ **SÌ** | ✅ **SÌ** (se simboli duplicati o mancanti) |

---

### 🔹 5.2 Guida Risolutiva: I 5 Comandi di Compilazione ed Errori del Linker

Nei compiti d'esame vengono presentati 2 file sorgente (es. `main.c` e `out.c`, oppure `calc.c` e `stampa.c`) e viene chiesto quali dei 5 comandi provocano un errore del linker e perché.

```
                  ┌────────────────────────────────────────────────────────┐
                  │           C'è il flag '-c' nel comando?                │
                  └──────────────────────────┬─────────────────────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                    SÌ │                                           │ NO
                       ↓                                           ↓
        ┌─────────────────────────────┐             ┌─────────────────────────────┐
        │   NESSUN ERRORE DI LINKER   │             │   IL LINKER VIENE ESEGUITO  │
        │ -c compila ed assembla solo │             └──────────────┬──────────────┘
        │ il file .o; il linker non   │                            │
        │ viene affatto invocato.     │                            ↓
        └─────────────────────────────┘             ┌─────────────────────────────┐
                                                    │ È un singolo file o sono 2? │
                                                    └──────────────┬──────────────┘
                                                                   │
                                     ┌─────────────────────────────┴─────────────────────────────┐
                    UN SOLO FILE .c  │                                                           │ ENTRAMBI I FILE .c
                                     ↓                                                           ↓
                      ┌─────────────────────────────┐                             ┌─────────────────────────────┐
                      │ 1. Manca il 'main'?         │                             │ Se i file si completano a   │
                      │    -> ERRORE: 'main' assente│                             │ vicenda (es. un file ha     │
                      │ 2. Chiama funzioni definite │                             │ main e l'altro la funzione),│
                      │    nell'altro file?         │                             │ -> NESSUN ERRORE DI LINKER! │
                      │    -> ERRORE: 'undefined ref'│                             └─────────────────────────────┘
                      └─────────────────────────────┘
```

#### 📌 Regole di valutazione standard per i 5 comandi:

1. **`gcc -c main.c` (oppure `gcc -c out.c`):**
   - **Esito:** **Nessun errore di linker.**
   - **Giustificazione all'esame:** *«Il flag `-c` compila ed assembla soltanto il sorgente producendo il file oggetto (`.o`), arrestando la pipeline prima del linking: il linker non viene invocato.»*
2. **`gcc -o main main.c` (quando `main.c` usa funzioni definite in `out.c`):**
   - **Esito:** **ERRORE di linker.**
   - **Giustificazione all'esame:** *«La funzione chiamata (es. `mostra` o `stampa`) non è definita nel file `main.c` (`undefined reference to mostra`).»*
3. **`gcc -o out out.c` (quando `out.c` contiene solo funzioni ausiliarie):**
   - **Esito:** **ERRORE di linker.**
   - **Giustificazione all'esame:** *«Il file `out.c` non contiene la funzione `main` (`undefined reference to main`), necessaria per produrre un eseguibile.»*
4. **`gcc main.c out.c -o prog`:**
   - **Esito:** **Nessun errore di linker.**
   - **Giustificazione all'esame:** *«Entrambi i file sorgente sono forniti al compilatore: `main.c` fornisce il punto di ingresso `main` e `out.c` fornisce la definizione della funzione; tutti i simboli si risolvono correttamente. Non serve alcuna correzione.»*

---

### 🔹 5.3 Guida Risolutiva: Analisi del Linkage e File di Definizione

All'esame viene chiesto di specificare per ogni identificatore:
1. **Se è definito o dichiarato** (e in quale file è definito).
2. **Il tipo di Linkage** (*Esterno*, *Interno*, *Nessun Linkage*).

```text
Identificatore
│
├── È un parametro formale (es. 'int a' nella firma)?
│   └── ➔ DEFINITO nella funzione | NO LINKAGE (Nessun Linkage)
│
├── È una variabile locale dentro una funzione?
│   ├── Senza 'static' (es. 'int x = 5;')  ➔ DEFINITO | NO LINKAGE
│   └── Con 'static' (es. 'static int k;') ➔ DEFINITO | NO LINKAGE (⚠️ Durata statica, ma NESSUN linkage!)
│
├── È dichiarata con 'extern' (senza inizializzazione)?
│   └── ➔ DICHIARATO | LINKAGE ESTERNO (se globale o se non collide con static precedente)
│
├── È preceduta da 'static' a livello globale di file?
│   └── ➔ DEFINITO nel file corrente | LINKAGE INTERNO (visibile solo in quel file .c)
│
└── È una variabile/funzione globale senza 'static'?
    ├── Solo tipo e nome (es. 'int k;')     ➔ DEFINIZIONE TENTATIVA (rimane dichiarazione se definita dopo) | LINKAGE ESTERNO
    ├── Con inizializzazione (es. 'int k=5;')➔ DEFINIZIONE EFFETTIVA | LINKAGE ESTERNO
    └── Firma funzione con corpo '{ ... }'  ➔ DEFINIZIONE | LINKAGE ESTERNO
```

> [!IMPORTANT]
> **Le 3 Regole d'Oro per non sbagliare il Linkage all'Esame:**
> 1. **Variabili Globali `static` (a livello di file):** Hanno **Linkage Interno**. Se in `main.c` c'è `int k = 5;` (Linkage Esterno) e in `out.c` c'è `static int k = 10;` (Linkage Interno), **NON c'è conflitto di nomi**: sono due variabili completamente separate allocate in due celle distinte della memoria dati.
> 2. **Variabili Locali `static` (dentro una funzione):** Hanno **Nessun Linkage (*No Linkage*)**, anche se hanno durata di memorizzazione statica (permanente).
> 3. **Definizioni Tentative multiple:** Scrivere `int k;` seguito da `int k = 5;` nello stesso file è lecito: `int k;` è una definizione tentativa che funge da dichiarazione, mentre `int k = 5;` è la definizione vera e propria con linkage esterno.

---

### 🔹 5.4 Guida Risolutiva: Tracciamento dell'Output (Terminazione vs Ciclo Infinito)

Per capire cosa stampa il programma, bisogna tracciare con precisione **quale variabile viene modificata da chi**:

#### 1. Verifica della condizione del ciclo in `main()`
Guarda la variabile testata nel `while`:
- **Caso A (Il ciclo TERMINA - es. Prova 1° Settembre 2026):**
  Nel `main`, dopo aver chiamato la funzione esterna, è presente l'istruzione `k -= 2;` che modifica la **`k` globale di `main.c`**.
  - `k` parte da 5 $\implies$ iterazione 1: $k=5 > 0$, poi $k$ diventa $3$.
  - Iterazione 2: $k=3 > 0$, poi $k$ diventa $1$.
  - Iterazione 3: $k=1 > 0$, poi $k$ diventa $-1$.
  - $k = -1 \not> 0 \implies$ **il ciclo termina dopo esattamente 3 iterazioni.**

- **Caso B (Il ciclo è INFINITO - es. Prova 8 Luglio 2026 / 22 Giugno 2026):**
  Nel `main`, la condizione è `while (val >= 0) { stampa(val); }` e dentro `main` la variabile `val` **non viene mai riassegnata**. La funzione `stampa(val)` riceve una copia per valore del parametro e modifica solo la propria variabile `static val` interna a `out.c`.
  - La variabile `val` di `main.c` resta fissa a 3 per sempre $\implies$ **CICLO INFINITO**.

#### 2. Tracciamento delle stampe dentro la funzione ausiliaria in `out.c`
- Guarda se la funzione usa la variabile `static` di `out.c`.
- Nel caso di `mostra(int a)` in `out.c`:
  - Riceve il parametro `a` (copia locale, `a--` non ha effetto su `main`).
  - Esegue `printf("%d\n", k += w);` dove `k` è la `static int k = 10;` e `w = 3`:
    - 1ª chiamata: $k = 10 + 3 = \mathbf{13}$
    - 2ª chiamata: $k = 13 + 3 = \mathbf{16}$
    - 3ª chiamata: $k = 16 + 3 = \mathbf{19}$
- Output finale stampato a video:
  ```text
  13
  16
  19
  ```

---

### 🔹 5.5 Esercizio d'Esame Risolto Completo (Prova 1° Settembre 2026 - Esercizio 4)

#### Testo del Problema:
Dati i seguenti due file:

```c
/* main.c */
int k;
int k = 5;
void mostra(int k);

int main(void) {
    extern int k;
    while (k > 0) {
        mostra(k);
        k -= 2;
    }
    return 0;
}
```

```c
/* out.c */
#include <stdio.h>
static int k = 10;
int w = 3;

void mostra(int a) {
    a--;
    printf("%d\n", k += w);
}
```

**Domande d'Esame:**
1. Dire quali compilazioni provocano errore a causa del linker (e perché):
   - `1) gcc -c main.c`
   - `2) gcc -o main main.c`
   - `3) gcc main.c out.c -o prog`
   - `4) gcc -c out.c`
   - `5) gcc -o out out.c`
2. In caso il punto 3) ritorni un errore, descrivere come può essere corretto.
3. Che tipo di linkage hanno `k` (in entrambi i file), `w`, e `mostra`, ed in quale file sono definite?
4. Cosa stampa il programma?

---

#### 📝 Soluzione Ufficiale Completa da Riportare su Foglio Protocollo:

#### Punto 1: Diagnosi dei Comandi di Compilazione
1. **`gcc -c main.c`:** **Nessun errore di linker**, in quanto il flag `-c` arresta il processo dopo la fase di assemblaggio (produce `main.o`), senza invocare il linker.
2. **`gcc -o main main.c`:** **ERRORE del linker** (`undefined reference to mostra`), poiché la funzione `mostra` è solo dichiarata in `main.c` ma definita in `out.c`.
3. **`gcc main.c out.c -o prog`:** **Nessun errore di linker**, poiché tutti i simboli esterni sono definiti (`main` in `main.c`, `mostra` in `out.c`) e la variabile `k` in `out.c` è `static` (linkage interno), quindi non collide con la `k` globale di `main.c`.
4. **`gcc -c out.c`:** **Nessun errore di linker**, in quanto il flag `-c` compila soltanto producendo `out.o`.
5. **`gcc -o out out.c`:** **ERRORE del linker** (`undefined reference to main`), poiché nel file `out.c` non è presente la funzione `main`.

#### Punto 2: Correzione del comando combinato
- Il comando al punto 3) **non genera alcun errore**, pertanto **non serve alcuna correzione**.

#### Punto 3: Tabella del Linkage e Definizioni

| Identificatore | File di Definizione | Tipo di Linkage | Motivazione |
| :--- | :--- | :--- | :--- |
| **`k` (in `main.c`)** | `main.c` | **Linkage ESTERNO** | `int k;` è una definizione tentativa; `int k = 5;` è la definizione effettiva globale senza `static`. |
| **`k` (in `out.c`)** | `out.c` | **Linkage INTERNO** | Dichiarata e definita a livello globale di file con lo specificatore `static`. È un oggetto distinto da `k` di `main.c`. |
| **`w` (in `out.c`)** | `out.c` | **Linkage ESTERNO** | Variabile globale definita con inizializzatore `int w = 3;` senza `static`. |
| **`mostra`** | `out.c` | **Linkage ESTERNO** | Dichiarata in `main.c`, definita in `out.c` come funzione globale non `static`. |
| **`a` (parametro)** | `out.c` | **NESSUN Linkage (*No Linkage*)** | Parametro formale della funzione `mostra`. |

#### Punto 4: Output e Traccia d'Esecuzione
In `main.c`, la variabile `k` globale parte dal valore $5$. Ad ogni iterazione del ciclo `while (k > 0)`:
1. Viene invocata `mostra(k)`, che riceve il valore per copia nel parametro `a`. Al suo interno, `mostra` modifica unicamente la propria variabile `static int k` di `out.c`, incrementandola di `w = 3` ($10+3=\mathbf{13}$, poi $\mathbf{16}$, poi $\mathbf{19}$) e stampandola.
2. In `main.c`, l'istruzione `k -= 2;` decrementa la `k` globale: $5 \to 3 \to 1 \to -1$.
3. Alla quarta verifica, $k = -1 \not> 0$, quindi il ciclo `while` termina e il programma restituisce 0.

**Output a video:**
```text
13
16
19
```

---

### 🔹 5.6 Tabella Comparativa degli Esercizi Multi-File tra le Prove d'Esame

| Prova d'Esame | Variabile in `main.c` | Variabile in `out.c` | Funzione chiamata | Il Ciclo Termina o è Infinito? | Output Prodotto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1° Settembre 2026** | `k = 5` (decrementata: `k -= 2`) | `static k = 10`, `w = 3` | `mostra(k)` $\to$ `k += w` | **Termina** (3 iterazioni) | `13`<br>`16`<br>`19` |
| **8 Luglio 2026** | `val = 3` (non modificata) | `static val = 6`, `j = 2` | `stampa(val)` $\to$ `val -= j` | **Ciclo Infinito** (`val` in `main` resta 3) | `4`<br>`2`<br>`0`<br>`-2`<br>... |
| **22 Giugno 2026** | `totale = 5` (non modificata) | `extern totale`, `static int k = 0` | `logga(totale)` $\to$ `k += 5` | **Ciclo Infinito** (`totale` in `main` resta 5) | `0`<br>`-5`<br>`-10`<br>`-15`<br>... |

---

### 🔹 5.7 Le 4 Zone di Memoria di un Programma C

```
  Indirizzi Alti  ┌───────────────────────────────┐
                  │ Stack (cresce verso il basso) │  <- Variabili locali automatiche, parametri
                  ├───────────────────────────────┤
                  │               ↓               │
                  │               ↑               │
                  ├───────────────────────────────┤
                  │  Heap (cresce verso l'alto)   │  <- Memoria dinamica (malloc, calloc, realloc)
                  ├───────────────────────────────┤
                  │ Segmento Dati / BSS (Statico) │  <- Variabili globali e statiche
                  ├───────────────────────────────┤
  Indirizzi Bassi │ Text / Code Segment (RO)      │  <- Istruzioni macchina eseguibili
                  └───────────────────────────────┘
```

#### Codice d'Esame Dimostrativo per le 4 Zone:
```c
#include <stdlib.h>

int g = 5;                        // 1. MEMORIA STATICA / PERMANENTE (Segmento Dati)

int main(void) {
    int a = 10;                   // 2. STACK (Memoria Automatica / Frame di main)
    static int s = 7;             // 3. MEMORIA STATICA / PERMANENTE (Segmento Dati)
    int *p = malloc(sizeof(int)); // Puntatore 'p' sullo STACK;
                                  // Blocco allocato '*p' sull'HEAP (4. HEAP)
    *p = 20;
    free(p);                      // Deallocazione Heap
    return a + g + s;
}
```

---

### 🔹 5.8 Gestione Dinamica della Memoria (`<stdlib.h>`)
* **`malloc(size)`:** Alloca `size` byte non inizializzati sull'Heap. Restituisce `NULL` se fallisce.
* **`calloc(n, size)`:** Alloca $n \times \text{size}$ byte e **azzera tutti i bit a 0**. `calloc(5, 3)` e `malloc(15)` allocano esattamente 15 byte.
* **Proprietà Formali di `realloc(ptr, new_size)` (Quesito d'esame frequente):**
  * Prende come parametri **l'indirizzo del blocco (`ptr`) e la nuova dimensione in byte (`new_size`)**.
  * Ritorna un valore di tipo `void *`.
  * Può ritornare `NULL` (oppure 0) in caso di fallimento o se `new_size == 0`.
  * L'indirizzo ritornato **può essere diverso** dall'indirizzo passato `ptr` (se il blocco viene spostato in un'altra area dell'Heap).
* **Errori Fatali d'Esame:**
  * ❌ `int a; int *p = &a; free(p);` $\implies$ **ERRORE GRAVE / Crash**. `free()` può essere invocata **solo** su puntatori ottenuti tramite `malloc`/`calloc`/`realloc`.

---

### 🔹 5.9 Concetto di Lvalue ed Rvalue
* **lvalue (*Locator Value*):** Espressione che fa riferimento a un oggetto con locazione di memoria identificabile e modificabile:
  * Variabili: `a`, `p`.
  * Dereferenziazioni: `*p`, `*&a`, `**&p`, `a[i]`.
* **rvalue (*Read Value*):** Valore temporaneo calcolato, privo di locazione di memoria persistente a cui riassegnare un valore:
  * Costanti e letterali: `5`, `'a'`.
  * Espressioni temporanee: `a + 2`, `x && y`.
  * Indirizzi temporanei: `&a` (è un rvalue, mentre `*&a` è un lvalue).

---

# 6. Strutture Dati Dinamiche: Liste Semplicemente Collegate

### 🔹 6.1 Struttura del Nodo
```c
struct Node {
    int info;
    struct Node *pNext;
};
```

### 🔹 6.2 Principi di Manipolazione Sicura dei Puntatori
1. **Regola del Salvataggio:** Prima di deallocare (`free(curr)`) o staccare un nodo (`curr->pNext = NULL`), memorizzare sempre il puntatore al nodo successivo (`struct Node *next = curr->pNext;`).
2. **Controllo Allocazione:** Verificare sempre che ogni chiamata `malloc()` ritorni un puntatore non `NULL`.
3. **Gestione del Puntatore di Testa (`pFirst`):** Se la testa viene modificata, aggiornare il puntatore globale o il valore di ritorno.

---

### 🔹 6.3 I 4 Algoritmi d'Esame Pronti e Risolti

#### 📌 Algoritmo 1: Fusione Alternata di Due Liste (`alternate`)
*Crea una nuova lista alternando gli elementi di `l1` e `l2`: $l1_0, l2_0, l1_1, l2_1, \dots$*
```c
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
```

---

#### 📌 Algoritmo 2: Cancellazione di un Elemento per Posizione (`canc_elem`)
*Cancella il nodo alla posizione `pos` (1-indexed) gestendo lista vuota, testa, nodi intermedi e posizioni non valide.*
```c
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
```

---

#### 📌 Algoritmo 3: Partizione e Spostamento Dispari in Testa (`sposta_dispari_in_testa`)
*Riorganizza la lista in-place posizionando tutti gli elementi dispari prima di quelli pari, preservando l'ordine relativo.*
```c
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
```

---

#### 📌 Algoritmo 4: Inserimento Ordinato Crescente (`inserisci_ordinato`)
*Inserisce un valore `x` mantenendo la lista ordinata in modo crescente.*
```c
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
```

---

# 7. Matrici 2D, Variable-Length Arrays (VLA) e Array Dinamici

### 🔹 7.1 Layout Row-Major e VLA (C99)
* Le matrici bidimensionali in C sono memorizzate in ordine **Row-Major** (riga per riga contigua in memoria). L'elemento `mat[i][j]` si trova all'offset:
  $$\text{Offset} = (i \times \text{cols} + j) \times \text{sizeof}(\text{tipo})$$
* **Regola sintattica fondamentale dei VLA:** Nei parametri di funzione, le **dimensioni** devono essere dichiarate **prima** della matrice stessa:
  ```c
  void process(int rows, int cols, int mat[rows][cols]); // Corretto
  ```

---

### 🔹 7.2 Formule Matematiche di Trasformazione Geometrica

| Trasformazione | Dimensione Input | Dimensione Output | Formula di Mappatura Indici |
| :--- | :---: | :---: | :--- |
| **Diagonale Principale** | $n \times n$ | Array $n$ | `diag[i] = mat[i][i]` |
| **Diagonale Secondaria** | $n \times n$ | Array $n$ | `diag[i] = mat[i][n - 1 - i]` |
| **Rotazione Antioraria 90°** | $m \times n$ ($r \times c$) | $n \times m$ | `B[n - 1 - j][i] = A[i][j]` |
| **Rotazione Oraria 90°** | $m \times n$ | $n \times m$ | `B[j][m - 1 - i] = A[i][j]` |
| **Rotazione 180°** | $m \times n$ | $m \times n$ | `B[m - 1 - i][n - 1 - j] = A[i][j]` |
| **Trasposta** | $m \times n$ | $n \times m$ | `B[j][i] = A[i][j]` |

---

### 🔹 7.3 Funzione di Rotazione e Stampa (`rotate90`)
```c
#include <stdio.h>

void rotate90(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice ruotata (VLA)

    // Trasformazione antioraria 90 gradi
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    // Stampa matrice ruotata
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```

---

### 🔹 7.4 Allocazione Dinamica di Array ed Estrazione Diagonale

#### Estrazione della Seconda Diagonale:
```c
#include <stdlib.h>

int *seconda_diagonale(int n, int m[n][n]) {
    if (n <= 0) return NULL;
    int *diag = malloc(n * sizeof(int));
    if (diag == NULL) return NULL;

    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }
    return diag;
}
```

#### Creazione Dinamica di Array di Fibonacci (`crea_fib`):
```c
#include <stdlib.h>

int *crea_fib(unsigned int n) {
    int *v = malloc(n * sizeof(int));
    if (v == NULL) return NULL;

    for (unsigned int i = 0; i < n; i++) {
        if (i < 2) v[i] = 1;
        else v[i] = v[i - 1] + v[i - 2];
    }
    return v;
}
```
