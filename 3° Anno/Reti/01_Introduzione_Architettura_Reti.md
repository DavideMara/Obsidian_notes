---
date: 2026-09-22
tags:
  - reti
type: lezione
---
# Introduzione all'Architettura delle Reti di Calcolatori

> [!INFO] Informazioni sul Corso e Modalità d'Esame
> * **Docente:** Prof. Osvaldo Gervasi
> * **Email:** `osvaldo.gervasi@unipg.it` /
> * **Affiliazione:** Dipartimento di Matematica e Informatica, Università degli Studi di Perugia.
> * **Testi di Riferimento Consigliati:**
>   * Andrew S. Tanenbaum — *Reti di Computer*, UTET / Prentice Hall International (ISBN 88-7750-453-6).
>   * Douglas Comer — *Internetworking con TCP/IP: Principi, protocolli, Architettura*, Jackson / Prentice Hall (ISBN 88-256-0346-0).
>   * Dispense e materiale didattico forniti dal docente.
> * **Modalità d'Esame:**
>   * 

---

## I. Contesto Tecnologico e Pervasività delle Reti

Una **rete di calcolatori** è un sistema distribuito di nodi autonomi (host, server, router, dispositivi terminali) interconnessi mediante canali di trasmissione fisici o wireless, regolati da protocolli di comunicazione standard per consentire la condivisione affidabile di risorse e l'elaborazione cooperativa dell'informazione.

```
┌─────────────────┐                                  ┌─────────────────┐
│ Host / Terminal │◄────┐                      ┌────►│  Cloud / Server │
└─────────────────┘     │                      │     └─────────────────┘
                        ▼                      ▼
┌─────────────────┐  ┌────────────────────────────┐  ┌─────────────────┐
│   Dispositivo   │◄─┤    Infrastruttura di Rete  ├─►│  Dispositivi    │
│    Aziendale    │  │    (Switch, Router, WAN)   │  │   IoT / Edge    │
└─────────────────┘  └────────────────────────────┘  └─────────────────┘
```

### Ambiti Chiave e Driver Architetturali
* **Reti Aziendali (Enterprise Networks):** Infrastrutture progettate per garantire alta disponibilità, segmentazione sicura del traffico (VLAN, subnetting), ridondanza dei link e politiche di controllo degli accessi.
* **Servizi Cloud:** Paradigma di erogazione elastica di risorse computazionali, archiviazione e connettività (IaaS, PaaS, SaaS) accessibili ubiquitamente via rete.
* **Internet of Things (IoT):** Pervasività di micro-dispositivi sensori e attuatori con vincoli stringenti di banda ed energia, integrati nello spazio di indirizzamento globale.
* **Evoluzione della Fruizione dei Servizi:** Passaggio da modelli monolitici centralizzati a pattern computazionali fortemente distribuiti, interattivi e basati sul web.

---

## II. Aspetti Etici, Giuridici, Economici e Open Standards

Lo studio dell'architettura di rete non si limita ai soli strati fisici e di trasporto, ma abbraccia le implicazioni su sovranità digitale, protezione dei dati e standard aperti.

```
                            ┌─────────────────────────────────────────┐
                            │    ECOSISTEMA APERTO E SOSTENIBILE      │
                            └────────────────────┬────────────────────┘
                                                 │
            ┌────────────────────────────────────┼────────────────────────────────────┐
            ▼                                    ▼                                    ▼
┌───────────────────────┐            ┌───────────────────────┐            ┌───────────────────────┐
│         FLOSS         │            │    OPEN STANDARDS     │            │  5-STAR OPEN DATA     │
│ Software Libero e     │            │ Specifiche e RFC      │            │ Formati aperti, URIs, │
│ Codice Ispezionabile  │            │ aperte non vincolate  │            │ Linked Open Data      │
└───────────────────────┘            └───────────────────────┘            └───────────────────────┘
```

### 1. Privacy, Profilazione e Modello Economico dei Servizi Gratuiti
* **Monetizzazione dei Dati:** I servizi telematici gratuiti per l'utente finale sostengono i propri costi infrastrutturali tramite la profilazione comportamentale, la raccolta massiva di metadati di navigazione e la vendita mirata di annunci pubblicitari (*"Se non stai pagando per il prodotto, il prodotto sei tu"*).
* **Tutele e Privacy by Design:** Necessità di protocolli cifrati, strumenti di anonimizzazione e rispetto dei quadri normativi (es. GDPR) per mitigare il tracciamento indiscriminato.

### 2. FLOSS (Free Libre Open Source Software) e Open Standards
* **FLOSS:** Software distribuito con licenze che garantiscono le quattro libertà fondamentali (uso per qualsiasi scopo, studio del codice sorgente, modifica e redistribuzione). Garantisce trasparenza, audit di sicurezza indipendenti e assenza di vendor lock-in.
* **Open Standards:** Specifiche tecniche pubbliche e liberamente implementabili (es. le RFC dell'IETF) che costituiscono l'ossatura dell'interoperabilità globale di Internet.
* **Modello Open Data a 5 Stelle (Tim Berners-Lee):**
  1. $\star$: Dati pubblicati sul web con licenza aperta in qualsiasi formato (es. scansione PDF).
  2. $\star\star$: Dati strutturati e machine-readable (es. foglio di calcolo Excel).
  3. $\star\star\star$: Dati in formati non proprietari (es. CSV, JSON, XML).
  4. $\star\star\star\star$: Dati conformi agli standard W3C (RDF/SPARQL), identificati univocamente da URI.
  5. $\star\star\star\star\star$: Dati collegati (*Linked Data*) ad altri dataset per creare un grafo di conoscenza semantico.

> [!INFO] Codice dell'Amministrazione Digitale (CAD)
> Il **CAD** (D.Lgs. 82/2005 e successive modifiche) è il quadro normativo italiano che impone alla Pubblica Amministrazione l'adozione prioritaria di software libero, standard aperti e formati interoperabili per garantire l'accessibilità e la sovranità sui dati pubblici.

---

## III. Architettura a Livelli e Suite di Protocolli

La complessità della comunicazione eterogenea su scala planetaria viene gestita mediante una strutturazione a strati gerarchici (*layering*), in cui ogni livello offre un insieme ben definito di servizi al livello superiore incapsulando i dettagli implementativi inferiori.

```
      MODELLO ISO/OSI (7 LIVELLI)                 SUITE TCP/IP (4 LIVELLI)
  ┌─────────────────────────────────┐           ┌─────────────────────────────┐
7 │ 7. Applicazione                 │           │                             │
  ├─────────────────────────────────┤           │ 4. Applicazione             │
6 │ 6. Presentazione                │──────────►│    (HTTP, DNS, SSH, SMTP)   │
  ├─────────────────────────────────┤           │                             │
5 │ 5. Sessione                     │           │                             │
  ├─────────────────────────────────┤           ├─────────────────────────────┤
4 │ 4. Trasporto (Segmento)         │──────────►│ 3. Trasporto (TCP, UDP)     │
  ├─────────────────────────────────┤           ├─────────────────────────────┤
3 │ 3. Rete / Network (Pacchetto)   │──────────►│ 2. Internet / Rete (IP)     │
  ├─────────────────────────────────┤           ├─────────────────────────────┤
2 │ 2. Collegamento Dati (Frame)    │──────────►│ 1. Accesso alla Rete        │
  ├─────────────────────────────────┤           │    (Ethernet, Wi-Fi, MAC,   │
1 │ 1. Fisico (Bit stream)          │──────────►│     interfacce fisiche)     │
  └─────────────────────────────────┘           └─────────────────────────────┘
```

---

## IV. Modello TCP/IP: Livello di Rete e Trasporto

### 1. Livello di Rete (Internet Layer)
* **IPv4 vs IPv6:**
  * **IPv4:** Indirizzamento a 32 bit ($\approx 4.3 \times 10^9$ indirizzi univoci), frammentazione a livello di router/host, dipendenza da tecniche NAT (*Network Address Translation*) per contrastare l'esaurimento dello spazio di indirizzamento.
  * **IPv6:** Indirizzamento a 128 bit ($2^{128}$ indirizzi), header semplificato a lunghezza fissa, supporto nativo all'autoconfigurazione stateless (SLAAC) e sicurezza integrata (IPsec).
* **Protocolli Ausiliari di Livello Rete:**
  * **ARP (Address Resolution Protocol):** Mappatura dinamica da indirizzo logico di rete (IPv4) a indirizzo fisico MAC (Livello 2).
  * **RARP (Reverse ARP):** Risoluzione inversa (da indirizzo MAC ad indirizzo IP, storicamente usato per host diskless).
  * **ICMP (Internet Control Message Protocol):** Gestione della diagnostica, messaggi di errore e controllo operativo (utilizzato da tool come `ping` e `traceroute`).

### 2. Livello di Trasporto (Transport Layer)
* **UDP (User Datagram Protocol):** Protocollo non orientato alla connessione (*connectionless*), non affidabile, privo di controllo di flusso o congestione. Offre overhead minimo e latenza ridotta (adatto per streaming multimediale, DNS, VoIP).
* **TCP (Transmission Control Protocol):** Protocollo orientato alla connessione (*connection-oriented*), affidabile, basato su handshaking a tre vie (*3-Way Handshake*), ordinamento dei byte stream, riscontri (ACK), ritrasmissione su timeout, controllo di flusso (sliding window) e algoritmi di controllo della congestione.

---

## V. Instradamento e Architettura del Routing

Il **Routing IP** consente di determinare il percorso ottimale che un datagramma deve attraversare dalla sorgente alla destinazione attraverso nodi intermedi (router).

```
   ┌────────────────────────────────────────────────────────┐
   │             Autonomous System (AS 100)                 │
   │                                                        │
   │      [Router A] ──(IGP: OSPF/RIP)── [Router B]         │
   └──────────────────────────┬─────────────────────────────┘
                              │
                        (EGP: BGP-4)
                              │
   ┌──────────────────────────┴─────────────────────────────┐
   │             Autonomous System (AS 200)                 │
   │                                                        │
   │      [Router C] ──(IGP: OSPF/RIP)── [Router D]         │
   └────────────────────────────────────────────────────────┘
```

### Classificazione del Routing
1. **Routing Statico:** Tabelle di instradamento configurate manualmente dall'amministratore di rete.
2. **Routing Dinamico:** Algoritmi distribuiti con cui i router scambiano informazioni topologiche per adattarsi automaticamente a variazioni di carico o guasti:
   * **IGP (Interior Gateway Protocol):** Protocolli utilizzati per l'instradamento all'interno di un singolo dominio amministrativo o **Autonomous System (AS)** (es. RIP basato su *Distance Vector*, OSPF basato su *Link State*).
   * **EGP (Exterior Gateway Protocol):** Protocolli utilizzati per scambiare informazioni di raggiungibilità e applicare politiche di instradamento tra distinti Autonomous System su scala Internet globale (es. **BGP - Border Gateway Protocol**).

---

## VI. Servizi Applicativi di Rete

I protocolli del livello applicativo erogano i servizi fondamentali per gli utenti finali e per la gestione infrastrutturale:

| Servizio / Protocollo | Protocollo di Trasporto | Porta Standard | Descrizione Funzionale |
| :--- | :---: | :---: | :--- |
| **DNS** (*Domain Name System*) | UDP / TCP | 53 | Risoluzione gerarchica distribuita di nomi simbolici (FQDN) in indirizzi IP. |
| **DHCP** (*Dynamic Host Configuration*) | UDP | 67 (Server) / 68 (Client) | Assegnazione automatica e dinamica di parametri di rete (IP, subnet mask, gateway, server DNS). |
| **HTTP / HTTPS** | TCP | 80 / 443 | Trasferimento di risorse ipertestuali e multimediali del World Wide Web (HTTPS cifrato con TLS). |
| **Posta Elettronica** (SMTP / IMAP / POP3) | TCP | 25, 587 (SMTP) / 143, 993 (IMAP) / 110, 995 (POP3) | Invio (SMTP) e ricezione/sincronizzazione remota (IMAP/POP3) di messaggi di posta elettronica. |
| **SSH** (*Secure Shell*) | TCP | 22 | Canale cifrato sicuro per login remoto a riga di comando ed esecuzione di comandi. |
| **NTP** (*Network Time Protocol*) | UDP | 123 | Sincronizzazione precisa dei clock di sistema tra host su reti a latenza variabile. |
| **One-Time Login / SSO** | TCP / HTTPS | Variabile | Meccanismi federati o token-based (OAuth2, SAML, Kerberos) per autenticazione centralizzata. |
| **NFS** (*Network File System*) | TCP / UDP | 2049 | File system distribuito per la condivisione trasparente di storage tra sistemi remoti. |
| **SNMP** (*Simple Network Management*) | UDP | 161 / 162 | Monitoraggio dello stato operativo, raccolta metriche e configurazione remota dei dispositivi di rete. |

---

## VII. Sicurezza, Reti Locali (LAN) e Geografiche (WAN)

### 1. Sicurezza di Rete
* **Firewall:** Dispositivi o software di filtraggio dei pacchetti in transito, basati sull'analisi degli header di livello 3/4 (stateless/stateful packet inspection) o su proxy a livello applicativo.
* **Transazioni Protette (SSL/TLS):** Protocolli crittografici che garantiscono riservatezza (*confidentiality*), integrità dei dati (*integrity*) e autenticazione bilaterale (*authentication*) tra entità comunicanti.
* **Strumenti di Anonimizzazione:** Reti di instradamento a cipolla (es. Tor, proxy relay) per disaccoppiare l'identità dell'utente dall'indirizzo IP di destinazione.
* **Tipi di Attacco e Analisi del Rischio:**
  * *Eavesdropping / Sniffing:* Intercettazione passiva di traffico in chiaro.
  * *Spoofing / Man-in-the-Middle (MitM):* Falsificazione dell'identità di mittente/destinatario.
  * *Denial of Service (DoS / DDoS):* Saturazione mirata delle risorse computazionali o di banda del target.
  * *Risk Assessment:* Identificazione delle vulnerabilità, quantificazione dell'impatto e definizione delle contromisure.

### 2. Tecnologie di Rete Locale (LAN) e Geografica (WAN)
* **Reti Locali (LAN):** Basate prevalentemente sullo standard **IEEE 802.3 (Ethernet)** e le sue evoluzioni ad alta velocità (Fast Ethernet, Gigabit Ethernet, 10GbE), con gestione delle collisioni (*CSMA/CD* sui bus condivisi, soppiantato dallo switching full-duplex).
* **Reti Geografiche (WAN):** Infrastrutture di dorsale che collegano LAN distanti geograficamente tramite linee dedicate, circuiti commutati, fibre ottiche e reti di provider di livello 1 (*Tier-1 ISP*).

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Reti]]
