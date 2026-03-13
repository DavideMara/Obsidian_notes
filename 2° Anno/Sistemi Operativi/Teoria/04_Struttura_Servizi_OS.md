---
date: 2026-03-04
tags:
  - teoriaSO
  - sistemi-operativi
type: lezione
---
# Struttura e Servizi del Sistema Operativo

## Componenti del Sistema di Elaborazione

> [!INFO] Appunti integrativi
> Questa prima parte della lezione richiama i concetti hardware fondamentali per comprendere come il Sistema Operativo gestisce le risorse.

Il sistema di elaborazione si basa su un'Unità Centrale e vari tipi di processori:
* **Microprocessore / CPU**: Può essere composto da un singolo o da molteplici core (multiprocessor). Utilizza la memoria **Cache** per velocizzare l'accesso ai dati.
* **Processore Grafico (GPU)**: Dotato di più core e memoria indipendente su un singolo chip o socket. 
> [!INFO] Nota hardware
> Rispetto a una CPU, la GPU ha una struttura più semplice ma è molto più veloce nel parallelizzare calcoli specifici, come quelli grafici.
* **Processore di Segnale Digitale (DSP)**: Sfrutta la tecnica SIMD (Single Instruction Multiple Data) per elaborare e codificare/decodificare segnali video e audio in tempo reale.

### Ciclo di Elaborazione e Interruzioni
L'esecuzione del codice avviene tramite il **Ciclo Fetch-Execute** (Estrai/Esegui), in cui le istruzioni vengono passate dalla memoria al processore e ai dispositivi di I/O.

> [!INFO] Gestione del flusso
> Il ciclo normale di esecuzione può essere sospeso tramite meccanismi specifici.

* **Interruzioni (Interrupts)**: Sospendono il normale ciclo di fetch/execute.
* **Timer**: Genera interruzioni a intervalli regolari, permettendo al sistema operativo di riprendere il controllo ed eseguire funzioni di gestione e supervisione.

---

## Servizi del Sistema Operativo

Il sistema operativo offre un ambiente per l'esecuzione dei programmi e fornisce servizi suddivisi in due categorie principali:

### 1. Servizi per l'Utente
* **Interfaccia Utente (UI)**: 
  * *Interfaccia Grafica (GUI)*: Approccio intuitivo tramite metafora della scrivania (icone, menu, touch-screen), sebbene non offra accesso a tutte le funzioni avanzate.
  * *Linea di Comando (CLI)*: Interprete che esegue comandi sequenziali, ideale per compiti ripetitivi tramite script.
  * *Batch*.
* **Esecuzione Programmi**: Gestisce caricamento, esecuzione e terminazione.
* **Operazioni di I/O**: Gestione della comunicazione con le periferiche.
* **File-System**: Permette creazione, cancellazione, lettura, scrittura e gestione dei permessi.
* **Comunicazione fra Processi (IPC)**: Avviene tramite condivisione di memoria o scambio di messaggi.
* **Rilevazione Errori**: Controllo su hardware, I/O e programmi.

### 2. Funzioni per l'Efficienza del Sistema
* **Allocazione delle Risorse**: Gestisce CPU, memoria, dischi e I/O per i vari processi.
* **Accounting**: Traccia l'uso delle risorse.
* **Protezione e Sicurezza**: Protezione controlla l'uso delle risorse, la sicurezza regola gli accessi al sistema dall'esterno.

> [!INFO] Riferimento Slide
> Passaggio ai concetti trattati nelle slide "03-servizi.pdf" (a partire da pag. 3).

---

## Chiamate di Sistema (System Calls)

Le system calls forniscono l'interfaccia di programmazione (API) ai servizi offerti dal kernel. Sono gestite dalle librerie di supporto run-time.
I parametri possono essere passati al sistema operativo in tre modi:
1. Tramite **Registri**.
2. In un **blocco/tabella in memoria**, il cui indirizzo viene caricato in un registro.
3. Tramite lo **Stack**, da cui il SO preleva i parametri tramite operazione di *pop*.

Le categorie principali includono: controllo dei processi, gestione dei file, gestione dispositivi I/O, gestione delle informazioni, comunicazioni e protezione.

---

## Struttura e Progettazione del Sistema Operativo

I moderni SO sono scritti principalmente in linguaggi ad alto livello come C o C++ per garantire compattezza e portabilità. Sezioni critiche restano in Assembler per la massima efficienza. Le architetture principali sono:

1. **Sistemi Monolitici**: Struttura non divisa in moduli formali. Tutte le funzioni risiedono in un unico grosso blocco (es. MS-DOS, UNIX tradizionale).
2. **Sistemi Stratificati (Layered)**: Struttura a livelli concentrici (dal Layer 0 dell'Hardware al Layer N della UI). Ogni livello nasconde i dettagli implementativi a quelli superiori. Vantaggio: facile debugging; Svantaggio: overhead prestazionale.
3. **Microkernel**: Trasferisce gran parte dei servizi a livello utente (server). La comunicazione avviene scambiando messaggi. Garantisce elevata affidabilità e portabilità, ma l'overhead di comunicazione è uno svantaggio.
4. **Moduli**: Il nucleo centrale (core) implementa solo le funzioni di base. Il resto delle funzionalità è diviso in moduli caricabili dinamicamente all'occorrenza, garantendo grande flessibilità.

---

## Generazione e Avvio del Sistema

Per implementare un SO si compila il codice sorgente, lo si configura in base all'hardware e lo si installa.
Il processo di accensione (**Boot**) segue questa catena:
1. L'esecuzione inizia da un indirizzo hardware predefinito in ROM contenente il **bootstrap loader**.
2. Questo micro-codice carica in memoria il **bootstrap program**.
3. A sua volta, quest'ultimo localizza e carica il **kernel** del SO, avviando il sistema.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Teoria_OS]]

-----