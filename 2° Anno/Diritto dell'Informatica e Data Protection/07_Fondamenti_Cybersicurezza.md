---
date: 2026-03-02
subject: Diritto dell'Informatica e Data Protection
tags:
  - Diritto
type: lezione
---
# Fondamenti di Cybersicurezza, Gestione del Rischio e Normativa

## Il Rischio Cyber e il Ruolo del DPO
La sicurezza informatica è intrinsecamente associata al concetto di rischio. In Italia, istituzioni e associazioni come l'Agenzia per la Cybersicurezza Nazionale (ACN) e il CLUSIT (attraverso l'annuale Rapporto Clusit) monitorano costantemente le tendenze e l'andamento delle minacce in ambito cyber a livello nazionale e globale. I rischi informatici sono in continua ed esponenziale espansione, con un boom significativo registrato durante la pandemia da COVID-19, portando a una chiara partizione percentuale dei tipi di attacco.

Nell'ambito del GDPR, l'articolo 39 stabilisce i compiti del Data Protection Officer (DPO), il quale ha il ruolo di supportare il Titolare del trattamento nell'attribuire le responsabilità interne e nel sensibilizzare e formare il personale sui rischi connessi al trattamento dei dati personali. Ciò significa che il DPO e le figure preposte devono conoscere approfonditamente le minacce informatiche più comuni (es. accesso abusivo, malware) per poter adeguare procedure e adottare adeguate misure tecniche e organizzative.

> [!LAW] Articolo 39 GDPR
> Definisce i compiti del DPO, tra cui la sorveglianza dell'osservanza del regolamento e la sensibilizzazione e formazione del personale che partecipa ai trattamenti.

> [!INFO] Collaborazione
>  È fondamentale la collaborazione e l'interscambio tra informatici, tecnici e giuristi per una corretta compliance aziendale. Al giorno d'oggi vi è un preciso obbligo di possedere competenze informatiche anche per le professioni legali e gli avvocati (es. caso Panama Papers).

## Standard Internazionali e Valutazione del Rischio
Un elemento centrale nella gestione aziendale è l'approccio basato sul rischio (Risk Management). Lo standard **ISO 31000** fornisce lo scheletro e le linee guida per un corretto impianto normativo e di processo.

> [!INFO] Struttura ISO 31000
> Si articola in due componenti principali:
> 1. **Framework:** Garantisce che la gestione del rischio sia integrata in tutte le attività (Leadership, Integrazione, Progettazione, Attuazione, Valutazione e Miglioramento).
> 2. **Processo:** L'applicazione operativa che include l'identificazione, l'analisi (stima di probabilità e impatto), la valutazione (confronto con i criteri di accettabilità) e il trattamento del rischio.

La formula fondamentale per la valutazione del rischio è **R = P x D** (Rischio = Probabilità x Danno/Impatto). 

> [!INFO] Analisi Qualitativa vs Quantitativa
> - **Qualitativa:** Si basa su scale descrittive (es. alto/medio/basso) e giudizi esperti. È utile quando i dati numerici sono limitati o per una valutazione rapida. Utilizza matrici di rischio per visualizzare la criticità.
> - **Quantitativa:** Impiega dati numerici e metodi statistici (es. simulazioni *Monte Carlo*) per calcolare la perdita attesa in termini monetari, come l'**ALE** (*Annual Loss Expectancy*). La formula standard è **ALE = SLE x ARO**, dove *SLE (Single Loss Expectancy)* è la perdita per singolo evento e *ARO (Annual Rate of Occurrence)* è la frequenza annuale ipotizzata. Richiede dati storici affidabili e competenze specialistiche.

Lo schema di valutazione si appoggia a modelli ciclici come il Ciclo di Deming (**PDCA**: Plan-Do-Check-Act) per garantire un miglioramento continuo (Kaizen) dei processi di gestione.

## Classificazione delle Minacce e Motivazioni
Le minacce informatiche possono essere classificate secondo diversi criteri per meglio comprendere il profilo di rischio:

### 1. Motivazione dell'Attaccante
- **Economica:** Il fine principale è il lucro (estorsione tramite ransomware, furto di credenziali bancarie, rivendita di dati nel dark web).
- **Spionaggio:** Attacchi mirati ad acquisire informazioni sensibili, segreti industriali o dati strategici di governi, spesso condotti in modo discreto per lungo tempo.
- **Ideologica (Hacktivismo):** Attacchi mossi da motivazioni politiche o sociali (es. Anonymous) per ottenere clamore mediatico tramite *DDoS* o *Defacement* (modifica non autorizzata della home page di un sito).
- **Advanced Persistent Threat (APT):** Minacce sofisticate condotte da attori statali o gruppi terroristici con notevoli risorse, che mirano a mantenere un accesso prolungato e non rilevato all'interno di un sistema.

### 2. Fonte e Superficie d'Impatto
Le minacce possono essere **interne** (dipendenti infedeli o negligenti) o **esterne**. La superficie d'impatto si estende su quattro ambiti:
- **Software:** Vulnerabilità del codice (es. *SQL Injection*, *Cross-Site Scripting*).
- **Hardware e Rete:** Componenti fisiche e infrastrutture di comunicazione.
- **Supply Chain:** Attacchi alla catena di approvvigionamento (es. compromettere un fornitore per colpire il cliente finale).
- **Fattore Umano:** Definito nell'ambiente hacker come **Wetware** (l'hardware biologico o software mentale), rappresenta la superficie più critica.

La resilienza informatica è diventata un pilastro strategico. In Unione Europea si pone forte accento sulla "sovranità digitale" per ridurre la dipendenza da tecnologie e software extra-UE (es. software americani o asiatici), come testimoniato dall'adozione di normative quali l'European Chips Act.

## Fondamenti di Sicurezza: La Triade CIA
I reati informatici e le violazioni di sicurezza incidono quasi sempre su almeno uno dei tre elementi fondamentali della sicurezza delle informazioni.

> [!INFO] CONCETTO IMPORTANTE: La Triade CIA.
La Triade CIA si compone di:
- **Confidentiality (Confidenzialità):** i dati devono poter essere letti ed elaborati esclusivamente da figure specifiche e autorizzate.
- **Integrity (Integrità):** l'informazione non deve subire alterazioni; se un soggetto non abilitato modifica i dati, l'integrità è compromessa.
- **Availability (Disponibilità):** i dati devono essere prontamente accessibili ai soggetti autorizzati, impedendone l'esposizione ai non autorizzati.

## Evoluzione Storica della Cybersicurezza
La sicurezza informatica non è nata contemporaneamente all'informatica: i primissimi sistemi non contemplavano il concetto di "sicurezza by design". Oggi, la cybersecurity riguarda e tutela sia le componenti hardware (es. mitigazione di vulnerabilità delle CPU come *Meltdown* basate su segnali anomali) sia quelle software.

> [!INFO] Fun fact: la derivazione del termine "bug" ha origine al MIT (e poi ad Harvard sul Mark II) per via di un insetto reale incastrato nei circuiti della macchina, il primo vero "bug" della storia dell'informatica.

Negli anni '50, i primi Big Mainframe come l'UNIVAC (1951) non avevano cyber-sicurezza. La protezione dell'hardware era esclusivamente fisica, volta a prevenire il danneggiamento più che il furto. La programmazione avveniva in linguaggio macchina (0 e 1), esponendo i sistemi a frequenti errori umani. In assenza di connessioni esterne, l'accesso fisico alla sala server fungeva da unica vera "autenticazione". Successivamente, con calcolatori come il Mark 1 (Harvard) basato su componenti meccanici (e con antenati come il Meccanismo di Anticitera di Archimede per calcoli astronomici), l'informatica si è evoluta. 
Con la nascita di ARPANET prima di Internet (anni '70), sono emerse le fondamenta della cybersicurezza moderna. 

> [!INFO] Esempio storico-culturale: il film "WarGames" e lo spavento del Presidente Reagan, che diede impulso alle primissime policy governative di sicurezza informatica negli USA.

Poiché i profili di rischio evolvono continuamente, è essenziale comprendere che la "sicurezza assoluta" in informatica non esiste.

## Il Quadro Normativo Nazionale e la Direttiva NIS
Una violazione di sicurezza che comporta accidentalmente o in modo illecito la distruzione, la perdita, la modifica, la divulgazione non autorizzata o l'accesso ai dati personali trasmessi, conservati o comunque trattati, configura giuridicamente un Data Breach (violazione dei dati personali).

Il legislatore interviene costantemente per arginare tali minacce. A livello europeo, la materia è presidiata dalla **Direttiva NIS2 (Reg. UE 2022/2555)**, che mira a eliminare le frammentazioni tra gli Stati membri espandendo i settori coinvolti e armonizzando i requisiti di sicurezza.
Punti chiave della NIS2:
- **Classificazione Soggetti:** Distingue tra *Soggetti Essenziali* (settori critici come energia, sanità, banche) sottoposti a vigilanza proattiva e *Soggetti Importanti* sottoposti a vigilanza reattiva.
- **Obblighi di Segnalazione:** Obbligo di notifica degli incidenti significativi alle autorità competenti (CSIRT) entro tempistiche stringenti.
- **Sanzioni:** Possono arrivare fino al **6% del fatturato annuo mondiale** del prestatore.

A livello nazionale, il quadro include la **Legge 90/2024**, che consolida le attribuzioni dell'Agenzia per la Cybersicurezza Nazionale (ACN) e introduce la figura del **"Referente per la cybersicurezza"** in ogni PA. Il Decreto Legge 105/2019 sul Perimetro di Sicurezza Nazionale Cibernetica e il Decreto Legge 138/2024 completano l'impianto, estendendo la protezione ad asset strategici.

> [!LAW] Decreto Legge 20/2021: Introduce raccomandazioni cogenti per la Pubblica Amministrazione, suggerendo fortemente di dismettere l'utilizzo di software russi (come gli antivirus Kaspersky) per arginare il rischio concreto di "backdoor" governative.

## Minacce, Fattore Umano e Social Engineering
L'anello debole della catena di sicurezza rimane l'utente. Spesso ci si riferisce al fattore umano con l'espressione "Problem Exists Between the Keyboard And the Chair" (PEBKAC). Aggiungendo specifiche motivazioni psicologiche, è possibile manipolare l'output e il comportamento delle persone.

Questa tecnica prende il nome di **Ingegneria Sociale (Social Engineering)**, che sfrutta le debolezze cognitive per ottenere accessi o informazioni riservate. Le caratteristiche e leve principali sfruttate sono:
- Autorevolezza
- Senso di colpa
- Panico
- Ignoranza
- Desiderio
- Avidità
- Compassione

Oltre alle leve psicologiche, l'ingegneria sociale utilizza tecniche fisiche e verbali specifiche:
- **Tailgating:** Seguire fisicamente una persona autorizzata all'interno di un'area protetta senza mostrare credenziali.
- **Piggybacking:** Simile al tailgating, ma avviene con la cooperazione o la disattenzione della persona autorizzata (es. farsi tenere aperta la porta).
- **Pretexting:** Creare uno scenario falso (un pretesto) per convincere la vittima a rivelare informazioni (es. fingersi un tecnico dell'assistenza IT).
- **Quid Pro Quo:** Offrire un servizio o un vantaggio in cambio di informazioni (es. "ti aiuto a risolvere un problema al PC se mi dai la password").
- **Dumpster Diving:** Ricerca di informazioni sensibili tra i documenti cartacei scartati e non distrutti correttamente.

> [!INFO] Lettura consigliata: "The Art of Deception" (L'arte dell'inganno) di Kevin Mitnick, testo fondamentale sulle tecniche di Social Engineering.

## Tipologie di Attacchi e Malware
Le reti sono esposte a diverse categorie di software malevolo, comunemente note come Malware. Una delle minacce più perniciose è il **Ransomware**, che cifra i dati dell'interessato e delle aziende estorcendo un riscatto economico. Le tipologie includono:
- **Locker:** blocca completamente l'accesso al sistema.
- **Crypto:** cifra specificamente i file rendendoli illeggibili.
- **Double Extortion:** oltre a cifrare, minaccia la divulgazione pubblica dei dati esfiltrati.
- **Ransomware as a Service (RaaS):** un modello criminale in abbonamento per l'utilizzo di ransomware da parte di terzi.

Ulteriori tipologie di attacchi includono attacchi per intercettazione, come il *Man in the Middle* o il *Man in the Mail* (es. Business Email Compromise), spesso orchestrati da grandi organizzazioni criminali. A livello di cyber-warfare governativo, si ricorda il celebre virus *Stuxnet*, creato ad hoc per distruggere le centrifughe del sistema di arricchimento dell'uranio in Iran o l'exploit **EternalBlue** usato per la diffusione di WannaCry.

Tra le nuove minacce emergenti, manipolazioni tramite intelligenza artificiale o minacce fisiche:
- **Deepfake**
> [!INFO] Manipolazione Subliminale
> Utilizzo di IA per creare contenuti audio/video falsi estremamente realistici. Oltre alla truffa (es. Nigerian Scam evoluta o frodi del CEO), il Deepfake lede la privacy e può essere usato per la manipolazione cognitiva bypassando i filtri razionali dell'utente, influenzando processi decisionali e opinione pubblica.

- **BadUSB (Rubber Ducky)**
> [!INFO] Vettore di Infezione Hardware
> Dispositivi apparentemente innocui (come le chiavette USB "Rubber Ducky") che vengono riconosciuti dal sistema non come memorie di massa, ma come tastiere (HID). Una volta collegati, digitano sequenze di comandi pre-programmati ad altissima velocità, permettendo l'esecuzione di script malevoli, l'apertura di backdoor o l'esfiltrazione di dati in pochi secondi, aggirando molti controlli di sicurezza tradizionali.

## Tattiche e Tecniche: Il Framework MITRE ATT&CK
Per standardizzare la descrizione degli attacchi, si utilizza il framework **MITRE ATT&CK**, una base di conoscenza mondiale sulle tattiche e tecniche degli avversari.

> [!INFO] Tattiche vs Tecniche
> - **Tattiche:** Rappresentano il **"perché"** dell'attaccante (l'obiettivo strategico, es. *Initial Access*, *Lateral Movement*, *Exfiltration*).
> - **Tecniche:** Rappresentano il **"come"** l'attaccante raggiunge l'obiettivo (il metodo specifico, es. *Phishing* per l'accesso iniziale o *Pass-the-Hash* per il movimento laterale).

Il framework identifica diverse fasi nel ciclo di vita di un attacco (kill chain), tra cui:
1. **Reconnaissance:** Raccolta informazioni sul bersaglio.
2. **Resource Development:** Preparazione di strumenti (malware, server C2).
3. **Execution:** Esecuzione di codice malevolo sul sistema.
4. **Persistence:** Mantenimento dell'accesso anche dopo il riavvio.
5. **Privilege Escalation:** Ottenimento di permessi di amministratore.
6. **Defense Evasion:** Elusione dei sistemi di sicurezza (antivirus, log).
7. **Credential Access:** Furto di nomi utente e password.
8. **Discovery:** Esplorazione del sistema per capire "dove ci si trova".
9. **Lateral Movement:** Spostamento all'interno della rete per raggiungere nuovi sistemi.
10. **Collection:** Raccolta dei dati di interesse.
11. **Command and Control (C2):** Comunicazione con i sistemi infetti per impartire ordini.
12. **Exfiltration:** Sottrazione e invio dei dati verso l'esterno.
13. **Impact:** Manipolazione, interruzione o distruzione di dati e sistemi.

---
## ⏭️ Navigazione

- **Index:** [[00_Index_Diritto]]
