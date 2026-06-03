# JAVA RIASSUNTO PROGRAMMA

## 1. INTRODUZIONE

I motivi principali per cui l’Object Oriented Programming è efficace sono:
1. L’aumento della produttività
2. Facilitare il programmatore
3. Velocizzare lo sviluppo
4. Ridurre gli errori

Nel caso di un linguaggio come il **C**, la programmazione è strutturata, vale a dire che un problema viene diviso in sottoproblemi più semplici, a loro volta divisi in sottoprogrammi, come funzioni e procedure (approccio *top-down*).

Nel caso, invece, dell’**OOP**, si costruisce un’applicazione montando oggetti più semplici; questi oggetti vengono progettati tramite classi, costruiti ed infine usati.  
Per progettare un oggetto si devono indicare le sue proprietà (attributi o campi) e le sue funzionalità (metodi o funzioni).

I tre pilastri dell’OOP sono:
1. **Ereditarietà**: è possibile riutilizzare un progetto già esistente e modificarlo per le proprie esigenze.
2. **Incapsulamento**: riuso del codice, astrazione, confinamento degli errori.
3. **Polimorfismo**: ogni oggetto si comporta a seconda del contesto e del valore.

---

## 2. LINGUAGGIO JAVA

L’ambiente Java comprende sia un compilatore che un interprete (Java Runtime Environment, JRE).

```
[Sorgente Java] -> (Compilatore) -> [Bytecode Java] -> (Interprete Java per SO) -> Esecuzione
```

Attraverso il compilatore, il codice sorgente Java viene convertito in **bytecode**, ovvero pseudo-istruzioni in un linguaggio indipendente dalla piattaforma.  
Gli interpreti traducono il bytecode in un eseguibile specifico a seconda del sistema operativo in cui si trova il bytecode (Windows, Linux, Mac). Questo permette un ottimo compromesso tra velocità e portabilità.

---

## 3. PROGRAMMAZIONE AD OGGETTI IN JAVA

La **classe** è il modello generico di un insieme di oggetti con caratteristiche simili.  
L’**oggetto** è la particolare istanza di un elemento di una classe.

Gli **attributi** (proprietà e campi) descrivono lo stato, l’aspetto e altre qualità dell’oggetto; sono rappresentati dai campi dell’oggetto. Esistono anche campi di classe.

Il **comportamento** di una classe indica come opera un oggetto di una classe; è definito dai **metodi** delle classi, ovvero funzioni definite all’interno della classe che operano sugli oggetti della classe e ne manipolano le proprietà. Non esistono funzioni definite al di fuori di una classe.

### Come viene creato un oggetto?
```java
Motocicletta m;              // Dichiarazione (creo la variabile m di tipo Motocicletta); m occupa 4 byte
m = new Motocicletta();      // Istanziazione (creo la nuova motocicletta)
m.marca = "Guzzi 1000";      // Inizializzazione
m.colore = "rossa";          // Inizializzazione (inserisco le proprietà alla variabile vuota m)
m.mostra();                  // Chiama il metodo "mostra", e i valori restituiti vengono assegnati ad m
```

### Come viene creato un oggetto con un costruttore?
Cosa fa un costruttore?
1. Istanzia l'oggetto e ne restituisce l'indirizzo.
2. Esegue le operazioni definite dal programmatore; di solito inizializza l'oggetto (assegna alle proprietà il valore iniziale, tipicamente ricevendolo come parametro).

```java
// Esempio di costruttore
public Motocicletta(String marca, String colore, boolean a) {
    this.marca = marca; 
    this.colore = colore; 
    accesa = a; // Assegno il valore del parametro alla proprietà dell’oggetto
}

public static void main(String args[]) {
    // L’oggetto è dichiarato, istanziato e inizializzato nella stessa riga attraverso i parametri
    Motocicletta m = new Motocicletta("Guzzi 1000", "rossa", false); 
}
```

### Come si comporta la memoria?
1. **STACK**: Vengono rappresentati gli spazi in cui i metodi vengono eseguiti, contenenti al loro interno i parametri e le variabili locali. È sempre presente il metodo `main` con il parametro `String args[]` e le sue variabili (in genere, i riferimenti agli oggetti inizializzati). Gli spazi dei metodi non statici rimangono fino a quando questi non hanno terminato la loro esecuzione.
2. **HEAP**: Vengono rappresentati gli spazi allocati per gli oggetti veri e propri, con all'interno le loro proprietà.
3. **STATIC**: Vengono inserite le variabili statiche, che possono essere usate in quanto globalmente definite.

Quando un oggetto viene dichiarato, la variabile che dà il nome all’oggetto contiene un valore (in base 16) che indica un indirizzo di memoria (riferimento a dove si trova l’oggetto reale). Inizialmente l'indirizzo è vuoto (`null`).  
L’oggetto viene creato con l’istanziazione tramite i costruttori; viene allocato uno spazio di memoria nell’heap per l’oggetto e le sue proprietà. La variabile conterrà quindi l'indirizzo di questo spazio di memoria.

Quando l’oggetto viene inizializzato, le proprietà associate all’oggetto vengono memorizzate all’interno del suo spazio nello heap.  
Gli oggetti non più utilizzati vengono deallocati automaticamente tramite il meccanismo di **Garbage Collection**. Per accedere ai campi di un oggetto e richiamare un metodo si usa la *notazione punto* (`.`).

### Il compito del compilatore e dell’interprete
1. **COMPILATORE**: Esegue controlli statici basandosi sulle dichiarazioni delle variabili e controlla se una variabile sia inizializzata o meno.
2. **INTERPRETE**: Esegue controlli dinamici a runtime basandosi sui valori effettivi delle variabili (es. utilizzo di un oggetto non costruito, accesso a posizioni fuori dai limiti di un array, tentativi di calcolare valori numerici da stringhe non conformi, cast non compatibili).

---

### a. Ereditarietà, interfacce e packages
È possibile definire una **sottoclasse**, discendente da una sovraclasse, che ne eredita campi e metodi tramite la parola chiave `extends` (gli elementi privati vengono ereditati ma non sono direttamente accessibili).

Java supporta esclusivamente l’**ereditarietà singola** (ogni classe può avere una sola sovraclasse diretta) per mantenere il linguaggio semplice e sicuro. Con l'ereditarietà multipla nascerebbero conflitti sui nomi dei campi omonimi e problemi di ambiguità strutturale a tempo di esecuzione.

Due approcci di progettazione:
- **Bottom-up**: da classi più semplici si costruiscono classi più complesse.
- **Top-down**: le classi vengono organizzate in una gerarchia ad albero a partire da sovraclassi generali fino a sottoclassi più specifiche.

Le **interfacce** (`interface` / `implements`) sono collezioni di dichiarazioni di metodi che consentono di definire comportamenti comuni in rami diversi della gerarchia delle classi. Una classe può estendere una sola classe, ma può implementare un numero illimitato di interfacce.  
Un'interfaccia può contenere:
1. Intestazioni di metodi di istanza astratti;
2. Costanti statiche;
3. Metodi di `default` implementati (ridefinibili nelle classi che implementano l'interfaccia);
4. Metodi statici implementati (non ridefinibili).

Un **package** è una collezione di classi ed interfacce. Consente di organizzare le classi in gruppi e previene conflitti di nome. Di default è disponibile solo il package `java.lang`; le altre classi devono essere importate tramite `import` o riferite col nome completo.

---

### b. Polimorfismo sui dati
Un oggetto di una certa classe può assumere valori di oggetti di una qualsiasi sua sottoclasse.  
Inoltre, dichiarando una variabile con tipo interfaccia, essa può referenziare oggetti di qualsiasi classe che implementi tale interfaccia.  
Ciò consente di definire strutture dati polimorfe (ad esempio, un array di oggetti di classi differenti ma con la stessa sopraclasse).

```java
// Esempio
Lavoratore l3 = new Operaio(); 
l3.stipendio(); 
// Il metodo stipendio() è definito in Lavoratore, ma viene eseguito quello specifico di Operaio.
```
- **Early binding (compilatore)**: considera l'oggetto in base alla sua dichiarazione statica (`Lavoratore`), verificando che il metodo invocato esista in quel tipo.
- **Late binding (interprete)**: a tempo di esecuzione determina il tipo effettivo dell'oggetto (`Operaio`) e ne invoca l'implementazione specifica. Java usa quasi sempre il *late binding* (eccetto per metodi statici, final o privati).

---

### c. Typecasting
Attraverso il **typecasting** il programmatore indica esplicitamente al compilatore la classe effettiva dell'oggetto referenziato. In questo modo il compilatore effettua i controlli statici sulla classe indicata nel cast anziché su quella originariamente dichiarata. Se a tempo di esecuzione il tipo dell'oggetto non è compatibile con la classe del cast, viene sollevata un'eccezione (`ClassCastException`).

---

### d. Array
Un **array** è una collezione ordinata di elementi dello stesso tipo. Poiché in Java anche gli array sono considerati oggetti, essi devono essere dichiarati e istanziati.

La creazione può avvenire in due modi:
1. Utilizzando l'operatore `new` specificando la dimensione esplicitamente.
2. Inizializzando direttamente il contenuto al momento della dichiarazione (dimensione implicita).

Tutti gli array dispongono del campo pubblico `length` che contiene il numero totale di elementi.

