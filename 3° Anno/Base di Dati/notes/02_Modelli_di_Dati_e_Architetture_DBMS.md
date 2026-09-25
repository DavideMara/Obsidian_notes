---
date: 2026-09-25
tags:
  - base-di-dati
type: lezione
---
# Modelli di Dati e Architetture di un Sistema di Basi di Dati

## I. Modelli dei Dati

Un **modello dei dati** e' un insieme di concetti per descrivere:

- la **struttura** di una base di dati, cioe' i tipi di dato, le associazioni tra i dati e i vincoli;
- le **operazioni** che possono essere eseguite sulla base di dati, come ricerche, inserimenti, aggiornamenti e cancellazioni.

Alcuni modelli consentono inoltre di specificare il comportamento dinamico della base di dati, associando dati e operazioni. Nel modello relazionale, per esempio, questo avviene tramite trigger e stored procedure.

> [!IMPORTANT] Struttura e comportamento
> Il modello dei dati non si limita a descrivere "che cosa" viene memorizzato, ma puo' specificare anche "come" i dati possono essere interrogati e modificati.

### Categorie di modelli dei dati

| Categoria | Caratteristiche |
| --- | --- |
| **Modelli concettuali o di alto livello** | Usano concetti vicini al modo in cui gli utenti finali percepiscono i dati e descrivono la struttura a un elevato livello di astrazione. |
| **Modelli implementabili** | Offrono concetti comprensibili agli utenti, ma sufficientemente vicini all'organizzazione dei dati nel calcolatore. Nascondono alcuni dettagli fisici e possono essere implementati direttamente. |
| **Modelli fisici o di basso livello** | Descrivono direttamente dettagli di organizzazione e accesso ai dati sul supporto di memorizzazione. |

La differenza fra le categorie riguarda il **grado di astrazione** rispetto all'organizzazione fisica della base di dati.

---

## II. Schemi, Istanze e Stati della Base di Dati

Indipendentemente dal modello adottato, e' importante distinguere la descrizione della base di dati dai dati effettivamente memorizzati.

### Schema e costrutti

- Lo **schema della base di dati** e' la descrizione della struttura della base di dati ed e' specificato durante la progettazione.
- Il **diagramma dello schema** e' una rappresentazione grafica dello schema, ma puo' mostrare soltanto alcuni dei suoi aspetti.
- Un **costrutto di schema** e' un singolo oggetto descritto dallo schema, per esempio uno studente, un corso o la relazione che li collega.

### Istanze e stato della base di dati

Lo **stato della base di dati** e' l'insieme dei dati presenti in un particolare istante temporale. Lo stato e' anche detto **istanza** della base di dati.

Ogni costrutto dello schema possiede un proprio insieme corrente di istanze. Il costrutto `Studente`, ad esempio, ha come istanze i singoli record che rappresentano gli studenti presenti in un dato momento.

| Concetto | Schema | Stato o istanza |
| --- | --- | --- |
| Contenuto | Descrizione della struttura | Dati memorizzati in un istante |
| Stabilita' | Cambia raramente | Cambia a ogni aggiornamento |
| Sinonimo | **Intensione** | **Estensione** |
| Esempio | Entita', attributi e relazioni definiti nel progetto | Studenti iscritti in un determinato giorno |

### Stati iniziale e valido

- Lo **stato iniziale** e' lo stato della base di dati quando essa viene popolata per la prima volta o caricata con i dati iniziali.
- Lo **stato valido** e' uno stato che rispetta la struttura e i vincoli definiti nello schema.

> [!EXAMPLE] Schema e istanza
> Schema: la base contiene un'entita' `Corso` con gli attributi `Codice` e `Nome`, oltre a una relazione `Iscrizione` che la collega a `Studente`.
>
> Istanza: in un dato momento la base contiene tre corsi e venti studenti, con un insieme specifico di iscrizioni. Un nuovo studente modifico' lo stato, ma non lo schema.

> [!WARNING] Schema logico e diagramma
> Il diagramma e' una rappresentazione parziale dello schema. Non deve quindi essere confuso con lo schema completo, che puo' includere ulteriori elementi non visualizzati nel grafico.

---

## III. Architettura a Tre Livelli

L'architettura a tre livelli organizza un DBMS in modo da supportare l'**indipendenza dei dati** e le **viste multiple** sugli stessi dati.

```text
+----------------------------------------------------------------+
|                        SCHEMA ESTERNO                          |
|        Viste dedicate a utenti e applicazioni diverse          |
+----------------------------------------------------------------+
                              |
                 mappatura esterno/concettuale
                              v
+----------------------------------------------------------------+
|                      SCHEMA CONCETTUALE                        |
|      Struttura logica della base di dati e relativi vincoli   |
+----------------------------------------------------------------+
                              |
                 mappatura concettuale/interno
                              v
+----------------------------------------------------------------+
|                       SCHEMA INTERNO                           |
|      Organizzazione fisica, accesso ai dati e indici strutturati  |
+----------------------------------------------------------------+
```

### Livello esterno

Descrive le **viste** offerte agli utenti e alle applicazioni. Ogni vista puo' mostrare solo una parte dei dati, adottando nomi, attributi e operazioni utili a un specifico contesto. Gli schemi esterni utilizzano generalmente gli stessi modelli dello schema concettuale.

### Livello concettuale

Descrive la struttura e i vincoli della base di dati per una comunita' di utenti. E' il livello di astrazione piu' elevato dell'architettura e puo' essere descritto mediante un modello concettuale o implementabile.

### Livello interno

Descrive la memorizzazione fisica dei dati e le strutture utilizzate per accedervi, come file, pagine, organizzazioni dei record e indici. Viene descritto mediante un modello fisico.

### Trasformazione tra i livelli

Il DBMS realizza le operazioni di **mappatura** tra i livelli:

- le richieste formulate rispetto allo schema esterno o concettuale vengono tradotte in operazioni sullo schema interno;
- i dati recuperati dal livello interno vengono riformattati per corrispondere alla vista esterna richiesta, per esempio trasformando il risultato di una query SQL nel formato di una pagina web.

> [!WARNING] Architettura a tre livelli e architettura client/server a tre livelli
> I due concetti non sono equivalenti. Il primo descrive i tre livelli di astrazione dello schema; il secondo distribuisce il software tra client, server applicativo e server della base di dati.

---

## IV. Indipendenza dei Dati

L'indipendenza dei dati permette di modificare un livello dello schema senza propagare la modifica ai livelli superiori e alle applicazioni che li utilizzano.

| Tipo di indipendenza | Livello modificato | Livelli che non devono cambiare |
| --- | --- | --- |
| **Indipendenza fisica** | Schema interno | Schema concettuale ed esterni |
| **Indipendenza logica** | Schema concettuale | Schemi esterni e programmi applicativi |

### Indipendenza fisica

Consiste nella capacita' di modificare lo schema interno senza modificare lo schema concettuale. Ad esempio, l'aggiunta di un indice puo' cambiare il modo in cui i dati vengono fisicamente organizzati e recuperati, senza alterare la struttura logica osservata dalle applicazioni.

### Indipendenza logica

Consiste nella capacita' di modificare lo schema concettuale senza modificare gli schemi esterni e i programmi applicativi associati. Le nuove caratteristiche possono essere rese disponibili attraverso nuove viste, mentre le interfacce esistenti continuano a funzionare.

Quando uno schema viene modificato a un livello piu' basso, devono essere aggiornate soltanto le mappature verso i livelli superiori. Quest ultimi e i programmi che li utilizzano possono restare invariati.

> [!EXAMPLE] Indipendenza fisica
> Si decide di riorganizzare i file su disco e di aggiungere un indice B-tree. Lo schema interno cambia, ma il modello concettuale delle tabelle e tutte le query applicative restano invariati.

---

## V. Linguaggi e Interfacce del DBMS

### Data Definition Language (DDL)

Il **DDL** (*Data Definition Language*) permette di specificare lo schema della base di dati. E' utilizzato soprattutto dagli amministratori e dai progettisti.

- Definisce strutture, attributi, tipi di dato, relazioni e vincoli.
- In molti DBMS definisce anche schemi interni ed esterni.
- In alcuni sistemi sono presenti linguaggi specifici: **SDL** per lo schema interno e **VDL** per gli schemi esterni.

### Data Manipulation Language (DML)

Il **DML** (*Data Manipulation Language*) specifica interrogazioni e aggiornamenti della base di dati.

I comandi possono essere:

- eseguiti direttamente tramite un linguaggio di interrogazione;
- incorporati in un linguaggio ospite come C, C++ o Java;
- utilizzati attraverso librerie che forniscono le funzioni di accesso al DBMS.

#### Linguaggi di alto livello o non procedurali

Sono **dichiarativi** e indicano quale risultato ottenere, senza specificare passo per passo come raggiungerlo. SQL e' l'esempio principale. Sono inoltre orientati agli insiemi (*set-oriented*): una singola operazione puo' operare su piu' record.

#### Linguaggi di basso livello o procedurali

Descrivono le operazioni da eseguire. Sono tipicamente orientati ai record e richiedono costrutti di loop e puntatori per raggiungere ed elaborare un insieme di record.

| Tipo | Specifica | Accesso ai dati |
| --- | --- | --- |
| **Non procedurale** | Il risultato desiderato | Orientato agli insiemi |
| **Procedurale** | La sequenza di operazioni | Record per record |

### Interfacce per l'accesso al DBMS

| Tipo di interfaccia | Funzione |
| --- | --- |
| **Interfaccia stand-alone** | Consente di immettere direttamente query in un linguaggio dichiarativo. |
| **Linguaggio incorporato** | Integra il DML in un linguaggio ospite, come embedded SQL per C/C++ o SQLJ per Java. |
| **API** | Espone funzioni di accesso; esempi: ODBC per diversi linguaggi e JDBC per Java. |
| **Linguaggio nativo del DBMS** | Integra SQL e programmazione strutturata, come PL/SQL per Oracle e PL/pgSQL per PostgreSQL. |
| **Interfacce user-friendly** | Offrono menu, form, controlli grafici, comandi *point-and-click* o interfacce basate su linguaggio naturale. |
| **Interfacce parametriche** | Sono usate da applicazioni che avviano operazioni predefinite, come prenotazioni o ordini. |
| **Interfacce per il DBA** | Gestiscono account, autorizzazioni, parametri di sistema, schemi e cammini di accesso ai dati. |

Sono possibili anche interfacce basate su browser web e input o output vocale.

---

## VI. Ambiente di Esecuzione del Sistema di Basi di Dati

### Architettura centralizzata

In un'architettura centralizzata, software DBMS, programmi applicativi, interfacce utente e risorse di elaborazione sono concentrati in un unico sistema. Gli utenti possono collegarsi anche da postazioni remote, ma le operazioni vengono eseguite centralmente.

### Architettura client/server

Nell'architettura client/server, i server sono specializzati in funzioni specifiche. Esempi sono server di stampa, file, DBMS, web ed email. Molteplici client forniscono all'utente le interfacce necessarie e accedono ai servizi attraverso una rete, locale o wireless.

#### Configurazione a due livelli per un DBMS

```text
+--------------------------------+       API       +------------------+
|           Client              | <-------------> |    DBMS Server   |
| Programma applicativo e UI    |  ODBC / JDBC    | Query e trans.   |
+--------------------------------+                 +------------------+
```

Il server gestisce tipicamente le funzionalita' transazionali e l'elaborazione delle interrogazioni. Nel caso di un RDBMS, e' spesso denominato server SQL, server delle interrogazioni o server delle transazioni. I programmi sul client accedono al DBMS tramite API come ODBC e JDBC.

La divisione del software non e' univoca. Il server puo' occuparsi della memorizzazione su pagine e della gestione di buffer e cache; il client puo' gestire il dizionario dei dati, l'integrazione con i compilatori e l'ottimizzazione globale delle interrogazioni.

#### Configurazione a tre livelli per applicazioni web

```text
+-------------+       HTTP       +----------------------+       SQL
|   Browser   | <--------------> | Server applicativo   | <--------------> | DBMS Server |
|   Client    |                  | o Web Server         |                  |              |
+-------------+                   +----------------------+                  +--------------+
```

Il server applicativo:

- contiene le regole aziendali, le procedure e i vincoli applicativi per l'accesso ai dati;
- trasmette dati parzialmente elaborati tra client e server della base di dati;
- puo' verificare le credenziali del client prima di inoltrare la richiesta al DBMS, riducendo l'esposizione diretta del server della base di dati.

---

## VII. Classificazione dei DBMS

Un DBMS puo' essere classificato secondo criteri diversi:

- **modello dei dati:** gerarchico, reticolare, relazionale, orientato agli oggetti o relazionale a oggetti;
- **distribuzione della base di dati:** centralizzata o distribuita;
- **ambito d'uso:** *general purpose* oppure *special purpose*;
- **costo e destinazione d'uso:** sistemi di fascia differente, orientati a impieghi specifici.

La classificazione per modello dei dati e' quella approfondita nella parte seguente.

---

## VIII. Modelli dei Dati: Classificazione Storica

### Modello gerarchico

Il modello gerarchico rappresenta i dati mediante una **struttura ad albero**. Da un record padre si accede ai record figli da cui dipende, secondo regole fissate dalla gerarchia.

Fu sviluppato nella prima fase dei DBMS, negli anni Sessanta, e fu implementato da IBM e North American Rockwell intorno al 1965. Non esiste un linguaggio standard per questo modello; un DML diffuso era DL/1 del sistema IMS.

**Vantaggio**

- Rappresenta bene domini che presentano una naturale gerarchia.

**Svantaggi**

- La struttura ad albero impone regole rigide su aggiornamenti e interrogazioni.
- Un record ha una sola posizione nella gerarchia, quindi la dipendenza dei programmi dalla struttura e' elevata.
- Le relazioni many-to-many (*N:M*) non sono rappresentate in modo efficiente.
- Le relazioni piu' generiche possono richiedere l'introduzione di dati duplicati.
- L'ottimizzazione automatica delle query e' limitata.

### Modello reticolare

Il modello reticolare deriva dalla struttura gerarchica e rappresenta i dati come **record collegati mediante puntatori**. Un record puo' avere piu' record padri ed essere raggiunto da piu' direzioni.

Il primo DBMS reticolare fu implementato da Honeywell nel 1965 con IDS. Il modello fu sostenuto dal rapporto CODASYL DBTG del 1971 e fu alla base di sistemi come IDMS, DMS 1100, IMAGE e VAX-DBMS.

**Vantaggi**

- La molteplicita' di padri riduce la necessita' di duplicare i dati.
- Ogni nodo puo' fungere da punto di partenza per raggiungere un campo.
- Le relazioni *N:M* possono essere modellate.

**Svantaggi**

- La base di dati contiene un complesso reticolo di puntatori.
- La struttura e' fortemente legata ai programmi che la utilizzano.
- L'ottimizzazione automatica delle query e' limitata.

> [!IMPORTANT] Gerarchico e reticolare
> Il modello gerarchico ammette soltanto una relazione padre-figlio per ciascun livello. Il modello reticolare supera questo limite consentendo collegamenti multipli e una navigazione piu' flessibile, al costo di una struttura di puntatori piu' complessa.

### Modello relazionale

Il modello relazionale fu proposto nel 1970 da **Edgar F. Codd** di IBM. I primi sistemi commerciali comparirono intorno al 1981-1982 e portarono alla diffusione di prodotti quali DB2, Oracle, Microsoft SQL Server, Informix e Sybase.

La standardizzazione di SQL ha seguito un processo evolutivo che comprende SQL-89 (SQL-1), SQL-92 (SQL-2) e SQL:1999. Il modello relazionale e' quello dominante nello sviluppo commerciale di basi di dati.

### Modello orientato agli oggetti

Il modello orientato agli oggetti descrive la base di dati mediante **oggetti, proprieta' e operazioni associate**. Incorpora caratteristiche del paradigma object-oriented, come tipi di dati astratti, incapsulamento ed ereditarieta'.

Gli OODBMS iniziarono a diffondersi alla fine degli anni Ottanta. Inizialmente considerati concorrenti dei sistemi relazionali, non hanno raggiunto la stessa diffusione di questi ultimi.

### Modello relazionale a oggetti

Il modello relazionale a oggetti e' un approccio ibrido: un RDBMS incorpora concetti provenienti dal paradigma orientato agli oggetti, mantenendo il modello relazionale come base. Nel materiale sono indicati Informix Universal Server, Oracle, DB2 e PostgreSQL; SQL:1999 introduce estensioni orientate agli oggetti.

### Confronto sintetico

| Modello | Organizzazione dei dati | Caratteristica distintiva | Limite principale |
| --- | --- | --- | --- |
| Gerarchico | Albero | Accesso da padre a figli | Regole rigide e relazioni *N:M* difficili |
| Reticolare | Grafo di record | Piu' collegamenti e padri | Complessita' dei puntatori |
| Relazionale | Tabelle e relazioni | Indipendenza logica e standard SQL | Richiede adattamento ad applicazioni molto complesse |
| Orientato agli oggetti | Oggetti con proprieta' e comportamenti | Incapsulamento ed ereditarieta' | Minore diffusione storica rispetto al relazionale |
| Relazionale a oggetti | Ibrido relazionale e object-oriented | Tipi complessi ed estensioni object-oriented | Integrazione meno uniforme tra prodotti |

> [!NOTE] Contesto storico del materiale
> Le slide risalgono al 2010. Le indicazioni sulla diffusione degli OODBMS e i prodotti citati descrivono la situazione illustrata dal docente e non costituiscono una valutazione aggiornata del mercato attuale.

---

## Navigazione Lezioni

- **Index Corso:** [[00_Index_Base_di_Dati]]
