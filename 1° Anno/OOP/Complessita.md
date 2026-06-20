---
tags:
  - OOP
---
# COMPLESSITÀ COMPUTAZIONALE

---

## 1. INTRODUZIONE E QUALITÀ DEL SOFTWARE

Nello sviluppo del software, la bontà di un programma non si misura solo sul fatto che funzioni, ma su diverse metriche di qualità.

### I Parametri di Qualità
1. **Correttezza**: Il programma calcola i risultati corretti per tutti gli input validi?
2. **Economicità**: 
   - **Efficienza**: Consumo ottimale delle risorse di sistema.
   - **Manutenibilità e Modificabilità**: Bassi costi di manutenzione e modifica nel tempo. Ciò è garantito da:
     - Comprensibilità del codice.
     - Esistenza di una documentazione chiara ed esaustiva (commenti, Javadoc, manuali utente).

> [!NOTE]
> ### Efficienza e Risorse di Sistema
> L'efficienza si valuta in base al consumo di due risorse fondamentali durante l'esecuzione:
> - **Tempo**: Tempo di utilizzo della CPU (velocità di esecuzione).
> - **Spazio**: Memoria RAM allocata (occupazione di memoria).

---

## 2. PARADIGMI DI CONTROLLO: ITERAZIONE VS RICORSIONE

Per risolvere problemi computazionali che richiedono ripetizione, si utilizzano principalmente due paradigmi di controllo: l'**iterazione** e la **ricorsione**.

### Definizioni e Differenze

*   **Iterazione (Controllo Imperativo)**:
    Sfrutta strutture di ciclo esplicite (`for`, `while`, `do-while`) controllate da una condizione booleana o da un contatore.
    - **Avanzamento**: Avviene aggiornando lo stato delle variabili locali ad ogni ciclo.
    - **Terminazione**: Avviene quando la condizione di controllo diventa falsa.
    - **Spazio in memoria**: Richiede memoria costante $O(1)$ sullo Stack, poiché viene mantenuto un unico frame di attivazione per l'intero ciclo.

*   **Ricorsione (Controllo Funzionale)**:
    Sfrutta la scomposizione del problema in sotto-problemi analoghi ma di dimensione inferiore, autoinvocando lo stesso metodo con parametri diversi.
    - **Base ricorsiva (Passo base)**: Risolve direttamente il caso più semplice (senza ulteriore ricorsione). È fondamentale per evitare la ricorsione infinita.
    - **Passo ricorsivo**: Riduce il problema corrente a una o più istanze più piccole e invoca il metodo su di esse.
    - **Terminazione**: Garantita dalla convergenza dei parametri verso il passo base.
    - **Spazio in memoria**: Richiede memoria proporzionale alla profondità di ricorsione $O(D)$ (dove $D$ è la profondità massima delle chiamate pendenti), poiché ogni chiamata alloca un nuovo frame sullo Stack.

### Tabella Comparativa

| Criterio | Iterazione | Ricorsione |
| :--- | :--- | :--- |
| **Struttura di controllo** | Istruzioni di ciclo (`while`, `for`) | Autoinvocazione del metodo |
| **Stato del ciclo** | Variabile contatore / Condizione booleana | Parametri passati alle chiamate ricorsive |
| **Terminazione** | Condizione di ciclo falsa | Raggiungimento del passo base |
| **Uso dello Stack** | Costante: $O(1)$ (un solo frame) | Lineare: $O(D)$ (un frame per ogni chiamata attiva) |
| **Rischio di errore** | Loop infinito (tempo) | Stack Overflow (esaurimento memoria dello Stack) |

---

## 3. TEORIA DELLA COMPLESSITÀ COMPUTAZIONALE

La **teoria della complessità computazionale** studia le risorse necessarie (principalmente tempo e memoria) per l'esecuzione di un dato algoritmo e si occupa di determinare le risorse minime necessarie per risolvere un problema.

### Indipendenza dalla Tecnologia
Per misurare l'efficienza di un algoritmo in modo univoco, è fondamentale definire una **metrica indipendente dalle tecnologie utilizzate** (hardware, sistema operativo, linguaggio di programmazione). Altrimenti, lo stesso algoritmo sembrerebbe più efficiente su un computer più veloce.

* **Soluzione**: Consideriamo il **tempo di esecuzione proporzionale al numero di operazioni elementari** effettuate dall'algoritmo.

### Classi e Limitazioni
- I problemi vengono classificati in **classi di complessità**, basate sull'efficienza del *migliore algoritmo noto* in grado di risolverli.
- Una specifica soluzione (algoritmo) definisce un **limite superiore** (limitazione dall'alto) alla complessità del problema.
- Si parla di **complessità intrinseca** di un problema per indicare il costo minimo insito nel problema stesso (sotto il quale nessun algoritmo potrà mai scendere).

---

## 4. DIMENSIONE DEL PROBLEMA ($n$)

La complessità di un algoritmo viene valutata in funzione della **dimensione del problema** ($n$), che rappresenta una misura dell'occupazione in memoria dei dati in input.

### Esempi di Dimensione ($n$) in base alla Struttura Dati:
- **Array**: Lunghezza dell'array.
- **Liste**: Lunghezza della lista.
- **Alberi**: Numero di nodi (elementi) dell'albero.
- **Interi**: Il valore numerico dell'intero oppure il **numero di cifre** necessarie per rappresentarlo.

> [!IMPORTANT]
> ### Rappresentazione degli Interi in Memoria
> Per un numero intero con valore $v$ in base $b$:
> - Il numero di cifre $n$ è proporzionale a $\log_b v$.
> - Relazione: $n \text{ cifre} \leftrightarrow v \approx b^n \implies \text{numero cifre } n = \log_b v$.
> 
> *Esempio*:
> - Il valore $1234$ richiede $4$ cifre in base 10.
> - Con $4$ cifre in base 10 si possono rappresentare $10^4 = 10000$ valori diversi (es. da $-5000$ a $4999$).
> 
> **Concetto chiave**: Se il valore $v$ di un input intero cresce esponenzialmente, il numero di cifre $n$ (che è la vera misura dello spazio che occupa in memoria) cresce solo linearmente.

---

## 5. NOTAZIONI ASINTOTICHE

Per semplificare l'analisi ed evitare conteggi troppo dettagliati, si utilizzano le **approssimazioni asintotiche**, che valutano il comportamento dell'algoritmo al tendere della dimensione dell'input $n$ all'infinito ($\infty$).

### 1. Notazione $O(f(n))$ (O-Grande)
Rappresenta un **limite superiore asintotico** (worst case / caso peggiore).
$$g(n) \in O(f(n)) \iff \exists c > 0, n_0 \ge 0 \text{ tali che } \forall n \ge n_0, 0 \le g(n) \le c \cdot f(n)$$

*Esempio*: 
$$3n^2 + 5n + 6 \in O(n^2)$$
Se prendiamo $c = 4$, allora $3n^2 + 5n + 6 < 4n^2$ per ogni $n$ sufficientemente grande ($n_0 \ge 6$).

### 2. Notazione $\Omega(f(n))$ (Omega-Grande)
Rappresenta un **limite inferiore asintotico** (best case / caso migliore).
$$g(n) \in \Omega(f(n)) \iff \exists c > 0, n_0 \ge 0 \text{ tali che } \forall n \ge n_0, 0 \le c \cdot f(n) \le g(n)$$
- Indica che la funzione $g(n)$ cresce non più lentamente di $f(n)$.
- *Esempi*: $n^2 + 1000n + 6000 \in \Omega(n^2)$ e $n^2 - 1000n - 6000 \in \Omega(n^2)$.

### 3. Notazione $\Theta(f(n))$ (Teta-Grande)
Rappresenta una **stima esatta asintotica** (tight bound).
$$g(n) \in \Theta(f(n)) \iff \exists c_1 > 0, c_2 > 0, n_0 \ge 0 \text{ tali che } \forall n \ge n_0, 0 \le c_1 \cdot f(n) \le g(n) \le c_2 \cdot f(n)$$
Equivalentemente:
$$g(n) \in \Theta(f(n)) \iff g(n) \in O(f(n)) \land g(n) \in \Omega(f(n))$$
- Dà una stima esatta della funzione $g(n)$.

*Esempio*:
$$3n^2 + 5n + n \in \Theta(n^2)$$
- $3n^2 + 5n + n < 4n^2 \implies 3n^2 + 5n + n \in O(n^2)$
- $3n^2 + 5n + n > n^2 \implies 3n^2 + 5n + n \in \Omega(n^2)$

---

## 6. I CASI DI ANALISI (MIGLIORE, PEGGIORE, MEDIO)

Le prestazioni di un algoritmo dipendono sia dalla dimensione $n$ che dalla conformazione dei dati in ingresso. Si distinguono tre scenari:

| Caso | Descrizione | Utilità |
| :--- | :--- | :--- |
| **Caso Migliore** ($\Omega$) | Configurazione dei dati che richiede il minor numero di operazioni (es. array già ordinato). | Ottimistico, definisce il limite inferiore. |
| **Caso Peggiore** ($O$) | Configurazione dei dati che richiede il massimo numero di passi (es. cercare un elemento inesistente). | Garantisce una soglia massima invalicabile di tempo. |
| **Caso Medio** ($\Theta$) | Comportamento atteso su input generici. Spesso calcolato come media matematica ponderata su tutte le configurazioni. | Rappresenta lo scenario reale, ma è matematicamente complesso da calcolare. |

> [!TIP]
> Per analizzare il **caso medio** in situazioni complesse, si ricorre spesso a **simulazioni empiriche** (benchmarking) raccogliendo i tempi di esecuzione e interpolando una funzione matematica che ne approssimi l'andamento.

---

## 7. ANALISI DELLE RISORSE: STACK VS HEAP

### 1. Occupazione di Spazio in Memoria

La memoria RAM utilizzata da un programma Java si suddivide principalmente in:
- **Stack**: Dove vengono eseguite le chiamate ai metodi e memorizzate le variabili locali e i parametri.
- **Heap**: Dove risiedono gli oggetti dinamici creati con l'operatore `new`.

#### Confronto Stack/Heap in base al Paradigma di Controllo:

```text
ITERAZIONE:                                RICORSIONE:
  ┌─────────────────────────┐                ┌─────────────────────────┐
  │ Stack Frame (Metodo)    │                │ Stack Frame (Chiamata k)│
  │   - Variabili locali    │                ├─────────────────────────┤
  │   - Parametri           │                │ Stack Frame (Chiamata 2)│
  └─────────────────────────┘                ├─────────────────────────┤
   (Resta 1 frame costante)                  │ Stack Frame (Chiamata 1)│
                                             └─────────────────────────┘
                                              (Cresce con la profondità)
```

- **Iterazione (Cicli)**:
  - Lo Stack mantiene **1 solo frame** attivo per il metodo corrente. L'occupazione di spazio sullo Stack è **costante ($O(1)$)**.
- **Ricorsione**:
  - Ogni chiamata ricorsiva aggiunge un nuovo frame sullo Stack (Record di Attivazione). Lo Stack cresce proporzionalmente al numero di chiamate contemporanee pendenti (**profondità della ricorsione** $D$). Lo spazio occupato è $\Theta(D)$.

### 2. Numero di Operazioni (Tempo)

Per determinare il costo temporale:
- **Iterazione**: Si calcola il *numero di iterazioni* moltiplicato per il *numero di operazioni elementari* svolte in ciascun ciclo.
- **Ricorsione**: Si determina il *numero totale di chiamate ricorsive* moltiplicato per il *numero di operazioni elementari* svolte nella singola chiamata.

---

## 8. ANDAMENTO E COMPLESSITÀ DI SCALA

Come varia il tempo di esecuzione $T_N$ quando la dimensione del problema $N$ viene moltiplicata per una costante $c$?

### 1. Complessità Logaritmica $\Theta(\log N)$
- Con input $N \rightarrow T_N = \log N$
- Moltiplicando l'input per $c$ ($c \cdot N$) $\rightarrow T_{c \cdot N} = \log (c \cdot N) = \log c + \log N = \log c + T_N$
- **Effetto**: Il tempo aumenta in modo **additivo** di una costante ($\log c$). Ottimo per grandi quantità di dati.

### 2. Complessità Polinomiale $O(N^k)$ (con $k \ge 1$)
- Con input $N \rightarrow T_N = N^k$
- Moltiplicando l'input per $c$ ($c \cdot N$) $\rightarrow T_{c \cdot N} = (c \cdot N)^k = c^k \cdot N^k = c^k \cdot T_N$
- **Effetto**: Il tempo viene **moltiplicato** per $c^k$.
  - Se $k=1$ (lineare) e $c=10$, il tempo aumenta di $10$ volte.
  - Se $k=2$ (quadratico) e $c=10$, il tempo aumenta di $100$ volte.
  - Se $k=3$ (cubico) e $c=10$, il tempo aumenta di $1000$ volte.

### 3. Complessità Esponenziale $O(2^N)$
- Con input $N \rightarrow T_N = 2^N$
- Incrementando l'input di 1 ($N+1$) $\rightarrow T_{N+1} = 2^{N+1} = 2 \cdot 2^N = 2 \cdot T_N$ (Il tempo **raddoppia** per ogni elemento aggiunto!)
- Moltiplicando l'input per $c$ ($c \cdot N$) $\rightarrow T_{c \cdot N} = 2^{c \cdot N} = 2^{N + (c-1)N} = 2^{(c-1)N} \cdot T_N$
- **Effetto**: Algoritmi inefficienti, inutilizzabili per $N$ medio-grandi.

---

## 9. ALGORITMI DI ESPONENZIAZIONE A CONFRONTO

Analizziamo diverse implementazioni del calcolo di $b^e$ (base ed esponente).

### Algoritmo 1: Potenza Iterativa (Lineare)
```java
static double potenza(double base, long esponente) {
    double ris = 1;
    for (long i = 0; i < esponente; i++) {
        ris *= base;
    }
    return ris;
}
```
* **Spazio**: Costante ($O(1)$ sullo Stack).
* **Tempo**: Ciclo for eseguito $e$ volte $\rightarrow \Theta(e)$ (lineare sul *valore* dell'esponente).

### Algoritmo 2: Potenza Ricorsiva Standard (Lineare)
```java
static double potenzaR(double base, long esponente) {
    if (esponente == 0) {
        return 1;
    } else {
        return base * potenzaR(base, esponente - 1);
    }
}
```
* **Equazione di Ricorrenza**: 
  - Tempo: $T(e) = T(e-1) + \Theta(1) \implies T(e) \in \Theta(e)$ (lineare).
  - Spazio: $S(e) = S(e-1) + \Theta(1) \implies S(e) \in \Theta(e)$ (lineare).
* **Spazio**: $\text{esponente} + 1$ chiamate attive contemporaneamente sullo Stack $\rightarrow \Theta(e)$ (lineare).
* **Tempo**: $\text{esponente} + 1$ chiamate totali con operazioni costanti a ogni passo $\rightarrow \Theta(e)$ (lineare).

---

### Algoritmo "Contadino Russo" (Fast Exponentiation)

Questo approccio riduce drasticamente il numero di operazioni necessarie sfruttando le proprietà matematiche delle potenze:

$$b^e = \begin{cases} 
1 & \text{se } e = 0 \\ 
(b \cdot b)^{e/2} & \text{se } e \text{ è pari} \\ 
b \cdot (b \cdot b)^{(e-1)/2} & \text{se } e \text{ è dispari} 
\end{cases}$$

> [!NOTE]
> ### Esempio Numerico:
> - **Metodo Lineare ($e$ passi)**:
>   - Per calcolare $2^{10}$ servono 10 moltiplicazioni: $2 \cdot 2 \cdot 2 \dots \cdot 2$
> - **Contadino Russo ($\log_2 e$ passi)**:
>   - $2^{10} = (2 \cdot 2)^5 = 4^5 = 4 \cdot (4 \cdot 4)^2 = 4 \cdot 16^2 = 4 \cdot (16 \cdot 16)^1 = 4 \cdot 256 = 1024$ (Solo 4 passi di dimezzamento!)

#### Dimostrazione matematica del costo logaritmico:
Se dividiamo l'esponente per 2 ad ogni passo, dopo $k$ passi arriviamo a 0:
$$\frac{e}{2^k} \approx 1 \implies 2^k \approx e \implies k \approx \log_2 e \implies \text{Passi} \in \Theta(\log e)$$

---

### Algoritmo 3: Potenza Ricorsiva Veloce (Logaritmica)
```java
public static double potenzaCRR(double base, long esponente) {
    if (esponente == 0) {
        return 1;
    } else if (esponente % 2 == 0) {
        return potenzaCRR(base * base, esponente / 2);
    } else {
        return base * potenzaCRR(base * base, esponente / 2);
    }
}
```
* **Equazione di Ricorrenza**:
  - Tempo: $T(e) = T(e/2) + \Theta(1) \implies T(e) \in \Theta(\log e)$ (logaritmico).
  - Spazio: $S(e) = S(e/2) + \Theta(1) \implies S(e) \in \Theta(\log e)$ (logaritmico sullo Stack).
* **Spazio**: Profondità dello Stack proporzionale ai dimezzamenti dell'esponente $\rightarrow \Theta(\log e)$ (lineare sul *numero di cifre* binario dell'esponente).
* **Tempo**: $\Theta(\log e)$ (logaritmico sul valore dell'esponente).

### Algoritmo 4: Potenza Iterativa Veloce (Logaritmica)
```java
public static double potenzaCR(double base, long esponente) {
    double pot = 1;
    while (esponente != 0) {
        if (esponente % 2 == 0) {
            base = base * base;
        } else {
            pot *= base;
            if (esponente > 1) {
                base = base * base;
            }
        }
        esponente /= 2;
    }
    return pot;
}
```
* **Spazio**: Costante ($O(1)$ sullo Stack).
* **Tempo**: $\Theta(\log e)$ (grazie al ciclo `while` che divide l'esponente ad ogni iterazione).

---

## 10. ALGORITMI DI ORDINAMENTO (SORTING)

Vogliamo ordinare un array disordinato. Prendiamo come riferimento il vettore iniziale:
`3  1  5  9  7  2` (Lunghezza $N = 6$)

### 1. Selection Sort (Ordinamento per Selezione)
- **Idea**: Divide l'array in una parte ordinata (inizialmente vuota) ed una disordinata. Trova l'elemento minimo nella parte disordinata e lo scambia con il primo elemento non ordinato.
- **Analisi Matematica dei Confronti**:
  Ad ogni passo $i$ (da 0 a $N-2$), cerchiamo il minimo confrontando gli elementi rimasti ($N - 1 - i$).
  $$\text{Confronti} = \sum_{i=0}^{N-2} (N - 1 - i) = (N-1) + (N-2) + \dots + 1 = \frac{N(N-1)}{2} \in \Theta(N^2)$$
  Questo conteggio è fisso e non dipende dall'ordinamento iniziale dei dati.
- **Analisi Matematica degli Scambi**:
  Viene eseguito esattamente 1 scambio ad ogni iterazione del ciclo esterno $\rightarrow N-1$ scambi totali $\in \Theta(N)$.
- **Passaggi** (la barra `|` delimita la zona già ordinata):
  ```text
  | 3   1   5   9   7   2  -> Trova 1 (il minimo), scambia con il primo (3)
    1 | 3   5   9   7   2  -> Trova 2, scambia con il secondo (3)
    1   2 | 5   9   7   3  -> Trova 3, scambia con il terzo (5)
    1   2   3 | 9   7   5  -> Trova 5, scambia con il quarto (9)
    1   2   3   5 | 7   9  -> Trova 7 (già in posizione)
    1   2   3   5   7 | 9  -> L'ultimo elemento è necessariamente ordinato.
  ```

### 2. Insertion Sort (Ordinamento per Inserimento)
- **Idea**: Inserisce il primo elemento disordinato nella corretta posizione all'interno della porzione già ordinata, facendolo "scivolare" all'indietro.
- **Analisi Matematica**:
  - **Caso Migliore** (già ordinato): Ogni elemento viene confrontato solo una volta con il suo precedente senza scivolamenti $\rightarrow N - 1$ confronti $\in \Theta(N)$ e $0$ scambi.
  - **Caso Peggiore** (inversamente ordinato): Ciascun elemento deve scivolare fino all'inizio della parte ordinata.
    $$\text{Confronti/Scambi} = \sum_{i=1}^{N-1} i = \frac{N(N-1)}{2} \in \Theta(N^2)$$
  - **Caso Medio**: $\Theta(N^2)$ confronti e scambi.
- **Passaggi**:
  ```text
  | 3   1   5   9   7   2  -> Il primo elemento (3) è già considerato ordinato
    3 | 1   5   9   7   2  -> Inserisci 1: scivola prima del 3
    1   3 | 5   9   7   2  -> Inserisci 5: resta dopo il 3
    1   3   5 | 9   7   2  -> Inserisci 9: resta dopo il 5
    1   3   5   9 | 7   2  -> Inserisci 7: si inserisce tra 5 e 9
    1   3   5   7   9 | 2  -> Inserisci 2: scivola tra 1 e 3
    1   2   3   5   7   9 |
  ```

### 3. Bubble Sort (Ordinamento per Scambio)
- **Idea**: Esegue più passate. Ad ogni passata, confronta coppie di elementi adiacenti e li scambia se sono fuori ordine, portando l'elemento più piccolo "a galla" verso l'inizio del vettore.
- **Dettaglio del Primo Passo** (porta a galla il minimo, partendo dal fondo):
  ```text
  Confronto (2, 7) -> OK (nessuno scambio)      : 3   1   5   9   2   7
  Confronto (2, 9) -> fuori ordine (scambia!)  : 3   1   5   2   9   7
  Confronto (2, 5) -> fuori ordine (scambia!)  : 3   1   2   5   9   7
  Confronto (2, 1) -> OK (nessuno scambio)      : 3   1   2   5   9   7
  Confronto (1, 3) -> fuori ordine (scambia!)  : 1 | 3   2   5   9   7 (Fine 1° passo)
  ```
- **Dettaglio del ...** (porta a galla il secondo minimo):
  ```text
  1 | 3   2   5   7   9  (dopo confronti dal fondo)
  1   2 | 3   5   7   9  (Fine 2° passo)
  ```

---

### Implementazione e Analisi di Bubble Sort

```java
static public void ordina(int vettore[]) {
    int temp;
    for (int i = 0; i < vettore.length - 1; i++) {
        for (int j = vettore.length - 1; j > i; j--) {
            if (vettore[j] < vettore[j - 1]) {
                temp = vettore[j];
                vettore[j] = vettore[j - 1];
                vettore[j - 1] = temp;
            }
        }
    }
}
```

* **Spazio**: Costante ($O(1)$) in quanto l'ordinamento avviene *in-place*.
* **Confronti**: Il ciclo interno esegue $N-1-i$ confronti. In totale:
  $$\text{Confronti} = (N-1) + (N-2) + \dots + 1 = \frac{N(N-1)}{2} \in \Theta(N^2)$$
* **Assegnamenti (Scambi)**:
  - **Caso Migliore** (già ordinato): $0$ scambi.
  - **Caso Peggiore** (inversamente ordinato): Ad ogni confronto corrisponde uno scambio (3 assegnamenti).
    $$\text{Assegnamenti nel caso peggiore} = 3 \cdot \frac{N(N-1)}{2} = \frac{3N(N-1)}{2} \in \Theta(N^2)$$

> [!WARNING]
> ### Comportamento Medio del Bubble Sort
> Si dimostra matematicamente che nel **caso medio** il numero di scambi è proporzionale a quello del caso peggiore (circa la metà). Pertanto, la complessità temporale media resta **$\Theta(N^2)$**.

#### Dati Empirici dell'Esperimento:

| Dimensione Array ($n$) | Tempo $T$ (ms) | Tempo $T$ (se già ordinato) |
| :--- | :--- | :--- |
| **10.000** | 200 | - |
| **100.000** | 16.000 | - |
| **200.000** | 66.000 / 74.000 | 21.000 |
| **400.000** | 303.437 | - |

- Si nota che al raddoppiare di $n$ (da 100k a 200k), il tempo quadruplica ($T \approx n^2$), coerentemente con la natura quadratica dell'algoritmo.

---

## 11. ALGORITMI DI RICERCA

Analizziamo la ricerca di un elemento in un vettore non ordinato.

```java
static public int ricercaConWhile(int vettore[], int elem) {
    int i = 0;
    boolean nonTrovato = true;
    while (nonTrovato && i < vettore.length) {
        if (elem == vettore[i]) {
            nonTrovato = false;
        } else {
            i++;
        }
    }
    if (nonTrovato) {
        return -1;
    } else {
        return i;
    }
}
```

### Analisi della Complessità
- **Spazio**: Costante ($O(1)$) - viene usata solo la variabile di indice `i`.
- **Tempo**:
  - **Caso Migliore**: L'elemento si trova in prima posizione ($i=0$) $\rightarrow \Theta(1)$ (costante).
  - **Caso Peggiore**: L'elemento è all'ultimo posto o non è presente $\rightarrow \Theta(N)$ (richiede $N$ iterazioni).

### Calcolo della Complessità Media (Ricerca Lineare)
Per calcolare rigorosamente la complessità nel caso medio, facciamo le seguenti assunzioni:
1. L'elemento cercato è sempre presente nel vettore.
2. L'elemento può trovarsi in una qualsiasi delle $N$ posizioni con uguale probabilità:
   $$P(\text{elemento in posizione } i) = \frac{1}{N} \quad \forall i \in \{1, 2, \dots, N\}$$

Il numero di iterazioni richieste se l'elemento è in posizione $i$ è esattamente $i$. L'**operatore di aspettazione (valore atteso)** per il numero di iterazioni $I$ è:
$$E[I] = \sum_{i=1}^{N} (\text{iterazioni per il caso } i) \cdot P(\text{caso } i)$$
$$E[I] = \sum_{i=1}^{N} i \cdot \frac{1}{N} = \frac{1}{N} \sum_{i=1}^{N} i$$

Sfruttando la formula della progressione aritmetica di Gauss per la somma dei primi $N$ interi:
$$\sum_{i=1}^{N} i = \frac{N(N+1)}{2}$$

Sostituendo la somma nel valore atteso:
$$E[I] = \frac{1}{N} \cdot \frac{N(N+1)}{2} = \frac{N+1}{2}$$

Moltiplicando il numero medio di iterazioni per il costo di una singola iterazione ($c$), otteniamo la complessità temporale attesa:
$$T_{\text{medio}}(N) = c \cdot \left(\frac{N+1}{2}\right) \in \Theta(N)$$
*(La complessità media è lineare rispetto alla dimensione del vettore).*

---
◀️ *Back to:* [[00_Index_OOP]]