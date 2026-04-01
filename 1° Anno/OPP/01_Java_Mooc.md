---
tags:
  - OPP
---
# Fondamenti di Java: Stampa, Input e Variabili

## 1. Stampa a Schermo (Printing)
[cite_start]All'interno di Java, è possibile stampare testo utilizzando il comando `System.out.println("");`[cite: 1].
[cite_start]Utilizzando l'IDE Netbeans, la combinazione del comando `sout` + tab restituisce automaticamente la sintassi per la stampa[cite: 1].

## 2. Lettura dell'Input (Reading Input)
[cite_start]L'input si riferisce al testo scritto dall'utente e letto dal programma[cite: 1]. 
* [cite_start]L'input viene sempre letto come una stringa[cite: 2]. 
* [cite_start]Per leggere l'input, si utilizza lo strumento `Scanner` che è incluso in Java[cite: 2].
* [cite_start]Lo strumento può essere importato per l'utilizzo in un programma aggiungendo il comando `import java.util.Scanner;`[cite: 3].
* [cite_start]Questa importazione va inserita prima dell'inizio del blocco del programma principale (`public class ...`)[cite: 4].
* [cite_start]Lo strumento stesso viene creato con l'istruzione `Scanner scanner = new Scanner(System.in);`[cite: 5].

> [cite_start][!INFO] Introduce the scanner tool used for reading user input [cite: 6]
> [cite_start][!INFO] Create a tool for reading user input and name it scanner [cite: 7]
> [cite_start][!INFO] Print "Write a message: " [cite: 8]
> [cite_start][!INFO] Read the string written by the user, and assign it to program memory "String message = (string that was given as input)" [cite: 8]
> [cite_start][!INFO] Print the message written by the user [cite: 9]

[cite_start]Più precisamente, l'input viene letto con il metodo `nextLine()` dello strumento scanner[cite: 9]. 
* [cite_start]La chiamata `scanner.nextLine()` rimane in attesa che l'utente scriva qualcosa[cite: 10]. 
* [cite_start]Quando l'utente scrive qualcosa e preme Invio, la stringa fornita viene assegnata a una variabile di tipo stringa (in questo caso `message`)[cite: 11]. 
* [cite_start]Il programma è quindi in grado di fare riferimento alla variabile `message` più avanti — nell'esempio, la variabile `message` è richiamata nel comando di stampa[cite: 12].

[cite_start]L'esecuzione si ferma e attende l'input quando giunge a un'istruzione che tenta di leggere l'input dall'utente (come il comando `reader.nextLine()`)[cite: 18]. [cite_start]L'esecuzione continua solo dopo che l'utente ha scritto un input e premuto Invio[cite: 19].

### 2.1 Concatenazione: Unire le Stringhe
[cite_start]La stringa da stampare può essere formata da stringhe multiple utilizzando l'operatore `+`[cite: 13]. [cite_start]Per esempio, il programma può stampare "Hello world!" su un'unica riga[cite: 14]. [cite_start]Lo stesso metodo può essere impiegato per unire una stringa letterale (testo) al valore di una variabile stringa[cite: 15].

## 3. Variabili (Variables)
[cite_start]Il comando legge l'input dell'utente e restituisce una stringa; se si vuole usare questa stringa all'interno del programma, deve essere salvata in una variabile stringa — `String message = scanner.nextLine();`[cite: 16]. [cite_start]Un valore salvato in una variabile può essere utilizzato ripetutamente, ad esempio per stampare l'input dell'utente due volte[cite: 17]. 

[cite_start]Come per le stringhe, il valore di una variabile può essere unito a una stringa utilizzando il segno "+"[cite: 19]. 
* [cite_start]Il tipo della variabile viene dichiarato quando la variabile viene definita per la prima volta[cite: 19]. 
* [cite_start]Quando viene assegnato un nuovo valore alla variabile, il tipo non viene più dichiarato[cite: 20].
* [cite_start]**Persistenza del Tipo:** Una volta che il tipo di una variabile è stato dichiarato, non può più essere cambiato[cite: 21].
* [cite_start]**Eccezioni:** C'è un'eccezione: un numero intero (integer) può essere assegnato a una variabile di tipo decimale (double), poiché Java sa come convertire un intero in un double durante l'assegnazione[cite: 22].

### 3.1 Convenzioni sui Nomi (Name Convention)
* [cite_start]I nomi delle variabili non possono contenere determinati simboli speciali, come i punti esclamativi (!)[cite: 23].
* [cite_start]Anche gli spazi non sono permessi, poiché sono usati per separare le parti dei comandi[cite: 24].
* [cite_start]Invece degli spazi, la convenzione in Java è usare uno stile noto come `camelCase`[cite: 25].
* [cite_start]La prima lettera del nome di una variabile è sempre scritta in minuscolo[cite: 26].

## 4. Conversione dei Dati (Parsing)
I valori in formato stringa possono essere convertiti in altri tipi di dati tramite metodi specifici:
* [cite_start]**Lettura degli Interi:** `Integer.valueOf` converte una stringa in un intero (prende la stringa contenente il valore da convertire come parametro)[cite: 27].
* [cite_start]**Lettura dei Decimali:** `Double.valueOf` converte una stringa in un double[cite: 27].
> [cite_start][!INFO] convert a string to double [cite: 27]
* [cite_start]**Lettura dei Booleani:** `Boolean.valueOf` converte una stringa in un booleano[cite: 27].

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[]]

-----