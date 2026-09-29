---
date: 2026-09-28
tags:
  - programmazione-web
type: lezione
---
# Presentare e Inviare Dati: Tabelle, Form e Ripasso del Box Model

La lezione 3 ("Presentare e inviare dati") chiude il ciclo: riprende il **Box Model** e i **combinatori** gia trattati, aggiunge lo stile delle citazioni, e poi apre il capitolo nuovo con **tabelle** e **form**, cioe i due modi in cui una pagina web *mostra* dati e *raccoglie* dati dall'utente.

> [!INFO] Materiale di riferimento
> - `material/slides/pwm_lezione3.pdf` - Lezione 3, "Presentare e inviare dati (Tabelle, Form)", 13 slide:materialedidattico.
> - `material/slides/pwm_lezione2.pdf` - Lezione 2, pagine 26-41: ripasso di `background`, Box Model, selettori, combinatori, stile delle citazioni.
> - La scheda [[Tag_HTML_e_Proprieta_CSS]] raccoglie in forma tabellare tutti i tag e le proprietà toccati oggi: utile come riferimento rapido mentre si scrive il codice.

> [!NOTE] Limite della trascrizione
> Gli esempi di codice nelle slide sono immagini rasterizzate e nel PDF non esiste alcun layer di testo, quindi non sono estraibili automaticamente. Gli esempi riportati qui sono stati ricostruiti sulla sintassi ufficiale HTML5/CSS3 e sui concetti delle slide, non trascritti alla lettera dalle figure.

---

## I. Ripasso: il Box Model

Ogni elemento renderizzato viene modellato dal browser come una **scatola rettangolare** con quattro parti concentriche. La somma delle quattro misure dà la dimensione effettiva dell'elemento sulla pagina.

```
+-------------------------------------------------------------+
|                           MARGIN                            |  <- spazio esterno
|  +-------------------------------------------------------+  |
|  |                        BORDER                         |  |  <- linea perimetrale
|  |  +-------------------------------------------------+  |  |
|  |  |                     PADDING                     |  |  |  <- spazio interno
|  |  |  +-------------------------------------------+  |  |  |
|  |  |  |                  CONTENT                  |  |  |  |  <- width x height
|  |  |  +-------------------------------------------+  |  |  |
|  |  +-------------------------------------------------+  |  |
|  +-------------------------------------------------------+  |
+-------------------------------------------------------------+
```

| Parte | Definizione | Proprietà |
|---|---|---|
| **Content** | Area in cui viene visualizzato il contenuto (testo, immagini, elementi figli) | `width`, `height` |
| **Padding** | Spazio tra il contenuto e il bordo, per creare respiro interno attorno al contenuto | `padding` |
| **Border** | Linea che circonda il padding e il contenuto, personalizzabile in larghezza, stile e colore | `border` |
| **Margin** | Spazio esterno all'elemento, che lo separa dagli elementi circostanti | `margin` |

> [!IMPORTANT] Padding interno, margin esterno
> La distinzione da fissare: il **padding** sta *dentro* il bordo e separa il contenuto dal bordo stesso; il **margin** sta *fuori* dal bordo e serve a distanziare l'elemento dagli altri. Per la gestione della spaziatura verticale dei blocchi si usa il margin, per la spaziatura interna il padding.

### 1. Dimensionamento: `width` e `height`

Impostano rispettivamente la larghezza e l'altezza dell'area del contenuto. Accettano unità assolute (`px`), relative (`%`, `em`, `rem`) e parole chiave (`auto`, `max-content`, `min-content`).

```css
.card {
  width: 300px;
  height: 150px;
}
```

> [!NOTE] Nota del Prof
> Di solito si usa `em` per comodità: essendo un'unità relativa, l'elemento si ridimensiona da solo al variare della dimensione del testo circostante. La discussione completa sulle unità è in [[02_HTML5_e_CSS3_Fondamenti_e_Box_Model#IV. Fondamenti di CSS3: Regole, Collegamento e Tipografia|nota 02, sezione IV.5]].

### 2. Spaziatura interna: `padding`

Sintassi *shorthand* con valori in senso orario (top, right, bottom, left):

```css
/* 4 valori: top, right, bottom, left */
.card { padding: 10px 20px 15px 5px; }

/* 2 valori: verticali / orizzontali */
.card { padding: 10px 20px; }

/* 1 valore: tutti e quattro i lati */
.card { padding: 15px; }

/* Per un solo lato */
.card { padding-top: 20px; }
```

### 3. Bordi: `border`

`border` e una proprietà **shorthand** che combina tre proprietà, che possono anche essere usate singolarmente:

| Proprieta | Funzione | Valori comuni |
|---|---|---|
| `border-width` | Spessore della linea | `1px`, `2px`, `3px`, `thin`, `medium`, `thick` |
| `border-style` | Tipo di linea | `none`, `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge` |
| `border-color` | Colore della linea | `red`, `#333`, `rgb(51,51,51)` |

```css
.card {
  /* border: <width> <style> <color>; */
  border: 2px solid #333;

  /* Le stesse tre, scritte singolarmente */
  border-width: 2px;
  border-style: solid;
  border-color: #333;
}
```

**Rimuovere il bordo:** `border: none` (o `border-width: 0`).

```css
.card {
  border: none;      /* shorthand: azzera width, style e color */
  border-width: 0;   /* alternativa */
}
```

> [!WARNING] Lo shorthnd azzera tutto
> `border: none` non cancella solo lo stile di linea: azzera larghezza, stile e colore. Se prima avevi `border: 2px solid red` e poi aggiungi `border: none`, per riavere il bordo rosso spesso 2px devi riscrivere l'intera shorthand, non basta rimettere `border-style: solid`.

### 4. Angoli arrotondati: `border-radius`

Definisce il raggio di curvatura degli angoli dell'elemento. Accetta valori diversi per ogni angolo, indicati in ordine orario a partire dall'angolo superiore sinistro.

```css
/* Arrotondamento uniforme */
.card { border-radius: 8px; }

/* 4 valori: sup. sx, sup. dx, inf. dx, inf. sx */
.card { border-radius: 15px 50px 30px 5px; }

/* Solo l'angolo superiore sinistro */
.card { border-top-left-radius: 15px; }

/* Cerchio perfetto su elemento quadrato */
.card { border-radius: 50%; }
```

```
   15px      50px
   +-------+-------+
   |               |   <- angolo inferiore destro: 30px
   |               |
   +-------+-------+
     5px
```

> [!NOTE] Nota del Prof
> I pulsanti di Material Design sono arrotondati di proposito: e una scelta di design coerente con le linee guida, non un effetto casuale. `border-radius: 50%` su un elemento quadrato produce il classico pulsante circolare.

### 5. Margini: `margin`

Stessa sintassi a valori orari del padding, ma lo spazio e esterno al bordo.

```css
.card {
  margin: 20px;              /* tutti i lati */
  margin: 10px 20px;         /* verticale / orizzontale */
}

/* Centratura orizzontale di un blocco: ilobby di auto assorbe lo spazio residuo */
.container {
  width: 80%;
  margin: 0 auto;
}
```

> [!INFO] Margin collapsing
> Tra due blocchi adiacenti i margini verticali **non si sommano**: il browser applica solo il valore maggiore (*margin collapsing*). Per separare due elementi di 20px di margine ciascuno servono 20px di distanza, non 40px.

### 6. Esercizio svolto in aula

La slide proponeva di **replicare un elemento** (una "siretta", un banner promozionale) usando soltanto queste proprietà:

```
background   padding   border   font-size   width   text-align
```

La slide di risoluzione aggiungeva la domanda: **"Cosa ci manca?"** La risposta e che con quelle proprietà non si controlla nulla della **distanza dell'elemento dagli altri**: serve il `margin`. Senza, l'elemento resta attaccato ai vicini.

```css
/* Ricostruzione del banner */
.banner {
  background-color: #4a90d9;
  padding: 20px 30px;
  border: 2px solid #2c5f96;
  border-radius: 6px;
  font-size: 1.25em;
  width: 60%;
  text-align: center;
  margin: 20px auto;   /* <- la proprieta che mancava */
}
```

---

## II. Selettori e Combinatori

I **selettori** sono espressioni che permettono di selezionare gli elementi HTML a cui applicare le regole di stile. I tipi trattati:

| Tipo | Sintassi | Seleziona |
|---|---|---|
| Universale | `*` | Tutti gli elementi |
| Di tipo (tag) | `p` | Tutti i `<p>` |
| Di classe | `.mia_classe` | Tutti gli elementi con `class="mia_classe"` |
| Di ID | `#mio_id` | L'unico elemento con `id="mio_id"` |
| Discendente | `blockquote p` | I `<p>` dentro un `<blockquote>` |

I **combinatori** combinano due o piu selettori per esprimere relazioni strutturali nel DOM.

| Combinatore | Sintassi | Risultato |
|---|---|---|
| **Selector list** | `div, p` | Tutti gli elementi `<div>` **e** tutti gli elementi `<p>` |
| **Descendant** (discendente) | `div p` | Tutti i `<p>` dentro elementi `<div>`, a qualsiasi profondita |
| **Child** (figlio diretto) | `div > p` | Ogni `<p>` che e **figlio diretto** di un `<div>` |
| **Next-sibling** (fratello adiacente) | `div + p` | Il **primo** `<p>` posizionato immediatamente dopo un `<div>` |
| **Subsequent-sibling** (fratello generale) | `p ~ ul` | Tutti gli `<ul>` preceduti da un `<p>` con lo stesso genitore |

> [!EXAMPLE] Le quattro relazioni sullo stesso DOM
> ```html
> <div>
>   <p>Paragrafo 1 (figlio diretto)</p>
>   <section>
>     <p>Paragrafo 2 (discendente, non figlio diretto)</p>
>   </section>
> </div>
> <p>Paragrafo 3 (fratello adiacente)</p>
> <p>Paragrafo 4 (fratello generale)</p>
> ```
> | Selettore | Seleziona |
> |---|---|
> | `div p` | Paragrafo 1 **e** Paragrafo 2 |
> | `div > p` | solo Paragrafo 1 |
> | `div + p` | solo Paragrafo 3 |
> | `p ~ ul` / `div ~ p` | Paragrafo 3 **e** Paragrafo 4 |

### Esercizio: "Trovare gli intrusi"

La slide di riepilogo elencava i tag e le proprietà visti fino a quel punto, con l'istruzione **"Trovare gli intrusi"**: non tutti gli elementi dell'elenco erano infatti tratti a lezione.

**Elenco dei tag:** `<div>`, `<p>`, `<span>`, `<section>`, `<img>`, `<input>`, `<hr>`, `<h1>`-`<h2>`, `<span>`, `<a>`, `<em>`, `<strong>`, commento HTML.
**Elenco delle proprietà:** `color`, `background-color`, `background-image`, `font-size`, `font-weight`, `font-style`, `margin`, `padding`, `border`, `border-radius`, `list-style`, `width`, `height`.

> [!WARNING] Le risposte
> Due anomalie nell'elenco. La prima e banale: **`<span>` compare due volte**, una sola delle due voci e un duplicato. La seconda e quella che conta: **`<input>` e l'intruso vero**, perche a quel punto della lezione non era ancora stato introdotto. `<input>` diventa oggetto di studio solo con le form, che sono il tema di oggi. Le proprietà CSS dell'elenco sono invece tutte effettivamente viste.

---

## III. Stile delle Citazioni in CSS

> [!IMPORTANT] Cambiare i caratteri delle virgolette
> In CSS si possono cambiare i caratteri usati per le citazioni, senza toccare il testo del documento. I caratteri speciali da usare si possono consultare su <https://www.leformat.info/info/charset/UTF-8/list.htm> (tabella dei caratteri UTF-8 indicata dal prof).

La proprietà `quotes` definisce le coppie di caratteri di apertura e chiusura. Con **quattro valori** si specificano anche le coppie per le citazioni annidate:

```css
q {
  /* apertura esterna, chiusura esterna, apertura interna, chiusura interna */
  quotes: "\201C" "\201D" "\2018" "\2019";
}
```

| Valore | Carattere | Uso |
|---|---|---|
| `\201C` / `\201D` | virgolette caporali doppie " " | Citazione esterna (primo livello) |
| `\2018` / `\2019` | virgolette singole ' ' | Citazione annidata (secondo livello) |
| `\00AB` / `\00BB` | guillemets francesi " " | Stile alternativo, usato in italiano |
| `\201E` | doppia virgoletta bassa „ | Apertura in stile tedesco |

Le pseudo-classi `open-quote` e `close-quote` permettono di inserire i caratteri in modo automatico dagli elementi che richiedono le virgolette:

```css
/* Citazione con blockquote: le virgolette sono generate dal CSS */
blockquote {
  quotes: "\201C" "\201D";
  font-style: italic;
}
```

> [!NOTE] Differenza rispetto al markup
> In HTML5 esistono gia i tag `<q>` (inline) e `<blockquote>` (blocco), descritti in [[02_HTML5_e_CSS3_Fondamenti_e_Box_Model#III. Liste e Citazioni nel Markup HTML|nota 02, sezione III]]. I tag scelgono il *contenitore* della citazione; la proprietà CSS `quotes` sceglie i *caratteri* con cui viene marcata. Le due cose sono indipendenti: si puo avere un `<q>` con le virgolette caporali e senza.

---

## IV. Tabelle

### 1. Funzione e struttura

Le tabelle si utilizzano per **organizzare dati in righe e colonne**. La gerarchia dei tag e rigorosa:

```
<table>
  <tr>...</tr>   -> righe
</table>
   dentro ogni <tr>:
     <th>...</th>   -> intestazioni di colonna
     <td>...</td>   -> celle di dati
```

```html
<table>
  <tr>
    <th>Prodotto</th>
    <th>Prezzo</th>
  </tr>
  <tr>
    <td>Tastiera</td>
    <td>45,00 EUR</td>
  </tr>
</table>
```

> [!WARNING] Le tabelle non servono per il layout
> Le tabelle **non** si usano per allineare elementi all'interno della pagina: usare il CSS. Una tabella usata per impaginare falsifica la semantica del documento, confonde gli screen reader che narrano "riga 3, colonna 2" su contenuti che non sono dati tabellari, e spezza il flusso del documento. L'allineamento si ottiene con blocchi, flexbox e grid.

### 2. Le sezioni semantiche

La struttura completa separa intestazione, corpo e piede, e permette di dichiarare cosa descrive ogni intestazione:

```html
<table>
  <caption>Risultato dell'ultimo esame</caption>
  <thead>
    <tr>
      <th scope="col">Studente</th>
      <th scope="col">Voto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Rossi Mario</th>
      <td>28</td>
    </tr>
  </tbody>
</table>
```

| Elemento | Funzione |
|---|---|
| `<caption>` | Didascalia della tabella, figlia diretta di `<table>` prima di `<thead>` |
| `<thead>` | Raggruppa la/le righe di intestazione |
| `<tbody>` | Corpo dei dati |
| `<tfoot>` | Riga dei totali, sotto al corpo |
| `scope="col"` | L'intestazione descrive la colonna sottostante |
| `scope="row"` | L'intestazione descrive la riga che segue |

### 3. Stile di una tabella

Le tabelle **non hanno stile di default**: senza CSS appaiono come righe di testo senza bordi, senza spaziatura e con celle che si stringono al minimo. Servono quindi esplicitamente `border`, `padding` e gestione delle dimensioni.

```css
table {
  border-collapse: collapse;   /* unisce i bordi adiacenti in uno solo */
  width: 100%;
}

th, td {
  border: 1px solid #333;     /* serve border-collapse per un aspetto pulito */
  padding: 8px 12px;          /* le celle non hanno padding di default */
  text-align: left;           /* le celle non sono allineate a sinistra di default */
}

th {
  background-color: #f0f0f0;
}
```

> [!IMPORTANT] `border-collapse: collapse` e il dettaglio che si dimentica
> Di default le tabelle usano `border-collapse: separate`, dove ogni cella ha i propri bordi e quelli adiacenti si affiancano formando una linea doppia piu spessa. Senza `collapse` si ottiene un reticolo con righe e colonne che sembrano ognuna contornata due volte. E la prima proprieta da impostare su una tabella con bordi.

### 4. `rowspan` e `colspan`

Permettono a una singola cella di occupare piu colonne o piu righe della griglia.

| Attributo | Effetto |
|---|---|
| `colspan="n"` | La cella si estende su `n` colonne |
| `rowspan="n"` | La cella si estende su `n` righe |

Nella tabella dell'esercizio la griglia logica e 3x3, ma le celle hanno dimensioni diverse per effetto di `rowspan` e `colspan`:

```html
<table>
  <tr>
    <th colspan="2">Primo semestre</th>   <!-- occupa 2 colonne della riga 1 -->
    <th>Totale</th>
  </tr>
  <tr>
    <td rowspan="2">Appunti</td>          <!-- occupa le righe 2 e 3 -->
    <td>Teoria</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Esercizi</td>
    <td>12</td>
  </tr>
</table>
```

```
+------------------+-------------+
| Primo semestre   |  Totale     |   <- colspan="2"
+------------------+-------------+
| Appunti | Teoria |     18      |
|          +-------------+       |   <- rowspan="2" occupa
|          | Esercizi   |  12   |      anche la riga sotto
|          +-------------+       |
+------------------+-------------+
```

> [!NOTE] Vincolo sul conteggio
> L'attributo dichiara quante celle della griglia logica la cella "assorbe". Le celle delle righe successive non vengono contate: nell'esempio la terza riga ha solo due `<td>` perche la prima colonna e gia occupata dal `rowspan` della riga precedente. E il modo in cui il browser ricostruisce la griglia.

---

## V. Form

### 1. Cosa sono e a cosa servono

> [!IMPORTANT] Form
> Le form **raccolgono un input dall'utente e lo trasmettono al server**. Sono l'unico modo, in HTML puro, di ottenere dati digitati dall'utente e inviare themi al backend: i link e le immagini possono solo *portare* il click, non *raccogliere* dati strutturati.

```html
<form action="/registrazione" method="post">
  <!-- i controlli del modulo vanno qui -->
</form>
```

| Attributo | Funzione |
|---|---|
| `action` | Specifica **dove** vengono inviati i dati del form |
| `method` | Definisce il **metodo HTTP** usato per l'invio (`GET` o `POST`) |

> [!EXAMPLE] `GET` e `POST` nelle form
> La scelta del `method` e esattamente la scelta descritta in [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.5 Metodi HTTP|nota di sicurezza informatica, sezione 5.5]]:
> - **`method="get"`**: l'input dell'utente viaggia **nel campo URL della riga di richiesta**, in chiaro nella query string. Finisce nella cronologia del browser, nei log del server e nell'intestazione `Referer`. Va bene per ricerche e filtri non sensibili.
> - **`method="post"`**: l'input viaggia **nel corpo dell'entita** della richiesta, fuori dall'URL. Va usato per credenziali e dati personali.
> Le form HTML emettono solo `GET` e `POST`: `PUT` e `DELETE` non sono invocabili da una form, il che le rende meno esposte al cross-site request forgery.

### 2. `<input>` e `<label>`

* Il tag **`<input>`** consente all'utente di inserire dati di vario tipo: e un elemento **vuoto**, quindi non ha tag di chiusura e tutta la sua informazione e negli attributi.
* Il tag **`<label>`** serve per **descrivere un input**, associato tramite l'attributo `for`.

```html
<label for="nome">Nome</label>
<input type="text" id="nome" name="nome">
```

| Attributo | Funzione |
|---|---|
| `id` | Identifica un elemento in modo **univoco nel DOM**. E il valore a cui `for` della label deve corrispondere |
| `name` | Identifica i dati del campo **nel momento in cui la form viene inviata al server**: e il nome che compare nella chiave dei dati trasmessi |

> [!IMPORTANT] `id` e `name` non sono la stessa cosa
> `id` risolve il problema del **collegamento interno al DOM** (il `for` della label, il fragment `#id` nell'URL, i selettori CSS `#id`). `name` risolve il problema della **trasmissione dei dati** ed e visibile solo al momento dell'invio. Nella maggior parte dei controlli di un form i due valori coincidono per comodita, ma se si omettono si ottengono sintomi opposti: senza `name` il campo non viene inviato, senza `id` non si puo associare la label.
>
> Nota: `id` e `name` hanno anche una differenza di comportamento storico: su un `<form>` l'attributo `name` e cio che il DOM espone come `form.nomeCampo` per accedere ai campi da JavaScript, mentre su altri elementi vale il criterio dell'`id`.

> [!WARNING] `placeholder` non e un'etichetta
> Il placeholder sparisce appena l'utente inizia a scrivere, ed e invisibile agli screen reader e alla stampa. Il nome del campo va sempre in un `<label for="...">`.

### 3. Tipi di input

Il comportamento di un `<input>` e definito interamente dall'attributo `type` (ha come default `text`).

| `type` | Controllo | Note |
|---|---|---|
| `text` | Campo di testo a riga singola | Il default se `type` e omesso |
| `number` | Campo numerico | Accetta gli attributi `min` e `max` |
| `range` | Cursore/scorrimento | Accetta `min` e `max` |
| `email` | Campo per indirizzo email | Validazione del formato |
| `tel` | Campo per numero telefonico | Non valida il formato, solo il tipo di tastiera |
| `url` | Campo per indirizzo web | Validazione del formato |
| `password` | Campo per password | Il valore viene mascherato |
| `date` | Selettore di data | Formato `yyyy-mm-dd` |
| `time` | Selettore di orario | Formato `hh:mm` |
| `file` | Selettore di file da caricare | Apre il file picker del sistema |
| `color` | Selettore di colore | Valore esadecimale |
| `search` | Campo di ricerca | Ha un pulsante di reset in alcuni browser |
| `hidden` | Campo invisibile | **Deve includere l'attributo `value`** |

```html
<input type="text" name="nome">
<input type="number" name="eta" min="18" max="99">
<input type="range" name="volume" min="0" max="100">
<input type="email" name="email" placeholder="nome@dominio.it" required>
<input type="tel" name="telefono">
<input type="url" name="sito">
<input type="password" name="password">
<input type="date" name="nascita">
<input type="time" name="orario">
<input type="file" name="cv">
<input type="color" name="colore">
<input type="search" name="q">
<input type="hidden" name="csrf_token" value="aBc123XyZ">
```

> [!NOTE] Differenza tra validazione implicita e esplicita
> Gli attributi `min`, `max` e `required` attivano la **validazione implicita** del form: il browser blocca l'invio e mostra un messaggio, senza che serva JavaScript. E una difesa lato client quindi agevolmente aggirabile: la validazione che conta per sicurezza va replicata **sempre** lato server. `type="tel"` e `type="password"` invece non validano nulla, servono solo a indicare il tipo di tastiera e a mascherare il testo.

### 4. Altri tipi di input: selezione e pulsanti

| `type` | Controllo | Note |
|---|---|---|
| `checkbox` | Casella di spunta | Indipendente dalle altre: piu checkbox possono essere selezionate insieme |
| `radio` | Pulsante di scelta | Appartiene a un gruppo: una sola selezione possibile, le radio con lo stesso `name` formano il gruppo |
| `submit` | Pulsante di invio | Invia il form al server |
| `reset` | Pulsante di reset | Riporta i campi ai valori iniziali |

```html
<!-- Caselle di spunta indipendenti -->
<label><input type="checkbox" name="lingue" value="it"> Italiano</label>
<label><input type="checkbox" name="lingue" value="en"> Inglese</label>

<!-- Gruppo radio: stesso name, una sola selezione -->
<label><input type="radio" name="metodo" value="ritiro" checked> Ritiro in negozio</label>
<label><input type="radio" name="metodo" value="consegna"> Consegna a domicilio</label>

<!-- Pulsanti -->
<input type="submit" value="Invia ordine">
<input type="reset" value="Annulla">
```

> [!IMPORTANT] Il `name` e il `value` definiscono cosa viene inviato
> Il `name` del controllo e la **chiave** nei dati inviati, il `value` e il **dato** corrispondente. Su una checkbox non spuntata il `name` non compare affatto nei dati: per questo i checkbox non marcati risultano assenti, e non `value=""`. Il raggruppamento delle radio avviene esclusivamente tramite l'uguaglianza del `name`.

### 5. `select` e `optgroup`

Il `select` e un menu a tendina. Nella forma semplice contiene direttamente gli `<option>`; con `optgroup` le opzioni vengono raggruppate in sezioni etichettate.

```html
<!-- select semplice -->
<label for="citta">Citta</label>
<select id="citta" name="citta">
  <option value="">-- scegli --</option>
  <option value="perugia" selected>Perugia</option>
  <option value="roma">Roma</option>
</select>

<!-- select con optgroup -->
<label for="regione">Regione</label>
<select id="regione" name="regione">
  <optgroup label="Umbria">
    <option value="perugia">Perugia</option>
    <option value="terni">Terni</option>
  </optgroup>
  <optgroup label="Lazio">
    <option value="roma">Roma</option>
    <option value="latina">Latina</option>
  </optgroup>
</select>
```

| Attributo | Funzione |
|---|---|
| `value` | Valore effettivamente inviato, diverso dal testo mostrato |
| `selected` | Opzione predefinita |
| `optgroup` label | Titolo del gruppo di opzioni |
| `multiple` | (su `select`) Consente piu selezioni |
| `size` | (su `select`) Numero di righe visibili prima dello scroll |

### 6. `button` e `textarea`

```html
<!-- button: pulsante azionabile, con lo stesso aspetto e comportamento di submit -->
<button type="submit">Invia il modulo</button>
<button type="button">Annulla</button>

<!-- textarea: campo di testo su piu righe -->
<label for="messaggio">Messaggio</label>
<textarea id="messaggio" name="messaggio" rows="6" cols="50"
          placeholder="Scrivi qui il tuo messaggio"></textarea>
```

| Elemento | Note |
|---|---|
| `<button>` | Ha `type` esplicito: `submit` (invia), `button` (nessuna azione), `reset` (azzera). Il valore predefinito e `submit` |
| `<textarea>` | Il contenuto sta **fra i tag di apertura e chiusura**, non in un attributo |

> [!NOTE] `<textarea>` e `<input type="text">`
> La differenza non e solo la multisriga: il contenuto di `<textarea>` e testo reale fra i tag, il che permette di precompilarlo e di scrivere piu righe; l'input e un elemento vuoto, con il valore in attributo. Un `placeholder` dentro una `textarea` non funziona, va usato l'attributo.

### 7. `datalist` e `fieldset`

```html
<!-- datalist: suggerisce valori senza impedire di scriverne altri -->
<label for="browser">Browser</label>
<input type="text" id="browser" name="browser" list="browser-consigliati">
<datalist id="browser-consigliati">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Safari">
</datalist>

<!-- fieldset: raggruppa controlli correlati, legend ne dà il titolo -->
<fieldset>
  <legend>Dati di fatturazione</legend>
  <label for="via">Via e numero civico</label>
  <input type="text" id="via" name="via">
</fieldset>
```

| Elemento | Funzione |
|---|---|
| `datalist` | Fornisce un elenco di suggerimenti. L'utente puo scegliere dalla lista **oppure** digitare un valore qualsiasi |
| `fieldset` | Raggruppa controlli correlati, visivamente e semanticamente. L'attributo `disabled` disabilita l'intero gruppo |
| `legend` | Titolo del `fieldset`, deve essere il primo suo figlio |

> [!IMPORTANT] `datalist` non e un menu a tendina
> E la differenza che genera piu errori: `select` **vincola** la scelta a uno dei valori proposti, `datalist` **suggerisce** valori lasciando campo libero. Con `datalist` l'utente puo inviare una stringa che non era nella lista, quindi la validazione lato server non puo assumere un set di valori noti.

---

## VI. Esercizio per Giovedi

> [!EXAMPLE] Consegna
> Realizzare un **sito web di tre pagine**:
> 1. una **home** con la presentazione generale dei contenuti;
> 2. una pagina con una **tabella** e qualche **immagine**;
> 3. una terza pagina con una **form**, scelta tra quelle proposte in fondo alla slide 13.
>
> Le tre pagine devono condividere lo stesso foglio di stile. Vanno usate le proprietà e i tag visti fino ad ora, e in particolare la gestione del Box Model (`padding`, `margin`, `border`, `border-radius`) per la spaziatura e la cornice degli elementi.


---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Programmazione_Web]]
