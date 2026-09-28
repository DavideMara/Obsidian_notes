---
date: 2026-09-28
tags:
  - programmazione-web
type: esercizi
---
# Esercizi e Domande per Casa - Programmazione Web

Registro delle consegne del corso. Ogni lezione aggiunge una sezione con i propri esercizi; la tabella in testa fa da checklist di avanzamento. Gli esercizi pratici gia svolti e consegnati si trovano come codice nella cartella `exercises/`.

- [[#Registro Consegne]]
- [[#Lezione 03 - Tabelle e Form (28/09/2026)]]
  - [[#E.1 - Sito Web a Tre Pagine]]

---

## Registro Consegne

| # | Consegna | Lezione | Scadenza | Stato |
|---|---|---|---|---|
| [E.1](#E.1%20-%20Sito%20Web%20a%20Tre%20Pagine) | Sito web a tre pagine (home, tabella, form) | Lez. 03 | Giovedi | Da fare |

**Esercizi pratici gia archiviati in `exercises/`:**

| Cartella | Contenuto |
|---|---|
| `exercises/first_test/` | Prima verifica: struttura della pagina, collegamento CSS e JS |
| `exercises/esc_civetta/` | Esercizio su liste e immagini |
| `exercises/esc_liste/` | Esercizio sulle liste |
| `exercises/es_skywalker/` | Esercizio su selettori, combinatori e immagini |
| `exercises/project_devnotes/` | progetto DevNotes, portale di documentazione |

---

# Lezione 03 - Tabelle e Form (28/09/2026)

Materiale di riferimento: [[03_Tabelle_Form_e_Invio_Dati]] (Tabelle, Form e ripasso del Box Model). Consegnare entro **giovedi**.

## E.1 - Sito Web a Tre Pagine

*Riferimento: [[03_Tabelle_Form_e_Invio_Dati#IV. Tabelle|IV. Tabelle]] e [[03_Tabelle_Form_e_Invio_Dati#V. Form|V. Form]]*

**Consegna.** Realizzare un sito web di tre pagine:

1. una **home** con la presentazione generale dei contenuti;
2. una pagina con una **tabella** e qualche **immagine**;
3. una terza pagina con una **form**, scelta tra quelle proposte in fondo alla slide 13 della lezione 3.

Le tre pagine devono condividere lo stesso foglio di stile. Vanno usate le proprietà e i tag visti fino ad ora, e in particolare la gestione del **Box Model** (`padding`, `margin`, `border`, `border-radius`) per la spaziatura e la cornice degli elementi.

### Requisiti per pagina

| Pagina | Contenuto richiesto | Punti da curare |
|---|---|---|
| `index.html` | Home con presentazione dei contenuti | Struttura semantica, gerarchia degli heading senza salti, navigazione fra le tre pagine |
| `tabella.html` | Una tabella e qualche immagine | `<caption>`, `<thead>`/`<tbody>`, `colspan` o `rowspan`, `border-collapse: collapse`, `<img>` con `alt` |
| `form.html` | Una form fra quelle proposte in slide 13 | `<label for>` collegato a ogni `id`, `name` su ogni controllo, tipi di input appropriati, `<select>` o `<datalist>`, pulsante di invio |

### Criteri di valutazione

La logica e quella del contest della lezione 2 (`pwm_lezione2.pdf`, pagina 44): correttezza della pagina HTML e del foglio CSS, e presentazione con aspetto grafico.

In concreto, le checklist da rispettare:

```html
<!-- Struttura -->
ogni documento ha <!DOCTYPE html>, lang="it", meta charset, meta viewport
un solo <h1> per pagina, nessun salto di livello negli heading
le tre pagine sono collegate con <nav> e <a href>

<!-- Tabelle -->
border-collapse: collapse impostato
border e padding espliciti sulle celle (td, th)
nessun <table> usato per il layout: solo per dati tabellari

<!-- Immagini -->
ogni <img> ha src e alt
alt descrittivo, non il nome del file

<!-- Form -->
ogni controllo ha un <label for> che punta al suo id
ogni controllo ha un name (senza, il dato non viene inviato)
nessun uso di placeholder al posto della label
un pulsante di invio

<!-- CSS -->
tutti gli stili in un foglio .css collegato, nessuno stile inline
nessun attributo di presentazione (bgcolor, align, border="1")
spaziature gestite con padding e margin, non con spazi nel testo
nessun !important
```

> [!WARNING] Errori che costano piu punti
> I tre piu frequenti, tutti invisibili a schermo e silenziosi in console:
> * **`<table>` per il layout.** Falsifica la semantica, confonde gli screen reader e spacca il flusso del documento.
> * **Placeholder al posto della label.** Sparisce al primo carattere digitato, ed e invisibile agli screen reader e alla stampa.
> * **Dimenticare `border-collapse: collapse`.** Senza, la tabella si presenta con un reticolo a linee doppie, che e l'effetto di default e quasi sempre non voluto.

> [!EXAMPLE] Ordine di lavoro consigliato
> 1. Costruisci la struttura semantica della home senza stile, verifica che il contenuto si legga in ordine.
> 2. Crea il foglio di stile con reset e Box Model, applicalo, poi affina le spaziature.
> 3. Passa alla pagina tabella, partendo dal markup e aggiungendo il CSS dopo.
> 4. Chiudi con la form, verificando in devtools (pannello Network) che i campi arrivino con i nomi attesi.
> 5. Ultimo passo: rileggi l'HTML verificando che non ci siano stili inline e attributi di presentazione.

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Programmazione_Web]]
- **Teoria di riferimento :** [[03_Tabelle_Form_e_Invio_Dati]]
