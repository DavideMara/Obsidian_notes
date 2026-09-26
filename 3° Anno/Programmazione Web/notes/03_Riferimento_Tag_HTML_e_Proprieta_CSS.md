---
date: 2026-09-26
tags:
  - programmazione-web
type: riferimento
---
# Funzioni dei Tag HTML e Proprieta CSS

---

## I. Struttura del Documento

| Elemento | Tipo | Funzione | Quando usarlo |
| :--- | :--- | :--- | :--- |
| `<!DOCTYPE html>` | dichiarazione | Attiva la modalita standard di rendering nel browser | Sempre, come primissima riga. Assente, il browser passa in *quirks mode* |
| `<html lang="it">` | contenitore | Radice del documento. `lang` dichiara la lingua per screen reader e motori di ricerca | Sempre, con la lingua reale del contenuto |
| `<head>` | contenitore | Metadati non visibili: charset, viewport, titolo, link a risorse esterne | Sempre. Nessun contenuto visibile qui dentro |
| `<body>` | contenitore | Unico contenitore ammesso per il contenuto visibile della pagina | Sempre |
| `<meta charset="utf-8">` | vuoto | Dichiara la codifica dei caratteri | Sempre, per prima riga di `<head>` |
| `<meta name="viewport">` | vuoto | Imposta la larghezza della finestra logica, abilita il layout responsive | Sempre: `width=device-width, initial-scale=1.0` |
| `<title>` | di testo | Titolo del documento: label della scheda, titolo del link nei risultati, segnalibro | Sempre, unico e descrittivo |
| `<link rel="stylesheet">` | vuoto | Collega un foglio di stile esterno | Per ogni CSS. Sempre nel `<head>` |
| `<script src="...">` | vuoto | Collega ed esegue uno script esterno | In fondo al `<body>`, oppure nel `<head>` con `defer` |

> [!WARNING] `<link>` non carica uno script
> `rel="scripts"` non e un valore valido di `rel`. Gli script si caricano con `<script src="main.js"></script>`. `<link>` serve solo per risorse che il browser non interpreta (CSS, icone, font, prefetch).

---

## II. Elementi Strutturali (Landmark)

Questi elementi non descrivono l'aspetto: dichiarano **il ruolo** del contenuto. E esattamente cio che cercano screen reader, crawler e modelli di linguaggio.

| Elemento | Funzione | Quando usarlo |
| :--- | :--- | :--- |
| `<header>` | Intestazione di una pagina o di una sezione, tipicamente con titolo e navigazione | Sempre uno per pagina. Puo essere anche l'intestazione di un solo `<article>` |
| `<nav>` | Blocco di link di navigazione, principale o secondario | Menu, indice delle sezioni, link di navigazione interni. Solo se il contenuto e una lista di link |
| `<main>` | Contenuto principale e unico della pagina | **Esattamente uno per documento**, mai annidato |
| `<article>` | Blocco di contenuto autonomo, completo e potenzialmente distribuibile da solo | Un articolo, una scheda, un post: tutto cio che ha senso leggere senza il resto della pagina |
| `<section>` | Sezione tematica di un documento, raggruppata per argomento | Sempre introdotta da un heading. Se non ha un heading, e un `<div>`: usa `<div>` |
| `<aside>` | Contenuto tangenziale, complementare al contenuto principale | Sidebar, glossario, note, box promozionali |
| `<footer>` | Chiusura di una pagina o di una sezione | Autore, anno, licenza, link di contatto |

> [!IMPORTANT] Sezione senza heading non e una sezione
> `<section>` non e un contenitore generico come `<div>`: rappresenta un'affermazione di struttura, e la sua unità di organizzazione e l'heading. Una sezione vuota, o senza `<h2>`, non ha nessun vantaggio semantico e si risolve con `<div>`.

---

## III. Elementi di Testo

| Elemento | Tipo | Funzione | Quando usarlo |
| :--- | :--- | :--- | :--- |
| `<h1>` - `<h6>` | blocco | Heading, titolo di una sezione. Da `<h1>` a `<h6>` in ordine, senza salti | Un solo `<h1>` per pagina. Non usarli per la grandezza del testo: quello e CSS |
| `<p>` | blocco | Paragrafo di testo | Qualsiasi testo da leggere. Non dentro `<h1>` o `<li>` |
| `<strong>` | inline | Enfasi forte, importanza non solo estetica | "Questo e **fondamentale**" |
| `<em>` | inline | Enfasi debole o intento del testo | "Lo ha **detto** lui" |
| `<code>` | inline | Frammento di codice, nome di file, identificatore | `snip --lang` |
| `<pre>` | blocco | Testo preformattato, conserva spazi e a capo | Contenuto di `<pre><code>` |
| `<blockquote>` | blocco | Citazione lunga o estratto. Supporta l'attributo `cite` con la fonte | Citazione estesa, con `<p>` all'interno |
| `<q>` | inline | Citazione breve. Il browser aggiunge le virgolette | Citazione dentro un paragrafo |
| `<cite>` | inline | Titolo dell'opera citata (non un generico "fonte") | Titolo di un libro, standard, paper |
| `<abbr title="...">` | inline | Sigla con espansione completa nel `title` | `<abbr title="HyperText Markup Language">HTML</abbr>` |
| `<span>` | inline | Contenitore generico inline, senza semantica | Solo per applicare una classe o un attributo a una porzione di riga |
| `<div>` | blocco | Contenitore generico di blocco, senza semantica | Raggruppamento per layout o stile. **Mai** per testo da leggere |
| `<hr>` | vuoto | Separazione tematica tra sezioni | Un interruptor di argomento, non un bordino decorativo |
| `<br>` | vuoto | Interruzione di riga forzata | Solo dove serve davvero: spezzare il flusso del testo con `<br>` e un errore di layout |
| `<time datetime="...">` | inline | Data o ora leggibile da macchina | `<time datetime="2026-09-26">26 settembre 2026</time>` |

> [!WARNING] `<br>` non e un separatore di blocchi
> I `<br>` sono un residuo della produzione tipografica. Fra due paragrafi si usa `margin` in CSS; per separare sezioni si usa un heading o un `<hr>`. Un testo a pezzi a meta e un difetto di marcatura, non di stile.

---

## IV. Liste

| Elemento | Tipo | Funzione | Quando usarlo |
| :--- | :--- | :--- | :--- |
| `<ul>` | blocco | Lista non ordinata, con marcatori | Insieme di elementi omogenei senza ordine di importanza |
| `<ol>` | blocco | Lista ordinata, con numerazione | Procedura sequenziale, ordine di priorita |
| `<li>` | blocco | Voce di lista | Figlio diretto di `<ul>` o `<ol>`. Ogni voce puo contenere una lista annidata |
| `<dl>` | blocco | Lista di descrizione: coppie termine-definizione | Glossari, elenchi di parametri, schede di configurazione |
| `<dt>` | blocco | Termine definito in una `<dl>` | Il nome della chiave, il nome del parametro |
| `<dd>` | blocco | Definizione che descrive il `<dt>` | La descrizione, il tipo, il valore predefinito |

> [!EXAMPLE] Annidamento
> La sotto-lista va dentro il `<li>` che la introduce, non come `<li>` sorella:
> ```html
> <ul>
>   <li>Primo Anno
>     <ul>
>       <li>Programmazione I</li>
>     </ul>
>   </li>
> </ul>
> ```
> Il CSS annidato con selettori figli (`ul > li`) e questo vantaggio a sfruttare.

---

## V. Link, Immagini e Figure

| Elemento | Tipo | Funzione | Attributi chiave |
| :--- | :--- | :--- | :--- |
| `<a>` | inline | Collegamento ipertestuale, l'ancora | `href` (obbligatorio), `target`, `rel="noopener"`, `title`, `download` |
| `<img>` | inline vuoto | Immagine informativa: entra nel flusso del documento, e leggibile dagli screen reader | `src` (obbligatorio), `alt` (obbligatorio), `width`, `height`, `loading` |
| `<figure>` | blocco | Contenitore autonomo di un contenuto illustrato, con didascalia | `class` |
| `<figcaption>` | blocco | Didascalia di `<figure>` o `<picture>` | deve essere **primo o ultimo** figlio di `<figure>` |
| `<picture>` | blocco | Fornisce immagini alternative per formato e densita di pixel | `srcset`, `sizes` |
| `<source>` | vuoto | Risorsa alternativa per `<picture>` o `<video>` | `srcset`, `type`, `media` |

> [!IMPORTANT] `alt` dice *cosa* mostra, `src` dice *dove* si trova
> `alt="mojito.png"` non serve a nessuno. `alt="Coppa di mojito con fette di lime e foglie di menta"` descrive l'informazione. Immagine puramente decorativa: `alt=""`, vuoto, e non un testo fittizio.

### Regola di scelta: contenuto o decorazione

| Vuoi mostrare | Usa | Perche |
| :--- | :--- | :--- |
| Foto di un prodotto, grafico, avatar, screenshot | `<img>` con `alt` | L'informazione e nel contenuto: deve essere letta, indicizzata, stampata |
| Sfondo di sezione, texture, banner astratto, icona decorativa | `background-image` in CSS | Non trasmette informazione: e solo cornice |

---

## VI. Tabelle

| Elemento | Funzione | Note |
| :--- | :--- | :--- |
| `<table>` | Tabella di dati | Solo per dati tabellari, mai per impaginare il layout |
| `<caption>` | Didascalia della tabella | Figlio diretto di `<table>`, prima di `<thead>` |
| `<thead>` | Riga di intestazioni | Raggruppa la/le righe di `<th>` |
| `<tbody>` | Corpo dei dati | Obbligatorio: il parser lo aggiunge se manca, ma scrivilo |
| `<tfoot>` | Riga di totals | Opzionale, sotto al corpo |
| `<tr>` | Riga | |
| `<th>` | Cella di intestazione | Con `scope="col"` o `scope="row"` per dichiarare cosa descrive |
| `<td>` | Cella di dato | |

```html
<table>
  <caption>Chiavi riconosciute in config.json</caption>
  <thead>
    <tr>
      <th scope="col">Chiave</th>
      <th scope="col">Tipo</th>
      <th scope="col">Predefinito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>editor</code></td>
      <td>stringa</td>
      <td><code>vim</code></td>
    </tr>
  </tbody>
</table>
```

| Attributo | Funzione |
| :--- | :--- |
| `scope="col"` | L'intestazione descrive la colonna sottostante |
| `scope="row"` | L'intestazione descrive la riga che segue |
| `colspan="n"` | La cella si estende su `n` colonne |
| `rowspan="n"` | La cella si estende su `n` righe |

> [!EXAMPLE] Perche `scope` conta
> Uno screen reader che incontra la cella "stringa" annuncia solo "stringa", senza sapere a cosa si riferisce. Con `scope="col"` annuncia "Tipo: stringa": il contesto arriva dal markup, non dall'occhio di chi ascolta.

---

## VII. Elementi Vuoti (Void)

Nessun tag di chiusura, nessun contenuto interno. **Tutta** l'informazione e codificata negli attributi.

| Tag | Attributi obbligatori | Funzione |
| :--- | :--- | :--- |
| `<img>` | `src`, `alt` | Immagine del contenuto |
| `<input>` | `type` (ha default `text`) | Campo di input, comportamento definito da `type` |
| `<link>` | `rel`, `href` | Collegamento a risorsa esterna |
| `<meta>` | `name` + `content`, oppure `charset` | Metadato del documento |
| `<br>` | nessuno | Interruzione di riga |
| `<hr>` | nessuno | Separazione tematica |
| `<area>` | `alt` | Area clicabile dentro una mappa immagine |
| `<source>` | `srcset`/`src` | Risorsa alternativa |
| `<embed>`, `<track>`, `<wbr>`, `<col>`, `<param>`, `<base>` | vari | Casi rari |

> [!WARNING] `<img></img>` non e un errore che ti segnala il browser
> Il parser HTML non segnala niente: chiude l'elemento vuoto al primo `>` e tutto il resto della pagina finisce nel `<body>. Un `<br>` di troppo sposta l'intero layout senza alcun messaggio in console.

---

## VIII. Moduli (Form)

| Elemento | Funzione | Attributi chiave |
| :--- | :--- | :--- |
| `<form>` | Contenitore di un modulo, definisce l'invio dei dati | `action`, `method`, `name` |
| `<label>` | Etichetta di un campo, collegata al campo con `for` | `for` (deve corrispondere all'`id` del campo) |
| `<input>` | Campo di input monolinea | `type`, `name`, `value`, `placeholder`, `required` |
| `<textarea>` | Campo di testo su piu righe | `name`, `rows`, `cols`, `placeholder` |
| `<select>` | Menu a tendina | `name`, `multiple`, `size` |
| `<option>` | Voce di un `<select>` | `value`, `selected` |
| `<button>` | Pulsante azionabile | `type="submit"`, `type="button"`, `disabled` |
| `<fieldset>` | Raggruppa controlli correlati | `disabled` |
| `<legend>` | Titolo di un `<fieldset>` | primo figlio del fieldset |
| `<output>` | Valore calcolato o risultato | `for` |

> [!IMPORTANT] `placeholder` non e un'etichetta
> Il placeholder sparisce appena l'utente scrive, ed e invisibile agli screen reader e alla stampa. Il nome del campo va sempre in un `<label for="...">`.

---

## IX. Attributi Globali

| Attributo | Funzione | Nota |
| :--- | :--- | :--- |
| `id` | Identificatore univoco nel documento | Minuscolo. Usalo per gli ancoraggi `#id` e per i selettori CSS ad alta specificita |
| `class` | Classificazione riutilizzabile su piu elementi | Preferiscila per lo stile: `id` per l'unicita, `class` per il layout |
| `title` | Tooltip e, su `<abbr>`, espansione della sigla | Non sostituisce `alt` |
| `lang` | Lingua del contenuto | Anche per un singolo parola straniero |
| `dir` | Direzione del testo: `ltr` o `rtl` | |
| `hidden` | Nasconde l'elemento | Equivalente a `display: none` |
| `tabindex` | Ordine di tabulazione | `0` lo rende raggiungibile, `-1` lo esclude |
| `data-*` | Dati personalizzati leggibili da JavaScript | `data-active="true"` |
| `aria-*` | Stato accessibile per le tecnologie assistive | `aria-live="polite"`, `aria-label` |

### Attributi vietati: di presentazione

`align`, `bgcolor`, `background`, `border` (sulle tabelle), `width` e `height` (sugli elementi non vuoti), `cellpadding`, `cellspacing`, `font`, `color`, `text`, `valign`, `hspace`, `vspace`.

> [!WARNING] Sono deprecati dallo standard HTML5 e non fanno nulla
> Non funzionano, e il browser li ignora. Se la tua pagina non e allineata, il motivo non e un attributo mancante: e una regola CSS che non hai ancora scritto.

---

## X. Blocchi, Inline e Inline sostituito

| Categoria | Comportamento | Elementi |
| :--- | :--- | :--- |
| **Blocco** | Inizia su una nuova riga, occupa tutta la larghezza disponibile | `<div>`, `<p>`, `<h1>`-`<h6>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<nav>`, `<aside>`, `<main>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<figure>`, `<blockquote>`, `<pre>` |
| **Inline** | Resta sulla riga corrente, occupa solo lo spazio del contenuto | `<span>`, `<a>`, `<strong>`, `<em>`, `<code>`, `<q>`, `<abbr>`, `<time>` |
| **Inline sostituito** | Inline, ma con dimensioni e contenuto propri | `<img>`, `<input>`, `<select>`, `<textarea>`, `<button>`, `<svg>`, `<video>`, `<canvas>`, `<iframe>` |
| **Vuoto** | Inline sostituito senza contenuto interno | `<img>`, `<input>`, `<br>`, `<hr>` |

> [!EXAMPLE] I tre elementi inline che si comportano come blocchi
> `width`, `height`, `margin` verticali e `padding` verticali **non si applicano** agli elementi inline. Ecco perche `vertical-align: top` e necessario su un `inline-block`: senza, i tre elementi si allineano per la loro baseline e risultano storti.
> ```css
> .card {
>   display: inline-block;
>   width: 33.33%;
>   vertical-align: top;
> }
> ```

---

## XI. Proprieta CSS per Funzione

### 11.1 Box Model

| Proprieta | Funzione | Valori comuni |
| :--- | :--- | :--- |
| `box-sizing` | Include padding e border nella `width` dichiarata | `border-box`, `content-box` (default) |
| `width` / `height` | Dimensione dell'area di contenuto | `px`, `%`, `auto`, `max-width` |
| `max-width` / `min-width` | Vincolo massimo o minimo | `960px`, `100%` |
| `padding` | Spazio interno, interno al bordo. Assume il colore di sfondo | `10px 20px` (verticale, orizzontale), `1rem 1.5rem 2rem` |
| `border` | Bordo, shorthand di `width style color` | `1px solid #e0e0e0` |
| `border-radius` | Arrotondamento degli angoli | `8px`, `50%` |
| `margin` | Spazio esterno, esterno al bordo | `0 auto` per centrare in orizzontale |
| `overflow` | Comportamento quando il contenuto eccede | `hidden`, `auto`, `scroll` |

### 11.2 Flusso e Posizionamento

| Proprieta | Funzione | Valori comuni |
| :--- | :--- | :--- |
| `display` | Modo di rendering dell'elemento | `block`, `inline`, `inline-block`, `none` |
| `float` | Estrae l'elemento dal flusso normale e lo alza a sinistra o a destra | `left`, `right`, `none` |
| `clear` | Consente a un elemento di scendere sotto i float precedenti | `both`, `left`, `none` |
| `vertical-align` | Allineamento verticale degli elementi inline | `top`, `middle`, `baseline` |
| `position` | Modalita di posizionamento | `static`, `relative`, `absolute`, `fixed`, `sticky` |
| `top` / `right` / `bottom` / `left` | Scostamento dalla posizione di riferimento | `0`, `10px`, `50%` |
| `z-index` | Ordine di sovrapposizione | `1`, `10`, `999` |

### 11.3 Tipografia e Colore

| Proprieta | Funzione | Valori comuni |
| :--- | :--- | :--- |
| `font-family` | Famiglie tipografiche, in ordine di preferenza con fallback | `'Helvetica Neue', Arial, sans-serif` |
| `font-size` | Dimensione del carattere | `1rem`, `100%`, mai `px` |
| `font-weight` | Spessore | `normal`, `bold`, `100`-`900` |
| `font-style` | Inclinazione | `normal`, `italic` |
| `line-height` | Altezza di riga | `1.6` (numero puro) |
| `letter-spacing` | Spaziatura fra le lettere | `0.05em`, `1px` |
| `text-align` | Allineamento orizzontale | `left`, `center`, `right`, `justify` |
| `text-decoration` | Linee di decorazione | `none`, `underline`, `line-through` |
| `text-transform` | Trasformazione del casing | `uppercase`, `capitalize`, `none` |
| `white-space` | Gestione degli spazi e dei ritorni a capo | `normal`, `pre` |
| `color` | Colore del testo | `#2b2b2b`, `rgb(43,43,43)`, `hsl(0,0%,17%)` |

### 11.4 Liste

| Proprieta | Funzione | Valori comuni |
| :--- | :--- | :--- |
| `list-style-type` | Tipo di marcatore | `disc`, `circle`, `square`, `decimal`, `lower-alpha`, `none` |
| `list-style-image` | Marcatore personalizzato | `url('bullet.png')` |
| `list-style-position` | Posizione del marcatore | `outside`, `inside` |
| `list-style` | Shorthand dei tre precedenti | `none`, `square inside` |

### 11.5 Background

| Proprieta | Funzione | Valori comuni |
| :--- | :--- | :--- |
| `background-color` | Colore di sfondo | `#f4f4f4`, `transparent` |
| `background-image` | Immagine di sfondo | `url('banner.png')`, `linear-gradient(...)` |
| `background-repeat` | Ripetizione | `no-repeat`, `repeat-x` |
| `background-position` | Posizione nell'area | `center`, `top left`, `50% 50%` |
| `background-size` | Ridimensionamento | `cover` (copre e ritaglia), `contain` (adatta senza ritagliare), `100% auto` |
| `background-attachment` | Scorrimento dello sfondo | `scroll`, `fixed` |
| `background` | Shorthand di tutte | `url('x.png') center / cover no-repeat` |

### 11.6 Transizione di Stato

| Proprieta | Funzione | Quando usarla |
| :--- | :--- | :--- |
| `display: none` | Rimuove l'elemento dal flusso e dal layout | Nascondere un elemento (classe `.is-hidden`) |
| `visibility: hidden` | Nasconde l'elemento ma **conserva lo spazio** | Quando lo spazio deve restare |
| `opacity` | Trasparenza, da `0` a `1` | Animazioni e sfondi semitrasparenti |

---

## XII. Selettori e Combinatori

### 12.1 Selettori di Base

| Selettore | Funzione | Valore specificita |
| :--- | :--- | :---: |
| `*` | Tutti gli elementi | 0 |
| `p` | Per tag | 1 |
| `.classe` | Per classe, riutilizzabile | 10 |
| `#id` | Per id, unico nel documento | 100 |
| `a[href^="http"]` | Per attributo: inizia con, contiene `[*=]`, uguale `[=]`, termina con `[$=]` | 10 |
| `:hover`, `:focus`, `:first-child`, `:last-child`, `:not(...)` | Pseudo-classe: stato o posizione | 10 |

### 12.2 Combinatori

| Combinatore | Funzione |
| :--- | :--- |
| `div, p` | Lista di selettori: entrambi |
| `div p` | Discendente: qualunque `<p>` dentro un `<div>`, a qualsiasi profondita |
| `div > p` | Figlio diretto: solo i `<p>` figli immediati |
| `div + p` | Fratello adiacente: il primo `<p>` subito dopo il `<div>` |
| `div ~ p` | Fratello generale: tutti i `<p>` che seguono il `<div>`, con lo stesso genitore |

### 12.3 Calcolo della Specificita

$$\text{Valore} = a \cdot 1000 + b \cdot 100 + c \cdot 10 + d$$

| Selettore | `(a, b, c, d)` | Valore |
| :--- | :--- | :---: |
| `p` | (0, 0, 0, 1) | 1 |
| `.card p` | (0, 0, 1, 1) | 11 |
| `ul.menu > li a` | (0, 0, 1, 3) | 13 |
| `#main-header h1` | (0, 1, 0, 1) | 101 |
| `style="..."` inline | (1, 0, 0, 0) | 1000 |

`a` stili inline, `b` ID, `c` classi, attributi e pseudo-classi, `d` tag e pseudo-elementi.

---

## XIII. Errori Frequenti

| Errore | Conseguenza | Correzione |
| :--- | :--- | :--- |
| `<div>` al posto di `<section>`, `<nav>`, `<article>` | Il layout funziona, la semantica no | Usa il landmark che descrive il ruolo del contenuto |
| `style="..."` dentro l'HTML | Annulla la separazione delle responsabilita | Sposta la regola nel foglio esterno |
| `!important` per vincere un conflitto | Foglio di stile incontrollabile | Rivedi il selettore: quasi sempre la specificita si risolve con `class` e combinatori |
| `<br>` fra i paragrafi | Testo impaginato a pezzi | `margin` in CSS |
| `alt` copia-incolla dal nome del file | L'immagine non e descritta | Scrivi cosa mostra, in una frase |
| `id` usato come hook di stile | Specificita da 100 su elementi ripetibili | Usa `class` per lo stile, `id` solo per l'unicita e gli ancoraggi |
| `font-size` in `px` | Non scala con le preferenze dell'utente | `rem` |
| `em` sui font-size di liste annidate | Crescita esponenziale a ogni livello | `rem` per i font, `em` solo per spaziature interne |
| `box-sizing: border-box` in fondo al foglio | Non si applica a nessuna regola precedente | Mettilo in cima, prima di ogni altra regola |
| Elementi inline-block affiancati senza `vertical-align: top` | Le colonne risultano disallineate | `vertical-align: top` |
| `<table>` per il layout | Struttura semantica falsata | Layout con blocchi, inline e float |
| `</br>`, `</img>`, `</input>` | Errori silenziosi, il parser li scarta | I tag vuoti non hanno chiusura |
| `<h2>` seguito da `<h4>` | Gerarchia degli heading interrotta | Scendi di un livello alla volta |

---

## XIV. Checklist di Validazione di un Documento

```bash
# Nessuno stile inline
grep -n 'style=' index.html
# Nessun attributo di presentazione deprecato
grep -n 'align=\|bgcolor=\|cellpadding=\|cellspacing=' index.html
# Nessun !important nel CSS
grep -c '!important' css/style.css
# Ogni img ha un alt
grep -o '<img[^>]*>' index.html | grep -vc 'alt='
# Un solo h1
grep -c '<h1' index.html
# Nessun font-size in px
grep -n 'font-size:.*px' css/style.css
# Nessun layout flex/grid se non ancora trattato
grep -n 'display:.*flex\|display:.*grid' css/style.css
```

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Programmazione_Web]]
- **Teoria correlata :** [[02_HTML5_e_CSS3_Fondamenti_e_Box_Model]]
- **Progetto :** [[project_devnotes/index.html]]
