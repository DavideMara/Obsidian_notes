---
date: 2026-09-30
tags:
  - intelligenza-artificiale
type: lezione
---
# Fondamenti di Intelligenza Artificiale, Machine Learning e Modelli Generativi

## I. Introduzione all'Intelligenza Artificiale e Tassonomia

L'Intelligenza Artificiale (IA) affonda le proprie radici teoriche nei primi anni '50. Nel 1950, Alan Turing, nell'articolo *"Computing Machinery and Intelligence"*, formulò la domanda fondamentale se una macchina potesse pensare ed interagire con l'essere umano utilizzando il suo stesso linguaggio naturale, introducendo l'*Imitation Game*, noto come Test di Turing.

L'ecosistema dell'IA moderna si struttura secondo una gerarchia insiemistica ben definita:

```text
IA Generativa ⊆ Deep Learning ⊆ Machine Learning ⊆ Intelligenza Artificiale
```

```text
┌─────────────────────────────────────────────────────────────┐
│ Intelligenza Artificiale (IA)                               │
│ ┌───────────────────────────────────────────────────────┐ │
│ │ Machine Learning (ML)                                  │ │
│ │ ┌─────────────────────────────────────────────────┐ │ │
│ │ │ Deep Learning (Reti Neurali Profonde)             │ │ │
│ │ │ ┌───────────────────────────────────────────┐ │ │ │
│ │ │ │ IA Generativa (LLM, VLM, Diffusion Model) │ │ │ │
│ │ │ └───────────────────────────────────────────┘ │ │ │
│ │ └─────────────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT] Definizioni Fondamentali
> - **Intelligenza Artificiale (IA):** Disciplina informatica che studia lo sviluppo di sistemi hardware e software capaci di risolvere compiti che richiederebbero intelligenza umana.
> - **Machine Learning (ML):** Sottoinsieme dell'IA basato su algoritmi che apprendono pattern e relazioni matematiche direttamente dai dati, senza essere esplicitamente programmati con regole rigide.
> - **Deep Learning (DL):** Branca del Machine Learning basata su reti neurali artificiali multi-strato caratterizzate da un elevato numero di parametri.
> - **IA Generativa:** Sistemi di Deep Learning progettati per generare nuovi contenuti (testo, codice, immagini, audio, azioni) a partire da distribuzioni di probabilità apprese.

> [!INFO] Cambio di Paradigma del Machine Learning
> Nella programmazione tradizionale, il programmatore combina dati e regole logiche predeterminate per calcolare le risposte. Nel Machine Learning, si forniscono all'algoritmo di apprendimento i dati e le risposte attese (esempi etichettati): l'algoritmo deduce automaticamente le relazioni statistiche, producendo un modello.

## II. Il Processo di Apprendimento Automatico

### 2.1 Definizione di Addestramento (Training)

L'addestramento (training) è il processo algoritmico volto a determinare i valori ottimali dei parametri interni di un modello, al fine di minimizzare l'errore di predizione sui dati di addestramento e garantire un'accurata capacità di inferenza su dati non ancora osservati.

```text
Dati di Input + Risposte Attese
        └───►  Algoritmo di Apprendimento  ───►  Modello Ottimizzato
```

L'algoritmo opera in modo iterativo:

- Aggiorna progressivamente i parametri passo dopo passo.
- Termina al raggiungimento della convergenza numerica (quando l'errore non diminuisce ulteriormente), oppure quando viene raggiunta una condizione di arresto prefissata (*early stopping*).

> [!IMPORTANT] Generalizzazione vs Memorizzazione
> L'obiettivo del Machine Learning è la **generalizzazione**, non la pura memorizzazione dei dati. Per questa ragione, il modello viene addestrato sul *training set*, ma le sue prestazioni devono essere tassativamente verificate e validate su un insieme disgiunto di dati mai visti durante il training (*test set*), prevenendo il fenomeno dell'*overfitting* (sovradattamento).

### 2.2 Complessità del Modello e Distribuzione delle Risposte

Per risolvere compiti complessi è necessario addestrare modelli con un elevato numero di parametri (elevata capacità rappresentativa), i quali richiedono proporzionalmente moli massicce di dati di addestramento per evitare l'instabilità o il *underfitting* (sottoadattamento).

Il modello attribuisce una **probabilità** a ogni possibile risposta dello spazio di output. L'obiettivo del processo di addestramento è incrementare progressivamente la massa di probabilità associata alla risposta attesa (*target*).

## III. Funzione di Perdita (Loss) e Ottimizzazione del Modello

### 3.1 Esempio Fondamentale: Classificazione Lineare

Considerando il problema di separare due classi di punti bidimensionali mediante un modello lineare (retta definita da pendenza $m$ e intercetta $q$):

1. **Inizializzazione casuale:** I parametri assumono valori casuali; la retta non separa correttamente i punti.
2. **Ottimizzazione iterativa:** L'algoritmo corregge i parametri passo dopo passo, orientando e traslando la retta verso la configurazione di massima separazione.
3. **Misura dell'errore:** Per guidare la correzione è necessario quantificare l'errore tramite una funzione obiettivo scalare: la *Loss* (funzione di perdita).

### 3.2 La Funzione di Loss

La *Loss* $L$ è un valore numerico che misura la discrepanza tra la predizione del modello e il valore reale *target*. Durante l'apprendimento, la curva della loss decresce progressivamente, tendendo idealmente a 0.

Nel contesto della classificazione probabilistica, si adotta frequentemente la *Cross-Entropy Loss* (o *Negative Log-Likelihood*):

$$
Loss = -\ln(P)
$$

dove $P \in (0,1]$ rappresenta la probabilità assegnata dal modello alla classe o risposta attesa:

- Se $P \to 1$ (predizione perfetta), $-\ln(1)=0 \implies Loss=0$.
- Se $P \to 0$ (predizione errata o incertezza elevata), $-\ln(P) \to +\infty \implies Loss$ molto alta.

### 3.3 Il Paesaggio della Loss e la Discesa del Gradiente

Ogni possibile combinazione dei parametri del modello definisce un punto all'interno dello *spazio della loss* (*loss landscape*).

> [!IMPORTANT] Concetti Fondamentali dell'Ottimizzazione
> - **Spazio dei Parametri:** Ogni coordinata $(m,q)$ corrisponde a un modello specifico.
> - **Gradiente ($\nabla L$):** Vettore delle derivate parziali che indica la direzione di massima salita della funzione di loss. L'ottimizzazione procede nella direzione opposta al gradiente (*Gradient Descent*).
> - **Learning Rate ($\eta$):** Iperparametro che determina l'ampiezza dello spostamento (lunghezza del passo) a ogni iterazione:
> $$\theta^{(t+1)} = \theta^{(t)} - \eta\,\nabla L(\theta^{(t)})$$

### 3.4 Ciclo Completo di Addestramento

Il ciclo iterativo di ottimizzazione si compone di 4 fasi:

1. **Predizione (*Forward Pass*):** Calcolo delle uscite del modello a partire dagli esempi di input.
2. **Calcolo della Loss:** Valutazione numerica dell'errore rispetto alle risposte attese.
3. **Calcolo del Gradiente (*Backward Pass* / *Backpropagation*):** Calcolo di quanto ciascun parametro ha contribuito all'errore.
4. **Aggiornamento dei Parametri:** Modifica dei pesi in direzione contraria al gradiente.

A convergenza raggiunta, i parametri vengono fissati (*congelati*) e il modello entra in fase di *inferenza*.

> [!INFO] Estensione alle Reti Neurali Profonde
> Il medesimo principio (forward pass, loss, gradiente, update) si applica invariato alle reti neurali profonde. La differenza risiede nella scala: da 2 parametri a centinaia di milioni o miliardi di parametri, organizzati in architetture stratificate.

## IV. Dai Classificatori ai Large Language Model (LLM)

### 4.1 Generazione come Classificazione del Token Successivo

A ogni singolo passo generativo, un Large Language Model (LLM) esegue un'operazione di classificazione multi-classe, in cui le classi corrispondono all'insieme di tutti i token presenti nel suo vocabolario.

| Aspetto | Classificatore Supervisionato | Pre-addestramento LLM | Personalizzazione/Allineamento |
|---|---|---|---|
| **Origine etichette** | Oracolo umano etichetta ogni esempio | Nessun oracolo: target = parola successiva già presente nel testo grezzo | Esperti umani: esempi di risposte desiderate e preferenze comparative |
| **Tipo apprendimento** | Apprendimento supervisionato classico | Apprendimento auto-supervisionato (*Self-Supervised Learning*) | Fine-Tuning, Instruction Tuning, RLHF/DPO |

> [!IMPORTANT] Il Principio dell'Auto-Supervisione
> Il modello apprende la struttura della lingua e la conoscenza del mondo minimizzando l'errore nella predizione della parola successiva (*Next-Token Prediction*) su miliardi di documenti testuali. La supervisione umana specializzata interviene solo a valle per allineare e personalizzare il modello verso compiti conversazionali o specifici.

### 4.2 Dal Testo ai Numeri: Tokenizzazione ed Embedding

I modelli computazionali elaborano esclusivamente vettori numerici. Il passaggio da linguaggio naturale a rappresentazione numerica si articola in due stadi:

```text
[Testo Grezzo] ──► [Tokenizzazione (Sub-word)] ──► [Vettori di Embedding] ──► [Modello]
```

1. **Tokenizzazione:** Il testo viene scomposto in unità discrete dette *token* (frammenti di parole o *sub-word*, es. `capitale` -> `capi` + `tale`).
2. **Embedding Vettoriale:** A ciascun token viene associato un vettore numerico denso ad alta dimensionalità, i cui pesi vengono appresi durante il training.
3. **Geometria Semantica:** Lo spazio geometrico degli embedding codifica le relazioni semantiche tra concetti. Parole semanticamente correlate o che ricorrono in contesti simili occupano posizioni vicine nello spazio vettoriale.

## V. L'Architettura Transformer e Generazione del Testo

### 5.1 Il Meccanismo di Attenzione

Introdotta nel 2017 nel paper *"Attention Is All You Need"*, l'architettura Transformer ha superato le limitazioni delle reti ricorrenti (RNN/LSTM).

> [!IMPORTANT] Caratteristiche del Transformer
> - **Elaborazione simultanea:** Consente a ciascuna posizione della sequenza di interagire contemporaneamente con tutti gli altri token del contesto (*Self-Attention*), senza processare il testo sequenzialmente parola per parola.
> - **Parallelizzazione massiva:** Durante l'addestramento, tutte le posizioni vengono elaborate in parallelo su cluster di acceleratori (GPU/TPU), rendendo fattibile il training su volumi di dati e parametri su scala planetaria.

### 5.2 Pipeline di Elaborazione

Il flusso di trasformazione interno si articola attraverso blocchi Transformer ripetuti in profondità:

```text
Testo ──► Token ──► Vettori ──► [ Attenzione + Rete Feed-Forward ] × N ──► Probabilità del Token Successivo
```

### 5.3 Generazione Autoregressiva e Campionamento

A ogni iterazione, il modello emette una distribuzione di probabilità sull'intero vocabolario.

- **Scelta deterministica (*Greedy*):** Seleziona sempre il token a probabilità massima. A parità di prompt, l'output generato sarà identico.
- **Campionamento probabilistico:** Estrazione stocastica pesata sulle probabilità (regolata da parametri come *temperature*, *top-k*, *top-p*). Esecuzioni multiple dello stesso prompt possono divergere, introducendo variabilità e creatività.

> [!WARNING] Fluidità vs Affidabilità
> La fluidità e la coerenza grammaticale del testo generato derivano esclusivamente dal calcolo probabilistico iterativo. L'apparente padronanza linguistica non implica di per sé comprensione semantica, correttezza fattuale o facoltà cognitive umane, esponendo il sistema a potenziali *allucinazioni*.

## VI. Tassonomia dei Modelli Generativi ed Evoluzione dell'IA

### 6.1 Famiglie di Modelli Generativi

| Modello | Input -> Output | Descrizione |
|---|---|---|
| **LLM** (Large Language Model) | Testo -> Testo | Elaborano sequenze testuali per produrre testo in uscita. |
| **VLM** (Vision-Language Model) | Immagine + Testo -> Testo | Elaborano congiuntamente immagini e testo per generare descrizioni o risposte. |
| **VLA** (Vision-Language-Action) | Immagine + Testo -> Azioni | Elaborano input visivi e istruzioni testuali per calcolare comandi attuativi per sistemi robotici. |
| **Modelli Generativi di Immagini** | Testo -> Immagine | Generano o modificano immagini sintetiche a partire da descrizioni testuali (modelli a diffusione). |

### 6.2 I Foundation Model

Un *Foundation Model* è un modello di grandi dimensioni pre-addestrato su vastissimi dataset eterogenei, in grado di fungere da base comune ed essere adattato (*fine-tuned*) a molteplici task applicativi verticali (inclusi sistemi multimodali come VLM e VLA).

### 6.3 Invarianti ed Evoluzione dell'IA

| Cosa Resta | Cosa Cambia |
|---|---|
| Apprendimento guidato dai dati | Scala di dati, parametri e calcolo |
| Minimizzazione di una funzione Loss | Architetture (avvento del Transformer) |
| Discesa del gradiente come motore matematico fondamentale | Metodologie di allineamento/tuning |
| Principio iterativo di ottimizzazione | Modalità d'uso: RAG, Tool e Agenti |

> [!INFO] Ruolo della Dimensione dei Parametri
> L'incremento del numero di parametri conferisce al modello una maggiore capacità di rappresentazione geometrica e generalizzazione concettuale. Il modello non opera come un database deterministico, sebbene alcuni dati fattuali frequenti possano rimanere memorizzati nei pesi.

## VII. Sistemi Basati su Documenti e Sistemi Agentici

### 7.1 Integrazione di Fonti Esterne (RAG)

L'accesso diretto a documenti e fonti informative esterne (*Retrieval-Augmented Generation* - RAG) garantisce vantaggi strutturali critici:

- Rende la risposta generata verificabile, ispezionabile e controllabile.
- Consente l'aggiornamento dinamico delle conoscenze senza richiedere costosi riaddestramenti del modello.
- Riduce drasticamente le allucinazioni, ancorando le asserzioni a contesti documentali certi.

### 7.2 Flusso Fisso vs Sistema Agentico

> [!IMPORTANT] Differenza Fondamentale
> La discriminante tra un'architettura documentale convenzionale e un sistema agentico risiede nell'autonomia decisionale sui passi operativi.

**I. Architettura a Flusso Fisso (Pipeline Deterministica)**

I passaggi esecutivi sono rigidamente prefissati dal progettista del software (es. Cerca nel DB -> Inserisci nel Prompt -> Genera Risposta). Il flusso compie un unico passaggio deterministico, invariante rispetto alla complessità della richiesta.

**II. Sistema Agentico (*Agent Loop*)**

Nel sistema agentico è il modello stesso a pianificare dinamicamente la sequenza di azioni necessarie per completare un obiettivo articolato:

1. **Pianificazione (*Plan*):** Analizza l'obiettivo e stabilisce il sotto-task immediato.
2. **Utilizzo di Strumenti (*Tool Use* / *Action*):** Invoca *tool* esterni specializzati (motori di ricerca, interpreti Python, calcolatori, API).
3. **Osservazione (*Observation*):** Riceve e interpreta il risultato prodotto dallo strumento.
4. **Valutazione e Decisione (*Reflect & Decide*):** Valuta se i dati raccolti sono sufficienti; decide se iterare il ciclo invocando ulteriori strumenti o formulare la risposta finale.

> [!IMPORTANT] Principio Architetturale
> Un sistema informativo arricchito con accesso a basi di dati o documenti non costituisce necessariamente un agente. La natura agentica è determinata dalla capacità del modello di scegliere in autonomia percorsi, strumenti e criteri di arresto su più passi iterativi.

---
## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Introduzione_AI]]