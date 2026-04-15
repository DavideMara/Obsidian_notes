---
date: 2026-04-03
tags:
  - IngegneriaSoftware
  - appunti
type: lezione
---
# Requisiti Funzionali e Non Funzionali

La definizione dei requisiti è la base su cui poggia ogni scelta successiva del processo di sviluppo. Queste scelte includono:
* Progettazione.
* Implementazione.
* Test e verifiche.
* Evoluzione futura.

> [!INFO] Focus
> La domanda principale in questa fase è sul "che cosa" deve fare il sistema.

## 1. Che cos'è un requisito?
Un requisito è una **descrizione chiara e condivisa di qualcosa che il sistema deve fare oppure di un vincolo che deve rispettare**. Rappresenta una vera e propria promessa tra chi richiede il sistema e chi lo realizza (Company and Customer) .

Un buon requisito offre diversi vantaggi:
* Riduce le ambiguità e le interpretazioni personali.
* Permette di verificare in modo oggettivo se il sistema si comporta come atteso.
* Guida direttamente la progettazione dei test.

Il criterio guida fondamentale è che un requisito deve essere sempre verificabile e, quando possibile, anche misurabile.
## 2. Livelli di Dettaglio: Utente vs Sistema
Un requisito può essere espresso a due livelli di dettaglio:
* **Lato utente**: Utilizza un linguaggio semplice, orientato ai bisogni, agli obiettivi e al contesto. È comprensibile a chi utilizzerà il sistema.
* **Lato sistema**: Fornisce una descrizione più precisa, utile a sviluppatori e progettisti per implementare concretamente il sistema.

**Esempio a due livelli:**
La necessità di base è la stessa, cambia solo il livello di precisione con cui la esprimiamo.
* *Versione lato utente*: «Il sistema deve permettere al docente di ottenere un riepilogo degli appelli d’esame.» 
* *Versione lato sistema*: Il sistema genera un elenco contenente corso, data, iscritti ed esiti. Il riepilogo può essere filtrato per periodo, corso o docente. Il risultato è disponibile sia a video sia in formato scaricabile.

## 3. Le due grandi famiglie di requisiti
I requisiti si dividono in due grandi famiglie:

1. **Requisiti Funzionali**: Descrivono cosa il sistema deve fare, definendo servizi, operazioni e comportamenti osservabili dagli utenti. Definiscono le funzioni dirette del sistema.
2. **Requisiti Non Funzionali**: Descrivono come il sistema deve funzionare, quali vincoli deve rispettare e quale livello di qualità, limiti e contesto operativo deve garantire.

![[Pasted image 20260414161212.png]]
###  Requisiti Funzionali
I requisiti funzionali definiscono la trama del sistema: senza di essi, il sistema non potrebbe svolgere la sua attività principale. Riguardano azioni specifiche come inserire dati, consultare elenchi, o avviare procedure.

> [!INFO] Il pericolo della vaghezza
> Un requisito funzionale vago (es. "Il sistema deve permettere di cercare gli esami") non è verificabile. Non indica con chiarezza il risultato atteso e non guida la definizione dei test. Ambiguità di questo tipo si accumulano nel tempo generando debito tecnico. Prima o poi sarà inevitabile dover rivedere codice e documentazione per riallinearli a una definizione più precisa.

### Requisiti Non Funzionali
I requisiti non funzionali non descrivono azioni specifiche, ma comportamenti e qualità attese. Riguardano aspetti trasversali fondamentali per la riuscita del progetto. Un sistema che "fa tutto" ma è lento o poco sicuro risulta comunque inadeguato.
Comprendono:
* **Prestazioni**: Tempi di risposta e capacità di gestire molti utenti contemporanei.
* **Sicurezza**: Protezione dei dati, autenticazione e autorizzazioni.
* **Affidabilità**: Continuità del servizio, recupero guasti e gestione degli errori.
* **Accessibilità e usabilità**: Chiarezza dell'interfaccia e riduzione delle barriere.
* **Compatibilità**: Integrazione con i sistemi già esistenti.
* **Rispetto di norme**: Regolamenti tecnici e gestione dei dati personali.

> [!INFO] Esempi Pratici dal Docente
> * **Affidabilità**: Garantire un server sempre attivo, che prevenga crolli con troppi utenti o a seguito di cali di tensione.
> * **Accessibilità/Usabilità**: Prevedere font adatti per utenti daltonici e assicurarsi che i template siano usabili.
> * **Compatibilità**: Assicurarsi che il software sia compatibile con diverse applicazioni esterne.

#### Le Tre Famiglie dei Requisiti Non Funzionali
* **Legati al prodotto**: Qualità interne (prestazioni, tempi di risposta, consumo di risorse).
* **Legati all'organizzazione**: Vincoli del contesto di sviluppo/uso (strumenti, procedure interne, integrazioni).
* **Legati all'ambiente esterno**: Normative, standard e regolamenti esterni da rispettare.
![[Pasted image 20260414161414.png]]

## 4. Requisiti Misurabili
Un requisito è utile solo se verificabile in modo oggettivo. Obiettivi generali come "veloce" o "facile da usare" non sono verificabili direttamente. Occorre trasformarli in requisiti misurabili.

Ad esempio, la transizione da "Il sistema deve essere veloce" a "Il sistema deve rispondere entro 2 secondi per almeno il 95% delle richieste". Questo evita interpretazioni diverse e guida in modo coerente le scelte architetturali.

## 5. Raccogliere i Requisiti
I requisiti non emergono spontaneamente; bisogna raccoglierli dialogando con gli stakeholder. Strumenti utili includono:
* Colloqui con gli utenti per comprendere bisogni e difficoltà.
* Osservazione delle attività reali senza filtri.
* Analisi di procedure e documenti esistenti.
* Prototipi e dimostrazioni per far emergere idee latenti.
Le esigenze si scoprono progressivamente, generando requisiti che all'inizio possono essere incompleti o in conflitto tra loro (es. "facile da usare" ma con "password complesse"). L'analisi serve proprio a chiarire, verificare la compatibilità e negoziare le priorità.
Una volta raccolti i bisogni, per rappresentare in modo semplice e comprensibile dobbiamo creare delle **User Story**
## 6. User Stories
Una user story descrive un'esigenza dal punto di vista dell'utente, in modo semplice e privo di dettagli implementativi. Serve ad allineare utenti e sviluppatori per popolare un backlog comprensibile.

> [!INFO] User Story vs Caso d'Uso
> * **User story**: Frase breve orientata a chi-cosa-perché, utile per la gestione del backlog e la prioritizzazione dei bisogni.
> * **Use case**: Descrizione strutturata e dettagliata del comportamento del sistema, usata per la modellazione formale e comportamentale (es. UML).

La forma tipica essenziale risponde a tre domande (chi, cosa, perché):
* «Come **[tipo di utente]**, voglio **[azione]** per **[obiettivo / beneficio]**.» 
De facto, per una user story ben formulata, si deve specificare: 
- **Chi** : l'attore che usa il sistema;
- **Cosa** : l'azione desiderata, espressa in modo semplice e osservabile;
- **Perché** : il valore/beneficio atteso per l'utente o per il processo;
*Es. << Come docente, voglio esportare la lista iscritti per preparare il verbale.>>*
## 7. Criteri di Accettazione
Ogni user story deve essere accompagnata da criteri di accettazione: condizioni chiare che stabiliscono quando la funzionalità è davvero completata.
Essi servono a:
* Eliminare ambiguità sulle aspettative.
* Definire il confine tra "fatto" e "non fatto".
* Fornire una base solida per i test di verifica.

Mentre la user story racconta l'intenzione, i criteri ne specificano la verifica concreta. Possono usare forme strutturate come «Dato che... Quando... Allora...».

## 8. Requisiti, Backlog e Priorità
Le user stories diventano elementi del backlog, una lista ordinata di ciò che il sistema offrirà. È necessario stabilire delle priorità, affrontando prima le funzionalità che portano più valore, che affrontano rischi tecnici, o che sbloccano dipendenze. Il backlog è un artefatto vivo che cambia e si aggiorna.
Anche i requisiti non funzionali entrano nel backlog:
* Possono diventare **attività specifiche** (es. migliorare i tempi di risposta o potenziare la sicurezza).
* Possono rappresentare **vincoli trasversali** da rispettare in ogni funzionalità (es. normativa sui dati o compatibilità).

Ignorarli nelle prime fasi porta quasi sempre a interventi più costosi (rework) e rischiosi in seguito.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]