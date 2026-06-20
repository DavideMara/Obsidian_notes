---
tags:
  - OOP
---
# RIASSUNTO CORSO JAVA

---

## 1. INTRODUZIONE

I motivi principali per cui la **Programmazione Orientata agli Oggetti (OOP)** è efficace sono:
1. **Maggiore produttività**
2. **Semplificazione del lavoro del programmatore**
3. **Sviluppo più rapido**
4. **Riduzione degli errori**

### Programmazione Strutturata vs. OOP
* **Programmazione Strutturata (es. C)**: Un problema viene suddiviso in sottoproblemi più semplici, a loro volta suddivisi in sottoprogrammi, come funzioni e procedure (approccio *top-down*).
* **OOP (es. Java)**: Un'applicazione viene costruita assemblando e facendo interagire **oggetti** più semplici. Gli oggetti sono progettati tramite le **classi**, costruiti e infine utilizzati. Per progettare un oggetto, si specificano:
  * **Proprietà** (attributi o campi / properties o fields)
  * **Funzionalità** (metodi o funzioni)

> [!NOTE]
> ### I Tre Pilastri dell'OOP
> 1. **Ereditarietà (Inheritance)**: La capacità di riutilizzare un design esistente e modificarlo per le proprie esigenze.
> 2. **Incapsulamento (Encapsulation)**: Riutilizzo del codice, astrazione e contenimento degli errori.
> 3. **Polimorfismo (Polymorphism)**: La capacità di un oggetto di comportarsi in modo diverso a seconda del contesto e del valore.

---

## 2. IL LINGUAGGIO JAVA

L'ambiente Java include sia un **compilatore** (compiler) che un **interprete** (interpreter) (Java Runtime Environment, **JRE**).

```text
[Codice Sorgente Java] 
          │
          ▼ (Compilatore)
[Bytecode Java] (indipendente dalla piattaforma)
          │
          ├─► (Interprete JRE - Windows) ──► Esecuzione
          ├─► (Interprete JRE - Linux)   ──► Esecuzione
          └─► (Interprete JRE - macOS)   ──► Esecuzione
```

* **Bytecode**: Pseudo-istruzioni indipendenti dalla piattaforma generate dal compilatore.
* **Interprete (JVM)**: Traduce il bytecode in un eseguibile specifico per il sistema operativo. Questo garantisce un'ottima combinazione di **velocità** e **portabilità** (portability).

---

## 3. PROGRAMMAZIONE ORIENTATA AGLI OGGETTI IN JAVA

* **Classe (Class)**: Il modello generico o "template" per un insieme di oggetti con caratteristiche simili.
* **Oggetto (Object)**: La particolare istanza (elemento concreto) di una classe.
* **Attributi (Proprietà/Campi - Attributes/Properties/Fields)**: Descrivono lo stato, l'aspetto e le qualità dell'oggetto. Esistono campi di istanza (instance fields) e campi di classe (class fields, `static`).
* **Metodi (Comportamenti - Methods/Behaviors)**: Funzioni definite all'interno di una classe che operano sugli oggetti e ne manipolano le proprietà. In Java, *non* è possibile definire funzioni al di fuori di una classe.

### Creazione di un Oggetto
```java
Motocicletta m;              // 1. DICHIARAZIONE: Crea la variabile di riferimento 'm' (occupa 4 byte in memoria)
m = new Motocicletta();      // 2. ISTANZIAZIONE: Alloca fisicamente e crea la nuova motocicletta
m.marca = "Guzzi 1000";      // 3. INIZIALIZZAZIONE: Assegna le proprietà alla variabile
m.colore = "rossa";          
m.mostra();                  // 4. INVOCAZIONE: Chiama il metodo sull'oggetto
```

### Costruttori (Constructors)
Un costruttore è un metodo speciale che:
1. Istanzia l'oggetto e restituisce il suo indirizzo di memoria.
2. Inizializza lo stato dell'oggetto (assegnando i valori iniziali alle proprietà a partire dai parametri).

```java
// Definizione del Costruttore
public Motocicletta(String marca, String colore, boolean a) {
    this.marca = marca; 
    this.colore = colore; 
    this.accesa = a; 
}

// Dichiarazione, istanziazione e inizializzazione su una singola riga
Motocicletta m = new Motocicletta("Guzzi 1000", "rossa", false);
```

### Gestione della Memoria (Memory Management)
La memoria a runtime di Java è divisa in tre aree principali:

| Area di Memoria | Descrizione                                                                                                                                                                                                                     |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **STACK**       | Spazio in cui vengono eseguiti i metodi. Contiene parametri e variabili locali. Il metodo `main` con `args[]` è sempre presente. Gli spazi per i metodi non statici rimangono solo fino al completamento della loro esecuzione. |
| **HEAP**        | Spazio dinamico in cui risiedono gli oggetti effettivi insieme alle loro proprietà.                                                                                                                                             |
| **STATIC**      | Spazio in cui risiedono le variabili statiche, che sono accessibili globalmente.                                                                                                                                                |

> [!IMPORTANT]
> **Riferimenti e Indirizzi (References and Addresses)**: Quando viene dichiarata una variabile oggetto, essa memorizza un indirizzo esadecimale (un puntatore all'area allocata nell'Heap). Inizialmente è `null`. Con `new`, viene allocato lo spazio nell'Heap e l'indirizzo viene memorizzato nella variabile.
> La deallocazione degli oggetti che non sono più riferiti avviene automaticamente grazie al **Garbage Collector**.

### Compilatore vs. Interprete
* **Compilatore (Controlli Statici)**: Si basa sulle dichiarazioni delle variabili; verifica la correttezza sintattica e che le variabili siano inizializzate prima dell'uso.
* **Interprete (Controlli Dinamici a Runtime)**: Rileva gli errori durante l'esecuzione, come:
  * Utilizzo di un oggetto non costruito (`NullPointerException`).
  * Accesso a un indice di array fuori dai limiti (`ArrayIndexOutOfBoundsException`).
  * Parsing di stringhe non numeriche (`NumberFormatException`).
  * Cast tra classi incompatibili (`ClassCastException`).

---

### a. Ereditarietà, Interfacce e Package (Inheritance, Interfaces, and Packages)
* **Ereditarietà (`extends`)**: Consente di definire una sottoclasse (subclass) che eredita campi e metodi da una superclasse (superclass). I campi privati vengono ereditati ma non sono direttamente accessibili.
  * **Ereditarietà Singola (Single Inheritance)**: In Java, ogni classe può estendere solo una superclasse per garantire semplicità e sicurezza al compilatore, evitando ambiguità strutturali.
* **Approcci di Design**:
  * *Bottom-up*: Le classi più complesse vengono costruite a partire da quelle più semplici.
  * *Top-down*: Le classi sono organizzate in una struttura ad albero, partendo da superclassi generali/astratte fino a sottoclassi specifiche.

* **Interfacce (`interface` / `implements`)**: Collezioni di dichiarazioni di metodi che consentono a classi situate in rami diversi della gerarchia di condividere comportamenti simili. Una classe può implementare **più interfacce**. Un'interfaccia può contenere:
  1. Firme di metodi di istanza astratti (senza corpo).
  2. Costanti statiche.
  3. Metodi `default` implementati (sovrascrivibili / overridable).
  4. Metodi statici implementati (non sovrascrivibili / non-overridable).

* **Package**: Raggruppano classi e interfacce correlate per evitare conflitti di nomi. Per impostazione predefinita, viene importato solo `java.lang`; le altre classi richiedono una direttiva `import` o il loro nome completo (fully qualified name).

---

### b. Polimorfismo dei Dati (Data Polymorphism)
Un oggetto di una sottoclasse può essere assegnato a una variabile del tipo della superclasse. Allo stesso modo, una variabile di tipo interfaccia può riferirsi a oggetti di qualsiasi classe che implementi tale interfaccia.

```java
Lavoratore l3 = new Operaio(); // Operaio eredita da Lavoratore
l3.stipendio();                // Esegue il metodo sovrascritto in Operaio
```

> [!TIP]
> * **Early Binding (Compilatore)**: Controlla staticamente che il metodo invocato sia dichiarato nella classe della variabile (`Lavoratore`).
> * **Late Binding (Interprete)**: Determina il tipo effettivo dell'oggetto a runtime (`Operaio`) ed esegue il suo metodo specifico. Java utilizza sempre il late binding, tranne che per i metodi statici, final o privati.

---

### c. Typecasting
Consente di informare esplicitamente il compilatore del tipo effettivo dell'oggetto riferito per sbloccare l'accesso a metodi specifici non presenti nella superclasse. Se il tipo è incompatibile a runtime, viene lanciata una `ClassCastException`.
```java
Operaio o = (Operaio) l3; // Typecast esplicito
```

---

### d. Array
Un array è un oggetto che raccoglie elementi omogenei dello stesso tipo.
* **Creazione Esplicita**: `int[] arr = new int[10];`
* **Creazione Implicita**: `int[] arr = {1, 2, 3, 4};`
* Possiede un campo pubblico in sola lettura `length` che ne indica la dimensione.

---

## 4. MANIPOLAZIONE DEGLI OGGETTI (OBJECT MANIPULATION)

### Assegnazione di Valori agli Oggetti
Un riferimento può essere valorizzato tramite:
1. Chiamata a un costruttore (`new`).
2. Assegnazione di `null`.
3. Assegnazione di un valore costante non nullo.
4. Assegnazione del valore di ritorno di un metodo compatibile.
5. Assegnazione del riferimento di un altro oggetto (condividendo la stessa posizione di memoria).

### Costanti (`final`)
La parola chiave `final` impedisce la modifica successiva del valore.
* **Variabile final**: Non può essere riassegnata.
* **Classe final**: Non può essere estesa (es. `String`).
* **Metodo final**: Non può essere sovrascritto (override) nelle sottoclassi.

### Membri di Classe (`static`)
* **Campi Statici (Static Fields)**: Variabili globali uniche per la classe, condivise da tutte le istanze e utilizzabili anche senza istanziare la classe.
* **Metodi Statici (Static Methods)**: Metodi invocabili direttamente sulla classe (`NomeClasse.metodo()`). Non possono accedere ai campi e ai metodi non statici (di istanza) della classe e non supportano il polimorfismo.

### Confronto tra Oggetti
* **Operatore `==` / `!=`**: Confronta se le variabili contengono lo **stesso indirizzo di memoria** (se puntano allo stesso oggetto).
* **Metodo `equals()`**: Controlla l'uguaglianza del **contenuto** dell'oggetto (deve essere sovrascritto, ad esempio per le stringhe).

### Incapsulamento (Encapsulation)
Nasconde le parti interne e i dettagli di implementazione di un oggetto, consentendo l'accesso e l'uso solo attraverso l'interfaccia pubblica definita dal programmatore.

#### Modificatori di Visibilità (Visibility Modifiers):
* `public`: Accessibile ovunque.
* `protected`: Accessibile all'interno del package e nelle sottoclassi (anche fuori dal package).
* *default* (nessun modificatore): Accessibile solo all'interno del package.
* `private`: Accessibile solo all'interno della stessa classe.

#### Obiettivi dell'Incapsulamento:
1. **Protezione dei Dati (Data Protection)**: I metodi setter validano i parametri di input.
2. **Nascondere le Informazioni (Information Hiding)**: I dettagli interni sono nascosti all'esterno.
3. **Astrazione (Abstraction)**: Capacità di modificare l'implementazione interna senza influire sul codice client.
4. **Contenimento degli Errori (Error Containment)**: Previene effetti collaterali indesiderati al di fuori dei metodi.

### La parola chiave `this`
Rappresenta il riferimento all'oggetto corrente. Utilizzata all'interno di metodi di istanza e costruttori per risolvere ambiguità di nome o per passare l'oggetto stesso come argomento.

### Passaggio dei Parametri (Parameter Passing)
In Java, i parametri vengono **sempre passati per valore** (viene creata una copia locale).
* *Tipi primitivi*: Viene copiata la variabile stessa (le modifiche rimangono locali).
* *Oggetti*: Viene copiata la variabile contenente l'indirizzo. Pertanto, non è possibile modificare l'oggetto a cui punta il riferimento esterno, ma è possibile modificare i campi dell'oggetto riferito.

### Overloading (Sovraccarico)
La capacità di definire più metodi all'interno della stessa classe con lo stesso nome ma con **firme diverse** (diverso numero o tipo di parametri).

### Classi e Metodi Astratti (Abstract Classes and Methods)
* **Classe Astratta (`abstract`)**: Non può essere istanziata; funge da base per le sottoclassi.
* **Metodo Astratto**: Dichiarato senza corpo. Forza le sottoclassi concrete a fornirne un'implementazione.

---

## 5. COMPLESSITÀ (COMPLEXITY)

La **complessità computazionale** valuta le risorse necessarie per eseguire un algoritmo in funzione della dimensione dell'input ($n$).

### Valutazione di $n$:
* **Interi**: Numero di cifre dell'intero ($v \leftrightarrow \text{numero di cifre} = \log_b v$).
* **Array**: Lunghezza dell'array.
* **Liste**: Lunghezza della lista.
* **Alberi**: Numero di nodi.

### Risorse Analizzate:
1. **Tempo (Time)**: Operazioni eseguite per completare l'elaborazione.
2. **Spazio (Space)**: Memoria allocata, inclusi i frame dello Stack per la ricorsione.

### Notazioni Asintotiche:
* **$O(f(n))$** (O-grande / Big-O): Limite asintotico superiore. Rappresenta il comportamento nel caso peggiore (worst-case) ($g(n) \le c \cdot f(n)$).
* **$\Omega(f(n))$** (Omega): Limite asintotico inferiore. Rappresenta il caso migliore (best-case) ($g(n) \ge c \cdot f(n)$).
* **$\Theta(f(n))$** (Theta): Limite asintotico stretto ($c_1 \cdot f(n) \le g(n) \le c_2 \cdot f(n)$).

### Costo Computazionale: Iterazione vs. Ricorsione
* **Iterazione**:
  * *Tempo*: Numero di cicli $\times$ costo di ciascun ciclo.
  * *Spazio*: $O(1)$ (costante).
* **Ricorsione**:
  * *Tempo*: Numero totale di chiamate ricorsive.
  * *Spazio*: $O(\text{profondità di ricorsione})$ (ogni chiamata aggiunge un frame allo Stack).

---

## 6. RICORSIONE (RECURSION)

La ricorsione consiste nel risolvere un problema chiamando la funzione stessa su dati di dimensioni ridotte.

> [!IMPORTANT]
> ### Regole per una Corretta Ricorsione
> 1. Presenza di almeno un **caso base** risolto direttamente (senza ricorsione).
> 2. Passi ricorsivi che riducono l'input per convergere verso il caso base.
> 3. Un parametro che tiene traccia della dimensione o della posizione corrente.

### Classificazione della Complessità Temporale:
1. **Logaritmica ($O(\log n)$)**: Ricerca in un vettore ordinato.
2. **Lineare ($O(n)$)**: Somma di elementi, calcolo del fattoriale.
3. **Polinomiale ($O(n^k)$)**: Moltiplicazione di matrici.
4. **Esponenziale ($O(2^n)$)**: Torre di Hanoi.

### Algoritmi ed Esempi di Codice

#### 1. Fattoriale con Ricorsione in Coda (Tail Recursion)
In una funzione ricorsiva in coda (tail-recursive), la chiamata ricorsiva è l'ultima operazione eseguita. Non ci sono calcoli in sospeso dopo il ritorno della chiamata, consentendo ai compilatori che supportano la Tail Call Optimization (TCO) di riutilizzare il frame dello stack corrente.
* **Complessità Temporale**: $O(n)$ - esattamente $n$ passi ricorsivi.
* **Complessità Spaziale**: 
  - $O(1)$ (costante) in ambienti che supportano la TCO.
  - $O(n)$ sulla JVM standard (che attualmente non supporta nativamente la TCO, allocando quindi un frame per chiamata).

```java
private static long factRC(int n, long ris) {
    if (n == 0) return ris;                  // Caso base: ritorna il risultato accumulato
    else return factRC(n - 1, ris * n);      // Chiamata ricorsiva in coda: 'ris * n' funge da accumulatore
}
public static long factRC(int n) { 
    return factRC(n, 1);                     // Wrapper di supporto che inizializza l'accumulatore a 1
}
```

#### 2. Successione di Fibonacci (Ricorsiva Standard)
Utilizza una ricorsione binaria semplice, che crea un albero profondo di calcoli ridondanti.
* **Complessità Temporale**: $O(2^n)$ - crescita esponenziale dovuta al ricalcolo di sottoproblemi sovrapposti.
* **Complessità Spaziale**: $O(n)$ - la profondità massima dello stack di chiamate è proporzionale a $n$.

```java
static long fiboR(int n) {
    if (n <= 2) return 1;                    // Caso base: i primi due numeri di Fibonacci sono 1
    else return fiboR(n - 1) + fiboR(n - 2); // Ricorsione binaria: somma dei due valori precedenti
}
```

#### 3. Esponenziazione Veloce (Fast Exponentiation)
Riduce drasticamente le operazioni di moltiplicazione elevando al quadrato la base e dimezzando l'esponente a ogni passo.
* **Complessità Temporale**: $\Theta(\log e)$ - l'esponente viene diviso per 2 a ogni passo.
* **Complessità Spaziale**: $\Theta(\log e)$ - richiede uno spazio di stack proporzionale al numero di divisioni.

```java
public static double potenzaR2(double b, long e) {
    if (e == 0) return 1;                                // Caso base: b^0 = 1
    else if (e % 2 == 0) return potenzaR2(b * b, e / 2); // Esponente pari: b^e = (b^2)^(e/2)
    else return b * potenzaR2(b * b, e / 2);             // Esponente dispari: b^e = b * (b^2)^((e-1)/2)
}
```

#### 4. Ricerca Binaria (Array Ordinato - Binary Search)
Una classica strategia di ricerca divide-et-impera che scarta metà degli elementi rimanenti a ogni passo.

* **Versione Ricorsiva**:
```java
public class Vettore {
    int[] dati;
    
    public int ricercaBinRic(int x) { 
        return ricercaBinRic(dati, x, 0, dati.length - 1); // Wrapper di supporto che avvia la ricorsione
    }
    
    private static int ricercaBinRic(int[] dati, int x, int inizio, int fine) {
        if (inizio > fine) return -1;                                      // Caso base: elemento non trovato
        int centro = (inizio + fine) / 2;                                  // Calcola l'indice medio
        int c = dati[centro];
        if (c == x) return centro;                                         // Elemento trovato: ritorna il suo indice
        else if (x < c) return ricercaBinRic(dati, x, inizio, centro - 1); // Cerca nel sotto-array sinistro
        else return ricercaBinRic(dati, x, centro + 1, fine);              // Cerca nel sotto-array destro
    }
}
```
* **Versione Iterativa**:
```java
public static int ricercaBinIter(int dati[], int x) {
    int inizio = 0, fine = dati.length - 1;
    while (inizio <= fine) {
        int centro = (inizio + fine) / 2;      // Calcola l'indice medio
        int c = dati[centro];
        if (c == x) return centro;             // Elemento trovato: ritorna l'indice
        else if (x < c) fine = centro - 1;     // Scarta la metà destra
        else inizio = centro + 1;              // Scarta la metà sinistra
    }
    return -1;                                 // Elemento non trovato dopo la fine del ciclo
}
```
* *Confronto di Complessità*:
  - Ricorsiva: Tempo $O(\log N)$, Spazio $O(\log N)$ (a causa dei frame dello Stack).
  - Iterativa: Tempo $O(\log N)$, Spazio $O(1)$ (preferita per l'overhead di memoria costante).

#### 5. Quicksort
Un algoritmo di ordinamento efficiente basato sul paradigma *Divide et Impera*.

```java
static int partition(int[] array, int inizio, int fine) {
    int pivot = array[fine]; // Seleziona l'ultimo elemento come pivot
    int i = inizio - 1;      // Indice dell'elemento più piccolo
    for (int j = inizio; j < fine; j++) {
        if (array[j] <= pivot) { // Se l'elemento corrente è minore o uguale al pivot
            i++;
            int temp = array[i]; // Scambia array[i] e array[j]
            array[i] = array[j];
            array[j] = temp;
        }
    }
    int temp = array[i + 1]; // Scambia array[i+1] e array[fine] (pivot) per posizionare il pivot al posto giusto
    array[i + 1] = array[fine];
    array[fine] = temp;
    return i + 1; // Ritorna l'indice di partizionamento del pivot
}

private static void quicksort(int v[], int inizio, int fine) {
    if (inizio < fine) {
        int mid = partition(v, inizio, fine); // Partiziona l'array e posiziona il pivot
        quicksort(v, inizio, mid - 1);        // Ordina ricorsivamente il sotto-array sinistro
        quicksort(v, mid + 1, fine);         // Ordina ricorsivamente il sotto-array destro
    }
}
```
* **Complessità**:
  - **Tempo**: Migliore/Medio $\Theta(N \log N)$ (divisioni bilanciate), Peggiore $O(N^2)$ (input già ordinato o ordinato al contrario in cui le divisioni della partizione sono estremamente sbilanciate).
  - **Spazio**: Medio $O(\log N)$ spazio sullo Stack per i frame di ricorsione.
* **Quicksort Iterativo**: Può essere implementato simulando esplicitamente lo stack delle chiamate ricorsive tramite una struttura dati Stack (logica LIFO) per memorizzare gli intervalli `[inizio, fine]` rimanenti da elaborare.

#### 6. Torre di Hanoi (Towers of Hanoi)
* **Complessità Temporale**: $O(2^N)$ - esattamente $2^N - 1$ mosse di dischi.
* **Complessità Spaziale**: $O(N)$ - la profondità dello Stack è proporzionale al numero di dischi.

```java
private void hanoi(int N, String S, String I, String D) {
    if (N == 1) trasferisci(1, S, D); // Caso base: sposta un singolo disco direttamente da S a D
    else {
        hanoi(N - 1, S, D, I);        // Passo 1: Sposta i primi N-1 dischi dal sorgente (S) all'intermedio (I)
        trasferisci(N, S, D);          // Passo 2: Sposta il disco più grande N dal sorgente (S) alla destinazione (D)
        hanoi(N - 1, I, S, D);        // Passo 3: Sposta gli N-1 dischi dall'intermedio (I) alla destinazione (D)
    }
}
```

#### 7. Bubblesort
* **Complessità Temporale**: $O(N^2)$ in tutti i casi (doppio ciclo che esegue $\frac{N(N-1)}{2}$ confronti).
* **Complessità Spaziale**: $O(1)$ (ordinamento in-place senza allocazione di memoria ausiliaria).

```java
static public void ordina(int vettore[]) {
    int temp;
    for (int i = 0; i < vettore.length - 1; i++) { // Ciclo esterno che esegue N-1 passaggi
        for (int j = vettore.length - 1; j > i; j--) { // Ciclo interno che scorre dalla fine fino all'indice i
            if (vettore[j] < vettore[j - 1]) { // Scambia elementi adiacenti se non sono ordinati
                temp = vettore[j];
                vettore[j] = vettore[j - 1];
                vettore[j - 1] = temp;
            }
        }
    }
}
```

---

## 7. ECCEZIONI (EXCEPTIONS)

Un'**eccezione** è un evento anomalo che si verifica durante l'esecuzione del programma. Tutte le classi di eccezione ereditano da `Throwable`.

```text
                  Throwable
                 /         \
            Error           Exception
                           /         \
           RuntimeException           Checked Exceptions
         (Unchecked Exceptions)      (IOException, ecc.)
```

* **`Error`**: Problemi di sistema gravi e non recuperabili (es. `OutOfMemoryError`). L'applicazione non dovrebbe cercare di catturarli.
* **`Exception`**: Condizioni anomale catturabili:
  1. **Unchecked Exceptions (Eccezioni non controllate)**: Derivano da `RuntimeException`. Rilevate a runtime. Non vi è alcun obbligo di catturarle o dichiararle (es. `NullPointerException`, `ClassCastException`, `IndexOutOfBoundsException`, `NumberFormatException`).
  2. **Checked Exceptions (Eccezioni controllate)**: Tutte le altre eccezioni. Il compilatore obbliga a gestirle con un blocco `try-catch` o a dichiararle nella firma con `throws` (es. `IOException`, `FileNotFoundException`).

### Gestione delle Eccezioni (`try-catch-finally`)
```java
try {
    // Codice che potrebbe lanciare eccezioni
} catch (FileNotFoundException e) {
    // Cattura e gestisce un'eccezione specifica
} catch (IOException e) {
    // Cattura e gestisce un'eccezione di I/O generica
} finally {
    // Eseguito in ogni caso (utile per chiudere file o connessioni)
}
```
> [!WARNING]
> I blocchi `catch` devono essere ordinati dal tipo più specifico a quello più generico. Se si inserisce `catch(Exception)` prima di `catch(IOException)`, il codice successivo non compilerà (errore di blocco catch irraggiungibile).

### Dichiarazione delle Eccezioni (`throws`)
Consente di delegare la gestione delle eccezioni al metodo chiamante.
```java
public void leggiFile(String nomefile) throws IOException { }
```
* **Override (Sovrascrittura)**: Un metodo sovrascritto in una sottoclasse può dichiarare meno eccezioni controllate rispetto al metodo originale nella superclasse, ma mai di più.

### Creazione e Lancio di Eccezioni (`throw`)
```java
// Definizione di un'eccezione controllata personalizzata
public class SunSpotException extends Exception {
    public SunSpotException() { }
    public SunSpotException(String msg) { super(msg); }
}

// Lancio dell'eccezione
if (connessionePersa) {
    throw new SunSpotException("Error: connection disrupted");
}
```

---

## 8. STREAM DI INPUT E OUTPUT (INPUT AND OUTPUT STREAMS)

Gli **I/O Stream** consentono il trasferimento di dati tra una sorgente e una destinazione. Le classi di riferimento appartengono al package `java.io`.

### Tipi di Stream

| Tipo di Stream | Descrizione | Classi Base | Esempi Concreti |
| :--- | :--- | :--- | :--- |
| **Byte Streams** | Per gestire dati binari generici (immagini, audio, oggetti serializzati). | `InputStream`<br>`OutputStream` | `FileInputStream` / `FileOutputStream`<br>`BufferedInputStream` / `BufferedOutputStream`<br>`DataInputStream` / `DataOutputStream`<br>`ObjectInputStream` / `ObjectOutputStream` |
| **Character Streams** | Per gestire dati testuali (file txt, log, configurazioni). | `Reader`<br>`Writer` | `FileReader` / `FileWriter`<br>`BufferedReader` / `BufferedWriter`<br>`InputStreamReader` / `OutputStreamWriter`<br>`PrintWriter`<br>`Scanner` |

### Chiusura degli Stream e Gestione delle Risorse
Tutti gli stream devono essere chiusi dopo l'uso per evitare perdite di risorse di sistema (resource leak).
A partire da Java 7, si raccomanda l'uso dell'istruzione **try-with-resources** per la chiusura automatica delle risorse sugli oggetti che implementano `AutoCloseable`:

```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String riga;
    while ((riga = br.readLine()) != null) {
        int n = Integer.parseInt(riga);
        // Elaborazione...
    }
} catch (IOException e) {
    System.out.println("Errore di I/O: " + e.getMessage());
} catch (NumberFormatException e) {
    System.out.println("Formato numero non valido: " + e.getMessage());
}
```

---

## 9. MULTITHREADING

### Concetti Fondamentali
* **Processo (Process)**: Un'istanza di un programma in esecuzione con uno spazio di memoria privato.
* **Thread**: Un percorso di esecuzione concorrente leggero all'interno di un processo. Condivide la memoria con gli altri thread dello stesso processo.

### Creazione dei Thread

#### Metodo 1: Estendere la classe `Thread`
```java
public class MioThread extends Thread {
    @Override
    public void run() {
        // Istruzioni eseguite nel thread parallelo
    }
}
// Avvio
MioThread t = new MioThread();
t.start(); // Crea il nuovo stack ed esegue asincronamente run()
```

#### Metodo 2: Implementare `Runnable`
Consigliato per superare il limite dell'ereditarietà singola.
```java
public class MiaAttivita implements Runnable {
    @Override
    public void run() {
        // Istruzioni
    }
}
// Avvio
Thread t = new Thread(new MiaAttivita());
t.start();
```

### Metodi Principali di Controllo
* `t.start()`: Avvia il thread.
* `yield()`: Rilascia temporaneamente la CPU a thread di pari priorità.
* `t.join()`: Sospende il thread chiamante finché il thread `t` non completa l'esecuzione.
* `Thread.sleep(millis)`: Sospende il thread corrente per un tempo specificato.
* *Metodi deprecati* (non sicuri): `suspend()`, `resume()`, `stop()`.

### Sincronizzazione (Synchronization)
Quando più thread modificano una risorsa condivisa concorrentemente, possono verificarsi stati incoerenti (*race conditions*).
* **Thread-safe**: Codice progettato per essere eseguito concorrentemente da più thread senza conflitti.
* **`synchronized`**: Garantisce l'accesso esclusivo (mutua esclusione) a un metodo o a un blocco di codice per un solo thread alla volta, acquisendo un **lock** sull'oggetto.
  * Se un thread tenta di accedere a un metodo `synchronized` già bloccato da un altro thread, viene sospeso in attesa che il lock venga rilasciato.
  * Un uso improprio può portare a colli di bottiglia nelle prestazioni o a blocchi permanenti (**deadlock**).

### Comunicazione tra Thread (`wait` e `notify`)
Metodi invocabili all'interno di contesti sincronizzati:
* `wait()`: Rilascia il lock dell'oggetto e sospende il thread corrente finché un altro thread non chiama `notify()`.
* `notify()`: Risveglia un singolo thread in attesa sul lock dell'oggetto.
* `notifyAll()`: Risveglia tutti i thread in attesa sul lock dell'oggetto.

---

## 10. PROGRAMMAZIONE DI RETE (NETWORK PROGRAMMING)

### Socket
Una **Socket** è un'astrazione software che rappresenta un endpoint di comunicazione per l'invio e la ricezione di dati sulla rete.
* **Indirizzo IP (IP Address)**: Identifica l'host sulla rete.
* **Porta (Port)**: Numero intero che rappresenta il processo sulla macchina di destinazione a cui viene consegnato il pacchetto.
* **Modello Client/Server**:
  * *Server*: Ascolta passivamente su una porta specifica.
  * *Client*: Avvia attivamente la connessione specificando l'IP e la porta.

### SocketStream (TCP)
Fornisce una connessione affidabile, stabile, orientata alla connessione e bidirezionale.
* **ServerSocket**: Utilizzato dal Server per accettare connessioni in ingresso.
  * Metodo `accept()`: Attesa bloccante di un client. Restituisce una `Socket` per scambiare dati.
* **Socket**: Utilizzata dal Client per connettersi o dal Server per comunicare. Fornisce due stream:
  * `getInputStream()`: Per ricevere byte.
  * `getOutputStream()`: Per inviare byte.

### Modello di Implementazione Client/Server

#### Codice Server:
```java
ServerSocket ss = new ServerSocket(indirizzo);
while (true) {
    try {
        Socket s = ss.accept(); // Accetta la connessione del client (bloccante)
        ThreadServer ts = new ThreadServer(s); // Gestisce in un thread separato
        ts.start();
    } catch (IOException e) {
        // Gestione degli errori di I/O
    }
}
```

#### Codice Client:
```java
String server = (args.length == 1) ? args[0] : "localhost";
try (Socket socket = new Socket(server, porta)) {
    // Canale stabilito, pronto per la comunicazione
} catch (IOException e) {
    // Gestione dell'errore di connessione
}
```

#### Modalità di Scambio Dati
Gli stream di I/O nativi della socket vengono avvolti (wrapped) a seconda delle esigenze:

```java
// 1. Inviare numeri (Client)
DataOutputStream out = new DataOutputStream(socket.getOutputStream());
out.writeInt(valore);
out.flush();

// 2. Ricevere numeri (Server)
DataInputStream in = new DataInputStream(socket.getInputStream());
int valore = in.readInt();

// 3. Inviare testo (Client/Server)
PrintWriter out = new PrintWriter(socket.getOutputStream(), true); // autoflush attivo
out.println("Messaggio di testo");

// 4. Ricevere testo (Client/Server)
BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
String riga = in.readLine();
```

> [!IMPORTANT]
> ### Sincronizzazione dei Dati in un Server Multithread
> Quando più thread paralleli sul Server modificano lo stesso insieme di dati condivisi:
> 1. Creare una classe dedicata per memorizzare i dati condivisi.
> 2. Dichiarare i campi della classe come `private`.
> 3. Rendere tutti i metodi di lettura e scrittura `public synchronized`.
> 4. Istanziare un solo oggetto di questa classe e passarlo come parametro ai costruttori di ciascun `ThreadServer` al momento dell'istanziazione.

---

◀️ *Torna a:* [[00_Index_OOP]]
