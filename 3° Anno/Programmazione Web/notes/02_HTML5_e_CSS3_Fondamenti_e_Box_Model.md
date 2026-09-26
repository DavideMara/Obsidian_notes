---
date: 2026-09-22
updated: 2026-09-24
tags:
  - programmazione-web
type: lezione
---
# HTML5 e CSS3: Struttura Semantica, Tipografia, Box Model e Selettori

Questa lezione approfondisce le specifiche e i componenti fondamentali del web moderno: l'evoluzione semantica di **HTML5**, la classificazione degli elementi per tipologia e comportamento di rendering, l'introduzione a **CSS3**, la gestione della tipografia e dei colori, i meccanismi di **Ereditarietà e Cascata**, il fondamentale **Box Model** e l'utilizzo avanzato di **Selettori e Combinatori CSS**.

---

## I. Lo Standard HTML5 e la Struttura del Documento

Lo standard **HTML5** è il risultato dello sforzo congiunto del **W3C (World Wide Web Consortium)** e del **WHATWG (Web Hypertext Application Technology Working Group)**. Rispetto alle versioni precedenti (HTML 4.01 / XHTML 1.0), HTML5 è stato progettato per rispondere alle esigenze di applicazioni web interattive e responsive, con l'obiettivo primario di introdurre **funzionalità semantiche strutturali**.

```
                  ┌──────────────────────────────────────────────┐
                  │                    HTML5                     │
                  └──────────────────────┬───────────────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│  Tag Semantici       │      │  Supporto Multimediale│     │  Mobile & Touch      │
│  <article>, <section>│      │  <audio>, <video>     │      │  Design responsivo e │
│  <header>, <nav>...  │      │  nativo (senza plugin)│      │  interazioni touch   │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
```

I pilastri evolutivi di HTML5 includono:
* **Tag Semantici Nativi:** Introduzione di elementi strutturali (`<article>`, `<section>`, `<header>`, `<footer>`, `<nav>`, `<main>`, `<aside>`) che descrivono chiaramente il ruolo del contenuto per browser, screen reader e motori di ricerca (SEO).
* **Supporto Multimediale Integrato:** Gestione nativa di flussi audio e video tramite `<audio>` e `<video>`, eliminando la dipendenza da plugin esterni proprietari (come Adobe Flash o Silverlight).
* **Progettazione Mobile-First:** Ottimizzazione per display touch, densità di pixel eterogenee e dispositivi mobili.

### Perché la Semantica è Fondamentale

Un documento semanticamente corretto non serve soltanto a essere "più bello": ogni elemento scelto comunica un'informazione sul **ruolo** del contenuto, e sono proprio questi ruoli a essere interrogati da programmi automatici che non leggono la pagina a occhio.

| Consumatore Automatico | Cosa cerca nel Markup | Conseguenza di un Markup Solo "Grafico" |
| :--- | :--- | :--- |
| **E-reader / Screen Reader** | Gli elementi di flusso testuale (`<p>`, `<h1>`–`<h6>`, `<li>`) per estrarre il testo da leggere all'utente | Testo impaginato con `<div>`/`<span>` letto come un unico blocco informe: l'utenza perde il contesto |
| **Web Crawler (SEO)** | La gerarchia degli heading, i `<title>`, i link `<a href>` | La pagina non viene correttamente interpretata e indicizzata |
| **Motori di Ricerca (Google)** | Standard di qualità: `<h1>` univoco, `<title>` descrittivo, `alt` sulle immagini, struttura semantica | Pagine "senza tag specifici" vengono declassate o escluse dall'indice |
| **Sistemi AI / Data Mining** | La struttura semantica e gli attributi dichiarativi (`alt`, `href`, `title`) per arricchire il contenuto | Contenuto non interpretabile automaticamente e metadati persi |

> [!IMPORTANT] Il Markup non è un Vestito, è un Contratto
> La scelta del tag corretto non è una questione estetica: usare `<p>` per il testo da leggere e `<h1>` per il titolo di una sezione significa che screen reader, crawler e modelli di linguaggio ricostruiscono correttamente la struttura del documento. Al contrario, usare un `<div>` per simulare un paragrafo fa perdere utente e posizionamento.

### Struttura Sintattica Minima di una Pagina HTML5

Ogni documento conforme allo standard HTML5 presenta la seguente alberatura gerarchica:

```html
<!DOCTYPE html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titolo della Scheda</title>
    <!-- Collegamento al foglio di stile esterno -->
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <!-- Contenuto visibile renderizzato nel viewport -->
    <header>
      <h1>Intestazione Principale</h1>
    </header>
    <main>
      <p>Contenuto della pagina...</p>
    </main>
  </body>
</html>
```

* `<!DOCTYPE html>`: Dichiarazione DTD che istruisce il browser a interpretare la pagina in modalità standard (*standards mode*), evitando il rendering retrocompatibile (*quirks mode*).
* `<html lang="it">`: Radice del documento; l'attributo `lang` definisce la lingua principale per i sintetizzatori vocali e l'indicizzazione.
* `<head>`: Contenitore dei metadati invisibili all'utente ma essenziali per il parser (charset, viewport, titolo, link a risorse esterne).
* `<meta charset="utf-8">`: Specifica la codifica universale dei caratteri UTF-8.
* `<title>`: Definisce il **titolo del documento**, mostrato come *label* nella scheda del browser e come titolo del link nei risultati di ricerca. Deve essere unico e descrittivo.
* `<body>`: Contiene l'intero albero di elementi visivi renderizzati nel browser ed è **l'unico elemento obbligatorio** di una pagina HTML: qualunque contenuto da mostrare all'utente deve essere al suo interno.

---

## II. Tassonomia dei Tag HTML: Semantica, Contenitori e Tipologie

Gli elementi HTML si classificano in base a due criteri ortogonali: la loro **struttura sintattica** (contenitori vs vuoti) e il loro **comportamento di layout predefinito** (blocco vs linea).

```
                      ┌─────────────────────────────────────────┐
                      │             ELEMENTI HTML               │
                      └────────────────────┬────────────────────┘
                                           │
          ┌────────────────────────────────┴────────────────────────────────┐
          ▼                                                                 ▼
┌───────────────────────────────────┐             ┌───────────────────────────────────┐
│     CLASSIFICAZIONE STRUTTURALE   │             │     COMPORTAMENTO DI RENDERING    │
├───────────────────────────────────┤             ├───────────────────────────────────┤
│ • Contenitori: <tag>...</tag>     │             │ • Blocco (Block-level):           │
│   (<div>, <p>, <section>)         │             │   Inizio nuova riga, width 100%   │
│ • Vuoti / Void: <tag>             │             │ • Di Linea (Inline):              │
│   (<img>, <input>, <hr>, <br>)    │             │   Nel flusso, width su contenuto  │
└───────────────────────────────────┘             └───────────────────────────────────┘
```

### 1. Tag Contenitori vs Tag Vuoti (Void Elements)
* **Tag Contenitori:** Possiedono sia il tag di apertura che quello di chiusura (`<tag> ... </tag>`). Possono racchiudere testo, nodi testuali o altri elementi figli annidati (es. `<div>`, `<p>`, `<section>`, `<article>`).
* **Tag Vuoti (Empty/Void Tags):** Non hanno un tag di chiusura né contenuto testuale interno; la loro configurazione avviene unicamente tramite attributi (es. `<img src="..." alt="...">`, `<input type="...">`, `<hr>`).

Ogni tag può avere attributi, alcuni **obbligatori** altri **opzionali**: in un elemento vuoto, poiché non esiste contenuto interno, *tutta* l'informazione è necessariamente codificata negli attributi.

| Tag Vuoto | Attributi Fondamentali | Ruolo |
| :--- | :--- | :--- |
| **`<img>`** | `src` (percorso dell'immagine), `alt` (descrizione testuale) | Immagine della pagina |
| **`<input>`** | `type` (`text`, `password`, `email`...), `name`, `value`, `placeholder` | Campo di input utente |
| **`<hr>`** | nessuno | Linea di separazione tematica tra sezioni |
| **`<br>`** | nessuno | Interruzione di riga esplicita (*a capo forzato*) |
| **`<link>`** | `rel`, `href` | Collegamento a risorse esterne (CSS, favicon) |
| **`<meta>`** | `charset`, `name`, `content` | Metadati del documento |

> [!TIP] L'Attributo `alt` non è un Dettaglio Estetico
> `src` indica solo *dove* si trova il file; `alt` indica *cosa* rappresenta. Sono gli screen reader e i modelli di linguaggio a utilizzare `alt` per descrivere l'immagine a chi non la vede: per questo è un requisito di accessibilità, non un accessorio. Quando l'immagine è puramente decorativa si usa `alt=""`.

### 2. Elementi di Blocco (Block-level) vs Elementi di Linea (Inline)
* **Elementi di Blocco (Block-level):**
  * Iniziano sempre su una **nuova riga** nel normale flusso del documento (es. il testo successivo a `</h1>` va a capo).
  * Occupano per default **l'intera larghezza disponibile** del loro contenitore genitore (`width: 100%`).
  * Possono contenere sia altri elementi di blocco sia elementi di linea.
  * *Esempi:* `<div>`, `<h1>` - `<h6>`, `<p>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<ul>`, `<ol>`, `<blockquote>`.
* **Elementi di Linea (Inline):**
  * Vengono renderizzati **in sequenza orizzontale** all'interno della riga corrente, senza forzare un'interruzione di riga.
  * Occupano **esclusivamente lo spazio necessario** a contenere il loro contenuto.
  * Non accettano margini e padding verticali per alterare il flusso di riga delle altre linee.
  * *Esempi:* `<span>`, `<a>`, `<em>`, `<strong>`, `<code>`, `<q>`, `<img>` (*inline-replaced*).

#### Glossario degli Elementi Più Usati

| Elemento | Tipo | Definizione |
| :--- | :--- | :--- |
| **`<div>`** | Contenitore di blocco | Contenitore **generico** di blocco, privo di semantica propria: serve al raggruppamento strutturale e al posizionamento nel layout, mai per il testo da leggere |
| **`<section>`** | Contenitore di blocco semantico | Sezione logica del documento (capitolo, parte di un articolo, argomento di una pagina): raggruppa contenuti tematicamente affini, in genere introdotta da un heading |
| **`<span>`** | Inline | Contenitore **generico inline**: racchiude una porzione di riga per applicarle una classe di stile o per attribuirle un significato semantico (con `<em>`, `<strong>`, `<code>`) |
| **`<a>`** | Inline (*ancora*) | **Ancora**: crea un collegamento ipertestuale tramite l'attributo `href`; supporta `target` (nuova scheda), `rel` (`noopener`) e `title` (tooltip) |
| **`<img>`** | Inline sostituito (*inline-replaced*) | Immagine: `src` fornisce il percorso del file, `alt` la descrizione testuale |
| **`<input>`** | Inline (modulo) | Campo di input: elemento vuoto il cui comportamento è definito dall'attributo `type` (con `type="text"` come valore predefinito) |

### 3. Attributi HTML e Separazione delle Responsabilità
Gli **attributi** sono coppie `chiave="valore"` dichiarate all'interno del tag di apertura di un elemento:
```html
<tag nome_attributo="valore">Contenuto</tag>
```
Alcuni attributi hanno **funzionalità** (es. `href` per i link, `src` per le immagini, `type` per gli input, `id` e `class` per i selettori), altri hanno **effetto sull'aspetto** (es. `align`, `bgcolor`, `font`, `width`): i secondi sono attributi di presentazione deprecati o rimossi dallo standard HTML5.

> [!IMPORTANT] Principio Architetturale di Separazione delle Responsabilità
> HTML deve occuparsi **esclusivamente della struttura e della semantica** del documento. Qualsiasi proprietà visiva (colori, margini, allineamenti, dimensioni, animazioni) **deve essere demandata ai fogli di stile CSS**, evitando categoricamente attributi di presentazione deprecati (come `align`, `bgcolor`, `font`): è considerata una **violazione grave** della buona pratica progettuale.

> [!EXAMPLE] Esercizio di Lezione
> Pagina dimostrativa con intestazione, immagini provviste di `alt` descrittivo ed enfasi testuale: [esc_civetta/main.html](../exercises/esc_civetta/main.html).

---

## III. Liste e Citazioni nel Markup HTML

### 1. Tipologie di Liste
HTML mette a disposizione tre strutture di lista per organizzare informazioni:

```
                            ┌───────────────────────────────┐
                            │          LISTE HTML           │
                            └───────────────┬───────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
│ Non Ordinate (<ul>)   │       │   Ordinate (<ol>)     │       │   Descrizione (<dl>)  │
│ Elementi con bullet   │       │ Elementi con numeraz. │       │ Coppie Termine-Descriz│
│ puntati (<li>)        │       │ sequenziale (<li>)    │       │ (<dt> e <dd>)         │
└───────────────────────┘       └───────────────────────┘       └───────────────────────┘
```

1. **Liste Non Ordinate (`<ul>` - Unordered List):** Presentano elementi associati a un marcatore grafico (*bullet point*). Gli elementi interni sono racchiusi in tag `<li>` (*List Item*).
2. **Liste Ordinate (`<ol>` - Ordered List):** Presentano elementi ordinati con numerazione sequenziale (numerica, alfabetica o romana).
3. **Liste di Descrizione (`<dl>` - Description List):** Strutturate per rappresentare coppie chiave-valore o glossari, formate da termini definiti (`<dt>` - *Definition Term*) e rispettive definizioni (`<dd>` - *Definition Description*).

#### Annidamento delle Liste (Nesting)
Le liste possono essere annidate ricorsivamente inserendo un sotto-blocco `<ul>` o `<ol>` all'interno di un tag `<li>`:

```html
<ul>
  <li>Primo Anno
    <ul>
      <li>Programmazione I</li>
      <li>Architettura degli Elaboratori</li>
    </ul>
  </li>
  <li>Secondo Anno</li>
</ul>
```

### 2. Citazioni: `<q>` vs `<blockquote>`
* **Citazioni Brevi (`<q>` - Inline):** Utilizzato per brevi citazioni inserite nel corpo del paragrafo. I browser inseriscono automaticamente le virgolette tipografiche adatte alla lingua impostata.
* **Citazioni Lunghe (`<blockquote>` - Block-level):** Utilizzato per estratti lunghi o interi passaggi; il browser applica di default un rientro a sinistra. Supporta l'attributo semantico `cite` contenente l'URL della fonte.

```html
<p>Secondo Dijkstra, <q>la semplicità è prerequisito per l'affidabilità</q>.</p>

<blockquote cite="https://en.wikipedia.org/wiki/Edsger_W._Dijkstra">
  L'informatica non riguarda i computer più di quanto l'astronomia riguardi i telescopi.
</blockquote>
```

> [!EXAMPLE] Esercizio di Lezione
> Struttura di una pagina con lista non ordinata degli ingredienti (`<ul>`) e lista ordinata dei passaggi della procedura (`<ol>`, con annidamento nel `<li>`): [esc_liste/main.html](../exercises/esc_liste/main.html).

---

## IV. Fondamenti di CSS3: Regole, Collegamento e Tipografia

**CSS3 (Cascading Style Sheets Level 3)** è il linguaggio dichiarativo standard per la formattazione grafica, la tipografia, il layout e l'adattabilità responsiva delle pagine web.

### 1. Sintassi di una Regola CSS
Una regola CSS è composta da un **selettore** e da un **blocco di dichiarazioni**:

```css
selettore {
  proprieta-1: valore;
  proprieta-2: valore;
}
```

```
     ┌────────── Selettore (individua i nodi DOM bersaglio)
     │
     p {
       color: #2b2b2b;        ◄─── Dichiarazione (proprietà: valore;)
       font-size: 16px;       ◄─── Dichiarazione
     }
     └───┬───────────┘
         └──────── Blocco di Dichiarazione (Declaration Block)
```

### 2. Modalità di Inclusione
Il metodo standard e raccomandato è il collegamento a un file esterno via tag `<link>` all'interno della sezione `<head>`:
```html
<link rel="stylesheet" href="styles.css">
```

### 3. Gestione dei Colori
La proprietà `color` definisce il colore del testo e accetta diversi formati:
* **Parole chiave:** `red`, `blue`, `transparent`.
* **Esadecimale:** `#RRGGBB` o `#RGB` (es. `#3636b5`).
* **RGB / RGBA:** `rgb(54, 54, 181)` oppure `rgba(54, 54, 181, 0.8)` con canale alfa per l'opacità.
* **HSL / HSLA:** `hsl(240, 54%, 46%)` (Tonalità, Saturazione, Luminosità).

> [!EXAMPLE] Anatomia di un Colore Esadecimale
> Il cancelletto `#` è il prefisso che introduce la notazione esadecimale, seguita da **tre canali** (Red, Green, Blue), ciascuno espresso con due cifre in base 16 nel range `00`–`FF`, cioè da 0 a 255 in base 10:
> ```text
> #  36     36     B5
> │  │      │      └── Canale Blue : 0xB5 = 181
> │  │      └───────── Canale Green: 0x36 =  54
> │  └──────────────── Canale Red  : 0x36 =  54
> └─────────────────── Prefisso della notazione esadecimale
>
> #3636b5  ≡  rgb(54, 54, 181)  ≡  hsl(240, 54%, 46%)
> ```
> La **scala di grigi** si ottiene ponendo i tre canali uguali: `#000000` (nero), `#808080` (grigio medio) e `#FFFFFF` (bianco) corrispondono rispettivamente a `rgb(0,0,0)`, `rgb(128,128,128)` e `rgb(255,255,255)`.

### 4. Tipografia e Font
Le principali proprietà per il controllo tipografico sono:
* `font-family`: Specifica la lista di famiglie tipografiche con fallback (es. `font-family: 'Helvetica Neue', Arial, sans-serif;`).
* `font-size`: Definisce la dimensione del font.
* `font-weight`: Regola lo spessore (`normal`, `bold`, `100`–`900`).
* `font-style`: Specifica lo stile (`normal`, `italic`, `oblique`).
* `text-align`: Allineamento orizzontale (`left`, `right`, `center`, `justify`).
* `text-decoration`: Linee di decorazione (`none`, `underline`, `line-through`).
* `text-transform`: Trasformazione del casing (`uppercase`, `lowercase`, `capitalize`, `none`).

### 5. Unità di Misura Tipografiche: `px`, `em`, `%` e `rem`

| Unità | Natura | Base di Calcolo | Comportamento al Ridimensionamento | Eredità & Comportamento | Casi d'Uso Tipici |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`px`** | **Assoluta** | Pixel virtuale CSS (1/96 di pollice) | Fissa, non scala con il font utente | Non ereditabile proporzionalmente | Bordi, ombre, layout a dimensione rigida |
| **`em`** | **Relativa** | Dimensione del font dell'**elemento corrente** (o del genitore per `font-size`) | Scala dinamicamente | **Effetto Moltiplicativo (Compounding):** Se annidato, accumula le scale dei genitori | Spaziatura interna relativa (`padding`, `margin`) |
| **`%`** | **Relativa** | Dimensione del font del **genitore diretto** | Scala dinamicamente | Mantiene un rapporto diretto con il genitore | Dimensionamento proporzionale su testo |
| **`rem`** | **Relativa** | Dimensione del font dell'**elemento radice (`<html>`)** | Scala uniformemente su tutta la pagina | **Non accumula:** Evita il problema del compounding | Dimensione font principale, layout responsive |

> [!WARNING] Rischio del "Compounding Effect" con l'Unità `em`
> Quando si imposta `font-size: 1.2em` su elementi annidati (es. liste `<ul> <ul> <ul>`), la dimensione del font cresce esponenzialmente ad ogni livello di profondità:
> $$ \text{Dimensione} = \text{Base} \times (1.2)^n $$
> Per i font è preferibile utilizzare **`rem`** (Root EM), mantenendo `em` per padding e margini scalabili con la dimensione del testo del componente stesso.

---

## V. Ereditarietà e Cascata dei Valori CSS

Il CSS è *Cascading Style Sheets* perché le regole si applicano **a cascata**; il meccanismo che le trasmette lungo l'albero del DOM è l'**ereditarietà** (*inheritance*): una proprietà dichiarata su un elemento viene ereditata da tutti i suoi discendenti, che ne ripetono il valore **salvo** qualora non dichiarino un valore proprio per la stessa proprietà.

```html
<body>
  <h1>Titolo</h1>  <!-- eredita il colore rosso -->
  <p>Testo</p>     <!-- eredita il colore rosso -->
</body>
```

```css
body { color: red; }   /* il rosso si propaga a tutto il sotto-albero */
h1   { color: blue; }  /* l'h1 sovrascrive (non eredita) il valore ereditato */
```

```
          <body>  color: red  (valore dichiarato)
            │
            ├── <h1>  color: blue  ──► sovrascrive il valore ereditato
            └── <p>   color: red   ──► valore ereditato dal genitore
```

### 1. Ereditarietà e Proprietà Non Ereditate
Non tutte le proprietà si trasmettono: la specifica CSS assegna a ciascuna un flag *inherited* che ne determina il comportamento.

| Proprietà Ereditate | Proprietà Non Ereditate |
| :--- | :--- |
| `color`, `font-family`, `font-size`, `font-style`, `font-weight`, `line-height`, `letter-spacing`, `text-align`, `text-transform`, `visibility`, `white-space`, `list-style` | `margin`, `padding`, `border`, `background`, `width`, `height`, `display`, `position`, `top`/`right`/`bottom`/`left`, `transform`, `opacity`, `overflow`, `z-index` |

> [!TIP] Controllare l'Ereditarietà: `inherit`, `initial`, `unset`
> La keyword `inherit` impone l'ereditarietà anche su una proprietà non ereditata (es. `div { padding: inherit; }` prende dal genitore il suo padding), `initial` ripristina il valore di fabbrica della specifica e `unset` vale come `inherit` per le proprietà ereditate e come `initial` per le altre.

> [!NOTE] Ereditarietà e Unità `em` (cfr. § IV.5)
> Poiché `font-size` è una proprietà **ereditata**, l'unità `em` si calcola sulla base della dimensione **effettiva** di ciascun elemento: ogni livello di annidamento eredita la dimensione del genitore e la moltiplica per il proprio fattore, generando l'effetto moltiplicativo descritto in § IV.5.

### 2. La Cascata e l'Ordine di Prevalenza
Quando più regole competono per lo stesso elemento, il browser risolve il conflitto applicando la **cascata**, ovvero valutando i seguenti criteri in ordine decrescente di prevalenza:
1. **Rilevanza** (`!important`): una dichiarazione marcata `!important` vince su qualsiasi dichiarazione "normale".
2. **Origine e contesto:** `animazioni` > foglio di stile dell'**autore** > foglio di stile dell'**utente** > foglio di stile di **default del browser**.
3. **Specificità** del selettore (vedi § V.3).
4. **Ordine di dichiarazione:** a parità di specificità vince la regola comparsa **per ultima** nel foglio di stile.

> [!IMPORTANT] Il `!important` è un Antidoto, non una Soluzione
> Usato in serie (`!important` ovunque) il foglio di stile diventa incontrollabile: le regole "forti" non possono più essere sovrascritte nemmeno dalle regole successive. Viceversa, l'attributo inline `style="..."` è una dichiarazione *inline* e batte il foglio di stile dell'autore, ma resta sconsigliato per il principio di separazione delle responsabilità HTML/CSS.

### 3. Il Calcolo della Specificità
Quando due selettori con lo stesso peso si incontrano, la **specificità** decide quale prevale: si calcola come sequenza di quattro cifre con peso decrescente, dove `a` conta gli stili inline, `b` gli ID, `c` le classi/attributi/pseudo-classi e `d` i tag/pseudo-elementi.

$$ \text{Specificità} = (a, b, c, d) \qquad \text{valore} = a \cdot 1000 + b \cdot 100 + c \cdot 10 + d $$

| Selettore | `(a, b, c, d)` | Valore | Elementi selezionati |
| :--- | :--- | :---: | :--- |
| `p` | (0, 0, 0, 1) | 1 | Tutti i `<p>` |
| `.card p` | (0, 0, 1, 1) | 11 | I `<p>` discendenti di `.card` |
| `p[lang="it"]` | (0, 0, 1, 1) | 11 | I `<p>` con attributo `lang="it"` |
| `ul.menu > li a` | (0, 0, 1, 3) | 13 | I link dentro le voci di `.menu` |
| `#main-header h1` | (0, 1, 0, 1) | 101 | L'`h1` dentro `#main-header` |
| `p#intro` | (0, 1, 0, 1) | 101 | Il `<p>` con `id="intro"` |
| `style="..."` (inline) | (1, 0, 0, 0) | 1000 | Il solo elemento con stile inline |

> [!EXAMPLE] L'Ordine di Prevalenza in Azione
> Nel foglio di stile seguente il paragrafo risulta **verde**, nonostante la regola "più debole" compaia **per ultima** nel file:
> ```css
> body p { color: green; }  /* (0,0,0,2) → 2 : vince, dichiarata per prima  */
> p      { color: red;   }  /* (0,0,0,1) → 1 : perde, dichiarata per ultima  */
> ```
> Al contrario, un `p { color: red !important; }` farebbe tornare il testo **rosso**, sovrascrivendo anche `#intro p { color: blue; }` (101), perché `!important` ha precedenza su ogni regola "normale".

---

## VI. Gestione dei Background e Confronto con Tag Semantici

### 1. Proprietà del Background in CSS
Il background di un elemento viene controllato tramite le seguenti sotto-proprietà:
* `background-color`: Colore solido di sfondo (es. `#f4f4f4`).
* `background-image`: Percorso dell'immagine sorgente tramite `url('sfondo.png')`.
* `background-repeat`: Regola la ripetizione (`repeat`, `no-repeat`, `repeat-x`, `repeat-y`).
* `background-position`: Posizionamento dell'immagine nel riquadro (`center`, `top left`, `50% 50%`, `10px 20px`).
* `background-size`: Controllo del ridimensionamento:
  * `cover`: L'immagine copre interamente l'area del contenitore, ritagliando le parti eccedenti se il rapporto d'aspetto differisce.
  * `contain`: L'immagine viene scalata per essere interamente visibile all'interno del contenitore senza ritaglio.
  * `auto` o dimensioni esplicite (es. `100% auto`, `200px 150px`).
* `background-attachment`: Stabilisce se l'immagine scorre con il viewport (`scroll`) o rimane fissa rispetto allo schermo (`fixed`).

### 2. Confronto Architetturale: `<img>` (HTML) vs `background-image` (CSS)

| Caratteristica | Tag `<img>` (HTML) | Proprietà `background-image` (CSS) |
| :--- | :--- | :--- |
| **Scopo Primario** | Contenuto informativo e **semantico** | Scopo puramente **decorativo ed estetico** |
| **Accessibilità** | Supporta l'attributo `alt` letto dagli screen reader | Non accessibile alle tecnologie assistive |
| **SEO & Indicizzazione** | Indicizzato dai motori di ricerca (Google Images) | Ignorato dall'indicizzazione dei contenuti |
| **Flusso del Layout** | Occupa spazio fisico nel flusso del DOM | Renderizzato dietro al contenuto, non occupa spazio |
| **Dimensionamento** | Definito con attributi `width`/`height` o CSS | Controllato tramite `background-size` e `background-position` |
| **Stampa del Documento** | Stampato di default dal browser | Spesso escluso dai profili di stampa predefiniti |

> [!IMPORTANT] Regola di Scelta: Semantica vs Decorazione
> * Usa **`<img>`** se l'immagine trasmette un'informazione rilevante per il lettore (foto di un prodotto, grafico, autore, avatar).
> * Usa **`background-image`** se l'immagine ha una funzione unicamente visiva, decorativa, di sfondo o texture (banner astratti, icone decorative, sfondi di sezione).

---

## VII. Il CSS Box Model: Dimensionamento, Spaziatura e Bordi

Ogni elemento renderizzato nella pagina viene modellato dal motore di rendering come un rettangolo a strati concentrici, noto come **CSS Box Model**.

```
+-------------------------------------------------------------+
|                           MARGIN                            |
|  +-------------------------------------------------------+  |
|  |                        BORDER                         |  |
|  |  +-------------------------------------------------+  |  |
|  |  |                     PADDING                     |  |  |
|  |  |  +-------------------------------------------+  |  |  |
|  |  |  |                                           |  |  |  |
|  |  |  |                  CONTENT                  |  |  |  |
|  |  |  |            (width x height)               |  |  |  |
|  |  |  |                                           |  |  |  |
|  |  |  +-------------------------------------------+  |  |  |
|  |  |                                                 |  |  |
|  |  +-------------------------------------------------+  |  |
|  |                                                       |  |
|  +-------------------------------------------------------+  |
|                                                             |
+-------------------------------------------------------------+
```

### Componenti del Box Model
1. **Content (Contenuto):** L'area centrale in cui sono renderizzati testo, immagini o elementi figli. Le sue dimensioni sono definite da `width` e `height`.
2. **Padding (Spaziatura Interna):** Lo spazio trasparente interposto tra il contenuto e il bordo dell'elemento. Assume il colore di sfondo dell'elemento.
3. **Border (Bordo):** La linea perimetrale che avvolge il padding e il contenuto.
4. **Margin (Margine Esterno):** Lo spazio trasparente esterno al bordo, utilizzato per distanziare l'elemento dagli altri blocchi circostanti.

### 1. Dimensionamento: `width` e `height`
Impostano rispettivamente la larghezza e l'altezza dell'area del contenuto. Possono essere espresse in unità fisse (`px`) o percentuali (`%`).

### 2. Spaziatura Interna: `padding`
Sintassi *shorthand* multi-valore (in senso orario: **Top $\rightarrow$ Right $\rightarrow$ Bottom $\rightarrow$ Left**):
```css
/* 4 valori: top, right, bottom, left */
padding: 10px 20px 15px 5px;

/* 2 valori: top/bottom, left/right */
padding: 10px 20px;

/* 1 valore: tutti i 4 lati */
padding: 15px;
```

### 3. Bordi: `border` e `border-radius`
* **Shorthand `border`:** Combina tre proprietà in un'unica dichiarazione:
  ```css
  /* border: width style color; */
  border: 2px solid #333333;
  ```
* **Angoli Arrotondati (`border-radius`):** Definisce il raggio di curvatura degli angoli.
  ```css
  /* Arrotondamento uniforme */
  border-radius: 8px;

  /* 4 valori: top-left, top-right, bottom-right, bottom-left */
  border-radius: 15px 50px 30px 5px;

  /* Cerchio perfetto (su elemento quadrato) */
  border-radius: 50%;
  ```

### 4. Margini: `margin`
Controlla la separazione esterna tra elementi con la stessa sintassi a 4 valori del padding.
* **Centratura Orizzontale di un Blocco:**
  ```css
  .container {
    width: 80%;
    margin: 0 auto; /* Centra il blocco orizzontalmente */
  }
  ```

> [!INFO] Margin Collapsing (Collasso dei Margini)
> Nei margini verticali tra elementi di blocco adiacenti, i margini non si sommano: il browser applica solo il valore del margine più grande tra i due (*margin collapse*).

---

## VIII. Selettori CSS e Combinatori

I selettori identificano i nodi del DOM a cui applicare il set di proprietà grafiche.

### 1. Selettori di Base
* **Universale (`*`):** Seleziona tutti gli elementi del documento.
  ```css
  * { box-sizing: border-box; margin: 0; }
  ```
* **Di Tipo / Tag (`p`, `div`, `h1`):** Seleziona tutti gli elementi con quel tag HTML.
  ```css
  p { line-height: 1.5; }
  ```
* **Di Classe (`.nome_classe`):** Seleziona tutti gli elementi con l'attributo `class="nome_classe"`. Riutilizzabile su più elementi.
  ```css
  .highlight { background-color: #ffeb3b; }
  ```
* **Di ID (`#nome_id`):** Seleziona l'unico elemento con l'attributo `id="nome_id"`. Univoco all'interno del documento.
  ```css
  #main-header { font-size: 2rem; }
  ```

### 2. Combinatori CSS (Combinators)

I combinatori mettono in relazione due o più selettori per esprimere gerarchie e adiacenze strutturali nel DOM.

```
┌────────────────────────────────┬─────────────────┬───────────────────────────────────────────┐
│ Combinatore                    │ Sintassi        │ Descrizione Selezione                     │
├────────────────────────────────┼─────────────────┼───────────────────────────────────────────┤
│ Lista di Selettori             │ div, p          │ Tutti i <div> e tutti i <p>               │
│ Discendente (Spazio)           │ div p           │ Tutti i <p> annidati a qualsiasi          │
│                                │                 │ livello dentro un <div>                   │
│ Figlio Diretto (>)             │ div > p         │ Solo i <p> figli immediati di un <div>    │
│ Fratello Adiacente (+)         │ div + p         │ Il primo <p> posizionato immediatamente   │
│                                │                 │ dopo la chiusura di un <div>              │
│ Fratello Generale (~)          │ p ~ ul          │ Tutti gli <ul> preceduti da un <p>        │
│                                │                 │ che condividono lo stesso genitore        │
└────────────────────────────────┴─────────────────┴───────────────────────────────────────────┘
```

> [!EXAMPLE] Applicazione Pratica dei Combinatori
> Dato il seguente albero DOM:
> ```html
> <div class="card">
>   <p>Paragrafo 1 (Figlio diretto e discendente)</p>
>   <section>
>     <p>Paragrafo 2 (Discendente ma non figlio diretto)</p>
>   </section>
> </div>
> <p>Paragrafo 3 (Fratello adiacente)</p>
> <p>Paragrafo 4 (Fratello generale)</p>
> ```
> * `.card p`: Seleziona **Paragrafo 1** e **Paragrafo 2**.
> * `.card > p`: Seleziona solo **Paragrafo 1**.
> * `.card + p`: Seleziona solo **Paragrafo 3**.
> * `.card ~ p`: Seleziona sia **Paragrafo 3** che **Paragrafo 4**.

---

## IX. Stile delle Liste e Proprietà Avanzate

### 1. Personalizzazione delle Liste in CSS
Le liste (`<ul>`, `<ol>`) possono essere personalizzate tramite le seguenti proprietà:
* `list-style-type`: Specifica il tipo di marcatore (es. `disc`, `circle`, `square`, `decimal`, `lower-alpha`, `none`).
* `list-style-image`: Imposta un'immagine personalizzata come marcatore tramite `url('bullet.png')`.
* `list-style-position`: Posizione del marcatore rispetto al blocco del testo:
  * `outside` (default): Il marcatore è all'esterno dell'area del testo.
  * `inside`: Il marcatore rientra all'interno del flusso del blocco.
* `list-style`: Proprietà *shorthand* per combinare tipo, posizione e immagine.

```css
/* Reset completo dei marcatori per menu di navigazione */
ul.nav-menu {
  list-style: none;
  padding: 0;
  margin: 0;
}
```

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Programmazione_Web]]
