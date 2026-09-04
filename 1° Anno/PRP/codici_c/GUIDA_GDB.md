# 🛠️ Guida Pratica a GDB per l'Esame di Programmazione Procedurale (PRP)

Questa guida è strutturata per farti padroneggiare **GDB (GNU Debugger)** partendo da zero, con comandi mirati direttamente alla verifica degli esercizi d'esame (conversioni, promozioni, mappa di memoria Little-Endian, liste collegate).

---

## 1. ⚙️ Prerequisiti: Come compilare per il Debugging

Per usare GDB al massimo delle sue potenzialità, il codice va compilato con due flag fondamentali:
```bash
gcc -g3 -O0 -Wall -Wextra sorgente.c -o eseguibile
```
* `-g3`: include tutte le informazioni di debug dettagliate (nomi delle variabili, numeri di riga e persino le macro `#define`).
* `-O0`: disabilita tutte le ottimizzazioni del compilatore. Senza questo flag, il compilatore potrebbe riordinare o eliminare variabili, rendendo il debug confuso.

Nella cartella `codici_c`, basta eseguire:
```bash
make
```

---

## 2. 🚀 Come Avviare ed Uscire da GDB

* **Avvio standard:**
  ```bash
  gdb ./03_mappa_memoria
  ```
* **Avvio con interfaccia visiva (TUI - Text User Interface):**
  ```bash
  gdb -tui ./03_mappa_memoria
  ```
  *(La modalità TUI mostra il codice sorgente in alto e la console GDB in basso. Usa `Ctrl+X` seguito da `A` per attivarla/disattivarla).*
* **Uscire da GDB:**
  ```text
  (gdb) quit    # oppure semplicemente 'q'
  ```

---

## 3. 🚦 Comandi Fondamentali di Controllo del Flusso

| Comando Completo | Abbreviazione | Descrizione |
| :--- | :---: | :--- |
| `run` | `r` | Avvia l'esecuzione del programma dall'inizio. |
| `break <target>` | `b <target>` | Imposta un punto di interruzione (*breakpoint*). Es: `b main`, `b 25`, `b test_mappa_1`. |
| `info breakpoints` | `i b` | Mostra la lista dei breakpoint attivi con il loro numero identificativo. |
| `delete <num>` | `d <num>` | Cancella il breakpoint specificato (o tutti se non passi argomenti). |
| `next` | `n` | Esegue la riga corrente e passa alla successiva (**NON entra** nelle funzioni chiamate). |
| `step` | `s` | Esegue la riga corrente (**ENTRA** dentro la funzione chiamata). |
| `continue` | `c` | Riprende l'esecuzione fino al prossimo breakpoint o alla fine. |
| `finish` | `fin` | Esegue fino al completamento della funzione corrente e ritorna al chiamante. |
| `list` | `l` | Mostra 10 righe di codice sorgente attorno alla posizione corrente. |

---

## 4. 🔍 Ispezione delle Variabili (`print`)

Il comando `print` (`p`) supporta formattatori speciali con la sintassi `p/FORMATO espressione`:

| Formato | Comando | Significato ed Esempio |
| :---: | :--- | :--- |
| **Decimale** | `p x` | Stampa il valore in base 10 con segno. |
| **Unsigned** | `p/u x` | Stampa il valore come intero senza segno (utile per vedere wrapping es. -5L). |
| **Esadecimale** | `p/x x` | Stampa in formato Hex (`0x...`). |
| **Binario** | `p/t x` | Stampa in formato binario (`t` sta per *two's complement / binary*). |
| **Carattere** | `p/c x` | Stampa come carattere ASCII. |
| **Indirizzo** | `p &x` | Mostra l'indirizzo di memoria della variabile. |
| **Tipo** | `whatis x` / `ptype x` | Mostra la definizione e il tipo esatto della variabile o `struct`. |

> 💡 **Display Automatico (`display`):**
> Se vuoi vedere il valore di una variabile aggiornato automaticamente a ogni passo `n`:
> ```text
> (gdb) display a
> (gdb) display/x a
> (gdb) undisplay 1
> ```

---

## 5. 🧠 Ispezione della Memoria Byte per Byte (`examine` / `x`)

Questo è il comando **più importante** per l'esame per verificare la mappa di memoria e la disposizione **Little-Endian**.

Sintassi:
$$\text{x / [Numero\_Elementi] [Formato] [Dimensione\_Unità] <Indirizzo>}$$

* **Dimensione Unità:**
  * `b`: Byte (1 byte, 8 bit) $\implies$ ideale per `char`
  * `h`: Halfword (2 byte, 16 bit) $\implies$ ideale per `short`
  * `w`: Word (4 byte, 32 bit) $\implies$ ideale per `int`
  * `g`: Giant word (8 byte, 64 bit) $\implies$ ideale per `long long` e puntatori su 64-bit

* **Formati Principali:** `x` (Hex), `t` (Binario), `d` (Decimale signed), `u` (Decimale unsigned), `c` (Char).

### 📌 Esempi Pratici per la Mappa di Memoria:
```text
(gdb) x/16xb &a       # Mostra 16 byte a partire da &a in formato Esadecimale (1 byte alla volta)
(gdb) x/16tb &a       # Mostra 16 byte in formato Binario (8 bit alla volta)
(gdb) x/4wd &a        # Mostra 4 int (32-bit) in decimale
(gdb) x/8hd &a        # Mostra 8 short (16-bit) in decimale
```

---

## 6. 🔗 Debugging di Puntatori e Liste Collegate

1. **Vedere il contenuto di una struct puntata:**
   ```text
   (gdb) p *curr
   $1 = {info = 5, pNext = 0x5555555592c0}
   ```
2. **Navigare i nodi successivi:**
   ```text
   (gdb) p curr->pNext->info
   (gdb) p *(curr->pNext)
   ```
3. **Impostare un Watchpoint (`watch`):**
   Interrompe il programma nel momento esatto in cui un valore o puntatore viene **modificato**:
   ```text
   (gdb) watch pFirst
   (gdb) watch curr->info
   ```

---

## 7. 📚 Stack Frame e Chiamate di Funzione

Quando si entra in funzioni ricorsive o annidate (`main` $\to$ `g1` $\to$ `g2`):
* `backtrace` (o `bt`): mostra tutta la catena delle chiamate attive nello stack.
* `frame <n>` (o `f <n>`): seleziona il frame `<n>` per esaminarne le variabili locali.
* `info locals`: stampa tutte le variabili locali del frame corrente.
* `info args`: stampa gli argomenti passati alla funzione del frame corrente.

---

## 8. 🎯 Sessione Pratica Guidata Passo-Passo

Fai questa prova sul terminale per vedere la memoria reale dell'Esercizio d'Esame:

```bash
cd "/home/davide/Uni/Obsidian_notes/1° Anno/PRP/codici_c"
gdb ./03_mappa_memoria
```

All'interno del prompt di GDB esegui in sequenza:

```text
(gdb) b test_mappa_1
(gdb) r
(gdb) n
(gdb) n
(gdb) n
(gdb) # Ora siamo subito prima delle modifiche *(q+2) = -1 e *((short*)&q[9]) = 513

(gdb) # Ispezioniamo i 16 byte iniziali dell'array 'a':
(gdb) x/16xb a

(gdb) # Facciamo i prossimi due step per applicare le modifiche:
(gdb) n
(gdb) n

(gdb) # Controlliamo come sono cambiati i singoli byte:
(gdb) x/16xb a

(gdb) # Valutiamo direttamente le espressioni dell'esame in GDB:
(gdb) p ((&a[3] - a) + p[5]) % 2
(gdb) p ((q[12] >> 2) | q[4]) >= 9

(gdb) c
(gdb) q
```

---

## 9. 📋 Tabella Riassuntiva dei Cheat Commands

```text
  AVVIO/STOP          FLUSSO             ISPEZIONE           MEMORIA & STACK
  ----------------    ---------------    ----------------    -----------------
  gdb ./prog          r (run)            p var               x/16xb &var
  q (quit)            b <line/func>      p/x var             x/4wd &var
  make                n (next)           p/t var             bt (backtrace)
                      s (step)           p/u var             info locals
                      c (continue)       whatis var          info args
                      fin (finish)       watch var           display var
```
