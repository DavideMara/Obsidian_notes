---
tags:
  - ProceduralProgramming
  - ExamPrep
  - Theory
  - CheatSheet
---
◀️ *Torna all'Indice Generale:* [[00_Index_Programmazione_Procedurale]]

# 📐 Guida Definitiva: Teoria, Tabelle di Conversione e Regole per gli Esercizi — PRP

---
## 🔀 Tipologia 1: Conversioni di Tipo Implicite e Promozione Aritmetica

I riferimenti principali nelle note complete si trovano in **[[PRP_Complete_Notes#05-type-conversions]]** e **[[PRP_Complete_Notes#21-data-representation--computer-arithmetic-c-context]]**.

### 📊 Prontuario e Tabelle di Conversione Rapida

#### Tabella 1.1: Tipi di Dato C, Grado di Conversione (Rank), Dimensione e Range
| Tipo di Dato           | Dimensione Tipica (x86_64 / LP64) | Grado (Rank) | Range Approssimativo / Esatto                        | Note Promozione                                |
| :--------------------- | :-------------------------------: | :----------: | :--------------------------------------------------- | :--------------------------------------------- |
| `char` / `signed char` |          1 byte (8 bit)           |      1       | da $-128$ a $+127$                                   | Promosso a `int` nelle espressioni             |
| `unsigned char`        |          1 byte (8 bit)           |      1       | da $0$ a $255$                                       | Promosso a `int`                               |
| `short` / `short int`  |          2 byte (16 bit)          |      2       | da $-32768$ a $+32767$                               | Promosso a `int`                               |
| `unsigned short`       |          2 byte (16 bit)          |      2       | da $0$ a $65535$                                     | Promosso a `int`                               |
| `int` / `signed int`   |          4 byte (32 bit)          |      3       | da $-2^{31}$ a $+2^{31}-1$ ($-2.14 \times 10^9$)     | Tipo di base per integer promotion             |
| `unsigned int`         |          4 byte (32 bit)          |      3       | da $0$ a $2^{32}-1$ ($4294967295$)                   | Domina su `int` per Regola 1                   |
| `long` / `long int`    |       8 byte (64 bit Linux)       |      4       | da $-2^{63}$ a $+2^{63}-1$                           | Domina su `unsigned int` se 64-bit (Regola 2a) |
| `unsigned long`        |       8 byte (64 bit Linux)       |      4       | da $0$ a $2^{64}-1$                                  | Domina su `long` e tipi inferiori              |
| `float`                |          4 byte (32 bit)          |   Reale 1    | $\approx \pm 3.4 \times 10^{38}$ (6-7 cifre sig.)    | Convertito a `double` se accoppiato            |
| `double`               |          8 byte (64 bit)          |   Reale 2    | $\approx \pm 1.7 \times 10^{308}$ (15-17 cifre sig.) | Tipo standard nei calcoli reali                |
| `long double`          |       16 byte (80/128 bit)        |   Reale 3    | Massima precisione                                   | Domina tutti i tipi reali                      |

---

#### Tabella 1.2: Gerarchia delle Conversioni Aritmetiche Implicite (`A op B`)
Quando due operandi partecipano a un'operazione binaria (`+`, `-`, `*`, `/`, `<`, `>`, `==`, etc.):

```text
      [ long double ]  <-- Massima priorità reale
            ^
       [ double ]
            ^
        [ float ]
            ^
  ===================== (Se entrambi gli operandi sono interi) =====================
  1. Integer Promotion: char / short -> int (o unsigned int)
  2. Valutazione Tipi Interi (Usual Arithmetic Conversions):
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ Condizione Tipi Operandi (A, B)      │ Risultato Conversione             │
     ├──────────────────────────────────────┼───────────────────────────────────┤
     │ Stesso Segno (entrambi Signed/Unsigned)│ Operando con Rank minore -> Rank maggiore │
     │ Unsigned Rank >= Signed Rank (Regola 1)│ Operando Signed -> Unsigned       │
     │ Signed Rank > Unsigned Rank (Regola 2a)│ Unsigned -> Signed (se capiente)  │
     │ Signed Rank > Unsigned Rank (Regola 2b)│ Entrambi -> Unsigned del Signed   │
     └──────────────────────────────────────┴───────────────────────────────────┘
```

---

#### Tabella 1.3: Assegnazioni Negative a Tipi Unsigned (Modulo $2^N$)
In C, l'assegnazione o la conversione di un valore negativo $V < 0$ a un tipo `unsigned` di $N$ bit applica la formula:
$$\text{Valore Unsigned} = (V + 2^N) \pmod{2^N}$$

| Valore Negativo Iniziale | Tipo Destinazione Unsigned | Dimensione ($N$ bit) |     Modulo $2^N$      |      Risultato Finale Unsigned      |
| :----------------------: | :------------------------- | :------------------: | :-------------------: | :---------------------------------: |
|          `-1L`           | `unsigned char`            |        8 bit         |      $2^8 = 256$      |      $-1 + 256 = \mathbf{255}$      |
|          `-1L`           | `unsigned short`           |        16 bit        |   $2^{16} = 65536$    |    $-1 + 65536 = \mathbf{65535}$    |
|          `-5L`           | `unsigned short`           |        16 bit        |   $2^{16} = 65536$    |    $-5 + 65536 = \mathbf{65531}$    |
|          `-7L`           | `unsigned short`           |        16 bit        |   $2^{16} = 65536$    |    $-7 + 65536 = \mathbf{65529}$    |
|           `-1`           | `unsigned int`             |        32 bit        | $2^{32} = 4294967296$ | $-1 + 2^{32} = \mathbf{4294967295}$ |

---

#### Tabella 1.4: Tabella ASCII Rapida per gli Esercizi d'Esame
> **Nota Fondamentale:** In C, le costanti carattere (es. `'a'`, `'g'`, `'0'`) sono **espressioni di tipo `int`** con valore numerico pari al relativo codice ASCII.

| Carattere | Codice ASCII (`int`) | Espressione / Differenza Frequente d'Esame             |   Risultato Calcolato    |
| :-------: | :------------------: | :----------------------------------------------------- | :----------------------: |
|   `'0'`   |          48          | `'5' - '0'` (conversione cifra char $\rightarrow$ int) |  $53 - 48 = \mathbf{5}$  |
|   `'a'`   |          97          | Baseline minuscole                                     |           $97$           |
|   `'b'`   |          98          | `'b' - 'a'`                                            |  $98 - 97 = \mathbf{1}$  |
|   `'d'`   |         100          | `'d' - 'a'`                                            | $100 - 97 = \mathbf{3}$  |
|   `'e'`   |         101          | `'e' - 'a'`                                            | $101 - 97 = \mathbf{4}$  |
|   `'g'`   |         103          | `'g' - 'a'` (Esame 3 Giugno)                           | $103 - 97 = \mathbf{6}$  |
|   `'k'`   |         107          | `'k' - 'd'` (Esame 15 Gennaio)                         | $107 - 100 = \mathbf{7}$ |
|   `'n'`   |         110          | `'n'` (Esame 3 Giugno)                                 |          $110$           |
|   `'A'`   |          65          | Baseline maiuscole                                     |           $65$           |

---

#### Tabella 1.5: Precisione e Rappresentabilità Floating-Point
| Tipo     | Bit Totali | Bit Mantissa | Cifre Decimali Significative | Integrità su Interi Superiori a                                                 |
| :------- | :--------: | :----------: | :--------------------------: | :------------------------------------------------------------------------------ |
| `float`  |   32 bit   |    24 bit    |       **6 - 7 cifre**        | Perdita di precisione se intero $> 2^{24} = 16.777.216$                         |
| `double` |   64 bit   |    53 bit    |      **15 - 17 cifre**       | Rappresentazione **esatta** per interi fino a $2^{53} \approx 9 \times 10^{15}$ |

---

### 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

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

## 🔄 Tipologia 2: Tracing di Codice C, Cicli, Bitwise e Precedenza Operatori


### 📊 Prontuario e Tabelle Rapide per il Tracing

#### Tabella 2.1: Conversione Basi Numeriche Recorrenti negli Esami
| Decimale | Ottale (Prefisso `0`) | Esadecimale (Prefisso `0x`) | Rappresentazione Binaria (8 bit) | Note / Esercizi d'Esame                  |
| :------: | :-------------------: | :-------------------------: | :------------------------------: | :--------------------------------------- |
|  **3**   |         `03`          |           `0x03`            |           `0000 0011`            | Costante ternario                        |
|  **6**   |         `06`          |           `0x06`            |           `0000 0110`            | Target di condizionale                   |
|  **10**  |         `012`         |       `0x0A` / `0xa`        |           `0000 1010`            | $1 \times 8 + 2 = 10$                    |
|  **12**  |         `014`         |       `0x0C` / `0xc`        |           `0000 1100`            | Valore intermedio shift                  |
|  **15**  |         `017`         |       `0x0F` / `0xf`        |           `0000 1111`            | Maschera 4 bit bassi                     |
|  **21**  |         `025`         |           `0x15`            |           `0001 0101`            | $2 \times 8 + 5 = 21$ (Esame 15 Gennaio) |
|  **26**  |         `032`         |       `0x1A` / `0x1a`       |           `0001 1010`            | $1 \times 16 + 10 = 26$                  |
|  **27**  |         `033`         |       `0x1B` / `0x1b`       |           `0001 1011`            | Esame 30 Gennaio                         |
|  **30**  |         `036`         |       `0x1E` / `0x1e`       |           `0001 1110`            | $1 \times 16 + 14 = 30$ (Esame 3 Giugno) |
|  **47**  |         `057`         |           `0x2F`            |           `0010 1111`            | $21 + 26 = 47$                           |
|  **59**  |         `073`         |           `0x3B`            |           `0011 1011`            | $7 \times 8 + 3 = 59$ (Esame 3 Giugno)   |
| **251**  |        `0373`         |       `0xFB` / `0xfb`       |           `1111 1011`            | Esame Prova 1                            |

---

#### Tabella 2.2: Operatori Bitwise (Tabella di Verità e Proprietà)
| Bit $A$ | Bit $B$ | AND (`A & B`) | OR (`A |  B`)  |           XOR (`A ^ B`)           | NOT (`~A`) su 8 bit |
| :-----: | :-----: | :-----------: | :----: | :---: | :-------------------------------: | ------------------- |
|    0    |    0    |     **0**     | **0**  | **0** | **1** (`11111111_2 = 255` o `-1`) |                     |
|    0    |    1    |     **0**     | **1**  | **1** |               **1**               |                     |
|    1    |    0    |     **0**     | **1**  | **1** |     **0** (`00000000_2 = 0`)      |                     |
|    1    |    1    |     **1**     | **1**  | **0** |               **0**               |                     |

* **Shift a Destra (`x >> k`):** Sposta i bit a destra di $k$ posizioni (divisione intera per $2^k$). Es: $26 >> 1 = 13$.
* **Shift a Sinistra (`x << k`):** Sposta i bit a sinistra di $k$ posizioni (moltiplicazione per $2^k$). Es: $3 << 1 = 6$.

---

#### Tabella 2.3: Precedenza e Associatività degli Operatori in C
| Priorità | Operatori | Descrizione | Associatività |
| :---: | :--- | :--- | :---: |
| **1 (Massima)** | `()`, `[]`, `->`, `.` | Parentesi, array, accesso membri | Da sinistra a destra |
| **2** | `++`, `--` (post), `!`, `~`, `+`, `-` (unari), `*` (indirezione), `&` (indirizzo), `(type)`, `sizeof` | Operatori unari e post-incremento | Da destra a sinistra |
| **3** | `++`, `--` (pre) | Pre-incremento e pre-decremento | Da destra a sinistra |
| **4** | `*`, `/`, `%` | Moltiplicazione, divisione, modulo | Da sinistra a destra |
| **5** | `+`, `-` | Addizione, sottrazione | Da sinistra a destra |
| **6** | `<<`, `>>` | Shift bitwise | Da sinistra a destra |
| **7** | `<`, `<=`, `>`, `>=` | Relazionali di confronto | Da sinistra a destra |
| **8** | `==`, `!=` | Uguaglianza / Disuguaglianza | Da sinistra a destra |
| **9** | `&` | Bitwise AND | Da sinistra a destra |
| **10** | `^` | Bitwise XOR | Da sinistra a destra |
| **11** | `\|` | Bitwise OR | Da sinistra a destra |
| **12** | `&&` | Logico AND (con Cortocircuito) | Da sinistra a destra |
| **13** | `\|\|` | Logico OR (con Cortocircuito) | Da sinistra a destra |
| **14** | `? :` | Ternario condizionale | Da destra a sinistra |
| **15** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `\|= ` | Assegnamenti scritti/composti | Da destra a sinistra |
| **16 (Minima)**| `,` | Operatore virgola (sequenziamento) | Da sinistra a destra |

---

#### Tabella 2.4: Cortocircuito e Valutazione Condizionale
| Espressione | Condizione Operando Sinistro | Esecuzione Operando Destro? | Risultato Espressione |
| :--- | :--- | :---: | :--- |
| `A && B` | Se `A == 0` (FALSO) | **NO (Cortocircuito)** | `0` (FALSO) |
| `A && B` | Se `A != 0` (VERO) | **SÌ** | `1` se `B != 0`, altrimenti `0` |
| `A \|\| B` | Se `A != 0` (VERO) | **NO (Cortocircuito)** | `1` (VERO) |
| `A \|\| B` | Se `A == 0` (FALSO) | **SÌ** | `1` se `B != 0`, altrimenti `0` |
| `C ? E1 : E2` | Se `C != 0` (VERO) | Valuta **solo `E1`** | Risultato di `E1` (`E2` ignorato) |
| `C ? E1 : E2` | Se `C == 0` (FALSO) | Valuta **solo `E2`** | Risultato di `E2` (`E1` ignorato) |
| `(E1, E2)` | Valuta `E1` poi `E2` | **SÌ (entrambi)** | Risultato di **`E2`** (`E1` scartato) |

---

### 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

1. **Converti tutte le costanti in decimale:**
   - Converti immediatamente ottali (`0...`) ed esadecimali (`0x...`) in decimale.
2. **Crea una tabella di tracciamento dello stato (Trace Table):**
   - Colonne: `Iterazione | Variabile | Condizione Ciclo | Modifiche Intermedie | Output Stampa`.
3. **Fai molta attenzione al cortocircuito (`||` e `&&`):**
   - In `if (a == 6 || a-- == 10)`, se `a == 6` è VERO, `a-- == 10` NON viene eseguito e `a` NON viene decrementato!
4. **Traccia attentamente gli incrementi e le istruzioni di salto (`break`, `continue`, `goto`):**
   - `continue` salta il resto del corpo del ciclo e passa all'incremento/test successivo.
   - `break` interrompe ed esce immediatamente dal ciclo.

---

## 🔗 Tipologia 3: Gestione di Liste Concatenate Dinamiche (`struct Node`)

### 📊 Prontuario e Tabelle di Riferimento per Liste Concatenate

#### Tabella 3.1: Operazioni Standard su Liste Simply Linked, Complessità e Gestione Puntatori
| Operazione | Complessità Tempo | Complessità Spazio | Gestione Caso Lista Vuota (`NULL`) | Invariante Puntatori da Mantenere |
| :--- | :---: | :---: | :--- | :--- |
| **Inserimento in Testa** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | `newNode->pNext = NULL; head = newNode;` | `newNode->pNext` deve puntare al vecchio `head` prima di aggiornare `head`. |
| **Inserimento in Coda** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | `head = newNode; tail = newNode;` | Scorri fino all'ultimo nodo (`curr->pNext == NULL`), poi `curr->pNext = newNode`. |
| **Cancellazione Testa** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Se `head == NULL` ritorna subito | `tmp = head; head = head->pNext; free(tmp);` |
| **Cancellazione in Posizione $k$** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Se $k=1$, cancella testa. Se $k > N$, nessuna operazione | Mantieni un puntatore al nodo precedente `prev` ($k-1$), ricollega `prev->pNext = target->pNext`, poi `free(target)`. |
| **Riordinamento In-Place (No Malloc)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Se `head == NULL` o `head->pNext == NULL` ritorna | Stacca i nodi uno ad uno (`curr->pNext = NULL`) e accoda alle sottoliste (es. `dispH`, `pariH`). Concatena alla fine. |
| **Creazione Nuova Lista (Alternata/Copia)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Ritorna `NULL` se le liste input sono vuote | Verificare **sempre** se `malloc()` ritorna `NULL`. |

---

#### Tabella 3.2: Errore vs Soluzione Corretta nelle Liste d'Esame
| Trappola / Errore Comune | Codice Errato ❌ | Codice Corretto ✅ | Conseguenza se Errato |
| :--- | :--- | :--- | :--- |
| **Memory Leak su Cancellazione** | `pFirst = pFirst->pNext;` | `struct Node *tmp = pFirst; pFirst = pFirst->pNext; free(tmp);` | Perdita di memoria non deallocata |
| **Use After Free** | `free(curr); curr = curr->pNext;` | `struct Node *next = curr->pNext; free(curr); curr = next;` | Segmentation Fault / Undefined Behavior |
| **Dereferenziazione Puntatore NULL** | `if (curr->pNext->info == x)` | `if (curr != NULL && curr->pNext != NULL && curr->pNext->info == x)` | Crash immediato del programma |
| **Perdita della Coda dopo Split** | `dispT->pNext = pariH;` (senza azzerare `pariT->pNext`) | `if (pariT != NULL) pariT->pNext = NULL; dispT->pNext = pariH;` | Ciclo infinito nei puntatori / Loop |
| **Allocazione non consentita** | Usare `malloc()` quando il testo dice "in-place" | Riorganizzare solo i puntatori `pNext` esistenti | Detrazione pesante punti esame |

---

#### Tabella 3.3: Passaggio della Lista: Puntatore Globale vs Parametro Formale
| Modello d'Esame | Firma della Funzione | Come Modificare la Testa della Lista | Esempio Tipico |
| :--- | :--- | :--- | :--- |
| **Puntatore Globale `pFirst`** | `void mia_funzione(void)` | Modifica diretta della variabile globale: `pFirst = nuovoNodo;` | Esame 3 Giugno, 22 Giugno, 15 Gennaio |
| **Passaggio per Valore `struct Node*`** | `struct Node* mia_funzione(struct Node* head)` | Ritorna il nuovo puntatore di testa col `return head;` | Esame 13 Febbraio (`alternate`) |
| **Passaggio per Riferimento `struct Node**`** | `void mia_funzione(struct Node** ppHead)` | Dereferenzia il doppio puntatore: `*ppHead = nuovoNodo;` | Esercizi avanzati / Modifica in-place |

---

### Struttura Nodo Standard:
```c
struct Node {
    int info;
    struct Node* pNext;
};
```

---

## 📊 Tipologia 4: Matrici e Array Bidimensionali (VLA e Memoria Dinamica)

### 📊 Prontuario e Tabelle di Conversione Indici per Matrici

#### Tabella 4.1: Formulario Trasformazioni Geometriche e Mappatura Indici
Sia $A$ una matrice sorgente di dimensioni $m \times n$ (riga $i \in [0, m-1]$, colonna $j \in [0, n-1]$) e $B$ la matrice destinazione:

| Trasformazione / Estrazione | Dimensione Risultato | Formula Indice Destinazione ($B$) | Esempio / Applicazione d'Esame |
| :--- | :---: | :--- | :--- |
| **Trasposta** ($A^T$) | $n \times m$ | $B[j][i] = A[i][j]$ | Scambio righe e colonne |
| **Rotazione 90° Anti-Oraria** | $n \times m$ | $B[n - 1 - j][i] = A[i][j]$ | **Esame 13 Febbraio** (`rotate90`) |
| **Rotazione 90° Oraria** | $n \times m$ | $B[j][m - 1 - i] = A[i][j]$ | Rotazione in senso orario |
| **Rotazione 180°** | $m \times n$ | $B[m - 1 - i][n - 1 - j] = A[i][j]$ | Capovolgimento completo |
| **Reflessione Orizzontale (Specchio)**| $m \times n$ | $B[i][n - 1 - j] = A[i][j]$ | Inversione di ciascuna riga |
| **Reflessione Verticale** | $m \times n$ | $B[m - 1 - i][j] = A[i][j]$ | Inversione ordine delle righe |
| **Diagonale Principale** ($n \times n$) | Array di len $n$ | `diag[i] = A[i][i]` per $i \in [0, n-1]$ | $i == j$ |
| **Diagonale Secondaria** ($n \times n$) | Array di len $n$ | `diag[i] = A[i][n - 1 - i]` per $i \in [0, n-1]$ | **Esame 30 Gennaio** ($i + j == n - 1$) |

---

#### Tabella 4.2: Confronto Tecniche di Dichiarazione e Gestione Matrici in C
| Tecnica di Allocazione | Sintassi Firma Funzione | Layout Memoria | Vantaggi / Svantaggi |
| :--- | :--- | :--- | :--- |
| **VLA (Variable Length Array - C99)** | `void f(int m, int n, int A[m][n])` | **Contiguo (Row-Major)** | Sintassi pulita `A[i][j]`. Dimensioni $m, n$ devono essere passate **prima** della matrice. Allocata nello Stack. |
| **Array 1D Simulato in Dynamic Heap** | `int* f(int m, int n)` con `malloc(m * n * sizeof(int))` | **Contiguo (Row-Major)** | Unica allocazione `malloc`. Accesso via offset: `A[i * n + j]`. |
| **Vettore di Puntatori (`int**`)** | `void f(int** A, int m, int n)` | **Non Contiguo** (array di puntatori a righe) | Richiede $m + 1$ allocazioni `malloc` e $m + 1$ deallocazioni `free`. Accesso `A[i][j]`. |

---

#### Tabella 4.3: Condizioni per Sotto-Regioni di Matrici Quadrate ($n \times n$)
| Regione della Matrice | Condizione Indici ($i, j$) | Numero di Elementi Totali |
| :--- | :---: | :---: |
| **Diagonale Principale** | $i == j$ | $n$ |
| **Sopra la Diagonale Principale (Triangolare Superiore)** | $i < j$ | $\frac{n(n-1)}{2}$ |
| **Sotto la Diagonale Principale (Triangolare Inferiore)** | $i > j$ | $\frac{n(n-1)}{2}$ |
| **Diagonale Secondaria** | $i + j == n - 1$ | $n$ |
| **Sopra la Diagonale Secondaria** | $i + j < n - 1$ | $\frac{n(n-1)}{2}$ |
| **Sotto la Diagonale Secondaria** | $i + j > n - 1$ | $\frac{n(n-1)}{2}$ |

---

## 🧠 Tipologia 5: Mappa di Memoria, Little-Endian, Puntatori e Bitwise (7 Punti)

### 📊 Prontuario e Tabelle di Conversione per Mappa di Memoria

#### Tabella 5.1: Conversione Valori Decimali Frequenti $\rightarrow$ Hex $\rightarrow$ Layout Byte Little-Endian
| Valore Decimale | Tipo / Dimensione | Esadecimale (Hex) | Byte 0 (Indirizzo Basso) | Byte 1 | Byte 2 | Byte 3 | Note / Esercizi d'Esame |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`2048`** | `short` (16 bit) | `0x0800` | **`0x00`** | **`0x08`** | — | — | LSB `00`, MSB `08` |
| **`4098`** | `short` (16 bit) | `0x1002` | **`0x02`** | **`0x10`** | — | — | $4096 + 2$ |
| **`4093`** | `short` (16 bit) | `0x0FFD` | **`0xFD`** | **`0x0F`** | — | — | $4095 - 2$ |
| **`257`** | `short` (16 bit) | `0x0101` | **`0x01`** | **`0x01`** | — | — | Byte uguali |
| **`-1`** | `short` (16 bit) | `0xFFFF` | **`0xFF`** | **`0xFF`** | — | — | Tutti bit 1 |
| **`-3`** | `short` (16 bit) | `0xFFFD` | **`0xFD`** | **`0xFF`** | — | — | Complemento a due |
| **`16385`** | `short` (16 bit) | `0x4001` | **`0x01`** | **`0x40`** | — | — | $4096 \times 4 + 1$ |
| **`65540`** | `int` (32 bit) | `0x00010004` | **`0x04`** | **`0x00`** | **`0x01`** | **`0x00`** | $65536 + 4$ |
| **`99`** | `char` (8 bit) | `0x63` | **`0x63`** | — | — | — | ASCII `'c'` |
| **`LLONG_MIN`** | `long long` (64 bit) | `0x8000000000000000` | `0x00` | `0x00` | ... | `0x80` (Byte 7) | Bit di segno a 1 |

---

#### Tabella 5.2: Sovrapposizione Indirizzi (Offset Byte) per Tipi Diversi nello Stesso Array
Sia `long long a[3]` un array di 24 byte totali (byte 0..23). Se `short *p = (short*)a` e `char *q = (char*)a`:

| Offset Byte | Elemento `a` (`long long` = 8 byte) | Elemento `p` (`short` = 2 byte) | Elemento `q` (`char` = 1 byte) | Note Sovrapposizione |
| :---: | :---: | :---: | :---: | :--- |
| **Byte 0 - 1** | `a[0]` (Byte 0-1) | **`p[0]`** | `q[0]`, `q[1]` | `p[0]` è formato da `q[0]` (LSB) e `q[1]` (MSB) |
| **Byte 2 - 3** | `a[0]` (Byte 2-3) | **`p[1]`** | `q[2]`, `q[3]` | `p[1]` sovrascrive byte 2 e 3 |
| **Byte 4 - 5** | `a[0]` (Byte 4-5) | **`p[2]`** | `q[4]`, `q[5]` | `p[2]` sovrascrive byte 4 e 5 |
| **Byte 6 - 7** | `a[0]` (Byte 6-7) | **`p[3]`** | `q[6]`, `q[7]` | `q[7]` è l'MSB di `a[0]` |
| **Byte 8 - 9** | `a[1]` (Byte 0-1) | **`p[4]`** | `q[8]`, `q[9]` | Inizio del secondo elemento `a[1]` |
| **Byte 10 - 11**| `a[1]` (Byte 2-3) | **`p[5]`** | `q[10]`, `q[11]` | — |
| **Byte 12 - 13**| `a[1]` (Byte 4-5) | **`p[6]`** | `q[12]`, `q[13]` | — |
| **Byte 14 - 15**| `a[1]` (Byte 6-7) | **`p[7]`** | `q[14]`, `q[15]` | `q[15]` è l'MSB di `a[1]` |
| **Byte 16 - 17**| `a[2]` (Byte 0-1) | **`p[8]`** | `q[16]`, `q[17]` | Inizio del terzo elemento `a[2]` |
| **Byte 18 - 19**| `a[2]` (Byte 2-3) | **`p[9]`** | `q[18]`, `q[19]` | — |
| **Byte 20 - 21**| `a[2]` (Byte 4-5) | **`p[10]`** | `q[20]`, `q[21]` | — |
| **Byte 22 - 23**| `a[2]` (Byte 6-7) | **`p[11]`** | `q[22]`, `q[23]` | `q[23]` è l'MSB di `a[2]` |

---

#### Tabella 5.3: Regole di Calcolo delle Espressioni nei Quesiti (A, B, C)
| Tipo di Operazione | Esempio Espressione Esame | Formula / Regola di Risoluzione | Risultato Esempio |
| :--- | :--- | :--- | :--- |
| **Sottrazione Puntatori Tipizzati** | `&p[9] - &p[2]` | $\text{Indice}_2 - \text{Indice}_1 = 9 - 2$ | **`7`** (elementi `short`) |
| **Sottrazione Puntatori con Cast `(int)`**| `(int)(p + 11) - (int)(a + 2)` | $(11 \times 2) - (2 \times 8) = 22 - 16$ | **`6`** (byte effettivi) |
| **Modulo Pari/Dispari su Risultato** | `(7 + 768) % 2` | $775 \% 2 = 1 \rightarrow$ **VERA** | **`1`** (dispari = VERA) |
| **Bitwise Shift + OR** | `(q[12] >> 4) \| q[4]` | $(99 >> 4) \ \| \ 21 = 6 \ \| \ 21$ | **`23`** |

---

### 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

1. **Disegna la Griglia di Memoria Byte per Byte:**
   - Prepara una tabella con le colonne: `Indice Byte | Offset Pointer (p[k], q[k]) | Contenuto Binario/Hex`.
   - Popola inizialmente l'array di partenza `a[...]` espandendo ciascun valore in Little-Endian.
2. **Applica le Modifiche Sovrapposte via Puntatore in Ordine:**
   - Applica le sovrascritture di `p[...]`, `q[...]` ed eventuali cast.
   - Converti i numeri da assegnare in binario/hex e scrivi i byte nelle rispettive celle Little-Endian.
3. **Valuta le 3 Affermazioni (A, B, C):**
   - Sostituisci i valori numerici dereferenziati ed esegui i calcoli aritmetici/bitwise.
   - Rispondi indicando **VERA** o **FALSA** con la giustificazione completa.

---

## 📚 Tipologia 6: Teoria C, Linkage, Zone di Memoria e Pipeline GCC

### 📊 Prontuario e Tabelle di Riferimento Teoria C e Compilazione

#### Tabella 6.1: Matrice Completa: Dichiarazione/Definizione, Linkage, Durata e Zona di Memoria
| Tipo di Identificatore C | Esempio Sintattico | Dichiarato vs Definito | Linkage | Storage Duration | Zona di Memoria |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Globale Inizializzata (non static)** | `int a = 5;` (fuori da funzioni) | **Definito** | **Esterno** | **Statica** | **Data Segment** |
| **Globale Non Inizializzata** | `int a;` (dichiarazione tentativa) | **Definito** (se unica) | **Esterno** | **Statica** | **BSS Segment** |
| **Globale Static Inizializzata** | `static int c = 1;` | **Definito** | **Interno** | **Statica** | **Data Segment** |
| **Globale Static Non Inizializzata** | `static int c;` | **Definito** | **Interno** | **Statica** | **BSS Segment** |
| **Simbolo Esterno Importato** | `extern int b;` | **Dichiarato** | **Esterno** | **Statica** | Allocato in altro file |
| **Funzione Static (File Scope)** | `static void f(void) {...}` | **Definito** | **Interno** | **Statica** | **Text / Code Segment** |
| **Prototipo di Funzione** | `extern long cfun(float, float);` | **Dichiarato** | **Esterno** | **Statica** | **Text / Code Segment** |
| **Variabile Locale Automatica** | `int q;` (dentro blocco/funzione) | **Definito** | **No Linkage** | **Automatica** | **Stack** |
| **Variabile Locale Static** | `static double e = 4.2;` | **Definito** | **No Linkage** | **Statica** | **Data Segment** |
| **Parametro Formale Funzione** | `int d` in `void f(int d)` | **Definito** | **No Linkage** | **Automatica** | **Stack** |
| **Memoria Allocata Dinamicamente** | `int *p = malloc(10 * sizeof(int))` | `p` **Stack**, `*p` **Heap** | **No Linkage** | **Dinamica** | **Heap** |

---

#### Tabella 6.2: Fasi della Pipeline di Compilazione GCC e Gestione Errori
| Fase Pipeline | Comando / Strumento | Estensione File Output | Flag GCC associato | Tipi di Errori Rilevati |
| :--- | :---: | :---: | :---: | :--- |
| **1. Preelaborazione** | Preprocessore (`cpp`) | `.i` | `gcc -E` | File include non trovato (`#include`), sintassi macro |
| **2. Compilazione** | Compilatore (`cc1`) | `.s` (Assembly) | `gcc -S` | Errori sintattici/semantici, tipi incompatibili, redeclarations incoerenti |
| **3. Assemblaggio** | Assemblatore (`as`) | `.o` (Oggetto) | `gcc -c` | Istruzioni assembly non valide (arresta prima del linker!) |
| **4. Linking** | Linker (`ld`) | Eseguibile (a.out / binario) | `gcc -o prog` | `undefined reference to ...` (funzioni/variabili non definite), `multiple definition of ...` |

> [!IMPORTANT]
> L'invocazione di `gcc -c` **interrompe il processo alla Fase 3** (produzione del file oggetto `.o`). Quindi `gcc -c` **NON invocherà mai il linker** e non potrà **mai** generare errori di `undefined reference`!

---

#### Tabella 6.3: Confronto Funzioni di Gestione Memoria Dinamica (`<stdlib.h>`)
| Funzione | Prototipo | Inizializzazione Memoria | Valore Restituito | Comportamento in Caso di Errore |
| :--- | :--- | :---: | :--- | :--- |
| **`malloc(bytes)`** | `void* malloc(size_t size);` | **NON inizializzata** (contiene valori spazzatura) | Puntatore `void*` alla memoria allocata | Restituisce `NULL` |
| **`calloc(n, size)`** | `void* calloc(size_t num, size_t size);` | **Inizializzata a ZERO** (`0`) | Puntatore `void*` a $n \times \text{size}$ byte allocati | Restituisce `NULL` |
| **`realloc(ptr, new_size)`** | `void* realloc(void* ptr, size_t new_size);` | Preserva contenuto precedente; nuova parte non inizializzata | Puntatore `void*` alla nuova area (può cambiare indirizzo) | Restituisce `NULL` (il vecchio `ptr` resta valido) |
| **`free(ptr)`** | `void free(void* ptr);` | N/A | `void` (nessun valore di ritorno) | Undefined Behavior / Crash se `ptr` non viene da `malloc/calloc/realloc` o double free |

---
