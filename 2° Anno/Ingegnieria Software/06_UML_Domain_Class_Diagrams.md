---
date: 2026-03-18
tags:
  - appunti
  - IngegneriaSoftware
type: lezione
---
# Domain Model e Class Diagram
## 1. Che cos'è un Domain Model
Il Domain Model è una **rappresentazione concettuale** del dominio del problema. È una "fotografia" del mondo a cui il sistema software si riferisce e non contiene dettagli tecnici.
Esso mostra:
* I **concetti rilevanti** (entità, oggetti, ruoli).
* Le **relazioni** tra questi concetti.
* Gli **attributi essenziali** che li caratterizzano.
Non contenendo alcun dettaglio implementativo, nel Domain Model non si parla di database, API, interfacce grafiche, e non vi sono metodi o algoritmi.
#### Perché è importante? 
Il Domain Model aiuta a capire il problema prima di pensare alla soluzione. Agisce come un linguaggio condiviso tra sviluppatori, analisti, domain expert e stakeholder non tecnici. Un modello chiaro facilita la transizione verso la progettazione.

## 2. Dalle Storie agli Oggetti del Dominio: La Tecnica
Per estrarre le entità concettuali dai requisiti o dai casi d'uso (es. "Lo studente si iscrive a un appello"), si utilizza una strategia basata sull'analisi testuale:
* **Evidenziare i sostantivi**: questi diventano i candidati concetti del modello.
* **Evidenziare i verbi**: questi diventano i candidati per le associazioni o le responsabilità.
Un concetto è considerato un buon candidato se è nominato spesso nei requisiti, se ha regole di business proprie o se è riconosciuto dagli stakeholder come un'entità reale del loro mondo (es. Studente, Corso, Appello).

## 3. Attributi Essenziali e Associazioni
Gli attributi descrivono informazioni importanti su un concetto. Essi dovrebbero essere pochi (seguendo il principio del minimalismo), stabili nel tempo, non derivabili e rilevanti per le regole di business.

**Errori frequenti nella scelta degli attributi:**
* Confondere il Domain Model con il database, inserendo id tecnici, timestamp di audit o campi di log.
* Aggiungere attributi troppo tecnici, come token di sessione o flag di caching.
* Inserire **attributi derivabili**, ovvero dati che possono essere ottenuti da altri (es. numero di esami superati derivabile dalle iscrizioni, o media voti).

### Associazioni e Molteplicità
Le associazioni rappresentano legami concettuali tra gli elementi del modello.
La **molteplicità** esprime quante istanze di un concetto possono essere collegate a un altro, traducendo in diagramma i vincoli reali del dominio.
La lettura rapida delle molteplicità è la seguente:
* `1`: esattamente una.
* `0..1`: opzionale.
* `0..*`: zero o molte.
* `1..*`: almeno una.

![[Pasted image 20260415172404.png]]
## 4. Dal Domain Model al Class Diagram
Esiste una netta differenza tra i due diagrammi:
* **Domain Model**: È concettuale. Mostra i concetti del mondo reale, gli attributi essenziali per capire il problema e le relazioni concettuali tra entità.
* **Class Diagram**: Guarda verso il software. Introduce il concetto di classe, mostra gli attributi che saranno effettivamente memorizzati e le relazioni che guideranno la struttura del codice.

### Checklist per il passaggio al Class Diagram
* **Cosa portare in questa fase**: I nomi chiari delle classi, gli attributi essenziali tipizzati (es. string, int) e le relazioni ispirate al Domain Model.
* **Cosa lasciare fuori in questa fase**: Metodi, logica di dettaglio, classi tecniche o di infrastruttura (Repository, DAO, Controller, helper) e dettagli legati ai framework.
## 5. Notazione UML Avanzata
Nei diagrammi di classe orientati al software si adottano notazioni specifiche:

* **Visibilità degli attributi**:
  * `+` public: visibile a tutti.
  * `-` private: visibile solo all'oggetto stesso.
  * `#` protected: visibile a classe e sottoclassi.
  * `~` package: visibile all'interno del package.
* **Attributo derivato**: Un attributo che può essere calcolato a partire da altri dati. Si indica ponendo il simbolo `/` davanti al nome (es. `/eta` derivato da `dataNascita`).
* **Attributo statico (di classe)**: Sono attributi condivisi tra tutte le istanze della classe. Si indicano sottolineando il nome (es. <u>contaCorsi</u>).
* **Ereditarietà (Generalizzazione)**: Si indica con una freccia a triangolo vuoto che punta verso la superclasse. Le sottoclassi ereditano attributi e operazioni dalla superclasse.
![[Pasted image 20260415172610.png]]
### Aggregazione e Composizione
Rappresentano particolari tipi di associazione in cui esiste un rapporto tra un "tutto" e una "parte":
* **Aggregazione (rombo vuoto)**: La parte può esistere anche indipendentemente dal tutto. Es. Se si elimina un Corso, i Docenti associati esistono comunque.
![[Pasted image 20260415172654.png]]
* **Composizione (rombo pieno)**: La parte dipende strettamente dal tutto per esistere (vincolo esistenziale). Es. Se si elimina un Appello, le Iscrizioni relative a quell'appello non hanno più senso e cessano di esistere.
![[Pasted image 20260415172719.png]]
---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]