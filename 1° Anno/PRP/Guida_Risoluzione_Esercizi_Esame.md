---
tags:
  - ProceduralProgramming
---
◀️ *Back to:* [[00_Index_Programmazione_Procedurale]] 

---
# 1. Conversioni di Tipo Implicite ed Esplicite, Promozioni e Precisione

### 🔹 1.1 Gerarchia dei Tipi (Conversion Rank)
$$\text{\_Bool} < \text{char} == \text{signed char} == \text{unsigned char} < \text{short} == \text{unsigned short} < \text{int} == \text{unsigned int} < \text{long} == \text{unsigned long} < \text{long long} == \text{unsigned long long} < \text{float} < \text{double} < \text{long double}$$

> [!NOTE]
> Su architetture Linux standard a 64 bit (data model **LP64**):
> - `char`: 1 byte (8 bit)
> - `short`: 2 byte (16 bit)
> - `int`: 4 byte (32 bit)
> - `long`: 8 byte (64 bit)
> - `long long`: 8 byte (64 bit)
> - `float`: 4 byte (32 bit)
> - `double`: 8 byte (64 bit)

---

### 🔹 1.2 Integer Promotion (Promozione ad Intero)
Si applica automaticamente prima di qualsiasi operazione aritmetica o logica:
- Qualsiasi valore di tipo con rango inferiore a `int` (`_Bool`, `char`, `signed char`, `unsigned char`, `short`, `unsigned short`) viene promosso a:
  - **`int`**: se `int` può rappresentare tutti i valori del tipo di partenza.
  - **`unsigned int`**: se `int` non può rappresentarli tutti (es. `unsigned short` su architetture a 16 bit dove `sizeof(int) == sizeof(short)`).
- **Letterali carattere:** I letterali come `'a'`, `'b'`, `'k'` hanno tipo **`int`** in C (con valore uguale al codice ASCII, es. `'a'` = 97, `'b'` = 98, `'e'` = 101, `'k'` = 107).

---

### 🔹 1.3 Usual Arithmetic Conversions (Conversioni Aritmetiche Usuali)
Regolano gli operandi di operatori binari aritmetici (`+`, `-`, `*`, `/`, `%`) e relazionali (`<`, `<=`, `>`, `>=`, `==`, `!=`):

1. **Floating-Point Dominance:** Se uno degli operandi è un tipo a virgola mobile, l'altro viene convertito al tipo floating-point con rango più elevato (`long double` > `double` > `float`).
2. **Se entrambi sono tipi interi:** Si applicano le promozioni ad intero e poi le seguenti regole:
   - **Stesso tipo:** Nessuna ulteriore conversione.
   - **Stesso signedness (entrambi signed o entrambi unsigned):** L'operando con rango minore viene promosso al tipo con rango maggiore.
   - **Regola 1 (Unsigned Dominance):** Se l'operando `unsigned TipoT` ha rango $\ge$ del rango dell'altro operando, l'altro operando viene convertito a `unsigned TipoT`.
     - *Esempio d'esame:* `int i = -1; unsigned int limit = 200U; if (i < limit)` $\implies$ `i` viene convertito a `unsigned int` (valore $4.294.967.295$). Risultato della condizione: **FALSO**.
   - **Regola 2 (Signed Dominance / Fallback):** Se l'operando con rango maggiore ha tipo `signed TipoT`:
     - Se `signed TipoT` può rappresentare **tutti** i valori del tipo dell'altro operando $\implies$ l'altro operando viene convertito a `signed TipoT`.
     - Se **non** può rappresentarli tutti $\implies$ entrambi gli operandi vengono convertiti a `unsigned TipoT` corrispondente al tipo di rango maggiore.
     - *Esempio d'esame (su LP64):* `unsigned int u = 200U; long l = 30L; u * l` $\implies$ `long` a 64 bit può contenere tutti i valori di `unsigned int` a 32 bit $\implies$ `u` viene convertito a `signed long`.

---

### 🔹 1.4 Aritmetica Modulare (Wrap-around) per i Tipi Unsigned
L'assegnazione o conversione di un valore intero $v$ (positivo o negativo) a un tipo `unsigned` a $N$ bit applica l'aritmetica modulo $2^N$:
$$\text{valore} = v \pmod{2^N}$$
Per un valore negativo $-k$:
$$\text{valore} = 2^N - k = (\text{TIPO\_MAX} + 1) - k$$
- `unsigned short x = -5L;` (16 bit $\implies 2^{16} = 65536$): $\text{valore} = 65536 - 5 = 65531$.
- `unsigned short a = -2LL;` (16 bit): $\text{valore} = 65536 - 2 = 65534$.
- `int b = -1U;` (32 bit): `-1U` vale $4.294.967.295$; assegnato a `signed int` (a 32 bit in complemento a 2) memorizza il pattern di bit `0xFFFFFFFF`, che corrisponde a $-1$.

---

### 🔹 1.5 Precisione Numerica: Float vs Double (IEEE 754)
All'esame viene spesso chiesto se il valore finale di una variabile sia determinabile o se si verifichi perdita di precisione:
- **`float` (32 bit totali):**
  - Mantissa a 24 bit (compreso bit implicito) $\implies \approx 6\text{--}7$ cifre decimali significative ($2^{24} = 16.777.216$).
  - **Non è possibile stabilire il valore esatto** se si sommano o manipolano valori che eccedono le 6-7 cifre decimali (es. `UINT_MAX + c - 7` dove `UINT_MAX = 4294967295` ha 10 cifre $\implies$ perdita di precisione per troncamento).
  - **È possibile stabilire il valore esatto** se il risultato ha $\le 6$ cifre decimali significative (es. $65533.0$ ha 5 cifre decimali $\implies$ perfettamente rappresentabile).
- **`double` (64 bit totali):**
  - Mantissa a 53 bit $\implies \approx 15\text{--}17$ cifre decimali significative ($2^{53} \approx 9 \times 10^{15}$).
  - Numeri con decine di cifre (es. $65542$ con 5 cifre) sono **esattamente rappresentabili**.

---

### 🛠️ Algoritmo di Risoluzione per Esercizi sulle Conversioni
1. **Identifica tutte le espressioni** (operazioni binarie, chiamate a funzione, ritorni, assegnamenti).
2. **Traccia gli argomenti di chiamata:** se passi `unsigned short` a un parametro `int`, annota la promozione `da unsigned short a int`.
3. **Analizza i letterali:** i caratteri passano da `int` a `char` se assegnati a variabili `char`, o subiscono promozioni aritmetiche ordinarie.
4. **Applica le regole binarie:** per ogni `+`, `-`, `*`, `/`, determina quale operando viene convertito in base a Dominance Floating-Point, Regola 1 o Regola 2.
5. **Traccia il tipo del valore di ritorno:** conversione dal tipo dell'espressione al tipo dichiarato della funzione.
6. **Traccia l'assegnamento finale:** conversione dal tipo di ritorno al tipo della variabile ricevente.
7. **Calcola il valore finale** e giustifica la precisione (conta le cifre significative rispetto alla mantissa del tipo target).

---

# 2. Mappe di Memoria, Endianness, Complemento a Due e Puntatori

### 🔹 2.1 Rappresentazione in Complemento a Due a $N$ bit
1. **Numeri Positivi ($x \ge 0$):**
   - Rappresentazione binaria diretta estesa su $N$ bit.
2. **Numeri Negativi ($-x < 0$):**
   - Calcola il valore assoluto su $N$ bit.
   - Inverti tutti i bit ($\sim$) e aggiungi $1$.
   - *Formula rapida:* valore binario $= 2^N - |x|$.
3. **Costanti Note e Trucchi d'Esame:**
   - `INT_MAX` (32 bit): `0x7FFFFFFF` (bit di segno 0, 31 bit a 1).
   - `INT_MIN` (32 bit): `0x80000000` (valore $-2^{31}$).
   - `(INT_MAX + INT_MIN) + 1` $= 0x7FFFFFFF + 0x80000000 + 1 = (-1) + 1 = 0$.
   - `LLONG_MIN` (64 bit): `0x8000000000000000` (valore $-2^{63}$).
   - `(LLONG_MAX + 1)` provoca overflow a 64 bit e coincide con `LLONG_MIN`.
   - `LLONG_MIN + 512`: byte 0-1 = `0x0200`, byte 2-6 = `0x00`, byte 7 (MSB) = `0x80`.

---

### 🔹 2.2 Architettura Little-Endian
Il **Byte meno significativo (LSB)** viene memorizzato all'**indirizzo di memoria più basso**:
- Es. `int val = 0x12345678;` allocato all'indirizzo base `0`:
  - Byte 0 (`base + 0`): `0x78` (LSB)
  - Byte 1 (`base + 1`): `0x56`
  - Byte 2 (`base + 2`): `0x34`
  - Byte 3 (`base + 3`): `0x12` (MSB)

---

### 🛠️ Algoritmo di Costruzione della Mappa di Memoria

```
 Indice Byte   Contenuto Esadecimale/Binario    Puntatori / Alias
 ──────────────────────────────────────────────────────────────────
   Byte 0      [ LSB elem 0 ]                 <- a, (short*)p, (char*)q
   Byte 1      [ ...        ]
   Byte 2      [ ...        ]                 <- &p[1] (se p è short*)
   Byte 3      [ MSB elem 0 ]
   Byte 4      [ LSB elem 1 ]                 <- &p[2] (se p è short*), &p[1] (se p è int*)
   ...
   Byte k      [ ...        ]                 <- q + k
```

1. **Calcolo della dimensione totale:** $\text{Totale Byte} = (\text{numero elementi array}) \times \text{sizeof}(\text{tipo array})$.
2. **Inizializzazione dei byte:**
   - Converti ogni elemento iniziale in esadecimale su $N$ byte.
   - Disponi i byte in tabella con indirizzo crescente (LSB all'indirizzo più basso).
3. **Calcolo dell'Offset delle Istruzioni Modificatrici:**
   $$\text{Offset in Byte} = \text{Indice} \times \text{sizeof}(*\text{puntatore})$$
   - `short *p = (short*)a; p[k] = val;` $\implies$ modifica 2 byte a partire dall'offset $k \times 2$.
   - `int *p = (int*)a; p[k] += val;` $\implies$ legge 4 byte da $k \times 4$, somma `val`, e riscrive in Little-Endian.
   - `char *q = (char*)a; *(q + k) = val;` $\implies$ modifica il singolo byte $k$.
   - `q[k] = ~q[k];` $\implies$ inverte tutti gli 8 bit del byte $k$.

---

### 🔹 2.3 Analisi delle Asserzioni e Trabocchetti Tipici

| Tipo di Espressione | Come si Valuta | Trabocchetto / Regola |
| :--- | :--- | :--- |
| **Sottrazione Puntatori:** `&p[i] - &p[j]` | Risultato intero $= i - j$ | Conta il numero di **elementi del tipo puntato**, non i byte! |
| **Differenza Indirizzi con Cast:** `(int)(p + i) - (int)(a + j)` | $(\text{Offset Byte}_p) - (\text{Offset Byte}_a)$ | Il cast a tipo intero calcola la distanza reale in **singoli byte**. |
| **Dereferenziazione Reinterpretata:** `*((long long*)(&p[i]))` | Legge 8 byte consecutivi a partire dal byte $i \times 2$ | Ricostruisci il valore in Little-Endian. Se il bit più significativo (bit 63) è $1$, il valore è **negativo**. |
| **Confronto Indirizzi:** `((long long*)(&p[1])) < ((short*)(&p[2]))` | Confronta la posizione in memoria di `&p[1]` vs `&p[2]` | L'indirizzo del byte 2 precede sempre il byte 4. Il cast al tipo puntato non cambia il valore dell'indirizzo! |
| **Operatori Bitwise su Puntatori:** `q[5] | (short*)(&a[4])` | **Errore di Compilazione** | Gli operatori bitwise (`|`, `&`, `^`) richiedono operandi di tipo intero e non sono definiti sui puntatori. |

---

# 3. Tracing di Codice: Basi Numeriche, Precedenze, Sequence Points e UB

### 🔹 3.1 Basi Numeriche nei Letterali Interi
- **Ottale (Base 8):** Inizia con lo zero `0...` (cifre ammesse 0-7).
  - `025` $= 2 \times 8^1 + 5 \times 8^0 = 16 + 5 = 21$.
  - `036` $= 3 \times 8^1 + 6 \times 8^0 = 24 + 6 = 30$.
- **Esadecimale (Base 16):** Inizia con `0x...` o `0X...` (cifre 0-9, a-f / A-F).
  - `0x1A` $= 1 \times 16 + 10 = 26$.
  - `0x2d` $= 2 \times 16 + 13 = 45$.
  - `0xae` $= 10 \times 16 + 14 = 174$.
  - `0xfb` $= 15 \times 16 + 11 = 251$.

---

### 🔹 3.2 Precedenza, Associatività e Catene di Operatori

1. **Catene di Operatori Relazionali:** In C le espressioni relazionali associano da **sinistra a destra**:
   - `0 > a++ < 0` viene valutata come: `(0 > a++) < 0`.
   - Se `a` vale 1: `(0 > 1)` produce `0` (falso). Poi `0 < 0` produce `0` (falso).
2. **Operatore Virgola (`,`):**
   - Ha la **priorità minima assoluta**.
   - Valuta il primo operando, introduce un **Sequence Point**, scarta il valore e valuta il secondo operando restituendone il risultato.
3. **Operatori di Cortocircuito (`&&`, `||`):**
   - `A && B`: Se `A == 0`, `B` **non viene eseguito**. Introduce un sequence point dopo `A`.
   - `A || B`: Se `A != 0`, `B` **non viene eseguito**. Introduce un sequence point dopo `A`.
4. **Operatore Ternario (`cond ? expr1 : expr2`):**
   - Introduce un sequence point dopo `cond`. Viene valutata solo l'espressione del ramo scelto.
5. **Operatori di Shift Bit a Bit (`<<`, `>>`):**
   - `a <<= 1` equivale a moltiplicare per 2 (shift a sinistra).
   - `a >>= 1` equivale a divisione intera per 2 (shift a destra).

---

### 🔹 3.3 Sequence Points e "Multiple Unsequenced Modifications" (UB)
Nello standard C, modificare una variabile più di una volta, o leggerla e modificarla contemporaneamente senza un **Sequence Point** intermedio, genera **Undefined Behavior (UB)** e warning del compilatore:

- ❌ `a = a++;` $\implies$ **UB / Warning** (due modifiche senza sequence point).
- ❌ `a++ + a++;` $\implies$ **UB / Warning**.
- ✅ `a = 2, a++;` $\implies$ **Valido** (la virgola `,` è un sequence point; contiene 2 effetti collaterali).
- ✅ `a++ && a++;` $\implies$ **Valido** (`&&` introduce un sequence point).
- ✅ `a++ || a++;` $\implies$ **Valido** (`||` introduce un sequence point).
- ✅ `a++ ? a++ : a++;` $\implies$ **Valido** (`?` introduce un sequence point).

---

### 🔹 3.4 Puntatori Fuori Limite e Stampa di Valori Indefiniti (`_`)
- Quando un puntatore viene incrementato oltre l'oggetto allocato (es. `int i; int *p = &i; p++; *p;`), l'accesso a memoria non appartenente all'oggetto è **Undefined Behavior**.
- Nei compiti d'esame, quando il codice dereferenzia un puntatore avanzato oltre l'oggetto, il valore corrispondente nella `printf` va indicato con **`_` (indefinito)**.
- **Aritmetica esadecimale e riporti:** Se `b` è a `0x7ffee4399ffe`, l'espressione `((short*)b) + 1` avanza di $\text{sizeof}(\text{short}) = 2$ byte:
  $$0\text{x}\dots9\text{ffe} + 2 = 0\text{x}\dots9\text{fff} + 1 = 0\text{x}\dots\text{a000}$$
- **Cast annidati su puntatori:** `(short*)(long*)b + 1` aggiunge la dimensione del tipo finale (`short` = 2 byte), non del cast intermedio `long*`.

---

# 4. Dichiarazioni, Definizioni, Scope, Linkage e Durata di Memorizzazione

### 🔹 4.1 I Concetti Fondamentali

Per risolvere correttamente gli esercizi d'esame su questo argomento, occorre tenere ben distinte 4 dimensioni ortogonali di ogni identificatore:

#### 1. Dichiarazione vs Definizione vs `typedef`
* **Dichiarazione (*Declaration*):** Notifica al compilatore l'esistenza e il tipo di un identificatore (variabile o funzione) senza allocare spazio in memoria.
  * Esempi: `extern int b;`, prototipi di funzioni come `extern long int cfun(float, float);`.
* **Definizione (*Definition*):** Riserva effettivamente memoria per una variabile (nel segmento dati o nello stack) oppure fornisce il corpo `{ ... }` di una funzione.
  * Esempi: `int a = 2;`, `static int c = 1;`, variabili locali `int q;`, `static double e = 4.2;`, funzioni con corpo `{ ... }`.
* **`typedef` (Alias di Tipo):**
  * Introduce un **sinonimo di un tipo di dato già esistente** (es. `typedef long int interol;`).
  * **Non dichiara né alloca alcuna variabile** in memoria.
  * Non influenza in alcun modo il linkage delle variabili che in seguito useranno quel tipo: scrivere `interol a = 2;` è al 100% equivalente a scrivere `long int a = 2;`.
* **Tentative Definition (Definizione Tentativa):**
  * Riguarda le dichiarazioni globali (a livello di file) prive di specificatori di classe di memoria (`extern`/`static`) e prive di valore iniziale (es. `interol a;` o `int a;`).
  * Se nel file esiste già una definizione esplicita della variabile (`interol a = 2;`), le successive righe `interol a;` rimangono **dichiarazioni**.
  * Se nel file non compare alcuna definizione con inizializzazione, la tentative definition si trasforma automaticamente nella definizione effettiva della variabile (inizializzata a zero dal compilatore).

---

#### 2. Scope (Ambito di Visibilità nel Codice Sorgente)
Lo **Scope** è una proprietà puramente sintattica gestita dal compilatore: indica *in quali righe del file sorgente* un determinato identificatore è visibile e utilizzabile per nome.

* **File Scope (Ambito di File / Globale):**
  * Riguarda identificatori dichiarati **fuori da qualsiasi funzione**.
  * Il nome è visibile dal punto esatto in cui viene dichiarato fino alla fine di quel file sorgente `.c`.
* **Block Scope (Ambito di Blocco / Locale):**
  * Riguarda identificatori dichiarati **all'interno di un blocco racchiuso tra parentesi graffe `{ ... }`**, inclusi i parametri formali della funzione.
  * Il nome è visibile esclusivamente dall'interno di quel blocco e cessa di essere accessibile alla chiusura della parentesi `}`.

---

#### 3. Linkage (Collegamento tra Unità di Traduzione / File)
Il **Linkage** è una proprietà gestita dal linker: stabilisce se dichiarazioni con lo stesso nome in punti diversi (o in file `.c` diversi) si riferiscono alla **stessa identica entità in memoria**.

* **Linkage Esterno (*External Linkage*):**
  * **Chi lo possiede:**
    * Variabili a livello di file dichiarate senza `static` (es. `interol a = 2;`, `int x;`).
    * Variabili o funzioni precedute da `extern` (es. `extern int b;`, `extern long int cfun(...)`).
    * Funzioni definite normalmente senza `static`.
  * **Cosa significa:** Il simbolo viene esportato nella tabella dei simboli dell'eseguibile. Può essere referenziato e condiviso da qualsiasi altro file `.c` del progetto tramite una dichiarazione `extern`.
* **Linkage Interno (*Internal Linkage*):**
  * **Chi lo possiede:**
    * Variabili globali e funzioni dichiarate a livello di file con la parola chiave **`static`** (es. `static int c = 1;`, `static int* my_func(...)`).
  * **Cosa significa:** Il simbolo è strettamente privato a quel singolo file `.c` (unità di traduzione). Il linker non lo esporterà verso altri file, evitando collisioni di nomi con variabili omonime in altri moduli.
  * *Casi particolari d'esame:* Se dentro una funzione locale si scrive `extern int c;`, e a monte a livello di file era stato definito `static int c = 1;`, quel riferimento locale eredita il **linkage interno** della definizione presente nel file.
* **Nessun Linkage (*No Linkage*):**
  * **Chi lo possiede:**
    * Tutte le entità a livello di blocco (variabili locali automatiche, parametri di funzioni, variabili locali marcate `static`).
  * **Cosa significa:** L'identificatore si riferisce solo a quell'entità locale e non partecipa a nessuna risoluzione da parte del linker tra blocchi o file differenti.

---

#### 4. Storage Duration (Tempo di Vita / Durata di Memorizzazione)
Indica *quando* viene allocata la memoria per l'oggetto e per quanto tempo rimane valida durante l'esecuzione del programma:

* **Static Storage Duration:** La memoria viene riservata all'avvio del programma (segmento dati/BSS) e rimane valida fino al termine dell'esecuzione. Hanno durata statica tutte le variabili a livello di file (globali) e le variabili locali dichiarate con `static`.
* **Automatic Storage Duration:** La memoria viene allocata nello stack frame all'entrata nel blocco di funzione e distrutta automaticamente all'uscita dal blocco (tipico di parametri formali e variabili locali normali).

---

### 🔹 4.2 Guida Pratica e Regole di Risoluzione per l'Esame

Quando all'esame viene richiesto di analizzare ogni identificatore specificando se è **definito o dichiarato** e il suo **linkage**:

1. **Linee con `typedef` (es. `typedef long int interol;`):**
   * Non è una variabile ma un alias di tipo.
   * *Risposta:* Definizione di tipo / Nessun linkage.

2. **Variabili globali (a livello di file):**
   * `interol a = 2;` $\implies$ **Definito**, **Linkage Esterno** (ha valore iniziale ed è fuori da funzioni senza `static`).
   * `interol a;` successiva $\implies$ **Dichiarato** (tentativo di dichiarazione che rimane dichiarazione poiché `a` è già definita sopra), **Linkage Esterno**.
   * `extern int b;` $\implies$ **Dichiarato**, **Linkage Esterno** (`extern` senza inizializzazione).
   * `static int c = 1;` $\implies$ **Definito**, **Linkage Interno** (`static` a livello file).

3. **Funzioni a livello di file:**
   * `extern long int cfun(float, float);` $\implies$ **Dichiarato**, **Linkage Esterno** (solo prototipo/firma).
   * `static int* my_func(int d) { ... }` $\implies$ **Definito**, **Linkage Interno** (ha corpo `{ ... }` e prefisso `static`).

4. **Identificatori dentro una funzione (Block Scope):**
   * Parametri formali (`int d`): **Definito**, **No Linkage**.
   * Variabili locali statiche (`static double e = 4.2;`): **Definito**, **No Linkage** (la durata è statica, ma il linkage è nullo).
   * Puntatori e variabili locali ordinarie (`double *f = &e;`, `int q;`): **Definito**, **No Linkage**.
   * Dichiarazioni `extern` locali (`extern int c;` dentro la funzione): **Dichiarato**, **Linkage Interno** se a monte nel file c'è una definizione `static int c`, altrimenti **Linkage Esterno**.

---

# 5. Gestione Dinamica della Memoria (Heap), Lvalue/Rvalue e Fasi di GCC

### 🔹 5.1 Funzioni per la Memoria Dinamica (`<stdlib.h>`)
1. **`void* malloc(size_t size)`**:
   - Alloca un blocco contiguo di `size` byte sull'Heap.
   - **I byte non vengono inizializzati** (contengono valori casuali/spazzatura).
   - Ritorna il puntatore al blocco o `NULL` in caso di memoria insufficiente.
2. **`void* calloc(size_t num, size_t size)`**:
   - Alloca `num * size` byte e **azzera tutti i bit** (imposta a 0).
   - `calloc(5, 3)` e `malloc(15)` allocano esattamente la stessa quantità di byte (15 byte).
3. **`void* realloc(void *ptr, size_t new_size)`**:
   - Prende **due parametri**: puntatore al blocco esistente e nuova dimensione in byte.
   - Ritorna `void*` (può essere lo stesso indirizzo o un nuovo indirizzo rilocato; ritorna `NULL` / `0` se fallisce).
   - Se `ptr == NULL`, si comporta come `malloc(new_size)`.
   - L'indirizzo ritornato **non è necessariamente uguale** all'indirizzo originario.
4. **`free(void *ptr)`**:
   - Dealloca memoria precedentemente allocata su Heap. Non restituisce valori (`void`).
   - ⚠️ **Errore Grave d'Esame:** Eseguire `free()` su una variabile allocata sullo **Stack** (es. `int a; int *p = &a; free(p);`) provoca **Undefined Behavior / Crash a runtime**.

---

### 🔹 5.2 Concetto di Lvalue ed Rvalue
- **lvalue (Locator Value):** Espressione che identifica una locazione di memoria memorizzabile e persistente (un "oggetto"). Può comparire a sinistra di un operatore di assegnamento:
  - Variabili: `a`, `p`.
  - Dereferenziazioni: `*p`, `*&a`, `**&p`, `a[i]`.
- **rvalue (Read Value):** Espressione temporanea che rappresenta un valore computato. Non ha una locazione di memoria a cui riassegnare direttamente un valore:
  - Costanti e letterali: `5`, `3.14`, `'a'`.
  - Risultati di espressioni aritmetiche/logiche: `a + 2`, `x && y`.
  - Indirizzi temporanei: `&a` (è un rvalue, mentre `*&a` è un lvalue).

---

### 🔹 5.3 Le 4 Fasi del Compilatore GCC

$$\text{Sorgente (.c)} \xrightarrow{\text{1. Preprocessore (cpp)}} \text{.i} \xrightarrow{\text{2. Compilatore (cc1)}} \text{Assembly (.s)} \xrightarrow{\text{3. Assembler (as)}} \text{Oggetto (.o)} \xrightarrow{\text{4. Linker (ld)}} \text{Eseguibile}$$

1. **Preprocessore (`cpp`):** Elabora le direttive con cancelletto `#` (`#include`, `#define`, `#ifdef`), rimuove i commenti ed effettua l'espansione testuale delle macro.
2. **Compilatore (`cc1`):** Esegue l'analisi lessicale, sintattica e semantica del codice C espanso, traducendolo in file Assembly (`.s`).
3. **Assembler (`as`):** Traduce le istruzioni Assembly in linguaggio macchina, generando un file oggetto binario rilocabile (`.o`).
4. **Linker (`ld`):** Risolve le chiamate alle funzioni di libreria e i simboli esterni tra molteplici file oggetto, assemblando il file eseguibile finale.

---

# 6. Strutture Dati Dinamiche: Liste Semplicemente Collegate

### 🔹 6.1 Struttura del Nodo Standard
```c
struct Node {
    int info;
    struct Node *pNext;
};
```

---

### 🔹 6.2 Metodologia per la Manipolazione di Liste

1. **Controllo di Esistenza e Casi Limite:**
   - Verificare sempre se la lista è vuota (`head == NULL`) o se ha meno elementi di quelli richiesti dall'operazione (es. `head->pNext == NULL`).
2. **Cancellazione in Posizione $k$ (con puntatore globale o locale):**
   - Mantenere due puntatori: `prev` (che punta al nodo $k-1$) e `curr` (che punta al nodo $k$).
   - Ricollegare: `prev->pNext = curr->pNext;`
   - Deallocare sempre la memoria: `free(curr);`

---

### 📋 Modelli di Risoluzione d'Esame

#### Modello 1: Cancellazione Condizionale del 3° Nodo con Puntatore Globale `pFirst`
```c
void cancella_se_3_posizione(int key) {
    struct Node *prev, *curr;

    // 1. Controllo preliminare: la lista deve contenere almeno 3 nodi
    if (pFirst == NULL || pFirst->pNext == NULL || pFirst->pNext->pNext == NULL) {
        return;
    }

    // 2. Posizionamento
    prev = pFirst->pNext;       // 2° nodo
    curr = prev->pNext;         // 3° nodo

    // 3. Verifica condizione e rimozione
    if (curr->info == key) {    // Oppure: curr->info % key != 0 in base alla traccia
        prev->pNext = curr->pNext; // Salta il 3° nodo ricollegando il 2° al 4°
        free(curr);                // Libera la memoria del 3° nodo
    }
}
```

#### Modello 2: Creazione / Fusione Alternata di Due Liste con Inserimento in Coda $O(1)$
```c
struct Node* alternate(struct Node *l1, struct Node *l2) {
    struct Node *head = NULL;
    struct Node *tail = NULL;

    while (l1 != NULL && l2 != NULL) {
        // --- Allocazione e copia elemento da l1 ---
        struct Node *n1 = malloc(sizeof(struct Node));
        if (n1 == NULL) return NULL; // Controllo obbligatorio allocazione
        n1->info = l1->info;
        n1->pNext = NULL;

        if (head == NULL) {
            head = tail = n1;
        } else {
            tail->pNext = n1;
            tail = n1;
        }

        // --- Allocazione e copia elemento da l2 ---
        struct Node *n2 = malloc(sizeof(struct Node));
        if (n2 == NULL) return NULL;
        n2->info = l2->info;
        n2->pNext = NULL;

        tail->pNext = n2;
        tail = n2;

        // Avanzamento delle liste sorgente
        l1 = l1->pNext;
        l2 = l2->pNext;
    }
    return head;
}
```

---

# 7. Matrici 2D e VLA (Variable-Length Arrays)

### 🔹 7.1 Regole sui VLA (C99)
- Nei parametri di funzione, le **dimensioni** della matrice devono essere passate **prima** della matrice stessa:
  ```c
  void elabora(int rows, int cols, int mat[rows][cols]); // Corretto
  ```
- In memoria le matrici C sono disposte in ordine **Row-Major** (riga per riga in modo contiguo). L'elemento `mat[i][j]` si trova all'offset:
  $$\text{Offset} = (i \times \text{cols} + j) \times \text{sizeof}(\text{tipo})$$

---

### 🔹 7.2 Formule Generali per Diagonali e Trasformazioni Geometriche

| Trasformazione / Estrazione | Dimensione Input | Dimensione Output | Formula di Mappatura Indici |
| :--- | :--- | :--- | :--- |
| **Diagonale Principale** | $n \times n$ | Array di $n$ | `diag[i] = mat[i][i]` |
| **Diagonale Secondaria** | $n \times n$ | Array di $n$ | `diag[i] = mat[i][n - 1 - i]` |
| **Rotazione Antioraria 90°** | $m \times n$ (righe $\times$ col) | $n \times m$ | `B[n - 1 - j][i] = A[i][j]` |
| **Rotazione Oraria 90°** | $m \times n$ | $n \times m$ | `B[j][m - 1 - i] = A[i][j]` |
| **Rotazione 180°** | $m \times n$ | $m \times n$ | `B[m - 1 - i][n - 1 - j] = A[i][j]` |
| **Trasposta** | $m \times n$ | $n \times m$ | `B[j][i] = A[i][j]` |

---

### 📋 Modelli di Risoluzione d'Esame

#### Modello 1: Estrazione Diagonale Secondaria con Allocazione Dinamica
```c
int* seconda_diagonale(int n, int m[n][n]) {
    if (n <= 0) return NULL;

    int *diag = malloc(n * sizeof(int));
    if (diag == NULL) return NULL;

    for (int i = 0; i < n; i++) {
        diag[i] = m[i][n - 1 - i];
    }
    return diag;
}
```

#### Modello 2: Rotazione Matrice Antioraria di 90° e Stampa
```c
void rotate90(int m, int n, int A[m][n]) {
    int B[n][m]; // Matrice VLA locale ruotata

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[n - 1 - j][i] = A[i][j];
        }
    }

    // Stampa riga per riga della matrice ruotata
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
}
```
