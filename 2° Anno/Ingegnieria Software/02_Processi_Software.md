---
date: 2026-02-26
tags:
  - IngegneriaSoftware
  - appunti
type: lezione
---
# Processi Software

## 1. Introduzione ai Processi Software

Sviluppare software non significa semplicemente scrivere codice, di fatto lo sviluppo di un sistema software è un'attività collettiva che coinvolge più persone, ruoli e decisioni distribuite nel tempo. Anche con programmatori molto competenti, l'assenza di un processo condiviso porta facilmente a incomprensioni, duplicazione di funzionalità e a un'evoluzione incoerente del sistema.

Un **processo software** fornisce una struttura organizzativa comune per:
* Decidere come procedere (fasi, iterazioni, rilasci).
* Coordinarsi nel tempo (chi fa che cosa e quando).
* Verificare il lavoro in modo sistematico.

L'obiettivo principale non è aggiungere burocrazia, ma ridurre il caos, garantire che il progetto proceda in modo tracciabile e aumentare la prevedibilità dei risultati. In questo modo, la qualità e la conoscenza non dipendono dal singolo individuo, ma dal team.

---

## 2. Dal Ciclo di Vita ai Processi

È importante distinguere tra **ciclo di vita** del software e **processo** software:

* **Ciclo di vita del software**: È una vista astratta delle fasi che qualunque progetto attraversa (requisiti, progettazione, implementazione, test, deploy e manutenzione).

* **Processi software**: Sono le strategie organizzative che stabiliscono come combinare le fasi del ciclo di vita. Rispondono a domande pratiche come: in quale ordine affrontare le attività, quanto approfondirle e quanto spesso tornare indietro a rivedere le decisioni.

La scelta del processo dipende sempre dal **contesto** e dal **livello di rischio e incertezza** del progetto. Di fatto l'obiettivo è garantire che il progetto proceda in modo coerente, tracciabile e comprensibile in tutti i soggetti coinvolti.
Qualunque sia il processo adottato, si ritrovano quattro **attività fondamentali**:
1. **Specifica**: Capire cosa il sistema deve fare e quali vincoli rispettare.
2. **Sviluppo**: Progettare e implementare la soluzione.
3. **Validazione**: Verificare che il sistema soddisfi i requisiti e si comporti come atteso.
4. **Evoluzione**: Modificare e mantenere il sistema in risposta a nuove esigenze.
Le differenze tra i vari modelli derivano proprio da come queste attività vengono bilanciate, combinate e iterate nel tempo.

![[Pasted image 20260319092445.png]]

## 3. I Modelli Classici di Processo

Esistono tre modelli classici, che non sono schemi rigidi e mutuamente esclusivi; spesso i progetti reali ne combinano elementi adattandoli al contesto.

### 3.1 Modello Waterfall (a cascata)
Organizza lo sviluppo come una sequenza ordinata e lineare di fasi ben separate. Ogni fase produce gli input per la fase successiva
(es. requisiti -> progettazione -> implementazione -> validazione -> rilascio).
* **Caratteristiche**: È un modello rigido che punta a minimizzare i ritorni indietro; si passa alla fase successiva solo quando la precedente è chiusa.
* **Pro**: Facile da comunicare, forte enfasi sulla documentazione, garantisce tracciabilità ed è ottimale per contesti stabili con obiettivi ben noti.
* **Contro**: Tornare indietro è molto costoso. Poiché gli utenti vedono il sistema completo solo alla fine, c'è un elevato rischio di scoprire troppo tardi mancanze o malintesi. Il *costo del cambiamento* cresce in modo non lineare man mano che si avanza nelle fasi.

![[Pasted image 20260319092915.png]]

>[!NOTE] È particolarmente adatto quando i requisiti sono ben noti e il contesto cambia lentamente ad esempio in alcuni ambiti industriali regolamentati
### 3.2 Modello Incrementale
Il sistema non viene progettato tutto insieme, ma costruito per passi successivi, crescendo attraverso piccoli rilasci progressivi.

![[Pasted image 20260319093351.png]]
* **Vantaggi**: Permette agli utenti di dare un feedback immediato dopo ogni rilascio. Questo consente di correggere la direzione prima, ridurre il rischio e concentrarsi sulle funzionalità di maggior valore.
	![[Pasted image 20260319093419.png]]

* **Attenzioni (Debito Tecnico)**: Richiede comunque una visione architetturale complessiva. Se ogni incremento è visto come un progetto a sé, si accumula *debito tecnico* (es. codice duplicato, mancanza di test), che rende i cambiamenti futuri più fragili e costosi. Gli incrementi devono far parte di un disegno coerente.

### 3.3 Modello a Spirale
Rappresenta lo sviluppo come una serie di cicli successivi per affrontare incertezze. 
Ogni giro della spirale include: definizione degli obiettivi, analisi dei rischi, sviluppo parziale (o prototipazione) e valutazione. Accetta che non tutto sia chiaro fin dall'inizio. Costruendo prototipi (versioni semplificate) è possibile ridurre rischi specifici, come testare una tecnologia o un'interfaccia utente. Man mano che i cicli avanzano, il rischio diminuisce.

![[Pasted image 20260319093623.png]]

> [!INFO] Confronto Modelli
> * **Waterfall**: Sequenziale, fasi fisse. Requisiti stabili, documentazione forte. Poco flessibile.
> * **Incrementale**: Rilasci progressivi. Feedback frequente, adattamento continuo. Più flessibile.
> * **Spirale**: Cicli iterativi guidati dal rischio. Gestione esplicita dell'incertezza, uso di prototipi. Molto flessibile ma più costoso.

---

## 4. Metodi Agili e Scrum

I modelli tradizionali nascono per contesti stabili, tuttavia, oggi i progetti affrontano ambienti altamente dinamici, con richieste mutevoli e aspettative di aggiornamenti continui. 

> [!INFO] Differenza temporale (rilasci)
> ![[Pasted image 20260323144211.png]]
> I processi tradizionali si basano su pochi rilasci distanti nel tempo. I processi agili introducono iterazioni brevi, con molti rilasci ravvicinati per ottenere feedback costanti e collaborazione continua.

Il focus dell'Agile è sulla capacità di adattamento: il software funzionante è la misura principale dell'avanzamento, e vengono valorizzate le persone, le interazioni e la collaborazione con gli stakeholder.

> [!INFO] I Triangoli del Progetto
> ![[Pasted image 20260323144319.png]]
> * **Tradizionale**: Tende a fissare lo **scopo** (tutte le funzionalità previste), lasciando variabili il *tempo* e il *costo*.
> * **Agile**: Fissa **tempo** e **costo**, rendendo flessibile lo *scopo* (le funzionalità) in base alla priorità e al valore per l'utente.

### 4.1 Scrum
Scrum è un framework logico/organizzativo che definisce come un team collabora, prende decisioni e rilascia valore in modo iterativo. Quella che studiamo è una versione *semplificata*.

Si basa su tre ruoli essenziali:
1. **Product Owner**: Rappresenta gli interessi degli utenti e degli stakeholder. Definisce la visione e stabilisce le priorità nel backlog.
2. **Scrum Master**: Facilita il lavoro del team, promuove le pratiche agili e aiuta a rimuovere gli ostacoli.
3. **Development Team**: Realizza concretamente gli incrementi, garantendo la qualità tecnica.
![[Pasted image 20260323144834.png]]

**Gli artefatti principali:**
* **Product Backlog**: Un elenco ordinato di funzionalità, miglioramenti e bug. È un artefatto "vivo" aggiornato continuamente in base ai feedback.
	![[Pasted image 20260323144941.png]]
* **Sprint**: Intervalli di tempo brevi e fissi (es. 2 settimane) con obiettivi limitati ma chiari.
* **Incremento**: Alla fine di ogni sprint, il team deve poter mostrare un incremento funzionante del sistema, consentendo di valutare i progressi e coinvolgere gli stakeholder regolarmente.
	![[Pasted image 20260323145050.png]]
---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]