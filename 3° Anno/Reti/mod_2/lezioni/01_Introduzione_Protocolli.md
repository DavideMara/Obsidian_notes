---
date: 2026-09-25
tags:
  - reti
type: lezione
---
# Introduzione ai Protocolli di Rete

> [!INFO] Informazioni sul Corso e Modalità d'Esame
> * **Modulo:** 2 - Protocolli di Rete
> * **Docente:** Prof. Damiano Perri (professore a contratto)
> * **Email:** `damiano.perri@unipg.it` / Homepage: `https://www.damianoperri.it/`
> * **Testi di Riferimento Consigliati:**
>   * Bruno Checcucci - *Reti di calcolatori*, Sarapar Editore.
>   * Gary Govanus - *TCP/IP: Per configurare, implementare e gestire TCP/IP sulla vostra rete*, McGraw-Hill.
>   * Dispense del docente disponibili su Unistudium.
> * **Modalità d'Esame:**
>   * Test scritto individuale svolto tramite la piattaforma **LibreEOL** (UNIPG), con domande a risposta multipla di tipo *Multiple Choice* e *Multiple Response*.
>   * Domande e risposte presentate in ordine casuale, di uguale difficoltà per tutti i candidati, vertenti sui contenuti erogati a lezione e resi disponibili sul sito ufficiale e su Unistudium.

---

## 1. Introduzione al Networking e Convergenza Telematica

Il settore delle reti di calcolatori e dei sistemi telematici è caratterizzato da una crescita pervasiva. Questa continua evoluzione tecnologica è trainata dalla convergenza di molteplici fattori abilitanti:

* **Sviluppo delle Telecomunicazioni:** espansione delle infrastrutture ad altissima capacità trasmissiva (dorsali in fibra ottica ad altissima velocità, tecnologie wireless cellulari e satellitari).
* **Sviluppo delle Micro e Nano-tecnologie:** avanzamento continuo della miniaturizzazione dei semiconduttori, che permette di integrare elevate capacità computazionali e interfacce di rete in chip compatti a bassissimo consumo energetico.
* **Sviluppo di Sensori ad Elevata Efficienza:** disponibilità di sensori sempre più miniaturizzati, affidabili ed economici, che costituiscono il presupposto per l'Internet of Things (IoT), i sistemi embedded e il monitoraggio ambientale e industriale continuo.
* **Sviluppo di Soluzioni Software Avanzate:** ingegnerizzazione di stack protocollari altamente performanti, architetture a microservizi e soluzioni di virtualizzazione delle funzioni di rete (*Software-Defined Networking*, SDN).
* **Sviluppo di Soluzioni Combinate Hardware/Software:**
  * Capacità di gestire e trasferire simultaneamente **dati numerici, flussi audio/voce e flussi video ad alta definizione**.
  * Requisito stringente di erogazione e sincronizzazione in **tempo reale (*real-time*)**, essenziale per videoconferenze, telemedicina e sistemi di controllo critici.

La transizione tecnologica ha segnato il superamento definitivo dei modelli centralizzati (fondati sui grandi mainframe con terminali passivi) a favore dei **sistemi di elaborazione distribuita**, sostenuti da tecnologie in grado di instradare volumi massivi di dati tramite segnali fisici a frequenze elevatissime.

### 1.1 La Piramide del Computing Distribuito

La convergenza hardware/software descrive una progressione architetturale in cui il carico computazionale si sposta progressivamente dal centro della rete verso i dispositivi periferici, fino a raggiungere la sorgente stessa del dato:

```
┌──────────────────────────────────────────────┐
│               CLOUD COMPUTING                │
│          elaborazione centralizzata          │
└──────────────────────────────────────────────┘
    ┌──────────────────────────────────────┐
    │            FOG COMPUTING             │
    │       distribuzione intermedia       │
    └──────────────────────────────────────┘
        ┌──────────────────────────────┐
        │        EDGE COMPUTING        │
        │    elaborazione al bordo     │
        └──────────────────────────────┘
            ┌──────────────────────┐
            │    IoT ECOSYSTEMS    │
            │ sensori e attuatori  │
            └──────────────────────┘
```

* **Cloud Computing:** risorse computazionali erogate come servizio on-demand da data center centralizzati, con accesso via rete e scala elastica.
* **Fog Computing:** strato intermedio che estende il cloud verso la rete, distribuendo l'elaborazione tra data center e periferie per ridurre latenza e traffico di rete.
* **Edge Computing:** elaborazione ai bordi della rete, in prossimità dei dispositivi che producono o consumano i dati.
* **IoT Ecosystems:** l'innesto di miliardi di dispositivi, sensori e attuatori che generano i dati alla fonte.

> [!INFO] Perché il Cloud da solo non basta
> Un'architettura esclusivamente centralizzata è vincolata dalla distanza fisica dalla sorgente del dato: la latenza di rete e il consumo di banda crescono con la distanza e i colli di banda ("edge" dei dati) dominano il costo. Spostando l'elaborazione verso il periferico si dimezza il percorso del dato, con effetti diretti su tempo di risposta, affidabilità e sostenibilità energetica.

---

## 2. Il Processo di Comunicazione Dati

L'infrastruttura globale consente a sistemi eterogenei di interagire e scambiare informazioni su qualsiasi scala geografica, da reti locali (LAN) fino all'interconnessione su scala planetaria (WAN) e Internet.

### 2.1 Gli Elementi del Processo Comunicativo

Si può parlare di processo comunicativo solo quando coesistono tre elementi costitutivi irrinunciabili:

1. **Sorgente dell'informazione (*Source / Trasmettitore*):** il dispositivo che genera i dati da trasmettere (es. personal computer, telecamera IP, sensore IoT).
2. **Mezzo Trasmissivo (*Transmission Medium / Cammino Fisico*):** il supporto o percorso fisico lungo il quale si propaga il segnale: mezzi guidati (rame, fibra ottica) oppure mezzi non guidati (spazio libero, propagazione tramite onde elettromagnetiche).
3. **Destinatario (*Destination / Ricevitore*):** il dispositivo a cui è destinato il flusso informativo e che acquisisce il segnale (es. server, workstation, attuatore).

```
┌──────────────────┐     ┌──────────────────────────┐     ┌──────────────────┐
│     SORGENTE     │     │    MEZZO TRASMISSIVO     │     │   DESTINATARIO   │
│     (Source)     │────►│     (Canale fisico)      │────►│  (Destination)   │
└──────────────────┘     └──────────────────────────┘     └──────────────────┘
      generazione               propagazione             acquisizione
```

### 2.2 Definizione di Comunicazione Dati e Sistema di Comunicazione

> [!IMPORTANT] Comunicazione Dati
> La **comunicazione dati** è lo scambio formale di informazioni tra due o più dispositivi, realizzato attraverso un idoneo mezzo di trasmissione.

Affinché la comunicazione abbia luogo con successo, i singoli apparati devono integrarsi all'interno di un **sistema di comunicazione** coerente, strutturato in due componenti complementari:

* **Hardware:** le interfacce fisiche di rete (NIC, *Network Interface Card*), modem, amplificatori, antenne, commutatori (*switch*) e instradatori (*router*).
* **Software:** i driver di periferica, gli stack protocollari del sistema operativo (es. suite TCP/IP) e i programmi applicativi di rete.

---

## 3. Teoria dell'Informazione e Modello di Shannon-Weaver

### 3.1 Definizioni Fondamentali ed Etimologia

> [!NOTE] Definizioni di Informazione e Comunicazione
> * **Informazione:** l'insieme di dati, correlati tra loro, con cui un'idea (o un fatto) prende forma ed è comunicata.
> * **Comunicazione:** dal latino *cum* ("con", "insieme") e *munire* ("legare", "costruire"), e dal verbo *communico* ("mettere in comune", "far partecipe"): il processo e le modalità di trasmissione di un'informazione da un individuo a un altro (o da un luogo a un altro), attraverso lo scambio di un messaggio elaborato secondo le regole di un determinato codice.
>
> Citazione da Giuliano Vigini, *Glossario di biblioteconomia e scienza dell'informazione*.

L'informazione è dunque il risultato di una **trasformazione**: dati grezzi diventano informazione quando vengono correlati e contestualizzati, e diventano conoscenza quando vengono assimilati, integrati e confrontati. Questa catena di trasformazioni è formalizzata nel modello gerarchico DIKW (sezione 4).

### 3.2 Il Modello di Shannon-Weaver (1949)

Formulato da Claude Shannon e Warren Weaver nei Bell Laboratories, il modello descrive la trasmissione dell'informazione attraverso **7 elementi fondamentali**:

```
                                  [1] SORGENTE  (Information Source)
                                  
                                  ▼
                                  [2] CODIFICA  (Trasmittitore)
                                  
                                  ▼
                                  [3] MESSAGGIO
                                  
                 ┌──────────────────────────────────┐
                 │  [4] CANALE / MEZZO TRASMISSIVO  │◄── [5] RUMORE
                 │        (Channel)                 │     (Noise Source)
                 └──────────────────────────────────┘
                 
                 ▼
                                  [6] DECODIFICA  (Ricevitore)
                                  
                                  ▼
                                  [7] DESTINATARIO  (Destination)
                                  
                                  └──►  FEEDBACK: retroazione verso la sorgente
```

1. **Fonte / Sorgente (*Information Source*):** l'entità che concepisce e genera il messaggio originario.
2. **Codifica (*Encoding / Trasmettitore*):** l'operazione che converte il messaggio logico in segnali fisici (elettrici, ottici o radio) trasmissibili attraverso il canale.
3. **Messaggio:** la sequenza informativa strutturata prodotta dal processo di codifica.
4. **Mezzo Trasmissivo / Canale (*Channel*):** il mezzo fisico che sostiene la propagazione dei segnali.
5. **Rumore (*Noise Source*):** disturbi casuali, attenuazioni, dispersioni o interferenze esterne introdotti dal canale, suscettibili di degradare o alterare il segnale.
6. **Decodifica (*Decoding / Ricevitore*):** l'operazione inversa che ricostruisce il messaggio logico originario a partire dai segnali fisici ricevuti.
7. **Destinatario (*Destination*):** la persona o il sistema finale a cui è indirizzata l'informazione.

> [!NOTE] Il Modello di Shannon-Weaver
> Rappresentazione bidirezionale e ciclica del processo comunicativo: la fonte codifica il messaggio per il canale (soggetto a rumore ed errori di trasmissione); il destinatario decodifica il messaggio e, attraverso un meccanismo di retroazione (*feedback*), può assumere il ruolo di sorgente invertendo il flusso della comunicazione.

---

## 4. La Gerarchia della Conoscenza: la Piramide DIKW

La gestione e la trasformazione delle informazioni nei sistemi telematici e decisionali è formalizzata nel modello gerarchico **DIKW** (*Data, Information, Knowledge, Wisdom*), che articola la conoscenza in quattro stadi ascendenti:

```
┌──────────────────────────────────────────────┐
│             SAGGEZZIA  (WISDOM)              │
│         giudizio critico, strategia          │
└──────────────────────────────────────────────┘
    ┌──────────────────────────────────────┐
    │       CONOSCENZA  (KNOWLEDGE)        │
    │         risponde al "come?"          │
    └──────────────────────────────────────┘
        ┌──────────────────────────────┐
        │ INFORMAZIONE  (INFORMATION)  │
        │     dati con significato     │
        └──────────────────────────────┘
            ┌──────────────────────┐
            │     DATI  (DATA)     │
            │    simboli grezzi    │
            └──────────────────────┘
```

1. **Dati (*Data*):**
   * Elementi grezzi, simboli non contestualizzati, misurazioni o segnali binari privi di significato intrinseco (es. il valore `25`, la stringa `10101`).
   * *Proprietà:* massimi livelli di **oggettività**, **volume** e **completezza**, ma utilità operativa nulla in assenza di un contesto interpretativo.
2. **Informazione (*Information*):**
   * Dati organizzati, correlati e contestualizzati, a cui viene associato un significato semantico ben preciso.
   * Risponde alle interrogazioni empiriche: *chi?*, *cosa?*, *dove?*, *quando?*
3. **Conoscenza (*Knowledge*):**
   * Comprensione contestuale derivata dall'assimilazione, dall'integrazione e dal confronto di informazioni mediante esperienza, regole inferenziali e modelli cognitivi.
   * Risponde alla domanda: *come?*
4. **Saggezza (*Wisdom*):**
   * Livello apicale della gerarchia: integra la conoscenza con il giudizio critico, la visione a lungo termine e le decisioni strategiche.
   * Risponde alla domanda: *perché?*

| Livello | Domanda a cui risponde | Caratteristiche Distintive | Funzione nel Sistema Informativo |
| :--- | :---: | :--- | :--- |
| **Saggezza** (*Wisdom*) | Perché? | Soggettività, alto valore aggiunto, sintesi, struttura | Supporto alle decisioni strategiche e comprensione di sistema |
| **Conoscenza** (*Knowledge*) | Come? | Integrazione, esperienza, regole inferenziali | Rilevazione dei pattern e delle anomalie |
| **Informazione** (*Information*) | Chi? Cosa? Dove? Quando? | Significato semantico, contestualizzazione | Codifica e trasporto di rete |
| **Dati** (*Data*) | -- | Oggettività, elevato volume, completezza, misurabilità | Memorizzazione, rilevazione sensoriale grezza |

> [!EXAMPLE] La scaletta DIKW applicata a un dato di rete
> Un sensore di temperatura in una sala server registra `25`: questo è un **dato**. Una volta associato a `sala server`, `11:59` e all'unità di misura si ottiene un'**informazione** (`"La temperatura registrata nella sala server alle 11:59 è di 25°C"`). Sapere che tale valore costante supera la soglia raccomandata per le CPU e comporta il rischio di *thermal throttling* è **conoscenza**. Progettare una riconfigurazione dell'impianto di climatizzazione e delle policy di carico computazionale, ottimizzando l'impatto energetico, è **saggezza**.

---

## 5. I Protocolli di Rete e gli Standard Internazionali

### 5.1 Il Concetto Fondamentale di Protocollo

Un **protocollo di rete** è un insieme formale di regole, formati e convenzioni condivise che stabiliscono le modalità con cui due o più entità devono comunicare.

Un protocollo specifica in modo deterministico:

* **Cosa si scambia (Sintassi e Semantica):**
  * *Sintassi:* la struttura del pacchetto, la disposizione dei bit e dei campi (header, payload, checksum) e i formati di codifica.
  * *Semantica:* il significato associato a ciascun pattern di bit o campo di controllo e le azioni da intraprendere alla ricezione di ciascun comando.
* **Come avviene lo scambio (Temporizzazione / *Timing*):**
  * La sincronizzazione temporale, l'ordine sequenziale dei messaggi e i meccanismi di regolazione della velocità trasmissiva (*flow control*).

> [!IMPORTANT] Necessità Ineludibile del Protocollo
> Due o più dispositivi possono essere fisicamente e correttamente collegati tramite cavi o onde radio, ma in assenza di un protocollo comune **non sono assolutamente in grado di comunicare**. Senza regole condivise, i segnali elettrici o ottici ricevuti risultano indecifrabili, analogamente a due individui collegati tramite una linea telefonica impeccabile che parlino due lingue del tutto sconosciute l'uno all'altro.

### 5.2 Chi Definisce gli Standard: ISO e CCITT

Affinché apparati realizzati da produttori indipendenti e basati su architetture differenti possano interoperare senza frizioni su scala mondiale, i protocolli devono essere formalizzati come **standard aperti**, prodotti da organismi di standardizzazione internazionali. Le slide del corso riportano due esempi:

```
┌────────────────────────────────────────────────────────────────────┐
│             ORGANI DI STANDARDIZZAZIONE INTERNAZIONALE             │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ISO  (International Organization for Standardization)             │
│      massima organizzazione mondiale indipendente e non            │
│      governativa per la standardizzazione tecnica internazionale   │
│      -> sistemi di comunicazione, modello di riferimento ISO/OSI,  │
│         sicurezza informatica, gestione dei dati                   │
│                                                                    │
│  ex CCITT  (Comité Consultatif International des                   │
│             Télécommunications Télégraphiques)                     │
│      organismo storico delle telecomunicazioni, oggi confluito     │
│      nell'ITU-T del settore delle Nazioni Unite                    │
│      -> standard dei sistemi di telecomunicazione                  │
└────────────────────────────────────────────────────────────────────┘
```

> [!INFO] ISO (International Organization for Standardization)
> L'**ISO** è la massima organizzazione mondiale indipendente e non governativa per la standardizzazione tecnica internazionale. I suoi standard coprono un vasto spettore di settori industriali, svolgendo un ruolo di riferimento nell'architettura dei sistemi di comunicazione (incluso lo sviluppo del celebre modello di riferimento **ISO/OSI** a 7 livelli) e nelle normative per la sicurezza informatica e la gestione dei dati.

> [!NOTE] CCITT
> Il **CCITT** è l'organismo internazionale che per decenni ha definito gli standard delle telecomunicazioni, confluito oggi nell'**ITU-T** del settore delle Nazioni Unite. Il suo esempio più noto in ambito networking è la **serie V** delle interfacce di rete, che rende omogenee le caratteristiche elettriche e procedurali degli accessi.

> [!WARNING] Standard de jure vs standard de facto
> Uno standard scritto da un organismo riconosciuto (ISO, ITU-T) non è necessariamente quello effettivamente implementato. La diffusione reale di un protocollo dipende dal mercato e dalla base storica di installazioni: questo è il motivo per cui lo standard de facto di Internet resta lo stack TCP/IP, nonostante la sua formalizzazione solo parziale in standard ufficiali.

### 5.3 Corrispondenza ISO/OSI e TCP/IP: i Livelli e le Unità Dati

Il modello di riferimento ISO/OSI a 7 livelli e la suite TCP/IP a 4 livelli descrivono lo stesso processo di comunicazione con granularità diversa. La tabella riporta la corrispondenza dei livelli e delle rispettive **unità dati** (data unit) elaborate a ciascun livello:

| Livello | ISO/OSI | Data Unit (ISO/OSI) | TCP/IP | Data Unit (TCP/IP) |
| :---: | :--- | :--- | :--- | :--- |
| 7-5 | Applicazione, Presentazione, Sessione | Dato (*Data*) | 4 - Applicazione | Dato / Messaggio |
| 4 | Trasporto | Segmento | 3 - Trasporto | Segmento (TCP) / Datagramma (UDP) |
| 3 | Rete | Pacchetto (*Packet*) | 2 - Internet | Datagramma IP |
| 2 | Collegamento Dati | Frame | 1 - Accesso alla Rete | Frame |
| 1 | Fisico | Bit (stream di bit) | 1 - Accesso alla Rete | Bit (stream di bit) |

> [!INFO] Cosa cambia tra i due modelli
> I tre livelli superiori di ISO/OSI (Applicazione, Presentazione, Sessione) sono fusi in un unico livello Applicazione TCP/IP, in cui le funzioni di codifica, cifratura e gestione delle sessioni confluiscono nell'applicazione stessa e nella libreria di trasporto. Il livello Fisico, invece, è accorpato al livello Collegamento Dati nel livello unico di Accesso alla Rete. Per il confronto completo dei due modelli si veda [[01_Introduzione_Architettura_Reti]].

---

## 6. I Principi dell'Architettura a Livelli

I moderni sistemi di telecomunicazione adottano un'architettura modulare a livelli (*layered architecture*), strutturata secondo tre principi cardine dell'ingegneria del software.

### 6.1 Astrazione e Separazione degli Interessi

Ogni livello (*layer*) risolve un sottoinsieme specifico di problematiche comunicative, offre servizi ben definiti al livello superiore e nasconde i dettagli implementativi sottostanti.

### 6.2 Incapsulamento

Ogni livello riceve dati dal livello superiore, aggiunge la propria informazione di controllo sotto forma di intestazione (*header*) o coda (*trailer*), generando la specifica unità dati di protocollo.

### 6.3 Interoperabilità e Flessibilità

La modifica interna di un protocollo a un determinato livello non impatta i livelli adiacenti, purché le interfacce di comunicazione rimangano inalterate.

> [!WARNING] La Stratificazione Introduce Vulnerabilita
> Sebbene comporti un inevitabile sovraccarico computazionale (*overhead* dovuto all'aggiunta di header per ogni strato), la stratificazione costituisce un fondamentale vantaggio difensivo. Consente di predisporre contromisure specializzate e disaccoppiate a ciascun livello della pila: *Port Security*, 802.1X e isolamento VLAN al livello Link; packet filtering, firewall di stato, IPsec, VPN e TLS ai livelli Rete/Trasporto; WAF, IPS e validazione semantica dei payload al livello Applicazione.

## 7. Host Layers vs Media Layers

I livelli architetturali si dividono in due macro-categorie funzionali.

> [!IMPORTANT] Le Due Macro-Categorie
> - **Host Layers** (livelli Host / End-to-End / Software): operano esclusivamente sui sistemi terminali (*End Systems* / *Hosts*). Sono implementati a livello software nel sistema operativo e nelle applicazioni utente, indipendentemente dal mezzo fisico sottostante. Gestiscono l'interazione con l'utente, la rappresentazione dei formati, il controllo di sessione e l'affidabilita del trasporto da estremo a estremo.
> - **Media Layers** (livelli Media / Subnet / Hardware-Network): governano il trasferimento effettivo delle informazioni attraverso i canali trasmissivi e gli apparati intermedi di rete (router, switch). Risolvono l'indirizzamento logico, l'instradamento (*routing*), l'indirizzamento fisico MAC, l'accesso al mezzo e la modulazione dei segnali.

### 7.1 Protocol Data Unit (PDU) per Livello

| Livello OSI | Host/Media | PDU (Data Unit) | Descrizione della PDU |
| :---: | :--- | :--- | :--- |
| 7. Application | Host Layer | Data (Dati) | Messaggio o payload applicativo originario |
| 6. Presentation | Host Layer | Data (Dati) | Dati formattati, cifrati o compressi |
| 5. Session | Host Layer | Data (Dati) | Flusso dati strutturato nella sessione logica |
| 4. Transport | Host Layer | Segment / Datagram | Segmento (TCP, con controllo di sequenza) o Datagramma (UDP) |
| 3. Network | Media Layer | Packet (Pacchetto) | Pacchetto di rete con indirizzi logici IP |
| 2. Data Link | Media Layer | Frame (Trama) | Trama con indirizzi fisici MAC e codici di controllo errore (CRC) |
| 1. Physical | Media Layer | Bits (Bit / Segnali) | Sequenza binaria grezza trasmessa sul mezzo fisico |

## 8. Le Sette Funzioni del Livello di Riferimento

| Livello OSI | Funzione | Competenze | Corrispondenza TCP/IP |
| :--- | :--- | :--- | :--- |
| **1. Fisico** | Trasmissione di bit grezzi non strutturati lungo il canale | Specifiche elettriche, ottiche, meccaniche; livelli di tensione; durata del bit; modulazione; connettori e cavi | Integrato nel Network Access Layer |
| **2. Collegamento Dati** | Trasferimento affidabile e privo di errori di trame tra nodi adiacenti sullo stesso canale | Indirizzamento fisico (MAC); controllo di flusso e di errore (CRC/FCS); sottolivelli LLC e MAC (IEEE) | Integrato nel Network Access Layer |
| **3. Rete** | Determinazione del cammino e instradamento dei pacchetti attraverso reti eterogenee | Indirizzamento logico gerarchico (IPv4/IPv6); tabelle di instradamento; frammentazione; controllo della congestione | Livello Internet (IP, ICMP, ARP) |
| **4. Trasporto** | Consegna trasparente, ordinata e affidabile da processo a processo (end-to-end) | Multiplexing/demultiplexing tramite porte; instaurazione e chiusura connessione; controllo di flusso; ritrasmissioni; controllo congestione | Livello Transport (TCP, UDP) |
| **5. Sessione** | Instaurazione, gestione, sincronizzazione e terminazione delle sessioni di dialogo | Gestione dei turni di dialogo (half-duplex o full-duplex); punti di sincronizzazione (*checkpoints*) | Integrato nel livello Application |
| **6. Presentazione** | Rappresentazione sintattica e semantica dei dati tra sistemi eterogenei | Conversione e normalizzazione dei formati (UTF-8, ASCII); crittografia/decifratura; compressione | Integrato nel livello Application |
| **7. Applicazione** | Interfaccia di comunicazione diretta ai processi e programmi utente | Protocolli applicativi specializzati (HTTP/HTTPS, DNS, SMTP/IMAP, SSH) | Livello Application (raggruppa 5, 6, 7) |

> [!EXAMPLE] Nota sul Livello Sessione in TCP/IP
> Il classico esempio di funzione di sessione assente in TCP/IP e lo stato mantenuto dal protocollo FTP: la sessione di controllo mantiene directory corrente e stato di autenticazione, funzionalita che nel modello OSI sarebbe appartenuta al livello Sessione.

## 9. Comunicazione End-to-End vs Inoltro di Rete

> [!IMPORTANT] Principio di Inoltro a Livello di Rete
> *"Network layer protocols forward encapsulated Transport Layer PDUs between hosts"*
> I protocolli dei livelli di trasporto e superiori operano **esclusivamente da estremo a estremo** tra i due host terminali. I protocolli del livello di rete inoltrano i pacchetti che incapsulano le PDU di trasporto attraversando la nuvola di rete mediante apparati intermedi (*hop-by-hop*).

### 9.1 Nodi Terminali (Host)

Implementano lo stack completo a 7 livelli (o tutti e 4 i livelli TCP/IP).

- Sul nodo sorgente, il messaggio applicativo **discende** l'intero stack, subendo l'incapsulamento progressivo fino al livello fisico.
- Sul nodo destinatario, il flusso di bit **risale** lo stack, subendo il processo inverso di decapsulamento fino al recapito all'applicazione.

### 9.2 Nodi Intermedi (Router)

Appartengono alla sottorete di comunicazione e implementano unicamente i tre **Media Layers**:

- **Livello 1 (Fisico):** riceve e trasmette i segnali e la sequenza di bit grezzi dai collegamenti fisici.
- **Livello 2 (Data Link):** acquisisce la trama, verifica l'integrita (CRC) e decapsula il pacchetto di rete rimuovendo header e trailer di livello 2.
- **Livello 3 (Network):** esamina l'indirizzo IP di destinazione, consulta la propria tabella di instradamento, seleziona l'interfaccia di uscita ottimale (*forwarding*) e re-incapsula il pacchetto in una nuova trama di livello 2 adatta al link successivo.

> [!WARNING] Trasparenza dei Nodi Intermedi
> I nodi intermedi sono del tutto trasparenti rispetto ai livelli 4-7: non ispezionano ne modificano i dati di trasporto o di applicazione, garantendo la netta separazione tra il trasporto dati dell'utente e l'infrastruttura di instradamento.

---

## ⏭️ Navigazione Lezioni
- **Modulo 2 - Lezione 1 :** [[01_Introduzione_Protocolli]] | *Lezione 2 :* [[02_Codifica_Dati_e_Flussi_Trasmissivi]]
- **Modulo 1 - Lezione 1 :** [[01_Introduzione_Architettura_Reti]]
- **Index Corso :** [[00_Index_Reti]]
