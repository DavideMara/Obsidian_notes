---
date: 2026-02-27
tags:
  - labSO
  - sistemi-operativi
type: lezione
---

# Sistemi Operativi con Laboratorio: BASH - Prime nozioni e primi comandi

## 1. Cenni Storici e Famiglie di Sistemi Operativi

### Unix
* **Unix** è una "famiglia" di sistemi operativi **multitasking** e **multiuser** che deriva dall'originale AT&T Unix.
* Lo sviluppo di AT&T Unix è iniziato nel 1969 al Bell Labs research center, principalmente ad opera di **Ken Thompson**, **Dennis Ritchie** e altri collaboratori.
* Inizialmente si è assistito a una forte frammentazione dove "ognuno si fece il suo", dando vita a varianti come BSD (UC Berkeley), Xenix (Microsoft), SunOS/Solaris (Sun Microsystems), HP-UX (HP), e AIX (IBM).
* Nel corso del tempo, sono stati fatti sforzi per standardizzare le varie release e varianti attraverso iniziative come **POSIX**, **SUS**, e **The OpenGroup**.

### (GNU/)Linux
* **Linux** è un discendente o derivato di Unix, definibile come **Unix-like**.
* È una "famiglia" **open-source** di sistemi operativi Unix-like.
* Si basa sul kernel Linux, rilasciato per la prima volta nel **1991** da **Linus Torvalds**.
* Tecnicamente, sarebbe più corretto parlare di sistema operativo **GNU/Linux**.
* È un sistema **POSIX compatibile**, seppur non ufficialmente POSIX-certified.
* Esistono varie **distribuzioni** (o "distro"), tra cui Debian, SUSE, RedHat, Fedora, Ubuntu e Mint.

### macOS
* Rappresenta un gruppo di sistemi operativi proprietari di casa **Apple**.
* Sono sistemi Unix-like e, soprattutto, **Unix certified** (certificati da The Open Group).
* Hanno attraversato diverse transizioni di **processori**: inizialmente PowerPC, poi dal 2006 sono passati ad Intel, e dal 2020 utilizzano processori 64-bit ARM-based come l'Apple M1 (seguiti da M2, M3, ecc.).
* Ad Ottobre 2024, Apple ha presentato il chip **M4**.

### Android
* Sistema basato su un **kernel Linux modificato**.
* Originariamente sviluppato dalla Open Handset Alliance, la sua versione più diffusa è oggi sviluppata principalmente da **Google**.
* Il resto del sistema, inclusi software vari e utilities, è scritto principalmente in **Java**.
* È specificamente pensato per sistemi **touchscreen mobile**, come telefoni e tablet.

---

## 2. Concetti Base dei Sistemi Unix

### Struttura e Architettura
* Sistemi **multitasking e multiuser**.
* **Modularità**: Unix non è un sistema monolitico.
    * Il **kernel** fornisce i servizi fondamentali del sistema.
    * La **shell** (o in alternativa l'interfaccia grafica) permette all'utente di interagire con il sistema operativo.
    * Esistono tante semplici utility che svolgono compiti base; queste possono essere combinate insieme tramite **pipe line** per eseguire compiti anche molto complessi.
* È stato concepito appositamente per supportare gruppi di sviluppatori che lavorano insieme.
* **Portabilità**: Essendo stato quasi subito riscritto in **C**, risulta molto più portabile rispetto ai vecchi sistemi scritti in assembly.
* I device e i vari strumenti per l'IPC (Inter-Process Communication) sono trattati e mostrati dal sistema come se fossero dei semplici **file**.
* Il formato di memorizzazione dei file è volutamente semplice (**plain text**).

### Autenticazione e Utenti
* Essendo multiutente, ogni utente possiede una **login**, una **password** e una **home directory** (uno spazio disco personale dove salvare i propri file).
* Esiste un utente privilegiato, chiamato **root**, che funge da amministratore del sistema.
* Ogni utente gestisce in autonomia i permessi di accesso sulle proprie cartelle e sui propri file.
* Gli utenti possono essere aggregati in **gruppi** per definire e semplificare privilegi comuni.

---

## 3. Terminale, Console e BASH

### Definizioni
* **Terminal**: Un ambiente di input e output testuale. Una finestra di terminale (o emulatore di terminale) è una finestra di solo testo che emula una console all'interno di una GUI (Graphical User Interface).
* **Console**: Un terminale fisico; un pannello della strumentazione contenente i controlli del computer. Una console è quindi un tipo specifico di terminale.
* **Shell**: È l'interfaccia vera e propria tra il sistema operativo e l'utente. Permette di eseguire programmi e offre funzionalità simili a un linguaggio di programmazione per automatizzare operazioni. Può essere a riga di comando (Bash, csh, ksh) o grafica (GNOME, KDE).

### BASH (Bourne Again Shell)
* È un interprete interattivo di comandi per sistemi Unix-like.
* È stata creata nel **1989** da **Brian Fox** per il progetto GNU, nata come alternativa ed estensione della preesistente sh (Bourne shell).
* È la shell di default in moltissime distribuzioni Linux ed è stata la default shell di macOS prima del 2019.
* È un normale programma che gira nello "spazio utente".
* Espone il **prompt** e attende che l'utente inserisca una linea di comando; successivamente la interpreta, la esegue e torna in attesa.
* Per terminare la sessione BASH si usa il comando `exit` oppure la scorciatoia da tastiera **EOF (Ctrl+d)**.

> [!IMPORTANT] Il Prompt di BASH
> Il prompt è la stringa di caratteri con cui la shell segnala di essere in attesa di un comando. 
> Esempio tipico: `fabio@fabiopc:/usr/lib/binfmt.d$`
> * **fabio**: username.
> * **fabiopc**: nome host (da non confondere col nome di dominio).
> * **/usr/lib/binfmt.d**: path corrente della directory di default in quel momento.
> * **$**: livello di privilegio dell'utente (il carattere `#` indica l'utente root, mentre `$` indica gli altri utenti).

### Perché usare una shell testuale?
Anche se esistono le interfacce grafiche, la shell testuale si usa perché:
* Aiuta a capire come funziona il sistema "sotto".
* Offre il massimo controllo sui comandi e sulle loro opzioni.
* Permette di configurare le distribuzioni in modo preciso.
* I comandi Unix sono stati nativamente progettati per le interfacce a riga di comando.
* Una volta imparati, risultano più veloci e flessibili.
* Sono estremamente veloci e facilmente accessibili da remoto.
* Funzionano sempre, anche in caso di problemi all'interfaccia grafica o con hardware obsoleto e poco performante.

---

## 4. Il Filesystem


Il filesystem è una struttura ad albero al cui interno sono memorizzati tutti i dati del sistema operativo.
* È organizzato in **File** e **Directory** (o cartelle).
* L'albero ha un'unica radice detta **root**, identificata dal path `/`. A differenza di Windows (che ha `C:`, `D:`, ecc.), in Unix tutti i dati convergono in quest'unico albero, indipendentemente dal numero di dischi o partizioni fisiche.

### Navigazione e Pathnames
Ogni processo nel sistema ha, in ogni singolo istante, una "directory corrente".
* **Pathname assoluto**: È il percorso che parte dalla radice root e porta all'oggetto. Comincia sempre con la barra `/` (es. `/etc/hosts` o `/home/fabio/Desktop`).
* **Pathname relativo**: È il percorso che porta all'oggetto partendo dalla directory corrente o da un punto specifico che non è la radice. Non inizia mai con `/` (es. `log/apache`).
* **Simboli speciali nei path**:
    * `.` (punto): indica la directory corrente.
    * `..` (due punti): indica la directory "padre", ovvero quella che contiene la directory corrente.

### Link e Device Files
* Nel filesystem possono essere presenti file speciali chiamati **link**, che fungono da puntatori/collegamenti ad altri oggetti (in modo analogo ai collegamenti di Windows). Compiere un'operazione su un link significa implicitamente compierla sull'oggetto a cui esso punta.
* Sono presenti anche **special files** o **device files**: espongono un dispositivo hardware all'interno del filesystem come se fosse un normale file. Questo fornisce un'interfaccia universale verso l'hardware, permettendo alle system calls di eseguire operazioni di Input/Output in modo standardizzato.

---

## 5. Primi Comandi BASH

I comandi BASH hanno tipicamente questa sintassi: `nome_comando <opzioni> <argomenti>`. 
Le **opzioni** iniziano tipicamente con il carattere `-` e modificano il comportamento del comando; possono essere accorpate (es. `ls -ltra` equivale a `ls -l -t -r -a`) e a volte richiedono argomenti aggiuntivi. Ogni comando restituisce un valore di ritorno che informa sull'esito, dove solitamente `0` indica che è andato tutto a buon fine.

### Comandi Interni vs Esterni
* **Comandi Esterni**: Sono veri e propri eseguibili registrati nei supporti di memorizzazione. La shell li cerca all'interno dei percorsi di filesystem specificati nella variabile di ambiente `$PATH`. Il comando `which` permette di scoprire dove è memorizzato l'eseguibile di un comando esterno.
* **Comandi Interni**: Sono riconosciuti ed eseguiti direttamente dalla shell stessa (es. i costrutti per lo scripting o il comando `cd`). È possibile vederne la lista utilizzando il comando interno `help`.

### Operazioni sul Filesystem

| Comando | Descrizione |
| :--- | :--- |
| **`ls`** | Elenca file e directory. Può prendere file/cartelle come argomenti specifici (es. `ls -l lettera foto`). |
| **`cd`** | Cambia la directory corrente (è un comando interno). Esempio: `cd /etc`. |
| **`cp`** | Copia file. Es: `cp pippo pluto`. Se pluto è una directory, pippo viene messo al suo interno. |
| **`mv`** | Sposta file o cartelle. Se i file hanno percorsi riferiti alla stessa directory, il comando rinomina il file originario. |
| **`mkdir`** | Crea nuove cartelle. |
| **`rm`** | Rimuove file. |
| **`rmdir`** | Rimuove cartelle, a condizione che siano **strettamente vuote** (altrimenti genera un errore). |
| **`ln`** | Crea collegamenti a file o directory. |
| **`pwd`** | Visualizza la directory corrente in cui ci si trova. |
| **`df`** | Elenca i file system attualmente montati. |
| **`cat`** | Visualizza per intero il contenuto di un file testo. |
| **`realpath`** | Visualizza il path assoluto "risolto" (molto utile per calcolare la vera destinazione di link o riferimenti relativi). |
| **`file`** | Ritorna il tipo reale di un file (testo, binario, pdf) in maniera totalmente indipendente dall'estensione nominale. |
| **`tail`** | Visualizza le ultime "n" linee di un file. |
| **`head`** | Visualizza le prime "n" linee di un file. |

#### Opzioni più Comuni per `ls`
* `-l`: Formato lungo (long format), mostra informazioni aggiuntive sui file.
* `-a`: Elenca tutti i file, compresi quelli "nascosti" (quelli che iniziano col carattere `.`).
* `-t`: Ordina i file mostrati in base alla data di ultima modifica (dal più recente al meno recente).
* `-r`: Inverte il senso dell'ordinamento.
* `-h`: Visualizza le dimensioni dei file in un formato "human readable" e facilmente leggibile.

> [!EXAMPLE] Esempio combinato
> Il comando `ls -lrta` elenca tutti i file e le cartelle (compresi i nascosti), ordinandoli in base al tempo di ultima modifica (dal meno recente al più recente) formattandoli in modalità lunga.

#### Opzioni più Comuni per CANCELLARE o COPIARE Cartelle
* `rm -r cartella`: Rimuove ricorsivamente una cartella e tutto il ramo di file/cartelle non vuote in essa contenute.
* `cp -ar dir1 dir2`: Copia ricorsivamente (`-r`) tutto l'albero sottostante `dir1` dentro `dir2`, preservando (`-a`) gli attributi originari dei file come la data di modifica.

#### Differenza nella creazione dei Link (`ln`)
* **Hard Link** (`ln pippo link1`): Crea una vera e propria copia che occupa spazio fisico sul disco. Se il file originario "pippo" viene cancellato, il file "link1" e il suo contenuto rimangono inalterati.
* **Symbolic Link** (`ln -s pippo link1`): Crea un collegamento simbolico (occupazione minimale su disco). "link1" contiene solo una stringa col percorso di "pippo". Se il file "pippo" originario viene cancellato, "link1" diventa semplicemente un collegamento non valido o rotto.

### Documentazione
Per sapere le funzioni e le opzioni dei comandi, ci sono diverse utility fondamentali:
* **`man <nome_comando>`**: Apre il manuale in linea completo del comando specificato.
* **`apropos <stringa>`**: Cerca e lista i comandi che contengono la stringa specificata all'interno della loro descrizione sintetica.
* **`whatis <comando>`**: Fornisce una descrizione estremamente sintetica del comando passato.
* **`locate <stringa>`**: Ricerca velocemente tutti i file aventi un path che contiene la stringa specificata, interrogando un database interno costruito tramite il tool `updatedb`.
* **`Switch di aiuto rapido`**: Generalmente ogni comando BASH, se invocato aggiungendo lo switch `-h` oppure `--help`, è in grado di stampare a terminale una rapida e sintetica descrizione delle proprie funzionalità.

---

◀️ *Back to:* [[00_Index_OS]]