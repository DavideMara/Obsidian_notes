---
date: 2026-10-01
tags:
  - base-di-dati
type: lezione
---
# Vincoli di Integrita nel Modello Relazionale

Dopo aver definito formalmente relazioni, schemi e istanze, la lezione affronta il meccanismo che garantisce che uno stato della base di dati sia *ammissibile*: i vincoli di integrita.

---

## I. I Vincoli di Integrita e la loro Classificazione

> [!IMPORTANT] Definizione di Vincolo di Integrita
> I **vincoli di integrita** sono predicati posti sui valori effettivi che caratterizzano uno stato (o istanza) di base di dati: uno stato e ammissibile **solo se li soddisfa tutti**, e la loro violazione rende lo stato incoerente rispetto al mini-mondo rappresentato.

Si distinguono **quattro categorie**:

### I.1 Vincoli Intrinseci (basati sul modello)

Sono imposti dalla struttura stessa del modello dei dati e **non richiedono di essere dichiarati esplicitamente**, essendo soddisfatti per costruzione da ogni costruzione consentita dal modello.

> [!EXAMPLE] Il Vincolo di Assenza di Tuple Duplicate
> Il divieto per una relazione di contenere tuple duplicate e un vincolo **intrinseco** al modello relazionale: non e dichiarato in alcun modo, eppure ogni istanza ammissibile lo rispetta. Il motivo e formale: poiche un'istanza di relazione e matematicamente un insieme di tuple, per definizione non puo contenere due elementi identici.

### I.2 Vincoli Basati sullo Schema

Sono esprimibili direttamente sugli schemi del modello dei dati, mediante il linguaggio di definizione **DDL** (*Data Definition Language*), e vengono di conseguenza verificati dal DBMS in modo **automatico e centralizzato**.

### I.3 Vincoli Non Esprimibili sullo Schema

Sono vincoli che non possono essere formalizzati negli schemi del modello dei dati e devono essere specificati realizzando **programmi applicativi**; la loro verifica e quindi demandata al codice applicativo e **non e garantita dal DBMS**.

### I.4 Vincoli di Dipendenza Funzionale

Costituiscono un ulteriore ed importante insieme di vincoli, impiegati principalmente per **verificare la qualita della progettazione** di basi di dati relazionali.

> [!IMPORTANT] Dove viene imposto il vincolo
> Le quattro categorie si distinguono in funzione del **soggetto che assume la responsabilita** di fare rispettare il vincolo:
> - il **modello dei dati**, che lo garantisce da solo e senza dichiarazione (vincoli intrinseci);
> - lo **schema**, che lo dichiara in DDL e ne affida la verifica al DBMS (vincoli basati sullo schema);
> - i **programmi applicativi**, che devono codificarlo a mano con i margini di errore che ne conseguono (vincoli non esprimibili sullo schema).
>
> Le **dipendenze funzionali** hanno invece un ruolo diverso da tutti gli altri: non vengono usate per reprimere stati incoerenti, ma per **valutare la bonta della progettazione**.

---

## II. I Vincoli Basati sullo Schema

I vincoli basati sullo schema, oggetto di studio sistematico di questa lezione, sono i vincoli che possono essere espressi direttamente negli schemi del modello dei dati tramite il DDL. La loro formalizzazione nello schema ha **due conseguenze decisive**.

> [!WARNING] Centralizzazione della Verifica
> Il vincolo diventa parte della **descrizione formale** della base di dati, anziche logica disseminata nei programmi che la accedono.

> [!WARNING] Verifica Automatica a Ogni Operazione
> Il DBMS puo controllare il rispetto del vincolo in corrispondenza di **ogni operazione di aggiornamento**, impedendo che uno stato non ammissibile venga mai materializzato.

A loro volta, i vincoli basati sullo schema si suddividono ulteriormente in due famiglie, distinte per l'ampiezza dell'ambito che coinvolgono.

### II.1 Le Due Famiglie

| Famiglia | Ambito di coinvolgimento | Portata della verifica |
| :--- | :--- | :--- |
| **Vincoli intrarelazionali** | Coinvolgono un unico schema di relazione | Verificabili relazione per relazione, in isolamento |
| **Vincoli interrelazionali** | Coinvolgono piu schemi di relazioni | Richiedono di considerare contemporaneamente lo stato di piu relazioni della base di dati |

> [!INFO] Una Distinzione Operativamente Netta
> La verifica di un vincolo intrarelazionale e un controllo **locale**, confinato all'interno di una singola relazione; quella di un vincolo interrelazionale e un controllo **globale**, che deve tenere conto contemporaneamente del contenuto di piu istanze di relazione e presuppone quindi un meccanismo di coordinazione tra le strutture coinvolte.

---

## III. Riepilogo

| Categoria | Dove e dichiarato | Chi verifica | Rischio |
| :--- | :--- | :--- | :--- |
| **Intrinseci** | Non dichiarati (imposti dal modello) | Il modello stesso, per costruzione | Nessuno: soddisfatti sempre |
| **Basati sullo schema** | DDL | Il DBMS, automaticamente a ogni update | Nessuno se ben formalizzati |
| **Non esprimibili sullo schema** | Codice applicativo | Il programmatore, manualmente | Margini di errore, omissioni |
| **Dipendenze funzionali** | Nella progettazione dello schema | Analisi della qualita progettuale | Non reprimono stati incoerenti |

> [!EXAMPLE] Riferimento ai Vincoli della Lezione 3
> Il principio "nessuna tupla duplicata" gia studiato tra le conseguenze del formalismo matematico (lezione 3, sez. VI.2) e la manifestatione concreta di un vincolo intrinseco: nessun `CREATE TABLE` lo dichiara, eppure il DBMS non ammette che si realizzi.

---
## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Base_di_Dati]]