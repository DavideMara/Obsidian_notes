---
date: 2026-09-21
tags:
  - base-di-dati
type: lezione
---
# Introduzione alle Basi di Dati e ai DBMS

> [!INFO] Informazioni sul Corso e Modalità d'Esame
> * **Libro di Testo:** *Sistemi di Basi di Dati (Fondamenti)* — R. Elmasri, S. B. Navathe.
> * **Software Laboratorio:** PostgreSQL.
> * **Modalità d'Esame:** Due prove scritte intermedie (esoneri) che sostituiscono l'orale se superate con profitto (il voto finale è la media aritmetica):
>   * *1ª Prova Parziale:* 9 Novembre (11:30 - 13:30, indicativa).
>   * *2ª Prova Parziale:* 18 Novembre (08:30 - 10:30, indicativa).
>   * *Nota Orale:* Se all'esame scritto standard si ottiene una votazione $< 21$ o $> 27$, l'orale è obbligatorio.

---

## I. Definizioni Preliminari

* **Dato:** Insieme di fatti noti memorizzabili sul supporto fisico dotati di un significato implicito.
* **Base di Dati (Database - BD):** Una collezione strutturata di dati logicamente correlati e coerenti tra loro, aventi un significato intrinseco.

### Proprietà Implicite di una Base di Dati
1. **Rappresentazione del Mini-Mondo:** Rappresenta un frammento del mondo reale (detto *Universo del Discorso* o *Mini-Mondo*). Qualsiasi evento o modifica nel mini-mondo deve riflettersi tempestivamente sui dati memorizzati.
2. **Coerenza Logica:** I dati memorizzati non sono aggregazioni casuali, ma rispondono a vincoli e relazioni con semantica definita.
3. **Scopo Specifico:** Viene progettata, costruita e popolata con dati destinati a un gruppo prefissato di utenti e applicazioni target.

### Sistema di Gestione di Basi di Dati (DBMS)
Il **DBMS** (*Data Base Management System*) è un sistema software general-purpose che facilita i processi di definizione, costruzione, manipolazione e condivisione di basi di dati tra diversi utenti e applicazioni software.

$$\textbf{Sistema di Base di Dati} = \textbf{Base di Dati (Dati)} + \textbf{Software DBMS}$$

---

## II. Principali Funzioni di un DBMS

Un DBMS moderno assolve alle seguenti macro-funzionalità:

1. **Definizione della Base di Dati (DDL - Data Definition Language):** Specifica i tipi di dato, la struttura concettuale/logica e i vincoli di integrità da rispettare.
2. **Costruzione e Popolamento:** Memorizzazione fisica iniziale dei record sui dispositivi di memoria di massa gestita dal DBMS.
3. **Manipolazione della Base di Dati (DML / Query):**
   * *Interrogazione (Querying):* Estrazione di sottoinsiemi informativi mediante linguaggi dichiarativi (es. SQL).
   * *Aggiornamento:* Inserimento, cancellazione e modifica dei dati garantendo la consistenza.
   * *Accesso Applicativo:* Esposizione di API/connettori verso applicazioni esterne (es. Web App, servizi REST).
4. **Condivisione e Concorrenza:** Accesso contemporaneo a più utenti senza incorrere in inconsistenze, conflitti di scrittura o race condition.
5. **Protezione e Manutenzione:**
   * *Sicurezza e Controllo Accessi:* Prevenzione di accessi non autorizzati con autenticazione e permessi basati sui ruoli.
   * *Backup e Recovery:* Ripristino dello stato consistente della base di dati in caso di guasti hardware, crash software o interruzioni improvvise.
6. **Processing Attivo e Triggering:** Capacità del sistema di reagire autonomamente a eventi interni mediante regole attive e trigger.

> [!NOTE] Rappresentazione dei Dati
> Nelle basi di dati relazionali, i dati sono rappresentati concettualmente sotto forma di **tabelle** (relazioni), fondate rigorosamente sulla teoria matematica dei predicati e dell'algebra relazionale.

---

## III. Caratteristiche dell'Approccio a Base di Dati vs Approccio Tradizionale a File

Nel paradigma tradizionale basato su file (*File Processing System*), ciascun programma applicativo definisce e gestisce direttamente i propri file privati, causando forte ridondanza e dipendenza codice-dati. L'approccio a BD introduce 4 innovazioni strutturali:

### 1. Natura Autodescrittiva (Catalogo di Sistema)
Il sistema di BD non contiene soltanto i dati applicativi, ma anche la descrizione completa della loro struttura e dei relativi vincoli. Questa informazione prende il nome di **metadati** (o *Data Dictionary* / *Catalogo di Sistema*), ed è costantemente consultata dal DBMS durante l'esecuzione di qualsiasi operazione.

### 2. Astrazione dei Dati e Indipendenza Dati-Programmi
Nei sistemi a file tradizionali, la struttura fisica dei record è hardcoded all'interno del codice sorgente delle applicazioni. Con il DBMS:
* Viene fornita agli utenti una rappresentazione **concettuale/astratta** (modello dei dati), nascondendo i dettagli fisici di memorizzazione su disco (allocazione blocchi, ordinamento, indici).
* **Indipendenza dei Dati:** È possibile modificare lo schema fisico (o logico) di memorizzazione senza dover ricompilare o riscrivere i programmi applicativi che interrogano il database.

### 3. Supporto di Viste Multiple (Views)
Ciascuna categoria di utenti necessita di una diversa prospettiva sui dati. Una **Vista** è una tabella virtuale derivata dai dati effettivi che consente di:
* Isolare e mostrare solo i dati di competenza dell'utente.
* Mascherare informazioni riservate o non pertinenti.

### 4. Condivisione dei Dati e Gestione delle Transazioni Multi-Utente
Il DBMS garantisce che accessi concorrenti non generino anomalie. La gestione è basata sul concetto di **Transazione**: un'unità logica di lavoro che deve rispettare le proprietà **ACID** (*Atomicità, Consistenza, Isolamento, Durabilità*).

---

## IV. Utenti di un Sistema di Basi di Dati

Gli utenti interagenti con un ecosistema DBMS si dividono in due grandi classi:

```
                  ┌───────────────────────────────────────────────┐
                  │          UTENTI DI UN SISTEMA BD              │
                  └───────┬───────────────────────────────┬───────┘
                          │                               │
            ┌─────────────┴─────────────┐   ┌─────────────┴─────────────┐
            │      ATTORI DI SCENA      │   │    DIETRO LE QUINTE       │
            └─────────────┬─────────────┘   └─────────────┬─────────────┘
      ┌───────────────────┼───────────────────┐           │
      ▼                   ▼                   ▼           ▼
┌───────────┐       ┌───────────┐       ┌───────────┐ ┌───────────────────────┐
│ Database  │       │Progettisti│       │  Utenti   │ │Progettisti DBMS,      │
│Admin (DBA)│       │  di BD    │       │  Finali   │ │Sviluppatori di Tool,  │
└───────────┘       └───────────┘       └─────┬─────┘ │Personale Manutenzione │
                                              │       └───────────────────────┘
                     ┌──────────────┬─────────┴────────────┬─────────────┐
                     ▼              ▼                      ▼             ▼
               ┌───────────┐  ┌───────────┐          ┌───────────┐ ┌───────────┐
               │  Casuali  │  │Parametrici│          │Sofisticati│ │ Autonomi  │
               │ (Casual)  │  │ (Naïve)   │          │(Engineers)│ │(Standalone│
               └───────────┘  └───────────┘          └───────────┘ └───────────┘
```

### 1. Attori di Scena (Actors on the Scene)
Coloro che operano direttamente sulla base di dati e sui suoi contenuti applicativi:
* **Amministratore della Base di Dati (DBA - Database Administrator):**
  * Responsabile dell'accesso, concessione dei privilegi e sicurezza.
  * Monitoraggio delle performance, allocazione risorse e backup/recovery.
* **Progettisti della Base di Dati (Database Designers):**
  * Responsabili della modellazione concettuale (schema E-R), logica e fisica, nonché della definizione dei vincoli.
* **Utenti Finali (End Users):**
  * *Utenti Casuali (Casual Users):* Interrogano occasionalmente il DB con query ad-hoc complesse.
  * *Utenti Parametrici/Naïve:* Utilizzano transazioni predefinite e interfacce semplificate (es. cassieri, operatori di sportello, prenotazioni online).
  * *Utenti Sofisticati:* Ingegneri, scienziati e analisti che conoscono a fondo il DBMS e sviluppano analisi dati avanzate.
  * *Utenti Autonomi (Standalone):* Gestiscono basi di dati personali tramite pacchetti applicativi pronti.
* **Analisti di Sistema e Sviluppatori Software:** Progettano e implementano le applicazioni software che integrano le query e le transazioni.

### 2. Attori Dietro le Quinte (Workers Behind the Scene)
Coloro che non sono interessati ai dati specifici, ma creano l'infrastruttura software del DBMS:
* **Progettisti e Implementatori del DBMS:** Sviluppano i moduli interni (query engine, buffer manager, transaction manager).
* **Sviluppatori di Strumenti (Tool Developers):** Creano software ausiliari per la progettazione grafica (CASE tools), monitoraggio prestazioni e profilazione.
* **Operatori di Sistema e Personale di Manutenzione:** Gestiscono l'hardware, i server e l'ambiente operativo su cui gira il DBMS.

---

## V. Vantaggi e Scenari d'Uso del DBMS

### Vantaggi Principali
* **Controllo della Ridondanza:** Riduzione delle duplicazioni dei dati per evitare disallineamenti (*inconsistenza dei dati*). Quando necessaria, viene adottata una *ridondanza controllata*.
* **Controllo degli Accessi:** Protezione dei dati sensibili tramite autorizzazioni granulari.
* **Memorizzazione Persistente di Strutture Dati Complesse:** Salvataggio trasparente di oggetti e relazioni senza dover gestire la serializzazione manuale.
* **Query Processing e Indicizzazione:** Uso di strutture di accesso dedicate (come *B-Tree* o *Hash Table*) per velocizzare l'esecuzione delle ricerche su milioni di record.
* **Integrità Referenziale e Vincoli:** Applicazione automatica di regole semantiche (chiavi primarie, chiavi esterne, domini, check).
* **Economie di Scala:** Unificazione dei dati aziendali con riduzione dei costi di gestione e sviluppo.

> [!WARNING] Quando NON Conviene Usare un DBMS
> L'impiego di un DBMS introduce overhead di costo, complessità computazionale e requisiti hardware. È sconsigliato in presenza di:
> * Sistemi con requisiti *real-time* strettissimi e vincoli temporali stringenti non compatibili con l'overhead del DBMS.
> * Basi di dati mono-utente a struttura fissa senza necessità di accessi concorrenti o sicurezza avanzata.
> * Risorse hardware e memoria estremamente limitate (es. microcontrollori embedded).

---

## VI. Cenni Storici ed Evoluzione dei Modelli di Dati

* **Anni '60 - '70 (Sistemi Gerarchici e Reticolari):**
  * Primi sistemi su mainframe aziendali/bancari (es. IMS di IBM).
  * *Limite critico:* Forte commistura tra legami concettuali e strutture fisiche di memorizzazione (puntatori espliciti su disco); modifiche fisiche richiedevano la riscrittura del codice applicativo.
* **1970 - La Rivoluzione Relazionale (Edgar F. Codd):**
  * Pubblicazione del fondamentale paper *"A Relational Model of Data for Large Shared Data Banks"* (CACM 1970).
  * Introduzione del modello relazionale basato su tabelle e logica matematica, garantendo totale indipendenza tra logica e memorizzazione fisica.
* **Anni '80 (RDBMS e Basi di Dati a Oggetti):**
  * Affermazione commerciale di RDBMS e linguaggio standard **SQL** (Oracle, IBM DB2).
  * Nascita delle basi di dati a oggetti (*OODBMS*) per gestire tipi strutturati complessi della programmazione OOP.
* **Anni '90 - Presente (Web, XML, NoSQL e Big Data):**
  * Integrazione con il Web, commercio elettronico e standard XML/JSON.
  * Sistemi di *Data Warehousing*, *Data Mining*, basi di dati NoSQL per grandi moli di dati e sistemi ibridi di Information Retrieval.

---

## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Base_di_Dati]]
