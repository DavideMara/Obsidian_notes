---
date: 2026-02-25
tags:
  - IngegnieriaSoftware
  - appunti
type: lezione
---
## 1. Il Software nei Sistemi Moderni

Il software costituisce ormai la struttura portante dei sistemi moderni in innumerevoli settori (trasporti, comunicazioni, sanità, finanza, ecc.). Di conseguenza, quando un sistema software fallisce, gli effetti possono essere immediati e critici. 

I principali impatti di un fallimento includono:
* Interruzione di servizi più o meno essenziali.
* Problemi legati alla sicurezza e all'esposizione indebita della privacy e dei dati sensibili.
* Perdite economiche e crollo della fiducia da parte del cliente o utente.
* Impossibilità di gestire e garantire la scalabilità del sistema durante i picchi di accesso (es. sistemi di prenotazione o piattaforme bancarie).

> [!INFO] Difatto è necessario **un approccio ingegneristico** per progettare, costruire e mantenere sistemi complessi e duraturi.
## 2. Le Cause dei Fallimenti e la Necessità dell'Ingegneria
In quasi tutti i casi di fallimento, il problema non è mai riducibile a "una singola riga di codice sbagliata". Le cause principali risiedono in carenze metodologiche:
* Requisiti iniziali poco chiari, ambigui o incompleti.
* Decisioni progettuali e architetturali prese in modo affrettato.
* Mancanza di test adeguati e di una corretta gestione del rischio.

> [!INFO] L'Ingegneria del Software nasce proprio per fornire metodologie che riducano la probabilità che questi scenari critici si verifichino (o per limitarne i danni qualora si presentassero).

## 3. Programmazione vs. Ingegneria del Software
La semplice programmazione (la stesura del codice) rappresenta solo una porzione limitata del lavoro complessivo. I piccoli progetti personali possono sembrare lineari, ma nei sistemi reali la complessità esplode a causa di numerosi fattori:
* Molti attori coinvolti con ruoli diversi (utenti, committenti, analisti, sviluppatori, tester, manutentori).
* Vincoli tecnici e organizzativi, uniti alla gestione di una grande mole di dati e all'interazione tra componenti eterogenei.
* Requisiti in continua evoluzione, cambiamenti tecnologici e molteplici contesti d'uso.

Per governare questa complessità entra in gioco una figura fondamentale come quella dell'analista, che si pone da tramite tra il committente (che esprime i propri vincoli verbali) e il programmatore. Il flusso corretto prevede:
* Cliente -> Vincoli verbali tradotti in requisiti chiari -> Progettazione di un'architettura modulare -> Sviluppo facilitato.

> [!INFO] Che cos’è l’Ingegneria del Software
> L'Ingegneria del Software è l'insieme di principi, metodi e strumenti volti a sviluppare e mantenere sistemi software che siano affidabili, utili ed economicamente sostenibili nel tempo.

L'attività di sviluppo è governata da quattro processi generici fondamentali:
1. **Specifica**: Comprendere esattamente cosa il software deve fare e identificare i vincoli che deve rispettare.
2. **Sviluppo**: Progettare l'architettura, le strutture interne del sistema e implementare (scrivere) il codice.
3. **Validazione**: Verificare e testare che il sistema sviluppato soddisfi realmente i requisiti attesi.
4. **Evoluzione**: Modificare e adattare il software per rispondere a nuove esigenze, correggere difetti e affrontare i cambiamenti del contesto operativo.

## 4. Analisi dei Costi e Ciclo di Vita

> [!INFO] Costi
> ![[Pasted image 20260319091048.png]]
> Generalmente, nei progetti reali, i costi si dividono in modo asimmetrico: circa il 20% delle risorse è assorbito dallo sviluppo della prima versione, mentre il restante 80% è destinato alla manutenzione, agli aggiornamenti e all'evoluzione del sistema.

La sostenibilità a lungo termine del software dipende drasticamente dalla *qualità delle scelte architetturali* effettuate nelle fasi iniziali. Un buon progetto facilita enormemente l'evoluzione futura, mentre un design fragile o frettoloso la rende costosa e altamente rischiosa.

Lo sviluppo necessita quindi di un percorso **rigoroso e ordinato** per evitare un lavoro caotico e incontrollabile. Il **ciclo di vita** del software fornisce questo quadro concettuale. Le sue fasi canoniche includono: raccolta dei requisiti, progettazione della soluzione, implementazione, verifica/test, rilascio (deploy) e manutenzione.

> [!INFO] Ciclo della vita sintenticamente
> ![[Pasted image 20260319091232.png]]Le attività iniziali seguono un flusso lineare: requisiti → progettazione → implementazione.
> Dopo il rilascio della prima versione, il processo abbandona la linearità per entrare in un ciclo continuo e iterativo fatto di test, rilascio e manutenzione. Ogni nuovo bugfix o modifica **riattiva** questo ciclo. Spesso, proprio le attività di manutenzione generano l'esigenza di nuovi requisiti, chiudendo il loop e riportando il processo alla fase iniziale.

## 5. Comprensione del Problema e Qualità

> [!INFO] **La costruzione del software deve partire da una reale comprensione del problema da risolvere e delle esigenze degli utenti.**
> Prima di scrivere codice, occorre rispondere a domande fondamentali: Chi userà il sistema? Con quali obiettivi? In quali contesti operativi? Con quali vincoli?.
> Un'analisi iniziale affrettata o superficiale porterà a sviluppare un software poco utile, scarsamente adottato o estremamente costoso da correggere a posteriori. Dedicare il giusto tempo alla comprensione del dominio evita errori strutturali di fondo che impatterebbero su client, maintainer e amministratori.

Poiché emergono costantemente nuove informazioni ed esigenze, nessun progetto procede in linea retta. Il processo reale è intrinsecamente iterativo e adattivo.

La qualità del prodotto si manifesta su due livelli interdipendenti:
1. **Qualità Esterna (Visibile)**: È quella percepita direttamente dall'utente e comprende l'esperienza d'uso (UX), le funzionalità offerte e le prestazioni.
2. **Qualità Interna (Invisibile)**: Riguarda l'architettura, la pulizia del codice, la testabilità, le dipendenze e la documentazione. Una scarsa qualità interna rende il sistema fragile e difficile da evolvere nel tempo, compromettendo infine anche la qualità esterna.
## 6. Figure nello Sviluppo
 Un sistema software è il risultato del lavoro coordinato di molte figure in ruoli differenti e competenze specifiche.
 Ad esempio possiamo trovare:
- utenti e committenti --> che definiscono bisogni e obiettivi;
- analisti e progettisti -->che traducono le esigenze in modelli e architetture;
- sviluppatori e tester--> che costruiscono e verificano il sistema;
- manutentori --> che garantiscono la continuità del servizio nel tempo.
 
![[Pasted image 20260319091817.png]]
L'ingegneria del Software deve far **convivere in modo coerente** ogni ruolo.

## 7. Comunicazione e Gestione del Rischio
Spesso i difetti e i ritardi di un progetto non derivano da limiti puramente tecnici, ma da incomprensioni tra i vari attori coinvolti. Ogni figura (utente, sviluppatore, architetto) osserva il sistema da una prospettiva differente e l'ingegneria del software deve farle convivere coerentemente.

> [!INFO] Rischio 
>  ![[Pasted image 20260319092021.png]]
> Esempi comuni di fallimenti comunicativi:
> * Requisiti fraintesi o espressi in modo ambiguo.
> * Aspettative degli stakeholder non esplicitate chiaramente.
> * Decisioni progettuali prese ma non documentate formalmente.
> * Informazioni critiche che non vengono condivise con tutto il team.
> Pertanto, una comunicazione efficace è da considerarsi parte integrante dell'ingegneria del software, tanto quanto il codice stesso.

La complessità (qualitativa e quantitativa) e le interazioni inaspettate sono il vero avversario del software. Senza metodo, ogni modifica diventa rischiosa e fa degenerare il sistema. L'Ingegneria del Software non elimina del tutto l'incertezza e gli imprevisti (es. requisiti instabili, stime errate, scelte tecnologiche premature), ma fornisce metodi e strumenti per:
* Prevedere con maggiore accuratezza tempi e costi di sviluppo.
* Valutare sistematicamente alternative architetturali prima dell'implementazione.
* Rilevare e risolvere i problemi in fase embrionale.
* Mantenere il controllo sul progetto anche in presenza di forti cambiamenti.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Ingegneria_Software]]