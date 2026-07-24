## Permessi file/directories

Prendendo come esempio il risultato di  `ls -l` :
`-rwxr-xr-x 1 davide davide 1452 Jul 24 15:41 compara.sh`

`--`           tipo file (in questo caso "normale")
`rwx`         il proprietario può leggere, scrivere ed execute
`r-x`         il gruppo può  leggere e execute
`r-x`         same per gli altri utenti

`1` hard link, indica quante voci del filesystem puntano a questo specifico inode (file semplici di solito è 1)
`davide`               proprietario
 
`davide`               gruppo
`1452`                   dimensione in byte
`data e ora`      dell'ultima modifica
`compara.sh`      nome del file/directory


## SYSTEM CALLS

Le syscalls sono dei servizi che offre il sistema operativo (direct all to the system), 
Ce ne sono di tipo *kernel mode* e *user mode*. Non sono invocate direttamente ma tramite funzioni wrappers della libreria `glibc`
#### **Per files**
l'Accesso ai file può avvenire con le syscalls (open,write ecc... meglio se wrappers) oppure con la Standard I/O library (fopen, fwrite ecc...)
- open
- close
- read
- write
- lseek -> sopsta il puntatore dentro il file
- stat(fstat, Istat) -> info sugli attributi di un file
- dup, dup2 ,dup3 -> Duplicate file descriptor
#### **Per directories** 
 - mkdir -> crea
 - rmdir -> elimina se vuota
 - chdir -> cambia la current directry
 ##### **Open()**
Serve ad aprire/create un file e restituisce un numero intero detto **FD** (File Descriptor)
Se l'operation ha successo il valore è >= `0`, se fallisce `-1` ed imposta la global var `errno` per indicare l'errore.

```c
#include <fcntl.h>   // Per open e i flag (O_WRONLY, O_CREAT, ecc.)
#include <unistd.h>  // Per close

int main() {
    // Apre un file in sola scrittura. 
    // Se non esiste lo crea (O_CREAT), se esiste cancella il contenuto (O_TRUNC).
    // Imposta i permessi a 0644 (Read/Write per owner, Read per altri).
    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

    if (fd == -1) {
        // Gestione errore
        return 1;
    }

    // ... operazioni di scrittura con write(fd, ...) ...

    close(fd); // Chiusura del file descriptor
    return 0;
}
```
- Apre il file specificato  da `pathname`
- `flags` specifica il comportamento dell'apertura (composto di varie opzioni come **bitwise OR** `|`.  
	- Deve includere una tra  `O_RDONLY, O_WRONLY o O_RDWR`
- `mode` serve solo se si sta *creando un file* (includendo il tag `O_CREAT`)
	- Definisce i permessi del file (rd, wr, ex per p, g and o)
	- i permessi effettivi al file saranno `mode & (~umask)` ( il `mode` ridotto dal sistema `umask` )
