# Recap Teorico di Ingegneria del Software

Questo documento riassume i concetti chiave discussi durante la sessione d'esame sul progetto **Gestione Biglietti Trasporto Urbano**. Questi argomenti rappresentano i pilastri del design del software orientato agli oggetti e dell'architettura delle applicazioni.

---

## 1. Principi SOLID Applicati

I principi SOLID garantiscono che il codice sia flessibile, manutenibile e scalabile nel tempo.

### Single Responsibility Principle (SRP)
*   **Definizione:** Una classe deve avere una sola responsabilità, ovvero un solo motivo per cambiare.
*   **Nel Progetto:** Lo split del vecchio servizio generico in due servizi distinti:
    *   `TicketPurchaseService` (gestisce solo l'acquisto).
    *   `TicketValidationService` (gestisce solo la convalida).
    *   *Presentation:* La scomposizione di `TicketCLI` in comandi polimorfici individuali (`BuyTicketCommand` e `ValidateTicketCommand`) evita che la CLI debba cambiare se si modifica il flusso di acquisto o di convalida.

### Open/Closed Principle (OCP)
*   **Definizione:** Le entità software dovrebbero essere aperte all'estensione ma chiuse alle modifiche.
*   **Nel Progetto:** L'uso del **Command Pattern** nel Presentation Layer. Se si desidera aggiungere una nuova opzione di menu:
    1.  Si crea una nuova classe che implementa `CLICommand`.
    2.  La si registra nel Composition Root (`Main.java`).
    3.  Non è necessario modificare il ciclo di controllo interno in `TicketCLI.java`.

### Liskov Substitution Principle (LSP)
*   **Definizione:** Gli oggetti di un programma dovrebbero essere sostituibili con istanze dei loro sottotipi senza alterare la correttezza del programma.
*   **Nel Progetto:** La conformità delle implementazioni in-memory anonime e delle implementazioni concrete MySQL (`MySQLTicketDAO` e `MySQLZoneDAO`) rispetto alle interfacce `ITicketDAO` e `IZoneDAO`. Entrambe possono essere sostituite all'avvio in `Main.java` senza alterare il funzionamento dei Servizi o della CLI.

### Interface Segregation Principle (ISP)
*   **Definizione:** I client non dovrebbero essere forzati a dipendere da interfacce che non usano.
*   **Nel Progetto:** La separazione delle interfacce dei servizi. Ad esempio, il modulo di convalida (`ValidateTicketCommand`) dipende unicamente da `ITicketValidationService` e non viene a conoscenza dei metodi legati alle tariffe delle zone o alla gestione dei fondi di acquisto presenti in `ITicketPurchaseService`.

### Dependency Inversion Principle (DIP)
*   **Definizione:** I moduli di alto livello non dovrebbero dipendere da moduli di basso livello. Entrambi dovrebbero dipendere da astrazioni.
*   **Nel Progetto:** 
    *   I Servizi dipendono dalle interfacce DAO (`ITicketDAO`, `IZoneDAO`) e non dalle implementazioni MySQL concrete.
    *   I DAO MySQL richiedono l'interfaccia generica `javax.sql.DataSource` per ottenere le connessioni, disaccoppiando l'infrastruttura SQL dalla gestione specifica della connessione.

---

## 2. Coesione e Accoppiamento (Cohesion & Coupling)

| Concetto | Obiettivo | Descrizione | Nel Progetto |
| :--- | :--- | :--- | :--- |
| **Accoppiamento (Coupling)** | **Basso (Weak / Loose)** | Misura quanto i moduli dipendono l'uno dall'altro. Meno dipendenze ci sono, più è facile modificare o testare un modulo senza rompere gli altri. | Ottenuto iniettando interfacce astratte nei costruttori (Dependency Injection) invece di usare riferimenti statici o istanziazioni hardcoded. |
| **Coesione (Cohesion)** | **Alta (Strong / High)** | Misura il grado di correlazione tra le responsabilità di un singolo modulo. Un modulo ad alta coesione esegue un unico compito ben definito. | Raggiunta estraendo le logiche dei singoli flussi della CLI da `TicketCLI` e posizionandole in singoli `CLICommand` specializzati. |

---

## 3. Domain Model: Anemic vs. Rich

Durante lo sviluppo di un'architettura a livelli, si incontra la scelta di come modellare le classi di business (come `Ticket`):

### Anemic Domain Model (Modello Anemico)
*   **Struttura:** Le entità di dominio sono semplici contenitori di dati (POJO / JavaBean) con getter e setter. La logica di business risiede interamente nelle classi di servizio.
*   **Pro:** Estremamente snello, facile da mappare su database relazionali tramite ORM, le funzioni di business sono centralizzate nei servizi.
*   **Contro:** Rischio di violazione dell'incapsulamento. Qualsiasi componente che ha accesso all'entità può modificarne lo stato (es. cambiare lo stato del biglietto senza aggiornare il timestamp) bypassando le regole di convalida, poiché le proprietà sono esposte tramite setter pubblici.

### Rich Domain Model (Modello Ricco)
*   **Struttura:** Le entità di dominio contengono sia lo stato (dati) che il comportamento (regole di business, transizioni di stato e validazioni). I servizi si limitano a coordinare il recupero delle entità e a salvare i cambiamenti.
*   **Pro:** Forte incapsulamento. L'entità autogestisce la propria consistenza e protegge le proprie invarianti (es. il metodo `ticket.validate()` controlla lo stato attuale e imposta internamente il timestamp di convalida).
*   **Contro:** Può aumentare la complessità dell'entità e renderne più difficoltoso il testing isolato se ha bisogno di collaborare con risorse esterne.

---

## 4. Gestione delle Risorse e Connection Pooling

Nell'integrazione di database SQL reali, la gestione delle connessioni è un fattore critico di prestazione:

> [!WARNING]
> **Il costo di `DriverManager.getConnection()`**
> Ogni invocazione diretta di `getConnection()` apre una nuova connessione socket TCP verso il server database ed effettua l'handshake di autenticazione. Questa operazione richiede tempo ed energia. Inizializzare e distruggere connessioni a ogni singola query è fortemente inefficiente.

### Soluzione: Connection Pooling (es. HikariCP)
*   Un **Connection Pool** mantiene una serie di connessioni fisiche sempre aperte e calde.
*   Quando un DAO richiede una connessione, il pool ne rilascia una esistente (tempo di accesso quasi nullo).
*   Quando la connessione viene "chiusa" (`connection.close()`), non viene interrotta la connessione TCP, ma viene semplicemente rimessa a disposizione del pool per le chiamate successive.
*   L'interfaccia `javax.sql.DataSource` funge da astrazione standard per permettere il passaggio trasparente da connessioni dirette a connection pool strutturati senza modificare la logica dei DAO.


---

## 5. Interface Segregation Principle (ISP) e Testing Isolato
*   **Domanda:** Separazione dei servizi in `ITicketPurchaseService` e `ITicketValidationService` in relazione a ISP e testabilità.
*   **Teoria:**
    *   **Interface Segregation Principle (ISP):** I client non devono essere forzati a dipendere da metodi che non utilizzano.
    *   **Testabilità:** Interfacce focalizzate e di piccole dimensioni rendono i test unitari molto più semplici. Se l'interfaccia di validazione è separata da quella di acquisto, non occorre fare il mocking di componenti non correlati (come le tariffe delle zone o il portafoglio dell'utente) durante il test di convalida di un biglietto.

---

## 6. Gestione delle Eccezioni e Consistenza in Memoria
*   **Domanda:** L'uso di eccezioni generiche (`RuntimeException` su zona non trovata) rispetto a eccezioni custom, e gestione dello stato in-memory del portafoglio se il DB fallisce.
*   **Teoria:**
    *   **Eccezioni Custom:** Aumentano l'espressività delle API. Permettono al chiamante (la CLI o i test unitari) di discriminare il tipo di errore (es. `ZoneNotFoundException` vs `InsufficientFundsException`) e reagire di conseguenza.
    *   **Consistenza dello stato (Rollback):** Se un servizio modifica uno stato in memoria (il saldo del `Wallet`) e poi fallisce il salvataggio persistente (con una `SQLException` sul DAO), il sistema si ritrova in uno stato incoerente. Il servizio deve implementare un blocco `try-catch` per effettuare un rollback del saldo in-memory in caso di errore infrastrutturale prima di propagare l'eccezione.

---

## 7. Strategia di Testing: Fake Manuali vs. Mocking Frameworks (Mockito)
*   **Domanda:** Scrittura manuale di implementazioni in-memory anonime (Fake) rispetto all'uso di Mockito.
*   **Teoria:**
    *   **Compile-time safety:** Il fake manuale garantisce che se l'interfaccia del DAO cambia (es. viene aggiunto un metodo), il compilatore rileva immediatamente l'errore nel test, forzando l'aggiornamento. Mockito crea mock a runtime e compila comunque, rischiando di nascondere bug o generare eccezioni a runtime.
    *   **Velocità ed Esecuzione:** I fake manuali non soffrono dell'overhead di riflessione di Mockito.
    *   **Boilerplate:** Il limite del fake manuale emerge su interfacce con molti metodi, dove Mockito consente di configurare solo le righe necessarie senza implementare tutti i metodi inutilizzati.

---

## 8. Architettura a Livelli: Strict vs. Relaxed Layering
*   **Domanda:** La dipendenza diretta della CLI (Presentation Layer) da `IZoneDAO` (Infrastructure Layer) e la sua risoluzione.
*   **Teoria:**
    *   **Strict Layering (Architettura Stretta):** Un livello $N$ può dialogare unicamente con il livello $N-1$ immediatamente inferiore. Nel nostro caso, la CLI (Presentation) non deve conoscere i DAO (Infrastructure), ma deve passare dal Service Layer per ottenere i dati (le zone).
    *   **Risoluzione:** Disaccoppiare la CLI rimuovendo la dipendenza da `IZoneDAO` ed esponendo la lista delle zone attraverso il Service Layer (`ITicketPurchaseService`), rispettando i confini architetturali e garantendo la manutenibilità in caso di filtri futuri sui dati.