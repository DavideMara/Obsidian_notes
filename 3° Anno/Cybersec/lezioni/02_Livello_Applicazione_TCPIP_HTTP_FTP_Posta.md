---
date: 2026-09-28
tags:
  - sicurezza-informatica
type: lezione
---
# Livello di Applicazione: TCP/IP, HTTP, FTP e Posta Elettronica

Prima di entrare nel merito degli attacchi, la lezione del 28/09 chiude il richiamo funzionale delle reti: senza il modello a strati e la conoscenza dei protocolli applicativi non si può capire *dove* un attaccante si inserisce e *cosa* intercetta. L'obiettivo e quindi duplice: (1) ricostruire il funzionamento dello stack TCP/IP come strumento di analisi, (2) evidenziare i difetti di progetto che rendono i protocolli originari fragili dal punto di vista della sicurezza.

> [!INFO] Esercizi e domande per casa
> Le 7 consegne assegnate dal prof durante questa lezione (3 teoriche e 4 pratiche di laboratorio) sono raccolte e sviluppate in [[Esercizi#Lezione 02 - Livello di Applicazione (28/09/2026)|Esercizi]]. Nella nota teorica resta solo il rimando al punto corrispondente.

---

## 1. Richiamo Preliminare: lo Standard TCP/IP

> [!IMPORTANT] Definizione di protocollo
> Un protocollo di rete definisce il **formato** e l'**ordine** dei messaggi scambiati tra due o più entità in comunicazione, oltre alle **azioni** intraprese in fase di trasmissione o ricezione di un messaggio.

Tre idee portanti che il prof ha ribadito:

* **Lo standard crea un canale virtuale.** La modalita di comunicazione non cambia con la distanza fisica: due host a pochi metri e due host in continenti diversi interagiscono attraverso le stesse regole formali. La distanza e solo un parametro di ritardo, non di semantica.
* **L'host non deve preoccuparsi del percorso.** Con l'architettura client/server l'host ragiona esclusivamente sull'interazione applicativa, affidandosi allo standard di comunicazione sottostante per instradare, frammentare e riassemblare.
* **Tutta l'attivita di Internet e governata dai protocolli.** Non esiste un "collegamento magico": ogni servizio funziona perche esiste una specifica precisa (spesso una RFC) che ne definisce il comportamento.

```
   HOST A                                                      HOST B
  +--------+          protocollo applicativo (HTTP)          +--------+
  | client | ----------------------------------------------> | server |
  +--------+ <---------------------------------------------- +--------+
        ^  la specifica ASTRAE il canale logico,
        |  il mezzo fisico e solo il supporto
     [ rete: router, switch, mezzi trasmissivi ]
```

---

## 2. La Pila di Protocolli TCP/IP

Il focus del corso e sui tre livelli superiori: **applicazione**, **trasporto**, **rete**.

### 2.1 Perche stratificare

Le reti sono sistemi complessi (host, router, molteplici mezzi trasmissivi, applicazioni, protocolli, hardware e software). La stratificazione risponde a due esigenze:

* **Analisi:** una struttura esplicita consente di identificare i componenti e le loro inter-relazioni, semplificando lo studio del sistema.
* **Modularizzazione e manutenzione:** le modifiche implementative a un livello sono **trasparenti** agli altri. Si puo sostituire il protocollo di trasporto (es. passare da TCP a UDP) senza riscrivere l'applicazione.

> [!WARNING] Il modello a strati e dannoso?
> Si potrebbe obiettare che la stratificazione introduca overhead (ogni livello aggiunge intestazioni) e complessita. Il contropeso e la modularita: un protocollo che non funziona puo essere sostituito senza impattare sui livelli circostanti. In ambito sicurezza, la stratificazione e anche un vantaggio difensivo: e possibile predisporre controlli a livello di link (IDS), trasporto (IPSec/TLS) e applicazione (WAF, validazione dei messaggi) in modo indipendente.

### 2.2 I cinque livelli

| Livello TCP/IP | Funzione | Protocolli | PDU |
|---|---|---|---|
| **Applicazione** | Supporto alle applicazioni di rete | HTTP, HTTPS, FTP, SMTP, DNS | **messaggio** |
| **Trasporto** | Trasferimento dei messaggi fra processo client e processo server | TCP, UDP | **segmento** / datagramma |
| **Rete** | Instradamento dei datagrammi dall'origine al destinatario | IP, protocolli di instradamento | **datagramma** |
| **Collegamento (link)** | Instradamento dei datagrammi attraverso una serie di commutatori | Ethernet, PPP | **frame** |
| **Fisico** | Trasferimento dei singoli bit sul mezzo | - | **bit** |

> [!NOTE] Nota del Prof
> In colloquio informatico con "pacchetto" si intende in modo generico **qualsiasi unità di dati**. Tecnicamente, la stessa informazione prende nomi diversi a seconda del livello in cui la si osserva: messaggio (applicazione), segmento (trasporto con TCP), datagramma (rete), frame (collegamento). E la stessa informazione che cambia nome passando per la pila, non un oggetto diverso.

### 2.3 Incapsulamento

Ogni livello aggiunge la propria intestazione ai dati ricevuti dal livello superiore: e il meccanismo di **incapsulamento** (e la sua inversa, la **decapsulazione**). Il router non legge il livello applicativo: si limita a leggere l'intestazione di rete e a inoltrare.

```
   origine                                                       destinatario
 +--------+                              +--------+
 |applica |                              |applica |    messaggio  M
 +--------+                              +--------+
 |trasporto| Ht                         |trasporto|
 +--------+ ------ +--------------+ -----+--------+
 |  rete  | Hn  <-|  segmento    | -> Hn|  rete  |    datagramma
 +--------+       +--------------+     +--------+
 |  link  | Hl <- |   datagramma  | -> Hl|  link  |    frame
 +--------+       +--------------+     +--------+
 |  fisico|       |     frame      |    |  fisico|    bit
 +--------+       +--------------+     +--------+
                    switch / router
```

---

## 3. Socket e Indirizzamento dei Processi

### 3.1 Processi Comunicanti

Un **processo** e un programma in esecuzione su un host. Due processi sullo stesso host comunicano tramite meccanismi interprocesso definiti dal sistema operativo; due processi su host diversi devono **scambiarsi messaggi** attraverso la rete.

* **Processo client:** da inizio alla comunicazione.
* **Processo server:** resta in attesa di essere contattato.

> [!NOTE] Nota del Prof
> Le applicazioni con architettura **P2P** hanno processi che sono contemporaneamente client e server: ogni peer avvia comunicazioni e al contempo resta in ascolto.

### 3.2 Definizione di Socket

> [!IMPORTANT] Socket
> Una **socket** e una sorta di "porta" logica attraverso cui un processo invia e riceve messaggi. Un processo che desidera inviare un messaggio lo fa uscire dalla propria porta (socket) e **presuppone l'esistenza di un'infrastruttura esterna** (TCP/IP) che lo trasportera attraverso la rete fino alla porta del processo di destinazione.

```
  processo          |          Internet         |        processo
  [applicazione]    |                            |       [applicazione]
   send()  -------->|----------------------------|------> recv()
   socket  <-- buffer, variabili --> TCP       |        socket
   ^ controllato dallo sviluppatore             |        ^ controllato dal SO
   ^ controllato dal SO (il trasporto)          |
```

Il **socket** e l'oggetto esposto al programmatore attraverso una **API** che permette di: (1) scegliere il protocollo di trasporto, (2) determinare alcuni parametri della connessione. Il trasporto stesso (TCP con buffer e variabili di stato) e invece controllato dal sistema operativo.

### 3.3 Indirizzamento: IP + Porta

> [!IMPORTANT] Perche servono anche le porte?
> L'indirizzo IP da solo **non basta**. Un indirizzo IP e univoco a 32 bit e identifica un **host**, ma sullo stesso host possono girare molti processi contemporaneamente. L'identificatore completo di un processo destinatario e quindi la coppia **(indirizzo IP, numero di porta)**.

* **Porta:** numero (intero a 16 bit) che identifica un servizio in ascolto sul lato server. La coppia con l'IP e detta **socket address**, nella forma `IP:porta`.
* **Porte well-known:** assegnate istituzionalmente ai servizi standard e riconoscibili da tutti. Es. **80** per il server HTTP, **25** per il server di posta (SMTP), **21** per il server FTP.
* **Porte lato client:** non sono note a priori e vengono assegnate dal sistema operativo. Le porte con numero inferiore a 1024 sono riservate ai servizi standard e richiedono privilegi di root per l'apertura; da 1024 in su il cliente puo scegliere liberamente una porta efimera.

> [!WARNING] Implicazione di sicurezza
> L'esposizione di una porta nota rende il servizio immediatamente riconoscibile a chi scansiona le porte. Il fingerprinting del servizio (ricavato dal banner, dal comportamento e dalla risposta a richieste malformate) e il primo passo di una enumerazione dei servizi su un host.

---

## 4. Protocolli a Livello di Applicazione

Un protocollo applicativo specifica:

1. **Tipi di messaggi** scambiati (ad esempio messaggi di richiesta e di risposta).
2. **Sintassi:** quali sono i campi del messaggio e come sono descritti.
3. **Semantica:** significato delle informazioni contenute nei campi.
4. **Regole** per determinare *quando* e *come* un processo invia e risponde ai messaggi.

| Categoria | Caratteristiche | Esempi |
|---|---|---|
| **Pubblico dominio** | Definiti nelle **RFC**, consentono l'interoperabilita tra implementazioni diverse | HTTP, SMTP, FTP, DNS |
| **Proprietari** | Definiti da singoli vendor, non garantiscono interoperabilita | KaZaA, RealNetworks |

> [!NOTE] Nota del Prof
> L'esistenza di una RFC pubblica e, di per se, un vantaggio di sicurezza: chiunque puo studiare il protocollo, quindi anche l'attaccante. Questo e pero bilanciato dal fatto che la specifica e verificabile e le implementazioni indipendenti tendono a essere corrette. Nei protocolli proprietari l'opacita e invece una protezione solo apparente.

### 4.1 TCP vs UDP: quale servizio di trasporto serve?

Le applicazioni hanno requisiti diversi su tre dimensioni: **tolleranza alla perdita di dati**, **ampiezza di banda** richiesta, **sensibilita al ritardo**.

| Applicazione | Perdita dati | Ampiezza di banda | Sensibilita al tempo |
|---|---|---|---|
| Trasferimento file | No | Variabile | No |
| Posta elettronica | No | Variabile | No |
| Documenti Web | No | Variabile | No |
| Audio/video in tempo reale | Si | Audio 5 Kbps - 1 Mbps, Video 10 Kbps - 5 Mbps | Si, centinaia di ms |
| Audio/video memorizzati | Si | Come sopra | Si, pochi secondi |
| Giochi interattivi | Si | Fino a pochi Kbps | Si, centinaia di ms |
| Messaggistica istantanea | No | Variabile | Si e no |

Da questa matrice derivano i due servizi di trasporto:

**TCP - affidabile, orientato alla connessione**
* E richiesto un *setup* fra i processi client e server.
* Trasporto **affidabile**: nessun byte perso, ritrasmissione dei dati corrotti, ordinamento dei segmenti.
* **Controllo di flusso:** il mittente non vuole sovraccaricare il destinatario.
* **Controllo della congestione:** il mittente viene "strozzato" quando la rete e sovraccaricata.
* Non offre: temporizzazione, ampiezza di banda minima garantita.

**UDP - inaffidabile, senza connessione**
* Trasferimento dati **inaffidabile**, nessun setup, nessun riordino, nessun controllo di flusso o congestione.
* Piu leggero e con latenza ridotta: e comunque usato per posta, web, trasferimento file e telefonia Internet nel caso di dati multimediali.

| Applicazione | Protocollo applicativo | Trasporto |
|---|---|---|
| Posta elettronica | SMTP [RFC 2821] | TCP |
| Accesso a terminali remoti | Telnet [RFC 854] | TCP |
| Web | HTTP [RFC 2616] | TCP |
| Trasferimento file | FTP [RFC 959] | TCP |
| Multimedia in streaming | Proprietario (es. RealNetworks) | TCP o UDP |
| Telefonia Internet | Proprietario (es. Vonage, Dialpad) | Tipicamente UDP |

> [!INFO] Perche esiste UDP, se TCP e piu affidabile?
> L'affidabilita ha un costo: ritrasmissioni, buffer, handshake e attese si traducono in **ritardo**. Per flussi in tempo reale (streaming, VoIP, gaming) un pacchetto perso dopo 200 ms e semplicemente da buttare, e ritrasmetterlo peggiorerebbe l'esperienza. Si preferisce una perdita occasionale a un ritardo accumulato. Inoltre UDP consente a un server di servire contemporaneamente un numero molto piu elevato di client, riducendo lo stato da mantenere per connessione.

---

## 5. Web e HTTP

### 5.1 Terminologia

* Una **pagina web** e costituita da **oggetti**: file HTML, immagini JPEG, applet Java, file audio, ecc.
* Ogni oggetto e referenziato da un **URL** nella forma `www.someschool.edu/someDept/pic.gif`, scomposta in **nome dell'host** + **nome del percorso**.
* Il file HTML base include i riferimenti agli oggetti che lo compongono.

### 5.2 Panoramica su HTTP

> [!IMPORTANT] HTTP - HyperText Transfer Protocol
> Protocollo a livello di applicazione del Web, basato sul modello **client/server**. Il *client* e il browser che richiede, riceve e visualizza gli oggetti; il *server* web invia gli oggetti in risposta. HTTP 1.0 e definito in [RFC 1945], HTTP 1.1 in [RFC 2068].

Il colloquio avviene su TCP, con la connessione aperta dal client verso la **porta 80** del server:

1. il client HTTP inizializza la connessione TCP (crea la socket) con il server sulla porta 80;
2. il server accetta la connessione TCP;
3. client e server si scambiano i messaggi HTTP;
4. la connessione TCP viene chiusa.

**HTTP e un protocollo "senza stato" (*stateless*):** il server non mantiene informazioni sulle richieste precedenti del client.

> [!NOTE] Nota del Prof
> I protocolli *con stato* sono considerati piu complessi: lo stato (la storia passata) deve essere memorizzato e, se server e client si bloccano o riavviano, le rispettive visioni dello stato possono divergere e vanno riconciliate. Questa semplicita e il prezzo della statelessness, che pero costringe a reintrodurre lo stato lato client - ed e esattamente cio che fanno i cookie.

> [!IMPORTANT] HTTP in disuso: HTTPS e IPS
> HTTP in chiaro e ormai **deprecato** per l'uso reale: le credenziali e i dati transitano in leggibilita sul canale. HTTPS aggiunge un **cifrario** (TLS) tra TCP e HTTP, preservando le interfacce applicative. Inoltre, in contesto di sicurezza, HTTP e sfruttato come vettore di attacco da un **IPS** (Intrusion Prevention System) e dal WAF, che ispezionano le richieste a livello applicativo.

### 5.3 Connessioni HTTP

* **Non persistenti:** almeno un oggetto viene trasmesso su una connessione TCP. E il comportamento di default di HTTP/1.0.
* **Persistenti:** piu oggetti vengono trasmessi su una singola connessione TCP tra client e server. E il default di HTTP/1.1.

Il tempo di risposta per una connessione non persistente, considerando RTT come il tempo di andata e ritorno di un piccolo pacchetto:

$$T_{\text{totale}} = 2 \cdot RTT + t_{\text{trasmissione del file}}$$

Uno a **RTT** per inizializzare la connessione TCP, uno a **RTT** per la richiesta e i primi byte della risposta, piu il tempo di trasmissione del file. Con 10 immagini JPEG referenziate, servono dunque 11 connessioni TCP separate.

Le connessioni non persistenti comportano **2 RTT per oggetto** e overhead di sistema operativo per ogni connessione; i browser quindi aprono connessioni TCP parallele. Nelle persistenti:

| Modalita | Comportamento | Costo |
|---|---|---|
| Persistente senza pipelining | Il client invia una nuova richiesta solo dopo aver ricevuto la risposta precedente | 1 RTT per oggetto |
| Persistente con pipelining | Il client invia le richieste appena incontra un oggetto referenziato | 1 RTT per tutti gli oggetti (default HTTP/1.1) |

> [!EXAMPLE] Esercizio per casa
> Versioning di HTTPS: vedi [[Esercizi#E.1 - Versioning di HTTPS|E.1]].

### 5.4 Messaggi HTTP

Esistono due tipi di messaggi HTTP: **richiesta** (*request*) e **risposta** (*response*). Entrambi sono in formato **ASCII**, quindi leggibili dall'utente, e condividono la stessa struttura: una **riga iniziale**, una serie di **righe di intestazione** e terminano con una **riga vuota** (un *carriage return* e un *line feed*, CRLF, indicano la fine del messaggio).

**Messaggio di richiesta**

```http
GET /somedir/page.html HTTP/1.1\r\n
Host: www.someschool.edu\r\n
User-agent: Mozilla/4.0\r\n
Connection: close\r\n
Accept-language: fr\r\n
\r\n
```

* **Riga di richiesta:** `METODO URL VERSIONE` (comandi `GET`, `POST`, `HEAD`).
* **Righe di intestazione:** campi `Campo: valore` che forniscono informazioni aggiuntive al server.

E fondamentale che l'intestazione `Host` indichi il **server giusto**: e il meccanismo che permette a un singolo server di ospitare piu siti (virtual hosting) e che, se mancante o alterato, apre la porta ad attacchi di **host header injection** e **cache poisoning**.

**Messaggio di risposta**

```http
HTTP/1.1 200 OK\r\n
Connection: close\r\n
Date: Thu, 06 Aug 1998 12:00:15 GMT\r\n
Server: Apache/1.3.0 (Unix)\r\n
Last-Modified: Mon, 22 Jun 1998 ...\r\n
Content-Length: 6821\r\n
Content-Type: text/html\r\n
\r\n
dati dati dati dati dati ...\r\n
```

* **Riga di stato:** `VERSIONE CODICE ESPRESSIONE` (es. `HTTP/1.1 200 OK`).
* **Righe di intestazione:** incluso `Last-Modified`, il momento di ultima modifica dell'oggetto.
* **Corpo (entity body):** i dati, ad esempio il file HTML richiesto.

**Codici di stato comuni**

| Codice | Significato |
|---|---|
| `200 OK` | Richiesta riuscita; l'oggetto richiesto e inviato nella risposta |
| `301 Moved Permanently` | L'oggetto e stato trasferito; la nuova posizione e nell'intestazione `Location:` |
| `400 Bad Request` | Il messaggio di richiesta non e stato compreso dal server |
| `404 Not Found` | Il documento richiesto non si trova su questo server |
| `505 HTTP Version Not Supported` | Il server non ha la versione di protocollo richiesta |

> [!EXAMPLE] Esercizio pratico
> Verificare HTTP da riga di comando: vedi [[Esercizi#E.4 - Verificare HTTP da Riga di Comando|E.4]].

### 5.5 Metodi HTTP

| Metodo | Versione | Semantica |
|---|---|---|
| `GET` | HTTP/1.0 | Recupera l'oggetto indicato nell'URL |
| `POST` | HTTP/1.0 | Invia l'input dell'utente contenuto nel **corpo dell'entita** della richiesta |
| `HEAD` | HTTP/1.0 | Chiede al server di **escludere l'oggetto richiesto** dalla risposta (stesse intestazioni di un GET, corpo vuoto) |
| `PUT` | HTTP/1.1 | Include il file nel corpo dell'entita e lo invia al percorso specificato nel campo URL |
| `DELETE` | HTTP/1.1 | Cancella il file specificato nel campo URL |

Il **form** e il caso d'uso principale della differenza GET/POST:

* **Metodo POST:** l'input dell'utente arriva al server nel **corpo dell'entita** del messaggio.
* **Metodo GET:** l'input arriva nel **campo URL della riga di richiesta**.

```http
GET /animalsearch?monkeys&banana HTTP/1.1
```

> [!WARNING] GET e metodo "sicuro" solo in teoria
> I parametri in URL finiscono nella cronologia del browser, nel log del server, nell'intestazione `Referer` e nelle cache intermedie. Usare GET per dati autentici o operazioni che modificano lo stato e quindi una scelta errata dal punto di vista della riservatezza, indipendentemente dall'uso di HTTPS.

> [!EXAMPLE] Esercizio per casa
> REST e metodi HTTP: vedi [[Esercizi#E.2 - REST e Metodi HTTP|E.2]].

### 5.6 Cookie

Molti dei piu importanti siti web usano i **cookie**, composti da quattro elementi:

1. una riga di intestazione nel messaggio di **risposta** HTTP del server;
2. una riga di intestazione nel messaggio di **richiesta** HTTP del client;
3. un **file cookie** mantenuto sul sistema terminale dell'utente e gestito dal browser;
4. un **database sul sito** che associa l'identificativo ai dati dell'utente.

**Flusso di esempio:** Susan accede sempre dallo stesso PC e visita per la prima volta un sito di commercio elettronico. Quando la richiesta HTTP iniziale giunge al sito, il server crea un **identificativo unico (ID)** e una entry nel database per quell'ID.

```
  client                                    server
    |  richiesta HTTP                         |
    |---------------------------------------->|
    |  risposta + Set-cookie: 1678            |   crea ID 1678 -> entry nel DB
    |<----------------------------------------|
    |  (file cookie: amazon:1678, ebay:8734)   |
    |  richiesta + Cookie: 1678               |
    |---------------------------------------->|
    |  risposta                               |
    |<----------------------------------------|
    |  ... una settimana dopo ...             |
    |  richiesta + Cookie: 1678               |
    |---------------------------------------->|
```

I cookie possono contenere: **autorizzazione** (cio che l'utente e autorizzato a fare), **carta per acquisti**, **raccomandazioni**, **stato della sessione** dell'utente (es. e-mail).

> [!WARNING] Cookie e problemi di sicurezza
> I cookie permettono ai siti di **imparare molte cose** sugli utenti: l'utente fornisce nome e indirizzo e-mail, i motori di ricerca usano reindirizzamento e cookie per sapere ancora di piu, le agenzie pubblicitarie ottengono informazioni dai siti. Poiché i cookie **memorizzano anche username e password**, HTTP in chiaro e diventato deprecato: le credenziali salvate lato client sarebbero intercettabili in transito.
>
> La risposta tecnica e il **flag `HttpOnly`** (impedisce l'accesso ai cookie da JavaScript, bloccando l'esfiltrazione via XSS) e il flag **`Secure`** (vieta l'invio su canali non cifrati).

> [!EXAMPLE] Esercizio per casa
> Cookie e cifratura: vedi [[Esercizi#E.5 - Cookie e Cifratura del Canale|E.5]].

### 5.7 Cache Web e Server Proxy

L'utente configura il browser per l'accesso al Web **tramite cache**: il browser trasmette tutte le richieste HTTP alla cache, che:

* se l'oggetto e **gia in cache**, lo fornisce direttamente;
* altrimenti richiede l'oggetto al **server d'origine** e lo inoltra al client, memorizzandolo per le richieste successive.

L'obiettivo e soddisfare la richiesta del client **senza coinvolgere il server d'origine**. La cache opera sia come client sia come server ed e tipicamente installata da un ISP (universita, aziende, ISP residenziali).

**Perche fare caching?**

* riduce i tempi di risposta alle richieste dei client;
* riduce il traffico sul collegamento di accesso a Internet;
* consente ai provider con scarsa banda di fornire dati efficacemente (esattamente come fa la condivisione file P2P).

#### GET condizionale e l'importanza di `Last-Modified`

L'obiettivo e non inviare un oggetto se la cache ne possiede gia una copia aggiornata. Il meccanismo si basa sull'intestazione **`Last-Modified`** nella risposta HTTP:

```
  cache                                  server
    |  Richiesta HTTP                      |
    |  If-modified-since: <data>           |
    |------------------------------------->|   copia in cache AGGIORNATA
    |  HTTP/1.0 304 Not Modified           |<--
    |  (oggetto non inviato)               |
    |                                      |
    |  Richiesta HTTP                      |
    |  If-modified-since: <data>           |
    |------------------------------------->|   copia in cache SCADUTA
    |  HTTP/1.1 200 OK + dati              |<--
    |  (oggetto modificato)                |
```

* La **cache** specifica la data della copia dell'oggetto tramite `If-modified-since: <data>`.
* Il **server** risponde con `304 Not Modified` **senza includere l'oggetto** se la copia nella cache e aggiornata; altrimenti risponde con `200 OK` e i dati.

> [!IMPORTANT] `Last-Modified` e integrita/affidabilita
> Il campo `Last-Modified` e un elemento di **integrita temporale** del contenuto: consente di validare che la copia in cache corrisponda ancora a quella del server, riducendo il carico di rete. Se pero viene alterato o se la cache e ingannata, si apre il problema del **web cache poisoning**: l'attaccante inietta contenuto fasullo che il client accetta come legittimo, senza mai raggiungere l'origine.

> [!EXAMPLE] Esercizio per casa
> Esporre un servizio web con ngrok: vedi [[Esercizi#E.6 - Esporre un Servizio Web con ngrok|E.6]].

---

## 6. FTP: File Transfer Protocol

> [!IMPORTANT] FTP [RFC 959]
> Protocollo per il **trasferimento di file da e verso un host remoto**, basato sul modello client/server. Il *client* e il lato che inizia il trasferimento, il *server* e l'host remoto. Il server FTP ascolta sulla **porta 21**.

### 6.1 Connessione di controllo e connessione dati

L'FTP usa **due connessioni TCP distinte**, peculiarita che lo rende un protocollo atipico:

1. il client contatta il server alla **porta 21** specificando TCP come protocollo di trasporto;
2. il client ottiene l'**autorizzazione** sulla connessione di controllo;
3. il client cambia directory remota inviando i comandi sulla connessione di controllo;
4. quando il server riceve un comando di trasferimento file, apre una **connessione dati TCP** (porta 20) verso il client;
5. al termine del trasferimento il server chiude la connessione dati; un file successivo richiede una nuova connessione dati.

| Connessione | Porta | Ruolo |
|---|---|---|
| **Controllo** | TCP 21 | Comandi e risposte testuali: autenticazione, navigazione, cambio directory |
| **Dati** | TCP 20 | Effettivo trasferimento del contenuto del file |

La connessione di controllo e detta **"fuori banda" (*out of band*)** perche il traffico dei comandi non transita sulla connessione che trasporta i dati: separare i due flussi permette al server FTP di mantenere il proprio **stato** (directory corrente, autenticazione precedente) mentre trasferisce file di grandi dimensioni.

> [!WARNING] FTP e sicurezza
> Il FTP nativo invia **in chiaro** sia le credenziali (`USER`/`PASS`) sia i dati, ed e quindi vulnerabile a intercettazione e man-in-the-middle. Inoltre l'autenticazione e il semplice invio di username e password in chiaro, senza crittografia del canale di controllo: SFTP e FTPS sono le varianti sicure (rispettivamente canale SSH e TLS). Il trasferimento inoltre non e "in banda" ma su canale separato, il che rende il firewall filtering del traffico dati non banale.

### 6.2 Comandi e risposte FTP

**Comandi comuni** (inviati come testo ASCII sulla connessione di controllo):

| Comando | Significato |
|---|---|
| `USER username` | Dichiara il nome dell'utente |
| `PASS password` | Invia la password |
| `LIST` | Elenca i file della directory corrente |
| `RETR filename` | Recupera (*get*) un file dalla directory corrente |
| `STOR filename` | Memorizza (*put*) un file nell'host remoto |

**Codici di ritorno comuni** (codice di stato ed espressione, come in HTTP):

| Codice | Significato |
|---|---|
| `331` | Username OK, password required |
| `125` | Data connection already open; transfer starting |
| `425` | Can't open data connection |
| `452` | Error writing file |

> [!IMPORTANT] Solo utenti autenticati
> Le operazioni sul servizio (navigazione delle directory, lettura e scrittura di file) sono consentite **solo a un utente autenticato**. Le risposte di FTP e di tipo comando/risposta e, a differenza di HTTP, il server **mantiene lo stato** della sessione.

### 6.3 Integrita dei dati: il checksum

> [!NOTE] Integrita dei pacchetti e sicurezza
> Il trasferimento deve garantire l'**integrita** dei dati, cioe la proprieta CIA di **Integrity**: il contenuto ricevuto deve essere identico a quello trasmesso. Il meccanismo e il **checksum** (somma di controllo), un valore numerico calcolato dal mittente e verificato dal destinatario.

Il funzionamento a livello di byte:

1. il mittente suddivide il payload in blocchi e calcola, per ciascun blocco, una **somma dei valori dei byte** (o un checksum CRC, ciclico, che rileva anche errori di riordino);
2. il risultato viene inserito in un campo dedicato dell'intestazione;
3. il destinatario ricalcola la somma sui dati ricevuti e la confronta con il valore dichiarato;
4. se i valori coincidono, l'integrita e garantita; altrimenti il blocco viene scartato e richiesto nuovamente (nel caso di TCP, che e esso stesso affidabile, il checksum serve come protezione contro corruzioni e bit errati introdotti dai meccanismi di collegamento).

Lo stesso concetto e applicato in modo differenziato nella pila:

* **TCP:** checksum su **pseudo-intestazione IP + intero segmento** (header TCP + dati). E obbligatorio sia in IPv4 che in IPv6.
* **IPv4:** checksum presente ma calcolato **solo sull'intestazione** IP. I payload non sono protetti dallo strato IP, che demanda l'integrita a TCP o al livello applicazione. In IPv6 il checksum di rete e stato eliminato per velocizzare il routing.
* **Ethernet:** FCS (Frame Check Sequence) a 32 bit con polinomio ciclico CRC, in grado di rilevare sequenze complesse di *burst error*.
* **HTTP/1.1:** non prevede alcun checksum nativo nel corpo; l'integrita e delegata interamente a TLS in HTTPS.

> [!EXAMPLE] Le Due Tecniche Fondamentali a Livello Fisico
> **Bit di parita:** si aggiunge un bit di controllo a una sequenza per rendere pari (*parita pari*) o dispari (*parita dispari*) il numero complessivo di bit a 1. Rileva **solo** errori su singolo bit.
>
> **Internet Checksum** (livello di trasporto e rete): il mittente raggruppa il segmento in parole a 16 bit e ne calcola la somma in **complemento a 1**; il complemento a 1 della somma viene inserito nel campo `Checksum` dell'header. Il ricevente somma tutte le parole a 16 bit, **incluso il checksum**: se il risultato e composto da tutti 1 (`0xFFFF`), il pacchetto non presenta errori accidentali; altrimenti viene scartato.

> [!WARNING] Checksum non e integrita crittografica
> Un checksum e una funzione **non crittografica**: un attaccante in grado di alterare il traffico puo ricalcolare il checksum e modificarlo insieme ai dati, rendendo la verifica priva di valore. L'integrita autentica richiede un **MAC** o una **firma digitale** (HMAC, AES-GCM, TLS). Il checksum protegge solo dagli errori accidentali del canale.

---

## 7. La Posta Elettronica

### 7.1 Architettura

Tre componenti principali:

* **Agente utente** (detto anche *mail reader*): composizione, editing e lettura dei messaggi. Esempi: Outlook, Thunderbird, elm. I messaggi in uscita e in arrivo sono memorizzati sul server.
* **Server di posta:** contiene la **casella di posta** (*mailbox*) con i messaggi in arrivo per l'utente e la **coda di messaggi da trasmettere**.
* **SMTP** (*Simple Mail Transfer Protocol*): protocollo usato tra server di posta per consegnare i messaggi.

### 7.2 SMTP [RFC 2821]

> [!IMPORTANT] SMTP
> Protocollo di trasferimento della posta elettronica. **Usa TCP** per trasferire in modo affidabile i messaggi dal client al server, sulla **porta 25**. Il trasferimento avviene in modo **diretto**: il server di posta trasmittente contatta direttamente il server ricevente.

L'interazione procede in tre fasi, secondo uno schema **comando/risposta** (comandi in testo ASCII, risposta con codice di stato ed espressione):

1. **Handshaking** (saluto)
2. **Trasferimento di messaggi**
3. **Chiusura**

Nel server SMTP il *client* e il server di posta trasmittente, lo "server" e quello ricevente.

**Scenario: Alice invia un messaggio a Bob**

1. Alice usa il suo agente utente per comporre il messaggio da inviare a `bob@someschool.edu`;
2. l'agente utente di Alice invia il messaggio al proprio server di posta, che lo mette in coda;
3. il lato client di SMTP apre una connessione TCP con il server di posta di Bob;
4. il client SMTP invia il messaggio sulla connessione TCP;
5. il server di posta di Bob mette il messaggio nella casella di posta di Bob;
6. Bob invoca il suo agente utente per leggere il messaggio.

```text
S: 220 hamburger.edu
C: HELO crepes.fr
S: 250 Hello crepes.fr, pleased to meet you
C: MAIL FROM: <alice@crepes.fr>
S: 250 alice@crepes.fr... Sender ok
C: RCPT TO: <bob@hamburger.edu>
S: 250 bob@hamburger.edu ... Recipient ok
C: DATA
S: 354 Enter mail, end with "." on a line by itself
C: Do you like ketchup?
C: How about pickles?
C: .
S: 250 Message accepted for delivery
C: QUIT
S: 221 hamburger.edu closing connection
```

> [!EXAMPLE] Esercizio pratico
> Interazione SMTP via telnet: vedi [[Esercizi#E.7 - Interazione SMTP via Telnet|E.7]].

**Caratteristiche e limiti di SMTP**

* Usa **connessioni persistenti**.
* Richiede che il messaggio (intestazione e corpo) sia nel formato **ASCII a 7 bit**.
* Determina la fine del messaggio con il terminatore **`CRLF.CRLF`**.
* Confronto con HTTP: HTTP e **pull** (il client richiede), SMTP e **push** (il server invia). Entrambi usano interazione comando/risposta in ASCII e codici di stato, ma in HTTP ogni oggetto e incapsulato in un messaggio di risposta separato, mentre in SMTP piu oggetti viaggiano in un unico messaggio.

> [!WARNING] La porta 25 come vettore: Open Relay e Mail Spoofing
> Poiche originariamente i server SMTP non richiedevano alcuna autenticazione e consentivano a **chiunque** di dichiarare qualsiasi mittente nel comando `MAIL FROM:`, i server configurati in modalita **Open Relay** sono stati massicciamente sfruttati per l'invio indiscriminato di spam e phishing. I moderni sistemi applicano protocolli di autenticazione e reputazione del mittente:

| Meccanismo | Funzione |
| :--- | :--- |
| **SPF** (*Sender Policy Framework*) | Record DNS che autorizza specifici indirizzi IP all'invio di email per quel dominio |
| **DKIM** (*DomainKeys Identified Mail*) | Firma crittografica a chiave pubblica apposta nell'header dell'email |
| **DMARC** | Policy che definisce le azioni da intraprendere (es. scarto o quarantena) qualora i controlli SPF o DKIM falliscano |

### 7.3 Formato dei messaggi di posta: RFC 822

SMTP e il protocollo per **scambiare** messaggi; l'**RFC 822** e lo standard che definisce il **formato** del messaggio di testo:

* **Intestazione** (righe di intestazione), ad esempio `To:`, `From:`, `Subject:`, separate dal corpo da una **riga vuota**. Sono **differenti dai comandi SMTP**.
* **Corpo:** il "messaggio", contenente soltanto caratteri ASCII.

```
+---------------------------------------+
|  intestazione  (To: / From: / Subject:) |
+---------------------------------------+
|  riga vuota                            |
+---------------------------------------+
|  corpo (solo caratteri ASCII)           |
+---------------------------------------+
```

### 7.4 MIME: estensioni per messaggi multimediali

Poiche oggi non si scambia piu solo ASCII nelle email (allegati binari, immagini, audio, video), e nato lo standard **MIME** (*Multipurpose Internet Mail Extensions*, RFC 2045 e 2056).

> [!IMPORTANT] MIME
> **M**ultipurpose **I**nternet **M**ail **E**xtensions. Consiste in **righe aggiuntive nell'intestazione** dei messaggi che dichiarano il **tipo di contenuto MIME** e il **metodo di codifica** usato per il corpo. Senza MIME il corpo deve restare ASCII a 7 bit; con MIME puo contenere dati arbitrari, purché codificati.

```http
From: alice@crepes.fr
To: bob@hamburger.edu
Subject: Picture of yummy crepe.
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Type: image/jpeg

base64 encoded data .....
..........................
......base64 encoded data
```

| Riga di intestazione | Funzione |
|---|---|
| `MIME-Version` | Versione di MIME utilizzata (1.0) |
| `Content-Transfer-Encoding` | Metodo usato per codificare i dati (`base64`, `quoted-printable`, `7bit`, `8bit`, `binary`) |
| `Content-Type` | Tipo di dato multimediale, sottipo e parametri (`image/jpeg`, `text/plain`, `application/pdf`) |

> [!EXAMPLE] Esercizio per casa
> Encoding base64: vedi [[Esercizi#E.3 - Encoding Base64|E.3]].

**Esempio reale di intestazione completa** (slide del prof):

```http
Return-Path: <fancello@sci.unich.it>
Received: from phobos.unich.it (phobos.unich.it [192.167.13.101])
	by gotham.sci.unich.it (8.12.8/8.12.8) with ESMTP id i8GAZMaS011065
	for <bista@sci.unich.it>; Thu, 16 Sep 2004 12:35:23 +0200
Message-ID: <001801c49bd8$b54118c0$0b5ca7c0@sci.unich.it>
From: "Maura Fancello" <fancello@sci.unich.it>
To: "stefano Bistarelli" <bista@sci.unich.it>
Subject: Re: lavagna luminosa e proiettore
Date: Thu, 16 Sep 2004 12:34:10 +0200
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="----=_NextPart_000_0015_01C49BE9.77729620"
X-Mailer: Microsoft Outlook Express 6.00.2800.1106
X-Antivirus: Scanned by F-Prot Antivirus (http://www.f-prot.com)
X-Spam-Status: No, hits=-4.8 required=3.0 tests=BAYES_00,HTML_MESSAGE
```

L'intestazione e un insieme di campi che veicolano informazioni **non destinate al corpo del messaggio**:

* `Return-Path` e le `Received` (tracciabilità della catena di passaggi, inserite da ogni server attraversato);
* `Message-ID` e `References` (identificatori univoci e relazioni con i messaggi citati, usati per il threading);
* `Content-Type: multipart/...` con il parametro `boundary` che separa le parti del messaggio;
* le intestazioni `X-` sono **non standard** (estensioni proprietarie del client di posta) e veicolano metadati del tutto innocui dal punto di vista del protocollo: versione del client, antivirus integrato, filtro antispam.

> [!INFO] Il `boundary` e il punto debole di multipart
> Il tipo `multipart/*` delimita le parti del corpo con un separatore testo chiamato `boundary`. Se il contenuto di un allegato contiene accidentalmente la stringa di boundary, le parti vengono mal interpretate: e alla base delle tecniche di **MIME boundary injection** e dei classici attacchi di **mail spoofing** / phishing multipart. Per questo la verifica dei messaggi non si ferma a From/Subject, ma guarda i record `Authentication-Results`, `DKIM-Signature` e `Received`.

### 7.5 Protocolli di accesso alla posta

SMTP serve per la **consegna e la memorizzazione** sul server del destinatario. Per **ottenere i messaggi** dal server servono protocolli di accesso dedicati.

| Protocollo | RFC | Funzionalita |
|---|---|---|
| **POP3** (*Post Office Protocol*) | RFC 1939 | Autorizzazione (agente <-> server) e download dei messaggi |
| **IMAP** (*Internet Mail Access Protocol*) | RFC 1730 | Funzionalita estese: manipolazione dei messaggi memorizzati sul server |
| **HTTP** | - | Hotmail, Yahoo! Mail e simili (webmail) |

**POP3** - Fase di autorizzazione: comandi `user` (dichiara il nome utente), `pass` (password); risposte del server `+OK` / `-ERR`.
Fase di transazione: `list` (elenca i numeri dei messaggi), `retr` (ottiene i messaggi per numero), `dele` (cancella), `quit`.

```text
S: +OK POP3 server ready
C: user bob
S: +OK
C: pass hungry
S: +OK user successfully logged on
C: list
S: 1 498
S: 2 912
S: .
C: retr 1
S: <message 1 contents>
S: .
C: dele 1
C: retr 2
S: <message 2 contents>
S: .
C: dele 2
C: quit
S: +OK POP3 server signing off
```

Due modalita operative: **scarica e cancella** (il precedente esempio: Bob non puo rileggere le e-mail se cambia client) e **scarica e mantieni** (copia i messaggi su piu client). POP3 e un protocollo **senza stato** tra le varie sessioni.

**IMAP** mantiene tutti i messaggi in un unico luogo (il server), consente di organizzarli in **cartelle** e conserva lo **stato dell'utente** tra le sessioni: i nomi delle cartelle e l'associazione tra identificatori dei messaggi e nomi delle cartelle.

> [!WARNING] Uso della porta 110/143
> POP3 (porta 110) e IMAP (porta 143) in chiaro espongono credenziali e contenuti, cosi come SMTP sulla 25. Le varianti sicure sono POP3S (995), IMAPS (993) e SMTPS (465/submission), tutte basate su TLS.

---

## 8. Differenza tra ISO/OSI e TCP/IP

Il modello **ISO/OSI** (ISO 7498) e il riferimento teorico a **7 livelli**; lo stack **TCP/IP** (Internet Protocol Suite) e quello realmente implementato, con **5 livelli**. La corrispondenza non e uno-a-uno: OSI separa esplicitamente **presentazione** e **sessione**, funzioni che in TCP/IP sono collassate nel livello applicazione.

```
  OSI (7 livelli)                    TCP/IP (5 livelli)
 +---------------------------+      +---------------------------+
 | 7  Applicazione           |      |                           |
 +---------------------------+      |   5  Applicazione          |
 | 6  Presentazione          |      |   (FTP, SMTP, HTTP, DNS)   |
 +---------------------------+      |                           |
 | 5  Sessione               |      +---------------------------+
 +---------------------------+      |   4  Trasporto             |
 | 4  Trasporto              |      |   (TCP, UDP)               |
 +---------------------------+      +---------------------------+
 | 3  Rete                   |      |   3  Rete                  |
 +---------------------------+      |   (IP, ICMP, ARP)          |
 | 2  Collegamento dati      |      +---------------------------+
 +---------------------------+      |   2  Collegamento          |
 | 1  Fisico                 |      |   (Ethernet, PPP)          |
 +---------------------------+      +---------------------------+
                                    |   1  Fisico                 |
                                    +---------------------------+
```

| OSI | TCP/IP | Funzione | Protocolli TCP/IP |
|---|---|---|---|
| 7 Applicazione | 5 Applicazione | Servizi all'utente finale | HTTP, HTTPS, FTP, SMTP, DNS |
| 6 Presentazione | (in Applicazione) | Formato dei dati, cifratura, compressione | TLS/SSL |
| 5 Sessione | (in Applicazione) | Controllo dialoghi, sincronizzazione | - |
| 4 Trasporto | 4 Trasporto | Affidabilita, controllo di flusso e congestione | TCP, UDP |
| 3 Rete | 3 Rete | Instradamento, indirizzamento logico | IP, ICMP, ARP |
| 2 Collegamento | 2 Collegamento | Trasferimento su singolo hop, framing, MAC | Ethernet, PPP |
| 1 Fisico | 1 Fisico | Trasmissione di segnali e bit | - |

Le differenze sostanziali:

* **Numero di livelli:** 7 contro 5. OSI e piu granulare, TCP/IP e piu semplice e realistico.
* **Praticita:** OSI e nato come standard di riferimento concettuale, e stato implementato solo parzialmente (X.25, ASN.1). TCP/IP nasce dall'evoluzione di ARPANET ed e il protocollo effettivamente implementato su Internet.
* **Separazione presentazione/sessione:** assente in TCP/IP, dove cifratura e compressione finiscono dentro l'applicazione (HTTPS) o in un livello intermedio (TLS sopra TCP).
* **Affidabilita:** in OSI la affidabilita e delegata solo al trasporto; in TCP/IP **ogni livello puo rilevare gli errori** (checksum a livello IP, TCP, Ethernet), riducendo l'impatto degli errori sui livelli superiori.

> [!NOTE] Nota del Prof
> Il passaggio OSI -> TCP/IP si legge in direzione inversa rispetto allo schema: passando dal livello piu basso a quello piu alto si incontra **fisico, collegamento, rete, trasporto, sessione, presentazione, applicazione**. Il glossario OSI resta comunque il riferimento lessicale con cui la maggior parte dei professionisti descrive i problemi di rete, anche quando lavora su TCP/IP.

---

## 9. Contromisure per Livello della Pila

La stratificazione introduce un sovraccarico computazionale (*overhead*) dovuto all'aggiunta di header per ogni strato, ma costituisce un fondamentale vantaggio difensivo: permette di predisporre contromisure specializzate e disaccoppiate a ciascun livello.

| Livello | Contromisure Tipiche |
| :--- | :--- |
| **Link** | Port Security, 802.1X, isolamento VLAN |
| **Rete / Trasporto** | Packet filtering, firewall di stato, IPsec, VPN, TLS |
| **Applicazione** | Web Application Firewall (WAF), Intrusion Prevention System (IPS), validazione semantica dei payload, autenticazione applicativa |

---

## 10. Quadro di Sintesi: Dove si Attacca la Pila

| Livello | Protocollo | Debolezza sfruttabile | Difesa tipica |
|---|---|---|---|
| Applicazione | HTTP, FTP, SMTP | Nessuna cifratura, credenziali in chiaro, input non validato, deserializzazione di header | HTTPS/TLS, validazione input, WAF, IPS |
| Applicazione (web) | HTTP / Cookie | Cookie senza `Secure`/`HttpOnly`, cache poisoning, host header injection | Flag di sicurezza, `Vary`, validazione header |
| Trasporto | TCP / UDP | Assenza di cifratura integrata, trust on first use (TCP), spoofing UDP | IPsec, VPN, DNSSEC, filtri anti-spoofing |
| Rete | IP | Assenza di integrita del payload (IPv4), ICMP redirect, fragfragmentation | IPsec, anti-spoofing (ingress/egress filtering) |
| Collegamento | Ethernet | Ethernet sniffer su hub, ARP spoofing | VLAN, port security, 802.1X |
| Fisico | - | Tapping, ascolto passivo | cifratura end-to-end, controllo accessi fisici |

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Cybersecurity]]
- **Esercizi :** [[Esercizi#Lezione 02 - Livello di Applicazione (28/09/2026)]]
- **Precedente :** [[01_Introduzione_alla_Sicurezza_Informatica]]