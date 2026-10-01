---
date: 2026-09-24
tags:
  - sicurezza-informatica
type: lezione
---
# Introduzione alla Sicurezza Informatica

> [!INFO] Comunicazioni del Corso
> - **Sospensione lezioni:** Dal 5 al 9 ottobre le lezioni sono sospese per la conferenza **AIxIA 2026** (eventi satellite previsti nel pomeriggio, es. panel "Impresa nell'era dell'IA").

---

## 1. Natura e Principi della Sicurezza

La sicurezza informatica non coincide con un singolo prodotto software o hardware, ma rappresenta un **processo continuo e multilivello** che coinvolge persone, procedure, configurazioni e tecnologie.

* **Processo, non prodotto:** L'adozione di strumenti isolati (come l'installazione di un firewall o di un antivirus) non rende di per sé un'infrastruttura sicura senza una corretta gestione operativa e di monitoraggio nel tempo.
* **Principio dell'anello più debole (*Weakest Link*):** Il livello di sicurezza complessivo di un sistema coincide con quello del suo componente o anello più vulnerabile (spesso costituito dal fattore umano o da configurazioni errate).
* **Natura non booleana:** Non esiste uno stato binario di "sistema sicuro al 100%" o "sistema insicuro". La sicurezza si misura sempre su una scala continua (livello di rischio accettabile) ed è strettamente **contestuale** rispetto al valore degli asset da proteggere e al modello di minaccia considerato.
* **Costo architetturale:** Implementare la sicurezza comporta un trade-off in termini di risorse computazionali, complessità di gestione, usabilità e costi economici. Molti protocolli e architetture storiche non erano nativamente progettati con requisiti di sicurezza, rendendo spesso necessario un ripensamento dell'intero design.

> [!NOTE] Sicurezza vs Crittografia
> La **crittografia** è una scienza esatta fondata su rigorosi principi matematici e complessità computazionale (es. l'impossibilità pratica di invertire RSA in tempo polinomiale). La **sicurezza**, al contrario, è una scienza inesatta ed empirica perché determinata dall'interazione imperfetta tra esseri umani, codice software, ambienti operativi e macchine.

### Falsi Miti sulla Sicurezza
* **Non è solo crittografia:** Un canale cifrato non protegge se gli endpoint sono compromessi o se la chiave privata viene sottratta.
* **Non è solo una password:** L'adozione di credenziali deboli, il riutilizzo di password tra servizi o gli attacchi a dizionario/brute-force vanificano i meccanismi di accesso.
* **Non è solo un firewall:** Il firewall filtra esclusivamente il traffico di rete secondo regole preimpostate, ma non blocca vulnerabilità a livello applicativo (es. bug logici o injection) che transitano su porte autorizzate (es. HTTP/HTTPS).

---

## 2. Definizioni: Computer Security, Cybersecurity e Information Assurance

La letteratura tecnica e gli standard di settore distinguono tre concetti strettamente correlati:

```
+-------------------------------------------------------------+
|                    Information Assurance                    |
|  (Governance, conformità, controlli tecnici e manageriali)  |
|                                                             |
|   +-----------------------------------------------------+   |
|   |                    Cybersecurity                    |   |
|   |     (Protezione dello spazio cibernetico e reti)    |   |
|   |                                                     |   |
|   |   +---------------------------------------------+   |   |
|   |   |              Computer Security              |   |   |
|   |   | (Protezione di risorse, host, SO e dati)    |   |   |
|   |   +---------------------------------------------+   |   |
|   +-----------------------------------------------------+   |
+-------------------------------------------------------------+
```

### Computer Security
Insieme di misure e controlli tecnici volti a garantire la protezione delle **risorse del sistema di elaborazione** (hardware, software, firmware, telecomunicazioni) e delle **informazioni** elaborate, memorizzate o trasmesse, prevenendo accessi, alterazioni o distruzioni non autorizzate.

### Cybersecurity
La capacità di proteggere, difendere e mitigare gli attacchi rivolti alle infrastrutture, ai servizi e agli utenti all'interno dello **spazio cibernetico** (*cyberspace*).

### Information Assurance (IA)
Insieme integrato di controlli tecnici, organizzativi e manageriali finalizzati a garantire confidenzialità, integrità, disponibilità, autenticità, non ripudio e controllo dei flussi informativi e dei relativi sistemi di gestione all'interno di un'organizzazione.

---

## 3. Pervasività delle Reti e Minacce Moderne

L'evoluzione tecnologica ha reso i sistemi informatici pervasivi e costantemente interconnessi, ampliando esponenzialmente la superficie di attacco (*attack surface*):
* **Ambiti critici interconnessi:** Dispositivi IoT, Industria 4.0, infrastrutture critiche (reti elettriche, acquedotti), servizi della Pubblica Amministrazione e settore bancario/finanziario.

### Caratteristiche delle Minacce Moderne
1. **Automazione e scala:** Gli attaccanti possono automatizzare violazioni di massa o micro-frodi (es. sottrarre frazioni minime di centesimo su milioni di transazioni) agendo quasi senza lasciare tracce evidenti.
2. **Assenza di confini fisici:** La rete azzera la distanza geografica. Un attacco condotto da giurisdizioni prive di accordi di estradizione o con normative cyber deboli crea un forte disallineamento tra il luogo dell'offesa e le leggi nazionali applicabili.
3. **Diffusione di tool e script (*Script Kiddies*):** La rapida propagazione di exploit, crack e script di attacco (es. tool per attacchi DoS o leak di codice sorgente) consente anche ad attaccanti privi di elevate competenze tecniche di condurre attacchi ad alto impatto.

### Tipologie Comuni di Minaccia
* **Identity Theft:** Furto e impersonificazione di identità digitali.
* **Data Breach:** Esfiltrazione o esposizione non autorizzata di database sensibili.
* **Ransomware:** Cifratura malevola dei dati con richiesta di riscatto per il ripristino.
* **Denial of Service (DoS / DDoS):** Saturazione delle risorse per interrompere l'erogazione di un servizio.
* **Attacchi Cyber-Fisici:** Manomissione di sistemi industriali o reti di controllo operativo (SCADA/ICS).
* **Cyberterrorismo e Spionaggio Industriale/Statale.**

---

## 4. Domini di Protezione e Piano di Sicurezza

La difesa di un'infrastruttura si articola su **cinque livelli di sicurezza**:

1. **Physical Security:** Controllo e protezione dell'accesso fisico alle macchine, ai datacenter e agli apparati di rete.
2. **Operational / Procedural Security:** Definizione di policy aziendali, procedure operative standard e linee guida per la gestione sicura.
3. **Personnel Security:** Formazione del personale, consapevolezza contro il *social engineering*, gestione dei privilegi e controllo del fattore umano.
4. **System Security:** Hardening del sistema operativo, gestione dei privilegi minimi, Access Control List (ACL) e tracciamento dei log.
5. **Network Security:** Monitoraggio e filtraggio del traffico di rete tramite firewall, router screening, sistemi IDS/IPS e canali cifrati (VPN, TLS).

### Fasi del Piano di Sicurezza (Gestione del Rischio)
Poiché il rischio zero non esiste, la sicurezza mira alla riduzione e mitigazione del rischio attraverso un approccio strutturato:

* **Risk Avoidance (Evitamento del rischio):** Valutare l'effettiva necessità di esporre determinati servizi (es. eliminare accessi diretti a Internet se non indispensabili).
* **Deterrence (Deterrenza):** Pubblicizzare la presenza di controlli, misure difensive e relative conseguenze legali/disciplinari per scoraggiare potenziali malintenzionati.
* **Prevention (Prevenzione):** Adozione di contromisure attive (firewall, patch di sistema, segmentazione della rete) per bloccare a monte i tentativi di intrusione.
* **Detection (Rilevamento):** Monitoraggio continuo e analisi delle anomalie nel traffico o negli accessi (es. tramite Intrusion Detection Systems).
* **Reaction & Recovery (Reazione e Ripristino):** Procedure di incidente response per isolare la minaccia, ripristinare i backup e intraprendere eventuali azioni legali/forensi.

> [!EXAMPLE] Risk Avoidance in Ambito Industriale
> Un sistema industriale SCADA critico che non necessita di un collegamento permanente a Internet puo essere disconnesso dalla rete pubblica, eliminando alla radice l'esposizione al rischio. E una scelta architetturale, non una contromisure tecnica.

---

## 5. Contromisure Tecnologiche contro gli Attacchi

Per contrastare efficacemente gli attacchi informatici si impiegano soluzioni tecniche integrate, che agiscono su piu fronti simultaneamente.

| Contromisura | Funzione | Esempi concreti |
| :--- | :--- | :--- |
| **Segmentazione della rete** | Suddividere la rete in zone con differenti livelli di fiducia | VLAN separate, **DMZ** (*Demilitarized Zone*) per isolare i server pubblici dalla rete interna, router e switch layer 3 / gestiti |
| **Hardening e integrita applicativa** | Ridurre la superficie d'attacco del codice e dei sistemi | *Secure Coding*, analisi statica e dinamica del codice, disabilitazione dei servizi superflui, verifica delle configurazioni di OS e server |
| **Filtraggio dei flussi di traffico** | Ispezionare, filtrare e bloccare il traffico anomalo | Firewall *packet filter*, *stateful inspection*, *application firewall*, router *screening* |
| **Crittografia e canali sicuri** | Cifrare i dati prima della trasmissione su canali non protetti | SSH per amministrazione remota, TLS/SSL per il traffico web, PGP/GPG per email e file, VPN con IPsec/OpenVPN per tunnel cifrati |

> [!WARNING] Perche il Firewall da Solo Non Basta
> Il firewall filtra esclusivamente il traffico di rete secondo regole preimpostate, ma **non blocca vulnerabilita a livello applicativo** (es. bug logici o injection) che transitano su porte gia autorizzate (es. HTTP/HTTPS). Per questo una difesa efficace richiede la combinazione di segmentazione, hardening e filtraggio, non un singolo apparato.

---

## 6. Proprietà di Sicurezza: La Triade CIA e il Modello Esteso CIAAA

I requisiti fondamentali di sicurezza vengono modellati storicamente dalla **Triade CIA**, estesa con le proprietà di **Autenticità** e **Tracciabilità** (**CIAAA**).

```
                  +-------------------------+
                  |    CIAAA Framework      |
                  +-------------------------+
                  |  C - Confidentiality    |
                  |  I - Integrity          |
                  |  A - Availability       |
                  |  A - Authenticity       |
                  |  A - Accountability     |
                  +-------------------------+
```

### 1. Confidentiality (Confidenzialità / Riservatezza)
Garantisce che i dati siano accessibili (**in lettura**) esclusivamente alle entità (utenti, processi) esplicitamente autorizzate.
* **Esempi:** Protezione di cartelle cliniche e dati personali (GDPR), cifratura dei dati delle carte di credito durante i pagamenti online, isolamento di tabelle riservate in un database.

### 2. Integrity (Integrità)
Garantisce che le informazioni e le configurazioni di sistema possano essere create, modificate o cancellate (**in scrittura**) soltanto da entità autorizzate e secondo modalità ammesse.
* **Esempi:** Impossibilità di alterare arbitrariamente i saldi di un conto corrente o i beneficiari di un bonifico bancario; garanzia che il firmware e i binari di sistema non siano stati manomessi.

### 3. Availability (Disponibilità)
Garantisce che i dati, i sistemi e i servizi di rete siano accessibili e utilizzabili tempestivamente dagli utenti autorizzati ogni qualvolta sia richiesto.
* **Esempi:** Continuità operativa di infrastrutture critiche (reti elettriche, sistemi sanitari), garanzia di Quality of Service (QoS) per chirurgia remota, resilienza dei servizi di voto elettronico e cloud contro attacchi di disservizio (DoS).

### 4. Authenticity (Autenticità)
Garantisce la capacità di verificare in modo certo l'identità dichiarata di un'entità (utente, dispositivo o sorgente del messaggio).
* **Esempi:** Procedure di login con autenticazione forte (MFA), verifica della provenienza dei messaggi email (SPF, DKIM), convalida del PIN presso un ATM.

> [!NOTE] Identificazione vs Autenticazione
> * **Identificazione:** L'atto in cui un soggetto dichiara la propria identità al sistema (es. inserimento dello *username*).
> * **Autenticazione:** Il processo con cui il sistema verifica e valida la prova dell'identità fornita dal soggetto (es. verifica della *password*, token OTP, impronta biometrica).
> È essenziale analizzare e prevenire scenari anomali in cui l'accesso viene concesso tramite autenticazione senza una corretta e vincolante fase di identificazione preliminare.

### 5. Accountability (Tracciabilità / Non Ripudio)
Garantisce che ogni azione, evento o transazione eseguita all'interno del sistema possa essere ricondotta in modo univoco all'entità responsabile, impedendo che questa possa negare l'azione compiuta (*non ripudio*).
* **Esempi:** Firme digitali su contratti o transazioni legali, log di audit immutabili e protetti, generazione di prove forensi (*digital forensics*) valide in sede giudiziaria.

### 6. Possesso o Controllo (Possession / Control)
Capacita del legittimo proprietario di esercitare il pieno controllo logico e fisico sui propri dati e sulle proprie infrastrutture.

### 7. Utilita (Utility)
Garanzia che le informazioni conservino la propria forma utile e fruibile.

> [!WARNING] Il paradosso della Utilita
> Dati cifrati la cui chiave di decifratura e andata perduta **restano confidenziali e integri**, ma perdono totalmente la propria utilita. Le tre dimensioni centrali (C, I, A) possono essere perfettamente soddisfatte mentre il sistema e practically inservibile: la sicurezza e una funzione multi-obiettivo, non un insieme di requisiti monotonicamente migliorabili.

---

## 7. Il Modello IAAA: Controllo degli Accessi

Il controllo degli accessi poggia su **quattro pilastri logici distinti ma interconnessi**.

| Pilastro | Definizione | Esempi |
| :--- | :--- | :--- |
| **Identificazione** (*Identification*) | Associazione formale tra un'entita logica (account) e la reale identita civile nel mondo fisico | Documento di riconoscimento, SPID, verifica notarile |
| **Autenticazione** (*Authentication*) | Validazione delle credenziali o evidenze fornite per dimostrare di essere chi si afferma di essere | Username e password, certificati digitali, token OTP, fattori biometrici |
| **Autorizzazione** (*Authorization*) | Determinazione e attribuzione dei privilegi operativi e dei diritti di accesso a specifiche risorse | Definizione di cosa l'utente autenticato puo leggere, modificare o eseguire |
| **Accounting** (*Auditing & Accountability*) | Monitoraggio e registrazione continuativa delle azioni svolte nel sistema | Registri di audit e log immutabili |

```text
[ Identificazione / Anagrafica ]
                 ↓
[ Autenticazione (Credenziali) ] ──► [ Autorizzazione (Policy & ACL) ] ──► [ Accounting (Log & Audit) ]
```

> [!INFO] Nota del Prof: Autenticazione vs Identificazione
> Nei sistemi informatici l'**autenticazione precede la verifica operativa dei permessi**: un utente fornisce credenziali (es. username/password o token) per autenticare la propria sessione prima che il sistema ne verifichi i diritti o ne colleghi formalmente l'identita. Le due fasi sono distinte ma non intercambiabili.

> [!EXAMPLE] Autenticazione Senza Identificazione
> Esistono scenari in cui un sistema effettua un'autenticazione valida **senza** procedere all'identificazione nominale della persona fisica:
> - **Blockchain e criptovalute:** le transazioni sono autenticate mediante firma crittografica con chiave privata senza richiedere l'identita anagrafica del firmatario (garantendo pseudonimato).
> - **Badge e token di accesso fisico anonimi:** biglietti elettronici, gettoni o badge numerati validano il diritto di ingresso (*autenticazione del titolo*) senza identificare l'individuo.
> - **Zero-Knowledge Proofs (ZKP):** protocolli che consentono di dimostrare di possedere un attributo valido (es. essere maggiorenne o iscritto a un servizio) **senza rivelare la propria identita**.

---

## 8. Riepilogo: Confini Concettuali

```text
┌─────────────────────────────────────────────────────────┐
│          Information Assurance (IA)                     │
│   Governo del dato: CIA, Autenticita, Policy, Utilita   │
│   ┌───────────────────────────────────────────────────┐ │
│   │              Cybersecurity                        │ │
│   │  Difesa e protezione delle risorse nel ciberspazio │ │
│   │   ┌─────────────────────────────────────────────┐ │ │
│   │   │           Computer Security                  │ │ │
│   │   │  Protezione di HW, SW, firmware e dati       │ │ │
│   │   │  in elaborazione, memorizzazione, trasmissione│ │ │
│   │   └─────────────────────────────────────────────┘ │ │
│   └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

> [!IMPORTANT] I Tre Confini
> - **Computer Security:** misure e controlli tecnici volti a garantire la confidenzialita, l'integrita e la disponibilita degli asset di un sistema di elaborazione, inclusi componenti hardware, software, firmware e informazioni durante l'elaborazione, la memorizzazione e la trasmissione.
> - **Cybersecurity:** capacita di proteggere, difendere e mitigare gli attacchi informatici condotti attraverso il ciberspazio (reti pubbliche, Internet e infrastrutture interconnesse).
> - **Information Assurance (IA):** insieme integrato di controlli tecnici, organizzativi e manageriali progettati per garantire confidenzialita, controllo del possesso, integrita, autenticita, disponibilita e utilita delle informazioni e dei sistemi informativi lungo tutto il loro ciclo di vita.

---

## ⏭️ Navigazione Lezioni
- **Lezione successiva :** [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta]]
- **Index Corso :** [[00_Index_Cybersecurity]]
