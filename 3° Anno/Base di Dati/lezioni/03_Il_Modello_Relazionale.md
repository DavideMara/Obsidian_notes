---
date: 2026-09-28
tags:
  - base-di-dati
type: lezione
---
# Il Modello Relazionale dei Dati: Origini, Fondamenti Matematici, Schemi ed Istanze

Il modello relazionale fu sviluppato negli anni '70 ed e attualmente il piu diffuso modello di basi di dati, sotteso ai DBMS commerciali e open-source.

> [!IMPORTANT] Le Due Caratteristiche alla Base della Diffusione
> - **Semplicita concettuale:** la base di dati e percepita dagli utenti in modo estremamente intuitivo come un insieme omogeneo di tabelle bidimensionali composte da righe e colonne.
> - **Linguaggi dichiarativi:** l'interrogazione e la manipolazione ad alto livello (SQL, Algebra Relazionale) specificano **cosa** reperire, demandando al DBMS il **come** eseguire l'accesso fisico.

---

## I. Introduzione al Modello Relazionale

Il modello relazionale fu teorizzato nel **1970** da **Edgar F. Codd** (ricercatore presso i laboratori IBM di San Jose), nell'articolo *"A Relational Model of Data for Large Shared Data Banks"*, con l'obiettivo primario di garantire una reale e rigorosa indipendenza dei dati (sia logica che fisica) rispetto alle applicazioni software.

Commercializzato a partire dai primi anni '80 (con l'avvento di piattaforme pionieristiche quali **System R**, **Oracle** e **IBM DB2**), rappresenta oggi il paradigma dominante dell'industria del software.

---

## II. Modello Relazionale vs Modelli Gerarchico e Reticolare

Il modello relazionale ha introdotto una netta discontinuita rispetto ai modelli precedenti.

### 2.1 Rappresentazione delle Associazioni tra Record

| | Modelli Gerarchico e Reticolare | Modello Relazionale |
| :--- | :--- | :--- |
| **Meccanismo** | Puntatori fisici espliciti e indirizzi di memoria incorporati nei record (*pointer-based*) | Associazioni basate interamente sui valori dei dati condivisi (*value-based*) |
| **Navigazione** | Vincolata ai cammini fisici previsti dal progettista | Confronto dei valori contenuti in campi correlati (es. corrispondenza chiave primaria / chiave esterna) |
| **Puntatori esposti** | Si, nel record | No, mai |

### 2.2 Fondamento Formale e Matematico

I modelli gerarchico e reticolare derivavano da approcci euristici e soluzioni implementative *ad-hoc*. Il modello relazionale poggia invece su solide basi formali tratte dalla **teoria matematica degli insiemi** e dalla **logica dei predicati del primo ordine**, consentendo la dimostrazione formale di equivalenze tra espressioni e l'ottimizzazione automatica delle query.

---

## III. Fondamenti Matematici: Dal Prodotto Cartesiano alle Relazioni

La formalizzazione del modello relazionale trae origine dai concetti di prodotto cartesiano e relazione matematica.

### 3.1 Prodotto Cartesiano

Siano $D_1, D_2, \ldots, D_n$ insiemi (detti insiemi di supporto o domini, non necessariamente distinti).

> [!IMPORTANT] Definizione di Prodotto Cartesiano
> Il prodotto cartesiano $D_1 \times D_2 \times \cdots \times D_n$ e l'insieme di tutte le n-uple ordinate $(d_1, d_2, \ldots, d_n)$ tali che ciascun elemento $d_i$ appartenga al rispettivo dominio $D_i$:
> $$D_1 \times D_2 \times \cdots \times D_n = \{(d_1, d_2, \ldots, d_n) \mid d_1 \in D_1, d_2 \in D_2, \ldots, d_n \in D_n\}$$

### 3.2 Relazione Matematica

> [!IMPORTANT] Definizione di Relazione Matematica
> Una relazione matematica $R$ definita sugli insiemi $D_1, D_2, \ldots, D_n$ e un qualsiasi sottoinsieme del loro prodotto cartesiano:
> $$R \subseteq D_1 \times D_2 \times \cdots \times D_n$$

- **Grado di una Relazione:** e il numero $n$ di insiemi/domini componenti il prodotto cartesiano (ovvero il numero di componenti di ciascuna n-upla).
- **Cardinalita di una Relazione** ($|R|$): e il numero complessivo di elementi (n-uple) appartenenti all'insieme $R$.

---

## IV. Dalle Relazioni Matematiche alle Relazioni nel Modello dei Dati

Sebbene il modello relazionale poggi sulla nozione matematica di relazione, esso introduce due importanti adattamenti per rispondere alle esigenze pratiche di memorizzazione e manipolazione dei dati.

| Relazione Matematica | Relazione nel Modello dei Dati |
| :--- | :--- |
| n-uple ordinate: $(d_1, \ldots, d_n)$ | Tuple **NON ordinate** |
| Posizione fissa per indice $i$ | Attributi nominati (nomi di colonna) |
| Nessun valore nullo ammesso | Supporto al valore speciale `NULL` (dato mancante/ignoto) |

1. **Assenza di ordinamento posizionale:** nelle relazioni matematiche gli elementi di una n-upla sono rigidamente ordinati per posizione; nelle basi di dati la sequenza orizzontale delle colonne non deve avere rilevanza semantica.
2. **Identificazione tramite attributi:** risulta conveniente e intuitivo associare a ciascuna componente un nome simbolico (attributo) esplicito (es. `Nome`, `Matricola`, `Stipendio`), anziche identificarla tramite il suo indice numerico posizionale $i$.

---

## V. Domini, Attributi e il Concetto Formale di Tupla

### 5.1 Domini

> [!IMPORTANT] Definizione di Dominio
> Un dominio $D$ e un insieme non vuoto di valori atomici (indivisibili dal punto di vista del DBMS).

Con `Dom(A)` indichiamo il dominio formalmente associato all'attributo $A$.

- **Esempio:** `Dom(Nazione)` rappresenta l'insieme delle stringhe di caratteri indicanti nomi validi di stati sovrani; `Dom(Voto)` rappresenta l'insieme dei numeri interi $\{18, 19, \ldots, 30, 30L\}$.

### 5.2 Attributi

Un attributo $A$ e un'etichetta o nome simbolico associato a un determinato dominio con un preciso significato semantico all'interno dello schema.

### 5.3 Il Concetto di Tupla

Sia $X = \{A_1, A_2, \ldots, A_n\}$ un insieme finito di attributi.

> [!IMPORTANT] Definizione di Tupla
> Una tupla $t$ definita sull'insieme di attributi $X$ e una funzione che associa a ogni attributo $A_i \in X$ un valore appartenente al suo dominio `Dom(A_i)`, oppure lo speciale valore `NULL`:
> $$t : X \longrightarrow \bigcup_{A_i \in X} \text{Dom}(A_i) \cup \{\text{NULL}\}$$
> tale che $t[A_i] \in \text{Dom}(A_i) \lor t[A_i] = \text{NULL}$

Con la notazione $t[A_i]$ (oppure $t.A_i$) indichiamo il valore assunto dalla tupla $t$ in corrispondenza dell'attributo $A_i$.

> [!WARNING] Il Valore Speciale NULL
> Il valore `NULL` indica l'assenza di un valore reale e viene impiegato per rappresentare **tre condizioni semantiche distinte**:
> 1. **Valore sconosciuto** (es. data di nascita non ancora registrata).
> 2. **Valore inesistente o non applicabile** (es. numero di patente per un cittadino non patentato).
> 3. **Valore omesso o riservato.**

---

## VI. Relazioni: Schemi ed Istanze

La distinzione tra livello intensionale (statico) ed estensionale (dinamico) si applica puntualmente alle relazioni.

### 6.1 Schema di Relazione

> [!IMPORTANT] Definizione di Schema di Relazione
> Dato un insieme di attributi $X = \{A_1, A_2, \ldots, A_n\}$, uno schema di relazione e costituito da un nome di relazione $R$ e dall'insieme di attributi $X$:
> $$R(X) \quad \text{oppure} \quad R(A_1, A_2, \ldots, A_n)$$

Qualora sia necessario esplicitare i domini di riferimento, si adotta la notazione estesa:

$$R(A_1 : \text{Dom}(A_1), A_2 : \text{Dom}(A_2), \ldots, A_n : \text{Dom}(A_n))$$

### 6.2 Istanza di Relazione

> [!IMPORTANT] Definizione di Istanza di Relazione
> Dato uno schema di relazione $R(X)$, un'istanza di relazione $r(R)$ (o semplicemente $r$) su $X$ e un insieme finito di tuple su $X$:
> $$r(R) = \{t_1, t_2, \ldots, t_k\}$$

> [!WARNING] Implicazioni della Natura di Insieme
> Poiche un'istanza e matematicamente un insieme di tuple:
> - **Non possono esistere tuple duplicate** identiche all'interno della medesima istanza.
> - **L'ordine delle tuple (righe) non ha alcuna rilevanza.**

---

## VII. Basi di Dati: Schemi ed Istanze

Estendendo il formalismo a livello di sistema globale.

### 7.1 Schema di Base di Dati

> [!IMPORTANT] Definizione di Schema di Base di Dati
> Uno schema di base di dati $B$ e una collezione di schemi di relazione con denominazioni distinte:
> $$B = \{R_1(X_1), R_2(X_2), \ldots, R_m(X_m)\}$$
> corredato dalla specifica dell'insieme dei relativi **vincoli di integrita** $I$.

### 7.2 Istanza di Base di Dati

> [!IMPORTANT] Definizione di Istanza di Base di Dati
> Un'istanza di base di dati $b$ definita sullo schema $B = \{R_1(X_1), \ldots, R_m(X_m)\}$ e un insieme di istanze di relazione:
> $$b = \{r_1, r_2, \ldots, r_m\}$$
> tale che ciascuna $r_i$ sia un'istanza valida dello schema di relazione $R_i(X_i)$ (per ogni $i \in \{1, \ldots, m\}$) e rispetti l'insieme dei vincoli $I$.

---

## VIII. Esempio Pratico di Formalizzazione

Si consideri uno schema universitario:

$$B = \{\text{Studente(Matricola, Nome)},\ \text{Corso(Codice, Nome)},\ \text{Iscrizione(Studente, Corso)}\}$$

**Istanza `Studente`** ($r_{\text{Studente}}$):

| Matricola | Nome |
| :--- | :--- |
| 37891 | Mario Rossi |
| 5421 | Luigi Verdi |

**Istanza `Corso`** ($r_{\text{Corso}}$):

| Codice | Nome |
| :--- | :--- |
| 1 | BD |
| 2 | ASD |

**Istanza `Iscrizione`** ($r_{\text{Iscrizione}}$):

| Studente | Corso |
| :--- | :--- |
| 37891 | 1 |
| 37891 | 2 |

Nel formalismo matematico delle funzioni/tuple, l'istanza globale corrisponde all'insieme:

$$
b = \left\{
\begin{array}{l}
\{\{(M, 37891), (N, \text{"Mario Rossi"})\}, \{(M, 5421), (N, \text{"Luigi Verdi"})\}\}, \\
\{\{(C, 1), (N, \text{"BD"})\}, \{(C, 2), (N, \text{"ASD"})\}\}, \\
\{\{(S, 37891), (C, 1)\}, \{(S, 37891), (C, 2)\}\}
\end{array}
\right\}
$$

---

## IX. Mappatura Terminologica: Concetto Formale vs Equivalente

| Concetto Formale (Modello Relazionale) | Equivalente Tabellare Informale | Corrispettivo nei File Tradizionali |
| :--- | :--- | :--- |
| **Relazione** | Tabella | File |
| **Attributo** | Intestazione di colonna / Campo | Campo del record |
| **Tupla** | Riga della tabella | Singolo record |
| **Dominio** | Tipo di dato e vincoli di colonna | Tipo di dato del campo |
| **Grado** | Numero di colonne della tabella | Numero di campi per record |
| **Cardinalita** | Numero di righe della tabella | Numero di record nel file |
| **Schema di Relazione** | Struttura / DDL dell'intestazione | Definizione del tracciato record |
| **Istanza di Relazione** | Insieme corrente di righe popolate | Contenuto del file su disco |

> [!EXAMPLE] Lettura dei Termini con SQL
> In SQL la stessa struttura viene denotata con altri nomi: la *relazione* diventa la **tabella** (o vista, se derivata), gli *attributi* diventano le **colonne**, le *tuple* diventano le **righe**. Il termine "relazione" viene spesso usato in senso informale per indicare una tabella, anche se formalmente una tabella e un'istanza di relazione, non lo schema.

---
## ⏭️ Navigazione Lezioni
- **Lezione precedente :** [[02_Modelli_di_Dati_e_Architetture_DBMS]]
- **Lezione successiva :** [[04_Vincoli_di_Integrita]]
- **Index Corso :** [[00_Index_Base_di_Dati]]