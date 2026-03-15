---
date: 2026-03-04
tags:
  - teoriaSO
  - sistemi-operativi
type: lezione
---
# Architettura e Servizi del Sistema Operativo

Lo sviluppo e la struttura di un sistema operativo ruotano attorno ad alcuni aspetti cardine: la gestione dei processi e della memoria, la protezione e la sicurezza dell'informazione, oltre alla schedulazione e alla gestione efficiente delle risorse. 
A livello strutturale, i sistemi operativi moderni adottano diversi approcci avanzati per garantire robustezza e scalabilità. Tra questi troviamo l'architettura microkernel, il multithreading per ottimizzare i processi concorrenti, il multiprocessing simmetrico (SMP) per sfruttare architetture hardware multi-core e logiche orientate agli oggetti che favoriscono la modularità e la manutenibilità del codice del kernel.

## 1.Servizi per l'utente

Il sistema operativo mette a disposizione diverse interfacce per permettere all'utente di accedere in modo intuitivo o programmatico alle funzionalità del sistema.  Le principali categorie includono:

* **GUI (Graphical User Interface):** Un'interfaccia grafica visiva e intuitiva basata su finestre, icone e puntatori (es. ambiente Windows o ambienti desktop Linux).
* **Command Line (CLI):** Un'interfaccia a riga di comando, testuale e più diretta, spesso preferita per operazioni amministrative, di sviluppo e per un controllo più preciso del sistema.
* **Batch:** Sistemi progettati per l'esecuzione automatizzata di script o lavori a lotti (batch jobs) senza la necessità di un'interazione continua da parte dell'utente.
* **Macchine Virtuali:** Una funzionalità avanzata in cui il sistema operativo permette la creazione e l'isolamento di macchine virtuali, ciascuna dotata della propria memoria e di un proprio sistema operativo "guest". Un componente software cruciale, chiamato Virtual Machine Monitor (VMM) o Hypervisor, gestisce in sicurezza le comunicazioni e l'isolamento tra questi sistemi operativi virtuali e l'hardware fisico sottostante. 
---
## 2. Le System Call (Chiamate di Sistema)

Le chiamate di sistema forniscono un'interfaccia per il programmatore ai servizi messi a disposizione dal sistema operativo. * Vi si accede attraverso un'API gestita dalla libreria di supporto run-time, la quale nasconde i complessi dettagli implementativi al programmatore.
* I parametri vengono passati al sistema operativo in tre modi principali:
	* Tramite i registri.
	* Inseriti in un blocco o in una tabella di memoria (il cui indirizzo viene passato in un registro).
	* Inseriti nello stack del programma, da cui vengono prelevati (pop) dal sistema operativo.

### Categorie di Chiamate di Sistema

* **Controllo dei processi:** Creazione e arresto; caricamento ed esecuzione; terminazione normale e anormale; esame e impostazione degli attributi. Include anche funzioni per mettere in pausa il processo (es. per un tempo indicato in attesa di un input a scadenza) e l'attesa/segnalazione di un evento. Consente inoltre l'assegnazione e il rilascio di memoria, poiché il processo solitamente non carica in RAM tutta la memoria disponibile, ma solo lo stretto *necessario*.
* **Gestione dei file:** Creazione e cancellazione; apertura, chiusura, lettura, scrittura e posizionamento. Permette l'esame e l'impostazione degli attributi, come ad esempio i permessi di lettura e scrittura assegnati al proprietario, al gruppo e a tutti gli utenti.
* **Gestione dei dispositivi I/O:** Richiesta e rilascio; lettura, scrittura e posizionamento; esame e impostazione degli attributi; inserimento ed esclusione logica.
* **Gestione delle informazioni:** Esame e impostazione dell'ora, della data e dei dati di sistema. Esame e impostazione degli attributi di processi, file e dispositivi.
* **Comunicazione:** Creazione e chiusura di una connessione, come le pipe, invio e ricezione di messaggi, e accesso a regioni di memoria condivisa. Include informazioni sullo stato dei trasferimenti e inserimento/esclusione di dispositivi remoti.
* **Protezione:** Controllo degli accessi alle risorse, visualizzazione/impostazione dei permessi e autorizzazione/divieto di accesso all'utente.

---

## 3. Programmi di Sistema (Utilities)

Un sistema operativo è fatto anche di programmi di sistema che servono a realizzare l'ambiente utile per lo sviluppo e l'esecuzione dei programmi applicativi.
Le principali categorie includono:
* Gestione files e Informazioni di stato.
* Modifica dei file, come i text editor.
* Supporto alla programmazione, ovvero i tool necessari per la compilazione, il linker e il debugger.
* Caricamento ed esecuzione dei programmi.
* Comunicazioni e servizi in background.

---

## 4. Progettazione del Sistema Operativo

In fase di progettazione è necessario definire obiettivi e specifiche, considerando l'hardware e il tipo di sistema da utilizzare. Bisogna bilanciare gli obiettivi dell'utilizzatore con quelli del sistema. Ad esempio, l'utilizzatore vuole che i propri programmi terminino nel minor tempo possibile, mentre l'obiettivo del sistema potrebbe essere non lasciare mai il processore inutilizzato.

È fondamentale la **separazione delle politiche dai meccanismi**: bisogna tenere separato *come* si fa una cosa, ovvero il meccanismo, dal *quando/chi* la fa, ovvero la politica. Ad esempio, il meccanismo può essere l'accesso al disco, mentre la politica è la scelta di servire le richieste FIFO.

In merito all'implementazione, i moderni OS sono scritti quasi interamente in linguaggi d'alto livello, come C o C++, per garantire facilità di sviluppo, manutenzione, compattezza e portabilità. Le sezioni critiche per l'efficienza restano in Assembler.

---

## 5. Strutture del Sistema Operativo

Esistono diverse architetture per strutturare un sistema operativo: 
* **Sistemi Monolitici:** Non sono divisi in moduli chiari. Esempi classici sono MS-DOS e lo UNIX tradizionale. Sono complessi: il nucleo ha un'interfaccia verso l'hardware per gestire le system call all'interno di un unico programma (kernel) che gestisce segnali I/O, file system e driver.
* **Sistemi Stratificati:** L'OS è diviso in layer. Ogni strato è l'implementazione di un oggetto astratto che nasconde i dettagli implementativi agli strati superiori. Questo porta vantaggi in termini di semplicità di scrittura, aggiornamento, debugging e portabilità. Lo svantaggio principale è la difficoltà nel definire rigorosamente gli strati. 
* **Microkernel:** Il nucleo fa il minimo indispensabile. Il grosso dei servizi viene trasferito a programmi utente-layer (server), e le richieste avvengono tramite scambio di messaggi tra client e server. Questo migliora l'aggiornamento e l'affidabilità, ma genera uno svantaggio in termini di *overhead*: il tempo di esecuzione aumenta perché il kernel deve gestire la comunicazione continua verso i programmi utente-server. 

> [!INFO] Recupero Appunti: I Moduli
> * **Moduli:** In questo approccio, il nucleo contiene solo le funzioni fondamentali. Le altre funzionalità risiedono in moduli che vengono caricati e collegati solo all'occorrenza, nascondendo i dettagli implementativi tra loro.

---

## 6. Debugging e Generazione del Sistema Operativo

Nella progettazione, il **debugging**, ossia la ricerca di errori e problemi di prestazione, è fondamentale. Gli OS sono sistemi estremamente complessi ed è normale che emergano errori che compaiono solo in situazioni particolari. Valutare le prestazioni richiede molta sperimentazione, supportata dalla generazione di *log files* per registrare il comportamento del sistema, dai *core dump* e dal monitoraggio continuo.

**Generazione e Avvio:**
Una volta scritto, il codice sorgente va compilato e configurato specificamente per il sistema su cui girerà. La configurazione si realizza modificando il codice pre-compilazione, usando tabelle e moduli precompilati, o affidandosi a un sistema guidato da tabelle. 
Per l'avvio, l'esecuzione inizia in un indirizzo predefinito della memoria ROM (non volatile), contenente il *bootstrap loader*. Questo programma base carica le istruzioni del *bootstrap program*, che a sua volta carica il kernel e avvia l'esecuzione vera e propria del sistema operativo.

---

## 7. I Processi

Un **processo (o job)** è, per definizione, un *programma in esecuzione*.
È importante distinguere: il programma è un'entità passiva, ovvero il file eseguibile su disco. Invece il processo è l'entità attiva, dotata di Program Counter e risorse associate. Nota bene: un singolo programma può essere associato a più processi eseguiti in parallelo.

Un processo in memoria è dotato di diverse sezioni: * **Program Counter e Registri:** Rappresentano l'immagine attuale del processore, indicando l'indirizzo della prossima istruzione da eseguire.
* **Stack:** Contiene i dati temporanei, come variabili locali, indirizzi di return e parametri delle funzioni. Cresce verso il basso man mano che si richiamano nuove funzioni.
* **Sezione Dati:** Dedicata alle variabili globali.
* **Sezione Testo:** Contiene il programma vero e proprio.
* **Heap:** Spazio riservato per l'allocazione dinamica della memoria, ad esempio con `malloc`. A differenza dello stack, l'heap si espande verso l'alto. Il sistema deve vigilare affinché stack e heap non collidano.

> [!INFO] Approfondimento: Stati del Processo
> Un processo attraversa diversi stati durante il suo ciclo di vita: 1. **Nuovo (New):** Il processo è in fase di creazione.
2. **Pronto (Ready):** Il processo attende l'assegnazione e la disponibilità della CPU.
3. **In esecuzione (Running):** Il processore sta attivamente eseguendo le sue istruzioni. Ad esempio, in UNIX, il processore può togliere l'esecuzione al processo per lo scadere del suo "time slice", rimandandolo in coda.
4. **In attesa (Waiting):** Il processo è fermo in attesa che si verifichi un evento, come un'operazione di I/O.
5. **Terminato (Terminated):** Il processo ha completato la sua esecuzione.

### Il Descrittore di Processo (PCB) e il Context Switch

Ad ogni processo è associata una struttura dati chiamata **PCB (Process Control Block)**. Contiene tutte le informazioni vitali del processo:
* Stato del processo
* Program counter
* Registri della CPU
* Parametri per lo scheduling
* Informazioni sulla memoria e sull'I/O

Quando avviene un interrupt o una system call, il sistema operativo deve fermare il processo in esecuzione, come P0, per passare a un altro, come P1. Questo avviene effettuando il salvataggio dello stato attuale all'interno del PCB0 e successivamente ricaricando lo stato dal PCB1, prima di rimettere il sistema in esecuzione. 

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Teoria_OS]]