---
date: 2026-03-10
tags:
  - sistemi-operativi
  - lezione
type: lezione
---
# I/O System Calls in C: Accesso ai File

> [!WARNING] Recupero Lezione
> La prima parte di questi appunti è stata ricostruita dalle slide del docente, integrandola con gli appunti diretti presi a partire da `write` e `read` insieme all'analisi del file `prova.c`.

## 1. Due modalità di accesso ai file

1. **System Calls:** Funzioni dirette del sistema operativo (es. `open(2)`, `write(2)`, `close()`). Sono chiamate non bufferizzate nello spazio utente e richiedono un cambio di contesto user-kernel.
2. **Standard I/O Library:** Funzioni di libreria C (es. `fopen(3)`, `fwrite(3)`). Bufferizzano nello spazio utente, risultando tipicamente più efficienti e veloci.

> [!INFO] System Calls per le Directory
> Oltre ai file, esistono system call per manipolare le cartelle: `mkdir` (crea una directory), `rmdir` (cancella una directory se vuota), e `chdir` (cambia la directory corrente).

---

## 2. Inizio del programma e gestione degli argomenti

Abbiamo analizzato come passare il nome del file direttamente da riga di comando usando gli argomenti del `main`: `int main(int argc, char *argv[])`. `argv` è un puntatore ad un array di puntatori a char. `argv[1]` contiene il nome del file passato dall'utente.

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int iRet = EXIT_SUCCESS, iReadRet;
    int fd;
    char sBuf[] = "Ciao Fabio!\n";
    char sReadBuf [128];
    char *filename;
    
    // Controllo argomenti da terminale
    if (argc < 2){
        printf("Dammi il nome del file!\n");
        exit(EXIT_FAILURE); 
    } else {
        filename = argv[1];
    }
```

---

## 3. Apertura del file (`open`)

La system call `open` apre il file specificato da `pathname`. 
* **`flags`**: Deve includere uno tra `O_RDONLY`, `O_WRONLY` o `O_RDWR`. Altri flag utili sono `O_CREAT` (se il file non esiste lo crea) e `O_TRUNC` (se il file esiste il contenuto viene azzerato).
* **`mode`**: Specifica i permessi da applicare in caso di creazione.
* Ritorna un **file descriptor** (intero positivo) o `-1` in caso di errore.

```c
    /* fd = file descriptor
       primo parametro = pathname (da riga di comando)
       secondo parametro = flags
       terzo parametro = mode (file mode bits) */
       
    fd = open(argv[1], O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    
    if (fd < 0) {
        printf("errno = %d\n", errno);
        perror("Errore in open()"); /* stampa la stringa: descrizione errore */
        iRet = EXIT_FAILURE;
    } else {
```

---

## 4. Scrittura nel file (`write`)

```c
ssize_t write(int fd, const void *buf, size_t count);
```
Scrive i primi `count` byte contenuti in `buf` nel file aperto identificato da `fd`. Ritorna il numero di byte scritti o `-1` in caso di errore. Le operazioni di scrittura sono eseguite a partire dalla posizione corrente (file offset) nel file.

```c
        // Tento la scrittura nel file
        if (write(fd, sBuf, strlen(sBuf)) == strlen(sBuf)){
            printf("Ho scritto nel file %s, fd = %d\n", argv[1], fd);
```

Se la `write` fallisce, viene gestito l'errore:

```c
        } else {
            printf("errno = %d\n", errno);
            perror("Errore in write()");
            iRet = EXIT_FAILURE;
        }
```

---

## 5. Riposizionamento del cursore (`lseek`)

```c
off_t lseek(int fd, off_t offset, int whence);
```
Riposiziona il puntatore nel file. 
* `SEEK_SET`: a offset byte dall'inizio.
* `SEEK_CUR`: a offset byte dalla posizione corrente.
* `SEEK_END`: a offset byte dopo la fine del file.
Ritorna la nuova posizione o `-1` in caso di errore.

```c
            // Riporto il cursore all'inizio (offset 0)
            if (lseek(fd, 0, SEEK_SET) != -1){
```

---

## 6. Lettura e il trucco di `dup2`

```c
ssize_t read(int fd, void *buf, size_t count);
```
Legge `count` byte dal file `fd` e li memorizza in `buf`. Ritorna il numero di byte letti, `-1` per errore o `0` che significa EOF (end of file).

Qui entra in gioco anche **`dup2`**.
```c
int dup2(int oldfd, int newfd);
```
Questa system call torna una copia di `oldfd` ma usa `newfd` come file descriptor copia. Se c'era già un file aperto con descrittore pari a `newfd` viene chiuso. I due file descriptor condividono la posizione corrente nel file.

> [!IMPORTANT] Il trucco della redirezione
> Eseguendo `dup2(fd, 1);`, stiamo dicendo al sistema operativo di prendere il file descriptor 1 (lo `stdout`, ovvero il terminale) e di forzarlo a puntare alla stessa entry di `fd`. Da questo momento in poi, la `printf` successiva scriverà direttamente dentro al file invece che sul terminale!

```c
                // Leggo dal file
                if( (iReadRet = read(fd, sReadBuf, sizeof(sReadBuf) -1 )) != -1){
                    char sWriteBuf[]= "questa proviene da write()\n";
                    int iCount = strlen(sWriteBuf);
                    
                    sReadBuf[iReadRet] ='\0'; // Termino la stringa letta
                    
                    // Redirigo lo stdout (1) sul file (fd)
                    dup2(fd, 1);
                    
                    // Questa printf scriverà nel file, non sul terminale!
                    printf("Ho riletto %d bytes: %s", iReadRet, sReadBuf);  
                    
                } else {
                    perror("Errore in read()");
                    iRet = EXIT_FAILURE;
                }
            } else {
                perror("Errore in lseek()");
                iRet = EXIT_FAILURE;
            }
```

---

## 7. Chiusura del file (`close`)

I file aperti dovrebbero essere chiusi prima di terminare il programma.

```c
    } // fine dell'else relativo all'apertura andata a buon fine

    close(fd);
    return iRet;
}
```

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_OS]]