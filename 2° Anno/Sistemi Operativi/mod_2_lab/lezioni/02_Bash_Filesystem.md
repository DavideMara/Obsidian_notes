---
date: 2026-03-11
subject: Sistemi Operativi con Laboratorio - BASH e Attributi dei File
tags:
  - sistemi-operativi
  - appunti
type: lezione
---

# Prime Nozioni su BASH e Filesystem

## Esecuzione dei Comandi e Path
* In un ambiente Unix/Linux, la shell BASH non esegue di default i comandi o gli script che non si trovano nella directory corrente.
* Questo è legato al concetto di processo all'interno del sistema.
* Per eseguire un file eseguibile situato nella cartella attuale (es. `a.out`), è necessario specificare il percorso relativo utilizzando `./a.out`.
* Il simbolo `.` rappresenta la directory corrente.
* Il simbolo `..` rappresenta la directory padre, ovvero quella che contiene la directory corrente.
* Il filesystem in Unix è strutturato come un albero rovesciato con un'unica radice principale chiamata `root` (indicata con `/`), a differenza dei sistemi Windows che usano lettere di unità (es. C:) per ogni disco o partizione.

## Variabili di Ambiente e Comandi Base
* Il comando `echo` viene utilizzato per stampare sul terminale ciò che gli viene passato come argomento, che si tratti di una stringa di testo o del contenuto di una variabile.
* Eseguendo `echo $PATH` è possibile visualizzare il percorso corrente configurato nel sistema, ovvero le cartelle in cui la shell cerca gli eseguibili.

> [!INFO] // dimostrazione di come lo cerca progressivamente nelle varie cartelle //

* La definizione di una variabile deve seguire una sintassi precisa:
    * Scrivere `$FABIO=Rossi` non è corretto.
    * La sintassi corretta è `FABIO=Rossi`.
    * Eseguendo successivamente `echo $FABIO`, il risultato stampato a terminale sarà `Rossi`.
* Usando il comando `env` è possibile visualizzare l'ambiente corrente e capire dove la variabile è stata memorizzata.
* Se modifichiamo la variabile `$PATH` aggiungendo la directory corrente tramite il comando `PATH=$PATH:.`, non sarà più necessario usare `./` e, eseguendo `a.out`, questo verrà avviato direttamente.
* È importante notare che se apriamo un'altra sessione o finestra della shell, non troveremo più la variabile appena creata, in quanto essa rimane confinata nella shell precedente in cui è stata definita.

## Struttura e Utilità della Linea di Comando
* Il comando `which COMMAND` permette di vedere la definizione e il percorso dell'eseguibile di un comando (si può usare anche `man` per consultare il manuale in linea).
* Il comando `clear` è un esempio di comando che pulisce lo schermo e non necessita di alcun argomento aggiuntivo.
* Analizzando una tipica linea di comando come `ls -l a.out`:
    * `ls` è il comando.
    * `-l` è l'opzione o variazione che modifica il comportamento del comando.
    * `a.out` è l'argomento (o variabile) su cui il comando agisce.
* Il comando `sudo` viene utilizzato per eseguire operazioni con i permessi di `root` (l'amministratore di sistema).
* Nel mondo Linux, i software vengono distribuiti e installati sotto forma di pacchetti.

---

# Attributi dei File e Permessi

## Lettura degli Attributi
* Eseguendo il comando `ls -l`, otteniamo informazioni dettagliate sugli attributi dei file o delle cartelle.
* Un output tipico è: `-rw-rw-r-- 1 fabio fabio 25618 dic 28 16:34 config.php`.

> [!INFO] // spiegare la struttura //

* Questa stringa informativa è così suddivisa:
    * **Tipo del file**: il primo carattere.
    * **Permessi di accesso**: i successivi nove caratteri.
    * **Numero di hard link**: i collegamenti al file (es. `1`).
    * **Utente proprietario**: chi possiede il file (es. `fabio`).
    * **Gruppo proprietario**: il gruppo di appartenenza (es. `fabio`).
    * **Dimensione del file**: espressa in byte (es. `25618`).
    * **Data e ora**: relative all'ultima modifica (es. `dic 28 16:34`).
    * **Nome del file**: l'identificativo finale (es. `config.php`).

## Tipi di File
* In BASH, il primo carattere dell'output di `ls -l` indica la tipologia dell'oggetto:
    * `-`: file "regolare".
    * `d`: cartella (directory).
    * `b`: device a blocchi.
    * `c`: device a caratteri.
    * `l`: link simbolico.
    * `p`: pipe.
    * `s`: socket.

## I Permessi (Lettura, Scrittura, Esecuzione)

> [!INFO] // slide 4 //

* I permessi si dividono in tre blocchi di tre caratteri, riferiti rispettivamente a: **Utente proprietario**, **Gruppo proprietario**, e **Tutti gli altri utenti**.
* Per i **File**:
    * `r`: permesso di lettura.
    * `w`: permesso di scrittura.
    * `x`: permesso di esecuzione (per script ed eseguibili).
* Per le **Cartelle**:
    * `r`: lettura, intesa come la possibilità di listare gli oggetti contenuti all'interno.
    * `w`: scrittura, intesa come la possibilità di cancellare o aggiungere oggetti contenuti.
    * `x`: accesso, ovvero la possibilità di rendere la cartella corrente (entrarci con `cd`).

## Modificare Proprietari e Permessi
* `chown`: Comando utilizzato per cambiare o modificare l'utente e il gruppo proprietari di un file o directory.
* `chmod`: Comando per cambiare i permessi di accesso a file e directory.

### Utilizzo del comando CHMOD
* La sintassi di base è: `chmod [-R] mode pathname`.
* Parametri:
    * `-R`: Esegue il comando ricorsivamente, applicandolo all'oggetto e a tutto il suo contenuto interno.
    * `mode`: Rappresenta la nuova maschera dei permessi da assegnare.
    * `pathname`: È l'oggetto (o anche più di un oggetto) a cui applicare la nuova maschera dei permessi.

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_OS]]