---
date: 2026-03-12
tags:
  - IngegnieriaSoftware
  - appunti
type: lezione
---

# UML e Use Case Diagram (Parte 1)

## Introduzione a UML
UML (Unified Modeling Language) è un linguaggio di modellazione standard condiviso, non un linguaggio di programmazione. Fornisce un insieme di diagrammi visivi per descrivere:
* La struttura statica del sistema.
* Il comportamento dinamico del software.
* Le interazioni tra le parti interne del sistema e gli attori esterni.

UML mette a disposizione diverse famiglie di diagrammi. I principali diagrammi trattati nel corso sono:
* **Use Case Diagram**: mostra la vista del sistema dal punto di vista degli attori esterni.
* **Modello di dominio**: è il modello concettuale del dominio, spesso rappresentato con un class diagram semplificato.
* **Class Diagram**: descrive la struttura statica del dominio, incluse classi, attributi e associazioni.
* **Sequence Diagram**: illustra le interazioni nel tempo tra oggetti e attori.
* **Activity Diagram**: rappresenta il flusso di attività, le decisioni e le responsabilità di processo.
* Altri diagrammi (come State Machine, Component, Deployment) fanno parte dello standard UML ma non saranno oggetto di questo corso.



## Focus: Use Case Diagram
Il diagramma dei casi d'uso è strettamente legato ai requisiti e alle user stories del sistema. Si concentra su chi usa il sistema e per quali obiettivi specifici.

> [!INFO] // slide fino alla 9 /// 

### Attori e Confini del Sistema
Nel diagramma dei casi d'uso, la separazione tra interno ed esterno è fondamentale:
* **Sistema**: Viene rappresentato graficamente da un rettangolo che racchiude i casi d'uso. Rappresenta il confine di ciò che il software deve fare.
* **Attori**: Sono ruoli esterni che interagiscono con il sistema, situati sempre al di fuori del rettangolo. Un attore può essere una persona (es. studente, docente), un altro sistema (es. sistema di autenticazione) o un dispositivo. Non indicano singole persone, ma una tipologia di utilizzatore.

### I Casi d'Uso
Un caso d'uso rappresenta un obiettivo di business significativo per un attore. Graficamente è rappresentato da un'ellisse contenente il nome dell'obiettivo.
* Non rappresenta una singola funzione tecnica (come una "query sul DB") o un singolo "click".
* Rappresenta un risultato di senso compiuto per l'utente, come ad esempio "Iscrizione all'appello" o "Registrazione voti" nel sistema UniManager.



### Relazioni nei Use Case Diagram
Oltre all'associazione base (linea) che collega un attore a un caso d'uso, esistono relazioni più complesse:
* **Include ($\langle\langle include \rangle\rangle$)**: Indica un comportamento comune e obbligatorio. Il caso d'uso "incluso" è un pezzo riusabile che viene eseguito sempre come parte del caso d'uso principale (es. l'autenticazione per potersi iscrivere a un appello).
* **Extend ($\langle\langle extend \rangle\rangle$)**: Rappresenta una variante opzionale. Il caso d'uso che "estende" aggiunge passi opzionali o condizioni particolari a un flusso normale, attivandosi solo in determinate circostanze (es. invio di una notifica opzionale dopo la registrazione di un voto).
* **Generalizzazione tra Attori**: Permette di creare una gerarchia per evitare ripetizioni. Un attore "padre" (es. Utente) raggruppa i casi d'uso comuni, mentre gli attori "figli" (es. Studente, Docente) ereditano le interazioni e aggiungono le proprie specificità. Viene indicata con una freccia triangolare vuota che punta verso l'attore generale.



### Elementi Organizzativi e Descrittivi
* **Package**: Raggruppano i casi d'uso per aree funzionali, migliorando la leggibilità visiva in sistemi complessi senza alterarne il comportamento.
* **Vincoli e Note**: I vincoli (scritti tra parentesi graffe `{}`) esplicitano regole di business fondamentali, come scadenze o prerequisiti. Le note aggiungono commenti testuali per chiarire assunzioni altrimenti ambigue.
* **Descrizione Testuale**: I diagrammi offrono una sintesi visiva, ma i casi d'uso critici richiedono una scheda testuale dettagliata. Questa deve includere: precondizioni, postcondizioni, flusso principale dei passi "normali" ed eventuali flussi alternativi o eccezioni.

## Strumenti per la Modellazione UML
Esistono svariati strumenti gratuiti per disegnare i diagrammi:
* Strumenti grafici e visuali come draw.io (diagrams.net), StarUML, o Modelio.
* Strumenti basati su testo e codice (MermaidJS, PlantUML).

> [!INFO] // plant uml consiglia il prof 

PlantUML permette di generare diagrammi da semplici righe di testo. Questo approccio "diagram-as-code" è altamente consigliato perché:
* È sempre coerente e veloce da modificare, senza dover "trascinare rettangoli".
* È perfetto per essere integrato nella documentazione tecnica e gestito nei repository Git per il versioning collaborativo.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]