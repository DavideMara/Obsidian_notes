---
date: 2026-05-03
tags:
  - IngegnieriaSoftware
  - appunti
type: lezione
---
# 04 - Modellazione Concettuale

## Introduzione alla Modellazione Concettuale
Il dominio rappresenta il mondo reale in cui il sistema si inserisce, ovvero l'insieme di persone, oggetti, regole e processi reali che il software deve rappresentare e supportare. La modellazione concettuale è l'attività che funge da ponte tra i requisiti e l'analisi strutturata, mirando a:
* Identificare i concetti importanti del dominio.
* Chiarire quali responsabilità ha ciascun concetto.
* Descrivere le relazioni tra questi concetti.



Questa fase descrive logicamente il problema, indipendentemente dalla soluzione tecnica (non si parla ancora di classi, metodi, tabelle del database o architetture). Lo scopo principale è costruire un vocabolario condiviso tra utenti, analisti e sviluppatori.

> [!INFO] Slide 3 e successive
> I concetti sono elementi significativi del dominio, non vanno ancora pensati come classi, tabelle o dettagli implementativi. La modellazione concettuale ci aiuta a individuare i concetti davvero importanti come una sorta di guida.

## Dai Requisiti ai Concetti
I requisiti testuali scritti in precedenza contengono già molti suggerimenti sulla struttura del dominio. Leggendoli con attenzione, possiamo estrarre gli elementi fondamentali:
* **Sostantivi:** Suggeriscono le potenziali *entità* del dominio (es. studente, appello, corso, voto, verbale, carriera).
* **Verbi:** Suggeriscono le *azioni* o le *relazioni* tra le entità (es. iscriversi, registrare, consultare).
* **Espressioni di vincolo:** Nascondono le *regole* e i limiti del dominio (es. "solo se", "entro").

> [!INFO] Slide 6: Analisi dei requisiti
> L'estrazione di sostantivi, verbi e vincoli non è una trasformazione meccanica, ma una guida pratica per la modellazione.

## Le Entità Concettuali
Un'entità concettuale è un nodo logico, un elemento del mondo che vogliamo rappresentare in modo esplicito nel sistema. Esiste indipendentemente dalla tecnologia scelta e ha un significato riconoscibile anche dai non tecnici.

> [!INFO] Entità Concettuale
> L'errore da evitare assolutamente in questa fase è confondere le entità concettuali con le strutture di codice (classi) o le tabelle del database.

> [!INFO] Esempi applicabili a UniManager (esempio pratico del prof)
> L'idea non è "definire le classi", ma capire in modo chiaro:
> * Che cosa rappresenta ciascuna di queste entità.
> * Perché è utile distinguerle.
> * Che tipo di informazioni ci aspettiamo che custodiscano.

Nel caso di studio UniManager, le entità principali individuate sono:
* **Studente:** Rappresenta la persona che segue i corsi e sostiene gli esami.
* **Corso:** Rappresenta l'insegnamento (nome, docente, CFU).
* **Appello:** Rappresenta un'occasione concreta per sostenere l'esame (data, ora, aula).
* **Iscrizione:** Rappresenta l'atto con cui uno studente si registra a uno specifico appello. Ha una propria data e stato, utile per tracciare la storia delle interazioni.
* **Voto:** Rappresenta l'esito ottenuto dallo studente in quell'appello. Non è un semplice attributo numerico dell'appello, ma ha uno stato proprio e può essere oggetto di statistiche o controlli.

Separare questi concetti permette di rappresentare accuratamente le situazioni reali. Ad esempio, uno studente può iscriversi più volte, può sostenere lo stesso corso in appelli diversi, e un appello può avere molti iscritti e voti.

### Responsabilità delle Entità
A ogni entità associamo delle responsabilità specifiche:
* Quali *informazioni* custodisce.
* In quali *interazioni* è coinvolta.
* Quali *decisioni* del dominio passano da essa.

## Le Relazioni tra le Entità
Le entità non vivono isolate; le relazioni tra i concetti rendono interessante un dominio. Si dividono in due famiglie principali:

> [!INFO] Dalla slide 12 in poi: Struttura vs Azioni
> Esistono relazioni strutturali (stabili) e relazioni basate sugli eventi.

1. **Relazioni Strutturali:** Descrivono l'organizzazione stabile del dominio.
   * *Corso - Docente:* Un corso è tenuto da uno o più docenti.
   * *Corso - Appello:* Un corso ha uno o più appelli nel tempo.
   * *Iscrizione - Appello:* Ogni iscrizione si riferisce a uno specifico appello.
2. **Relazioni di Azione/Evento:** Descrivono ciò che avviene nel sistema.
   * *Studente → Iscrizione:* Crea una nuova iscrizione a un appello.
   * *Docente → Voto:* Registra o aggiorna l'esito.

> [!INFO] Esempi pratici sulle Azioni
> Queste relazioni sono più vicine al comportamento del sistema e includono tipicamente precondizioni, effetti e controlli. L'obiettivo principale qui è **capire chi interagisce con chi e in che modo**.

## La Mappa Concettuale
La mappa concettuale è la rappresentazione visiva e informale della vista strutturale del dominio. Utilizza nodi per le entità ed etichette testuali (in italiano, senza simboli complicati) per le relazioni. Essa è uno strumento vivo che può evolvere e raffinarsi man mano che emergono nuovi bisogni (es. introducendo i concetti di Carriera, Sessione o Verbale).



Inoltre, è fondamentale definire i confini del sistema (attori coinvolti come Studenti o Segreteria, e sistemi esterni) per evitare di attribuire al software responsabilità che non gli competono.

> [!INFO] Verso la fine (Slide 25): Checklist Rapida
> Prima di procedere con UML formale o la scrittura del codice, verifica:
> * **Nomi chiari:** Comprensibili anche ai non tecnici (user friendly).
> * **Relazioni esplicite:** Coerenti con i requisiti.
> * **Niente dettagli tecnici:** Evitare accuratamente di pensare già a classi, DB o API.

> [!INFO] Conclusioni (Slide 25 in poi)
> Saltare la modellazione concettuale introduce vincoli tecnici prematuri, rischia fraintendimenti e rende le correzioni molto più costose nelle fasi avanzate. Investire tempo in questa fase riduce le ambiguità e consolida le basi per la progettazione architetturale successiva.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]