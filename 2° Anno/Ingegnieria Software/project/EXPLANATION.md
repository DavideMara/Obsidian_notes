# Progetto Ingegneria del Software - Spiegazione dei Componenti

Questo documento fornisce una spiegazione dettagliata dell'architettura e dell'implementazione del sistema, con particolare attenzione alle componenti **Database** e **CLI**.

---

## 📂 1. Struttura delle Directory e dei File

Il progetto segue l'architettura standard di Maven:

*   **`src/main/java/it/transport/manager/`**
    *   **`Main.java`**: Il punto di ingresso dell'applicazione. Controlla la disponibilità del database MySQL e inizializza i servizi e la CLI.
    *   **`entity/`**: Rappresenta le entità del dominio (i dati).
        *   `Ticket.java`: Modella il biglietto (ID, zona, stato, data emissione, data convalida).
        *   `Zone.java`: Modella la zona tariffaria (ID, nome, prezzo).
        *   `Wallet.java`: Modella il portafoglio dell'utente a runtime (gestito solo in memoria).
        *   `TicketStatus.java`: Definisce gli stati del biglietto (`TO_VALIDATE` e `VALIDATED`).
    *   **`dao/`**: Livello di persistenza (Data Access Object) che astrae l'accesso ai dati.
        *   `ITicketDAO.java` e `IZoneDAO.java`: Interfacce che dichiarano le operazioni di lettura/scrittura.
        *   `DBConnection.java`: Utility per connettersi al database MySQL tramite JDBC.
        *   `MySQLTicketDAO.java`: Implementazione delle query SQL per i biglietti.
        *   `MySQLZoneDAO.java`: Implementazione delle query SQL per le zone.
    *   **`service/`**: La logica di business disaccoppiata (Application Layer).
        *   `TicketPurchaseService.java`: Gestisce la logica di acquisto (scalare il saldo, creare il biglietto).
        *   `TicketValidationService.java`: Gestisce la logica di convalida a bordo.
    *   **`presentation/`**: La CLI dell'applicazione.
        *   `TicketCLI.java`: Menu interattivo e interazione con l'utente.

---

## 🗄️ 2. Il Layer Database (Persistenza)

L'interazione con il database MySQL avviene tramite **JDBC (Java Database Connectivity)**.

### A. Gestione Connessione (`DBConnection.java`)
Questa classe stabilisce la connessione con il driver MySQL:
```java
public static Connection getConnection() throws SQLException {
    String host = System.getenv().getOrDefault("DB_HOST", "localhost");
    // ...
    return DriverManager.getConnection(url, user, password);
}
```
*   **Variabili d'ambiente:** Legge l'host del database (es. `db` quando gira in Docker o `localhost` quando si avvia localmente), garantendo che l'applicazione funzioni in entrambi gli ambienti senza modifiche al codice.

### B. Persistenza Biglietti (`MySQLTicketDAO.java`)
Questa classe traduce i metodi Java in comandi SQL.
*   **Mappatura Relazionale:** Nella tabella SQL `tickets` non salviamo il nome della zona in formato stringa, ma usiamo la chiave esterna `zone_id` che fa riferimento alla tabella `zones`.
    *   **`saveTicket(Ticket t)`**:
        1. Esegue prima una query per trovare l'ID della zona dal nome:
           `SELECT id FROM zones WHERE name = ?`
        2. Esegue l'inserimento usando l'ID trovato:
           `INSERT INTO tickets (id, zone_id, status, created_at, validated_at) VALUES (?, ?, ?, ?, ?)`
    *   **`findTicketById(String id)`**:
        Usa una **`JOIN`** SQL per recuperare le informazioni del biglietto e il nome associato della zona contemporaneamente:
        `SELECT t.*, z.name AS zone_name FROM tickets t JOIN zones z ON t.zone_id = z.id WHERE t.id = ?`

*   **Prevenzione Memory/Connection Leaks:**
    Tutte le connessioni ed i prepared statements sono racchiusi in blocchi **`try-with-resources`** di Java. Questo assicura che le connessioni al database vengano chiuse automaticamente non appena l'operazione è conclusa, evitando blocchi e saturazione delle risorse del server DB.

---

## 💻 3. Il Layer CLI (Presentazione)

L'interfaccia utente è interamente testuale e interattiva.

### A. Ciclo di Controllo
La classe `TicketCLI` esegue un loop continuo (`while`) che legge i comandi inseriti dall'utente tramite `Scanner`:
*   Opzione **1**: Avvia il flusso di acquisto biglietto (`handleBuyTicket`).
*   Opzione **2**: Avvia il flusso di convalida (`handleValidateTicket`).
*   Opzione **3**: Chiude l'applicazione.

### B. Gestione degli Input e Robustezza
Per evitare crash dovuti a input errati da parte dell'utente (ad esempio, inserimento di lettere dove sono richiesti numeri):
*   **Validazione Prezzi:** Il saldo inserito dall'utente viene convertito usando `Double.parseDouble(balanceInput)`. Se l'utente scrive una stringa non valida (es. "ciao"), viene catturata la `NumberFormatException` e mostrato un messaggio di errore senza interrompere il programma.
*   **Validazione ID Zona:** Analogamente, la selezione della zona viene validata controllando che l'ID inserito corrisponda a un numero intero valido.

### C. Disaccoppiamento dai Servizi (SOLID)
La CLI non chiama mai direttamente le classi concrete del database. Interagisce esclusivamente con i servizi tramite le interfacce `ITicketPurchaseService` e `ITicketValidationService`. 

---

## ⚙️ 4. Avvio Dinamico e Fallback (`Main.java`)

Per rispettare l'ADR-005, la classe `Main.java` fa da "collante":
1. Tenta di stabilire una connessione con il database MySQL (`DBConnection.getConnection()`).
2. **Se la connessione riesce:** Inizializza le classi reali `MySQLTicketDAO` e `MySQLZoneDAO`.
3. **Se la connessione fallisce (es. DB offline):** Stampa un avviso e istanzia al volo dei **Fake DAO in memoria** (tramite classi anonime che salvano i dati dentro una `Map` e una `List` temporanee). 
4. Avvia la CLI con i servizi configurati. In questo modo, l'applicazione rimane sempre avviabile e testabile localmente.
