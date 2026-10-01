---
date: 2026-09-29
tags:
  - reti
type: lezione
---
# Codifica dei Dati, Flussi Trasmissivi e Valutazione delle Prestazioni di Rete

Questa lezione riprende il modello di riferimento ISO/OSI introdotto nella lezione precedente e scende al livello fisico, dove l'informazione diventa segnale. Vengono trattati i codici che consentono la rappresentazione digitale dell'informazione, le tre modalita di flusso trasmissivo, gli apparati che materializzano il collegamento (DTE, DCE, CPE) e infine i criteri e gli strumenti con cui si misura la qualita di una rete.

---

## 1. La Codifica dell'Informazione

### 1.1 Dal Carattere ai Codici

In un sistema elaborativo il carattere puo essere associato al singolo bit. Le sequenze significative di caratteri divengono quindi collezioni di bit all'interno di strutture di codifica denominate **codici**.

> [!IMPORTANT] La Quantita di Bit non e una Proprieta del Dato in Astratto
> Il numero di bit necessari per rappresentare un elemento dipende dalla **natura** dell'informazione, non dal concetto in astratto. Si consideri un'immagine, rappresentabile tramite una matrice di pixel: se ogni sequenza di bit deve rappresentare un pixel e il rispettivo colore, un'immagine a colori richiedera una quantita di bit per pixel superiore rispetto a una in bianco e nero, ove un singolo bit diventa sufficiente a rappresentare il colore del pixel. Piu l'insieme dei valori distinguibili e ampio, piu bit occorrono a ciascun elemento. E la stessa logica che presiede alla scelta dei codici testuali, dove l'ampiezza in bit e determinata dal numero di simboli distinti da rappresentare.

Tra i codici storici e ancora in uso:

- **BCD** (*Binary Decimal Code*)
- **AIKEN**
- **Gray**
- **EBCDIC** (*Extended Binary Coded Decimal Code*)
- **ASCII** (*American Standard Code for Information Interchange*)
- **UNICODE**

### 1.2 I Tre Codici Piu Usati

| Codice | Estensione | Note |
| :--- | :--- | :--- |
| **ASCII** (*American Standard Code for Information Interchange*) | 7 bit | Codice di base |
| **ASCII Extended** | 8 bit | Variante che introduce i caratteri accentati |
| **EBCDIC** (*Extended Binary Coded Decimal Code*) | 8 bit | Usato soprattutto dai sistemi IBM mainframe |
| **Unicode** (es. UTF-8) | variabile | Estensione che copre tutti i sistemi di scrittura |

> [!INFO] UTF-8 e Codifica a Lunghezza Variabile
> UTF-8 non e un codice a larghezza fissa: un carattere ASCII occupa 1 byte, i caratteri del set latino esteso 2 byte, quelli di altri alfabeti (greco, cirillico, arabo) 2-3 byte, i caratteri degli ideogrammi cinesi e delle emoji fino a 4 byte. Questa proprieta consente a un documento contenente prevalentemente testo italiano di rimanere byte-compatibile con il vecchio ASCII a 7 bit.

---

## 2. I Flussi Trasmissivi

Tra mittente e destinatario il flusso trasmissivo puo essere istituito secondo tre modalita, che si distinguono per il grado di bidirezionalita consentito.

| Tipo di Flusso | Schema | Comportamento | Esempio |
| :--- | :--- | :--- | :--- |
| **Simplex** | `A ---> B` | Solo uno dei dispositivi puo spedire informazione, mentre l'altro puo solo ricevere | Radio |
| **Half Duplex** | `<--->` | Ogni dispositivo puo sia trasmettere che ricevere, ma non contemporaneamente | Walkie-talkie |
| **Full Duplex** | `<--->` (2 canali) | Entrambi i dispositivi possono spedire e ricevere contemporaneamente, ottenendo bidirezionalita tramite 2 collegamenti fisici | Telefonia cellulare |

```text
SIMPLEX            HALF DUPLEX         FULL DUPLEX
                                      
 A ─────────► B    A ─────────► B      A ─────────► B
 (solo A tx)         A ◄─────────► B      A ◄─────────► B
                     (ma non insieme)     (contemporaneo, 2 link)
```

> [!INFO] La Progressione e Netta
> Il **simplex** azzera la bidirezionalita, l'**half duplex** la rende possibile ma mutuamente esclusiva (dato che i due dispositivi non possono operare contemporaneamente), il **full duplex** la rende simultanea su due collegamenti fisici distinti.

> [!EXAMPLE] Il Problema dell'Airtime nei Sistemi di Videosorveglianza
> Un flusso video 720p trasmesso 24 ore su 24 in full duplex consuma una quota significativa della banda disponibile. In impianti di videosorveglianza con piu telecamere, il collo di bottiglia non e il throughput del collegamento boccante, ma l'**airtime** della banda condivisa: ogni flusso deve ricevere una fetta di banda proporzionata al proprio bitrate.

> [!EXAMPLE] Duplex e Reti Mesh
> Nelle reti mesh wireless, i nodi devono trasmettere e ricevere simultaneamente per inoltrare i pacchetti verso i vicini. Senza la capacita full duplex, la trasmissione su un canale bloccherebbe la ricezione dello stesso canale, causando collisioni e crollo delle prestazioni. Per questo le tecnologie mesh moderne (802.11ax, reti wireless full-duplex) implementano soluzioni di duplexing avanzate.

---

## 3. Gli Apparecchi della Comunicazione: DTE, DCE e CPE

Il ruolo svolto da ciascun apparato lungo il canale di comunicazione e definito da una classe di sigla specifica.

> [!IMPORTANT] Le Tre Classi di Apparati
> - **DTE** (*Data Terminal Equipment*): il dispositivo informatico che permette la comunicazione dati (es. computer) e nel quale risiede l'applicazione utente.
> - **DCE** (*Data Circuit Terminating Equipment*, anche conosciuto come *Data Communication Equipment*): per connettersi alla linea si rende necessario un DCE, dispositivo che converte i segnali nella forma migliore per l'invio sul canale di comunicazione (es. modem).
> - **CPE** (*Customer Premises Equipment*): qualora sia richiesto un dispositivo di pertinenza dell'utente, solitamente inserito nell'abitazione del medesimo (es. reti ISDN, wireless o voice over IP), si parla di CPE.

> [!INFO] Il Ruolo della Rete di Comunicazione
> Il percorso tra due DTE non e l'unico elemento in gioco: e identificato dalla **rete di comunicazione**, che si interpone tra i due DTE e ne media il collegamento. Il DCE e l'apparato che adatta il segnale alla forma migliore per l'invio sul canale, e si colloca quindi **fra il terminale e la rete**: e questa distinzione DTE/DCE a consentire all'applicazione utente, ospitata nel DTE, di dialogare attraverso la rete.

```text
┌──────────┐    ┌──────────┐    ┌─────────────────────┐    ┌──────────┐
│   DTE    │◄──►│   DCE    │◄──►│  RETE DI COMUNICAZ. │◄──►│   DCE    │◄──►│   DTE    │
│  (applic. │    │ (adatta  │    │  (infrastruttura di  │    │ (adatta  │    │  (applic. │
│  utente) │    │ il segnale│    │  trasporto e routing)│    │ il segnale│    │  utente) │
└──────────┘    └──────────┘    └─────────────────────┘    └──────────┘    └──────────┘
   CPE (se di pertinenza dell'utente, es. modem/router domestico)
```

---

## 4. Le Reti e il loro Mondo

Si parla di **rete** intendendo un insieme di dispositivi connessi da canali di comunicazione. Una rete presenta uno o piu nodi capaci di inviare o ricevere dati, generati o ricevuti, da altri dispositivi o da altri nodi.

L'organizzazione delle funzioni computazionali all'interno della rete si articola in due modelli.

> [!IMPORTANT] I Due Modelli Organizzativi
> - **Reti ad elaborazione concentrata:** e il modello nativo per le reti telematiche; un potente DTE viene messo a disposizione di uno o piu DTE che ne sfruttano le capacita di calcolo.
> - **Reti ad elaborazione distribuita:** invece di essere un solo DTE a svolgere un compito, quest'ultimo viene diviso in varie parti, ognuna svolta da un nodo della rete.

### 4.1 Le Tre Procedure di Colloquio

Per entrambi i modelli proposti, il trasferimento dell'informazione tra DTE puo dare luogo a tre differenti procedure di colloquio.

| Procedura | Descrizione | Flessibilita concessa al DTE |
| :--- | :--- | :--- |
| **Inquiry** | Tipica forma di interrogazione ad uno o piu servizi messi a disposizione dal sistema elaborativo | Il DTE interroga uno o piu servizi |
| **Conversazionale** | Applicazione che permette al DTE di inviare tutte e sole quelle applicazioni previste secondo regole e formati di immissione preimpostati | Il DTE sceglie tra le applicazioni previste, ma deve rispettare regole e formati preimpostati |
| **Interattivo** | Risponde ad applicazioni flessibili; al DTE e permesso inviare tutte le applicazioni che consentono pieno sfruttamento di tutte le risorse elaborative | Pieno sfruttamento di tutte le risorse elaborative |

> [!INFO] Gradazione del Grado di Autonomia del DTE
> Le tre procedure si differenziano per la flessibilita concessa al terminale: nell'*inquiry* il DTE interroga uno o piu servizi messi a disposizione dal sistema elaborativo; nel *conversazionale* sceglie tra le applicazioni previste, ma deve rispettare regole e formati di immissione preimpostati; nell'*interattivo* ha il pieno sfruttamento di tutte le risorse elaborative.

---

## 5. Gli Aspetti di Valutazione di una Rete

La bonta della rete viene valutata in base a tre aspetti: **Affidabilita**, **Sicurezza** e **Prestazioni**.

### 5.1 Affidabilita

L'affidabilita di una rete e definita come la capacita della rete di:

- consegnare l'informazione priva di errori;
- porre rimedio a malfunzionamenti;
- essere robusta in situazioni critiche.

### 5.2 Sicurezza

La sicurezza di una rete ha come caratteristica principale la protezione dei dati che vengono gestiti all'interno della rete, al fine di impedire:

- accesso non autorizzato;
- modifiche non autorizzate;
- perdita di dati.

### 5.3 Prestazioni

Le prestazioni di una rete possono essere valutate misurando:

| Metrica | Definizione |
| :--- | :--- |
| **Ritardo** | Tempo di transito dei dati, ovvero tempo necessario a un dato messaggio per raggiungere la destinazione partendo dalla sorgente |
| **Tempo di risposta** | Tempo intercorrente tra il momento in cui si effettua una richiesta e il momento in cui arriva la risposta |
| **Throughput** | Quantita effettiva di dati spediti nell'unita di tempo (velocita) |

> [!IMPORTANT] Ritardo e Tempo di Risposta Misurano Cose Diverse
> Il **ritardo** e riferito al tempo di transito di un singolo messaggio, mentre il **tempo di risposta** e riferito all'intervallo fra una richiesta e la risposta ad essa corrispondente.

Le prestazioni dipendono anche da fattori strutturali, e non solo dalle misure stesse:

- numero di DTE presenti sulla rete;
- tipologia dei mezzi trasmissivi utilizzati;
- efficienza del software che gestisce la comunicazione.

### 5.4 La Banda

La **banda** e la banda passante di frequenze che puo essere utilizzata per la trasmissione di segnale attraverso un canale di comunicazione. Essendo collegata alla quantita d'informazione che puo essere inviata tramite quel segnale nell'unita di tempo, puo essere definita come la **massima velocita** alla quale e possibile trasmettere informazioni.

> [!INFO] Broadband e Digital Divide
> - **Broadband:** insieme di tecnologie che consentono di fornire all'utente collegamenti di velocita notevolmente superiore rispetto alla normale linea telefonica.
> - **Digital divide:** in presenza di disparita tra zone che dispongono o meno di accesso alla banda larga.

---

## 6. Gli Strumenti di Valutazione della Velocita

### 6.1 Il Comando `ping`

Il comando `ping` indica se un host remoto puo essere raggiunto. Puo essere utilizzato anche per riportare statistiche sui pacchetti persi e sul tempo di spedizione: fa uso dell'*Echo message* del protocollo **ICMP** (*Internet Control Message Protocol*) per forzare un host remoto a rispedire indietro all'host locale un pacchetto a lui inviato.

```bash
ping 141.250.5.2
PING 141.250.5.2 (141.250.5.2): 56 data bytes
64 bytes from 141.250.5.2: icmp_seq=0 ttl=64 time=0.352 ms
64 bytes from 141.250.5.2: icmp_seq=1 ttl=64 time=0.474 ms
^C
--- 141.250.5.2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.352/0.413/0.474/0.061 ms
```

> [!INFO] Comportamento del Comando
> Il comando riporta il tempo di trasmissione in millisecondi (ms) e si interrompe da solo oppure con i tasti `Ctrl+C`. Il comportamento cambia in funzione dello stato dell'host di destinazione: se l'host e situato su una rete inesistente si ottiene un errore immediato, mentre se l'host esiste ma non risponde il pacchetto resta in attesa fino all'interruzione.

```bash
# Host su rete inesistente -> errore immediato
ping 26.40.0.17
sendto: Network is unreachable

# Host esistente ma irraggiungibile -> attesa fino all'interruzione
ping 141.250.233.1
PING 141.250.233.1 (141.250.233.1): 56 data bytes
^C
--- 141.250.233.1 ping statistics ---
131 packets transmitted, 0 packets received, 100% packet loss
```

> [!IMPORTANT] I Due Parametri da Controllare nel Ping
> - **Packet Loss:** dovrebbe sempre essere pari a zero. In caso contrario ci potrebbe essere un problema alla connessione oppure, piu probabilmente, che il sito contattato sia congestionato o, al limite, disconnesso dalla rete.
> - **Round Trip Time:** per una buona connessione Internet dovrebbe essere dell'ordine di qualche millisecondo. Se questo parametro assumesse valori a tre cifre, indicherebbe un problema della vostra connessione Internet o uno piu generalizzato sulla rete.

### 6.2 Il Comando `traceroute`

Il comando `traceroute` (o `tracert` su Windows) dice quale instradamento prendono i pacchetti in uscita dal nostro sistema verso un sistema remoto. Mostra tutti i dispositivi di rete attraversati (nome e indirizzo tra parentesi) per arrivare a destinazione e da l'idea della "distanza" (in termini di numero di dispositivi attraversati, *hops*) che ci separa da essa.

```bash
traceroute 141.250.1.3
traceroute to 141.250.1.3 (141.250.1.3), 64 hops max, 40 byte packets
 1  gw25.dipmat.unipg.it (141.250.25.3)  2.556 ms 3.264 ms 4.534 ms
 2  141.250.115.77 (141.250.115.77)    4.220 ms 2.844 ms 2.996 ms
 3  fe.r.unipg.it (141.250.253.1)      3.856 ms 17.168 ms 3.464 ms
 4  sw-cs.r.unipg.it (141.250.253.21)  3.758 ms 2.281 ms 3.709 ms
```

> [!INFO] Lettura dell'Output
> Ogni riga corrisponde a un *hop*: il numero di righe fino a destinazione e il numero di dispositivi attraversati, e ciascun valore e il round trip verso quel dispositivo.

### 6.3 Speed Test

Per verificare la velocita effettiva della connessione si puo utilizzare il sito web **www.speedtest.net**.

> [!EXAMPLE] Come Funziona lo Speed Test
> Sul territorio italiano sono sparsi vari server di test: ne viene scelto uno, il piu vicino, e si da avvio alla prova. In un minuto si ottiene il risultato del test, con ping, velocita in download e in upload. Il server puo essere scelto anche automaticamente in base al ping: basta cliccare "Inizia Test" e sara direttamente il sistema a scegliere il server migliore.

---

## 7. Riepilogo

| Concetto | Definizione |
| :--- | :--- |
| **Codice** | Struttura che associa un valore a una sequenza di bit (ASCII 7 bit, ASCII Extended ed EBCDIC 8 bit, Unicode variabile) |
| **Flusso Simplex** | Unidirezionale: solo uno dei dispositivi trasmette |
| **Flusso Half Duplex** | Bidirezionale ma mutuamente esclusiva |
| **Flusso Full Duplex** | Bidirezionale e simultanea su due collegamenti fisici |
| **DTE** | Dispositivo terminale che risiede l'applicazione utente |
| **DCE** | Dispositivo che adatta il segnale per la trasmissione sul canale |
| **CPE** | Apparato di pertinenza dell'utente, spesso nella sua abitazione |
| **Ritardo** | Tempo di transito di un singolo messaggio |
| **Tempo di risposta** | Intervallo fra una richiesta e la risposta corrispondente |
| **Throughput** | Quantita effettiva di dati trasmessi nell'unita di tempo |

---
## ⏭️ Navigazione Lezioni
- **Modulo 2 - Lezione 1 :** [[01_Introduzione_Protocolli]]
- **Index Corso :** [[00_Index_Reti]]