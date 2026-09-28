---
date: 2026-02-27
tags:
  - appunti
  - lezione
  - linguaggi-formali
type: lezione
---

# Parole, Linguaggi e Grammatiche

## 1. Il problema dell'infinito e il Teorema di Cantor

Per descrivere qualsiasi cosa, che sia la Divina Commedia o il codice genetico umano, usiamo delle parole. 
In informatica teorica, un **linguaggio è definito come un insieme di parole**.

* **Linguaggi Finiti:** Se un linguaggio è finito, la sua descrizione è banale poiché è possibile elencarne tutti gli elementi uno per uno. Un esempio è $L=\{a,ab,abb,abbb\}$.
* **Linguaggi Infiniti:** Il problema sorge quando cerchiamo di descrivere linguaggi con infinite parole.

Il **Teorema di Cantor** ci pone un limite matematico insuperabile: non esiste una funzione iniettiva dall'insieme delle parti $\mathcal{P}(\Sigma^{*})$ all'insieme delle parole $\Sigma^{*}$. 
Di conseguenza, non è possibile associare a *ciascun* linguaggio possibile una parola univoca (la sua "descrizione") che lo caratterizzi in modo perfetto. In altre parole, non possiamo inventare una "parola descrittiva" univoca per tutti i possibili linguaggi infiniti esistenti.

> [!NOTE] L'approccio Informatico
> Nonostante il Teorema di Cantor, in informatica non abbiamo bisogno di descrivere *tutti* i linguaggi infiniti. È comunque possibile fornire **descrizioni finite** per *alcuni* linguaggi infiniti che ci sono particolarmente utili. Ad esempio, possiamo usare una regola descrittiva semplice come "tutte le parole sull'alfabeto $\{a,b\}$ di lunghezza dispari", oppure la notazione formale $\{a^{n}b^{n}|n\ge0\}$.

Un costrutto fondamentale per generare infinità è la **chiusura di Kleene** di un linguaggio $L$ (indicata con $L^{*}$). Essa è costituita dalla parola vuota, dalle parole appartenenti a $L$ e da tutte le parole che si ottengono concatenando due o più parole di $L$. Se $L$ è un linguaggio finito, il linguaggio derivato $L^{*}$ è ben definito e, in generale, infinito.

---

## 2. Alfabeti, Parole e le loro Proprietà (Definizioni Formali)

Per poter costruire delle regole rigorose, dobbiamo prima definire matematicamente gli elementi base.

### L'Alfabeto e le Parole
* **Alfabeto ($\Sigma$):** È un insieme finito e non vuoto di simboli. I suoi elementi sono chiamati **lettere**.
    * *Esempi di alfabeti:* $\Sigma_{0}=\{a,b\}$, $\Sigma_{1}=\{0,1\}$, $\Sigma_{2}=\{a,b,c\}$ e l'alfabeto esadecimale $\Sigma_{3}=\{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F\}$.
* **Parola:** Ogni sequenza finita di lettere appartenenti a un alfabeto $\Sigma$ è detta parola sull'alfabeto $\Sigma$. 
    * *Esempi:* "a", "abb", "ababbabb" sono parole su $\Sigma_{0}$; "2020" e "CD078B" sono parole su $\Sigma_{3}$.
* **L'insieme Universo ($\Sigma^{*}$):** L'insieme di *tutte* le parole generabili sull'alfabeto $\Sigma$ è denotato con $\Sigma^{*}$.
* **Parola Vuota:** Esiste anche la sequenza composta da zero lettere, che si denota con $\epsilon$ (oppure $\Lambda$) e si dice **parola vuota**.
* **Lunghezza ($|u|$):** Data una parola $u=a_{1}a_{2}\cdot\cdot\cdot a_{k}$ (con $k\ge0$), l'intero $k$ rappresenta la sua lunghezza e si denota con $|u|$ oppure $l(u)$.
    * *Esempi:* $|abb|=3$, $|\epsilon|=0$.

### Operazioni sulle Parole
* **Concatenazione:** Date due parole $u$ e $v$, la loro concatenazione $uv$ è semplicemente l'unione in sequenza delle loro lettere. Ad esempio, concatenando "abb" e "aaab" si ottiene "abbaaab".
    * *Proprietà Binaria:* È un'operazione binaria totale su $\Sigma^{*}$.
    * *Associatività:* Per ogni $u, v, w \in \Sigma^{*}$, vale $(uv)w=u(vw)$.
    * *Elemento Neutro:* La parola vuota $\epsilon$ fa da elemento neutro: $u\epsilon=\epsilon u=u$.
    * *Cancellatività:* Gode della cancellatività a destra e a sinistra (se $uw=vw$ oppure $wu=wv$, allora $u=v$).
* **Potenza n-esima ($w^{n}$):** Si ottiene concatenando $n$ copie della parola $w$ (es. $w^{n}=ww\cdot\cdot\cdot w$). Si definisce $w^{0}=\epsilon$. Se $u=abb$, allora $u^{2}=abbabb$.
* **Fattori, Prefissi e Suffissi:** Una parola $v$ è un **fattore** di $w$ se è contenuta al suo interno, ovvero se $w=xvy$ per opportune parole $x, y$.
    * **Prefisso:** Se $x=\epsilon$, allora $v$ si trova all'inizio ed è detto prefisso.
    * **Suffisso:** Se $y=\epsilon$, allora $v$ si trova alla fine ed è detto suffisso.
    * **Fattore Proprio:** Diremo che $v$ è un fattore proprio se $v\ne w$.

### Linguaggio Formale (Definizione Rigorosa)
Ogni sottoinsieme di $\Sigma^{*}$ si dice **linguaggio formale** (o semplicemente linguaggio) sull'alfabeto $\Sigma$.
Possono esserci linguaggi limitati come $L_{1}=\{a,ab,abb\}$, linguaggi infiniti come $L_{2}=\{ab^{n}a|n\ge0\}$, l'insieme vuoto $L_{3}=\emptyset$ o l'intero universo $L_{4}=\Sigma^{*}$.

---

## 3. L'Intuizione: Il Gioco delle Sostituzioni

Per capire operativamente come le "regole finite" possano generare "linguaggi infiniti", analizziamo un esempio pratico basato sul linguaggio naturale.

Vogliamo generare liste di nomi come "Aldo, Bianca e Carlo". Le regole logiche che governano queste frasi sono:
1.  I nomi sono separati da virgola, tranne gli ultimi due che sono separati dalla congiunzione 'e'.
2.  Sono ammesse ripetizioni di nomi (es. "Aldo, Bianca, Aldo...").
3.  Non c'è alcun limite alla lunghezza della lista.

Per istruire una macchina, dobbiamo usare dei **segnaposto** (come i termini "nome" o "frase") ed eseguire sostituzioni meccaniche secondo regole predefinite. 

> [!IMPORTANT] Il Problema delle Regole Globali vs Locali
> Un primo tentativo di creare queste regole umane includerebbe una direttiva del tipo: "prima di terminare, se sono presenti virgole, l'ultima va sostituita con la congiunzione e".
> Questa regola, tuttavia, è anomala rispetto alle altre: impone di analizzare l'intera frase simultaneamente per trovare "l'ultima virgola". Un calcolatore preferisce invece **regole di sostituzione rigorose e puramente locali**, dove un simbolo viene sostituito ciecamente a prescindere dal contesto globale.

### La Soluzione Formale: Ricorsione e Segnaposto
La soluzione "informatica" parte sempre da un segnaposto iniziale (es. `frase`) e procede sostituendolo finché non rimangono solo parole e punteggiatura reali. 

1.  **Regole di Base:** Il segnaposto $\langle nome \rangle$ può essere sostituito da Aldo, Bianca o Carlo.
2.  **Inizio:** $\langle frase \rangle$ può diventare un singolo $\langle nome \rangle$ oppure il blocco $\langle lista Nomi \rangle \langle fineLista \rangle$.
3.  **Il Motore dell'Infinito (Ricorsione):** $\langle lista Nomi \rangle$ può essere sostituito da $\langle nome \rangle$ oppure da $\langle nome \rangle, \langle lista Nomi \rangle$. 
    > [!EXAMPLE] Come si genera l'infinito
    > Contenendo se stessa nella parte destra dell'assegnazione, può essere applicata all'infinito per aggiungere quante virgole e quanti nomi desideriamo, creando una lunghezza illimitata a partire da una singola regola.
4.  **Chiusura:** Il blocco $\langle nome \rangle \langle fine Lista \rangle$ si sostituisce rigorosamente con $e \langle nome \rangle$. Questo trucco garantisce che, alla fine del processo meccanico, l'ultimo elemento sia sempre preceduto dalla 'e' e non dalla virgola.

Ci si arresta solo quando i segnaposto non compaiono più.
**Il concetto chiave è che un linguaggio di complessità e lunghezza infinita può essere generato meccanicamente e senza ambiguità tramite un set ristretto di regole di sostituzione locali**.

---

## 4. Grammatiche a Struttura di Frase (Formalizzazione)

Le regole di sostituzione viste nell'esempio vengono astratte nel concetto matematico di **Grammatica a Struttura di Frase**, formalmente definita come una quadrupla $G=\langle V,\Sigma,P,S\rangle$:

* **$V$ (Vocabolario Totale):** Un alfabeto finito che comprende tutti i simboli.
* **$\Sigma$ (Alfabeto dei Simboli Terminali):** Sottoinsieme di $V$ ($\Sigma\subseteq V$), comprende i simboli definitivi (es. "Aldo", la virgola, la "e").
* **$P$ (Insieme delle Produzioni):** Un insieme finito di regole di riscrittura della forma $\alpha\rightarrow\beta$.
    * La parte sinistra $\alpha \in V^{*} \setminus \Sigma^{*}$ deve contenere almeno una variabile.
    * La parte destra $\beta \in V^{*}$ può essere una sequenza qualsiasi di variabili e terminali.
* **$S$ (Simbolo Iniziale o Assioma):** È il punto di partenza del processo generativo ($S\in N$).
* **$N$ (Variabili):** Le lettere dell'insieme $N=V\backslash\Sigma$ si dicono variabili (i nostri "segnaposto").

### Convenzioni Notazionali
* Variabili ($N$): Si indicano con lettere maiuscole come A, B, C, X, Y, Z.
* Simboli Terminali ($\Sigma$): Si indicano con lettere minuscole come a, b, c.
* Parole sull'alfabeto $V$: Si indicano con lettere greche come $\alpha, \beta, \gamma$.
* Parole sui terminali $\Sigma$: Si indicano con $u, v, w$.

### Il Linguaggio Generato
Il processo con cui una grammatica crea parole si basa sulla **derivazione**:
* **Conseguenza Diretta ($\alpha\Rightarrow\beta$):** $\beta$ è una conseguenza diretta di $\alpha$ se posso applicare una singola produzione $\gamma\rightarrow\gamma^{\prime}$ (appartenente a $P$) a un frammento di $\alpha$. Formalmente: esistono $\gamma_{1}, \gamma_{2} \in V^{*}$ tali che $\alpha=\gamma_{1}\gamma\gamma_{2}$ e $\beta=\gamma_{1}\gamma^{\prime}\gamma_{2}$.
* **Derivazione ($\alpha\Rightarrow^{*}\beta$):** $\beta$ si deriva da $\alpha$ nella grammatica $G$ se esiste una catena di conseguenze dirette di lunghezza $n \ge 0$ passaggi ($\alpha=\alpha_{0}\Rightarrow\alpha_{1}\Rightarrow\cdot\cdot\cdot\Rightarrow\alpha_{n}=\beta$).
* **Forme Sentenziali:** Tutte le stringhe che si possono derivare a partire dal simbolo iniziale $S$.
* **Linguaggio Generato da $G$:** È l'insieme di tutte e sole le forme sentenziali che sono **prive di variabili** (cioè composte interamente da simboli terminali appartenenti a $\Sigma$).
### LEGENDA

| **Concetto**                  | **Simbolo / Notazione**              | **Descrizione**                                                   |
| ----------------------------- | ------------------------------------ | ----------------------------------------------------------------- |
| **Alfabeto**                  | $\Sigma$                             | Insieme finito di simboli (terminali).                            |
| **Vocabolario Totale**        | $V$                                  | Unione di terminali e variabili ($\Sigma \cup N$).                |
| **Variabili (Non-terminali)** | $N$ (o $V_{N}$)                      | Segnaposto indicati con lettere maiuscole ($A, B, S$).            |
| **Parola Vuota**              | $\epsilon$ (o $\Lambda$)             | Sequenza di lunghezza zero.                                       |
| **Chiusura di Kleene**        | $\Sigma^*$                           | Insieme di tutte le parole possibili su un alfabeto.              |
| **Produzione**                | $\gamma \rightarrow \gamma^{\prime}$ | Regola di riscrittura da una stringa a un'altra.                  |
| **Assioma**                   | $S$                                  | Il simbolo iniziale da cui parte ogni derivazione.                |
| **Conseguenza Diretta**       | $\alpha \Rightarrow \beta$           | Trasformazione di $\alpha$ in $\beta$ tramite **una** produzione. |
| **Conseguenza Derivazione**   | $\alpha \Rightarrow^* \beta$         | Trasformazione tramite **zero o più** passaggi.                   |
| **Lunghezza**                 | $                                    | w                                                                 |
| **Linguaggio generato**       | $L(G)$                               | Insieme delle parole terminali derivabili da $S$.                 |


## 5. Il nostro esempio: Formalizzazione della Grammatica

Applicando le definizioni formali alla lista di nomi generata nei passaggi precedenti, definiamo i parametri esatti della nostra grammatica.

### 1. Le Variabili ($N$)
L'insieme delle variabili (i nostri segnaposto) è composto da:
* $\langle frase \rangle$
* $\langle listaNomi \rangle$
* $\langle fineLista \rangle$
* $\langle nome \rangle$

### 2. I Simboli Terminali ($\Sigma$)
L'alfabeto dei simboli terminali (ovvero gli elementi che compariranno nella stringa finale prodotta) comprende:
* Le lettere delle parole **Aldo**, **Bianca**, **Carlo**
* La congiunzione **e**
* La **virgola** (`,`)
* Lo **spazio**

### 3. L'Insieme delle Produzioni ($P$)
Le regole di sostituzione formali della grammatica sono le seguenti:

* $\langle nome \rangle \rightarrow Aldo$
* $\langle nome \rangle \rightarrow Bianca$
* $\langle nome \rangle \rightarrow Carlo$
* $\langle frase \rangle \rightarrow \langle nome \rangle$
* $\langle frase \rangle \rightarrow \langle listaNomi \rangle \langle fineLista \rangle$
* $\langle listaNomi \rangle \rightarrow \langle nome \rangle$
* $\langle listaNomi \rangle \rightarrow \langle nome \rangle, \langle listaNomi \rangle$
* $\langle nome \rangle \langle fineLista \rangle \rightarrow e \langle nome \rangle$

