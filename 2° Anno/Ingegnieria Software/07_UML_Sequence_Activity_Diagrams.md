---
date: 2026-03-19
tags:
  - appunti
  - IngegneriaSoftware
---
# Sequence Diagram e Activity Diagram

Dal modello statico, che definisce la struttura del sistema (Domain Model e Class Diagram), si passa al livello dinamico per analizzare come gli oggetti collaborano durante uno scenario e in quale ordine avvengono azioni e decisioni. Per fare questo, si utilizzano due viste complementari: il Sequence Diagram per le interazioni tra partecipanti e l'Activity Diagram per il flusso del processo.

## 1. Sequence Diagram

Il Sequence Diagram si utilizza per **chiarire come uno scenario viene eseguito nel tempo**. È particolarmente utile per scenari di caso d'uso con esito positivo e per le relative varianti di errore. 
Risponde a tre quesiti operativi principali:
* **Chi interagisce con chi**.
* **In quale ordine** avvengono i messaggi.
* **Chi prende in carico ogni responsabilità**.

La lettura corretta di un Sequence Diagram segue due assi principali:
* **Verticale:** Il tempo scorre dall'alto verso il basso.
* **Orizzontale:** Mostra i diversi partecipanti coinvolti nello scenario.
![[Pasted image 20260416153515.png]]

***Quando usarlo:*** Quando la logica e l'ordine dei messaggi sono rilevanti per il comportamento del sistema.
***Errore da evitare:*** Disegnarlo ovunque senza un reale valore informativo.


### Componenti Principali del Sequence Diagram

* **Lifeline (Linea di Vita):** Ogni partecipante ha una lifeline che lo identifica nello scenario. L'obiettivo è rendere esplicito chi partecipa prima di dettagliare i messaggi. 
    * Possiamo distinguere diversi ruoli con diverse responsabilità: attore, interfaccia e servizio.
* **Activation (Barra di Attivazione):** Indica il periodo in cui il partecipante sta effettivamente eseguendo del lavoro. 
    * Serve a leggere meglio la durata logica e la nidificazione delle chiamate.

### Tipologie di Messaggi

* **Messaggio Sincrono:** Il chiamante invia il messaggio e attende il completamento dell'operazione, creando una dipendenza temporale immediata. Rappresentato da una freccia con punta piena.
![[Pasted image 20260416153722.png]]
* **Messaggio Asincrono:** Il chiamante invia il messaggio ma prosegue la sua esecuzione senza bloccarsi (es. in integrazioni event-driven). Rappresentato da una freccia con punta aperta. 
	* *Nota:* Se si manda un messaggio asincrono, qualcuno a un certo punto deve gestirne l'esito. 
![[Pasted image 20260416153741.png]]
* **Return Message:** Freccia tratteggiata che rappresenta il risultato di una richiesta sincrona, utile se il valore di ritorno guida una decisione successiva.
 ![[Pasted image 20260416153908.png]]
* **Create / Destroy:** Mostrano rispettivamente quando un oggetto nasce durante l'interazione e quando termina il suo ciclo di vita temporaneo (cleanup esplicito con una 'X').
* **Self-call:** Un partecipante invoca una propria operazione interna per evidenziare una sotto-fase significativa.
*![[Pasted image 20260416153941.png]]
### Frammenti (Fragments)

I frammenti permettono di modellare logiche complesse all'interno del Sequence Diagram:

* **Alt:** Modella rami alternativi mutuamente esclusivi (es. success/failure nello stesso scenario).
* **Opt:** Esprime un comportamento opzionale (simile a un *if* senza *else*), dove il flusso principale resta valido anche senza di esso.
* **Loop:** Rappresenta una ripetizione controllata da una condizione esplicita.
* **Break:** Interrompe il normale scenario in caso eccezionale; il resto del flusso principale non prosegue.
* **Par:** Descrive rami concorrenti eseguibili in parallelo, utile per discutere latenza e sincronizzazione.
* **Critical:** Delimita una sezione che richiede mutua esclusione e non deve essere interrotta.
* **Ref:** Rimanda a un'interazione definita altrove, riducendo la duplicazione di sotto-scenari ricorrenti.
* **Assert:** Indica una sequenza di protocollo o una traccia che deve valere obbligatoriamente.
* **Neg:** Rappresenta e rende esplicita una traccia vietata o un comportamento non ammesso.
* **Strict vs Seq:** `strict` impone un ordine globale totale senza interleaving, mentre `seq` (comportamento di default) permette un ordine parziale preservando solo i vincoli locali.

---

## 2. Activity Diagram

A differenza del Sequence Diagram che analizza il dettaglio dei messaggi, l'Activity Diagram si focalizza sul flusso complessivo del processo. È utile per descrivere flussi di attività, regole decisionali, passi operativi end-to-end e parallelismi.

### Struttura Base

* **Initial e Final Node:** Ogni attività parte da un nodo iniziale (cerchio nero pieno) e termina in un nodo finale (cerchio pieno con bordo), delimitando chiaramente il processo.
* **Action e Control Flow:** Le azioni (rettangoli arrotondati) sono i passi di lavoro, mentre il control flow (frecce piene) definisce l'ordine di esecuzione.

### Decisioni e Concorrenza

* **Decision e Merge:** Il *decision* (rombo con un ingresso e più uscite) separa i rami operativi in base a **guardie** esplicite (condizioni logiche tra parentesi quadre, es. `[posti > 0]`). Il *merge* (rombo con più ingressi e un'uscita) ricompone il flusso.
* **Fork e Join:** Il *fork* (barra nera spessa con più uscite) apre esecuzioni concorrenti, mentre il *join* (barra con più ingressi) le sincronizza convergendo in un unico flusso.
* **Swimlane:** Partizioni grafiche che assegnano chiare responsabilità organizzative ai vari passi, indicando chi fa cosa (es. Studente vs Sistema).

### Eventi, Segnali e Interruzioni

* **Send Signal:** L'attività emette un evento verso l'esterno e prosegue senza attendere una risposta immediata (integrazione event-driven).
* **Receive Signal:** Il flusso si interrompe restando in attesa di un evento esterno per poter proseguire.
* **Time Event:** Il processo reagisce a una transizione innescata dal tempo (scadenza temporale).
* **Interruptible Region:** Una regione del processo che può essere interrotta forzatamente da un evento (es. comando stop o annullamento utente).

---

## 3. Confronto Finale: Quando usare cosa?

* **Usa il Sequence Diagram:** Quando il rischio è distribuire male la logica e le responsabilità tra gli oggetti. È ideale per analizzare le interfacce e i messaggi precisi tra i componenti.
* **Usa l'Activity Diagram:** Quando il rischio è perdere la visione complessiva e il flusso logico end-to-end del processo di business, comprese decisioni e parallelismi.
* I due diagrammi sono complementari: vengono spesso usati insieme sullo stesso scenario per fornire una vista dinamica completa.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]