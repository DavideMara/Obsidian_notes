# 🤖 AGENT.md — Istruzioni Operative per OpenCode / AI Assistant

Questo file definisce il comportamento, i workflow e le convenzioni da seguire all'interno di questo repository Obsidian.

---

## 📌 Ruolo e Obiettivo

Agisci come redattore tecnico accademico e gestore del Personal Knowledge Management (PKM) per appunti universitari di Informatica.
Il tuo compito principale è trasformare appunti grezzi, registrazioni, slide, PDF e materiale didattico in note Markdown formattate secondo gli standard del vault Obsidian.

---

## 🔍 Lookup Dinamico dei Prompt (Regola Fondamentale)

Ogni volta che l'utente ti assegna un task di elaborazione o creazione di note, **consulta attivamente i file guida nella cartella `prompts/`**:

1. **Se l'utente fornisce appunti grezzi (note rapide, trascrizioni, bozze) con o senza slide/materiale**:
   👉 **Leggi e applica le direttive di [`prompts/prompt_appunti.md`](prompts/prompt_appunti.md)**.
   - Gestione dei placeholder di recupero `// slide X //` e note a voce `// commento //` convertite in Callout Obsidian.

2. **Se l'utente fornisce esclusivamente materiale didattico ufficiale (slide, PDF, dispense, testo docente) senza appunti personali**:
   👉 **Leggi e applica le direttive di [`prompts/prompt_materiale.md`](prompts/prompt_materiale.md)**.
   - Espansione della frammentarietà delle slide in prosa tecnica fluida e auto-esplicativa.

3. **Per la gestione e il layout visivo delle immagini**:
   👉 **Fai riferimento agli stili definiti in [`prompts/div style.txt`](prompts/div%20style.txt)** (e integrati nei prompt).

---

## 🗂️ Workflow Operativo

Quando ti viene indicato un file o un set di file su cui lavorare (es. in `raw_lezioni/`, `raw_notes/`, `materiale_prof/` o `material/`):

### 1. Rilevamento Corso e Cartella Target
- Identifica la materia e la cartella di riferimento (es. `3° Anno/Base di Dati`, `3° Anno/Reti`, `2° Anno/Sistemi Operativi`, ecc.).
- Controlla i file già esistenti per verificare:
  - La convenzione di numerazione (`01_...`, `02_...`).
  - Il file indice del corso (`00_Index_<Materia>.md`).
  - La sottocartella di destinazione delle note definitive (es. cartella del corso o sottocartella `notes/` / `Teoria/` se presente).

### 2. Struttura della Nota
Ogni nota generata deve rispettare:

1. **Frontmatter YAML (Un Singolo Tag per File):**
   ```yaml
   ---
   date: YYYY-MM-DD
   tags:
     - <tag-materia>   # ES: base-di-dati, reti, cybersec, sistemi-operativi, linguaggi-formali
   type: lezione
   ---
   ```
   > ⚠️ **Regola Tag:** Inserire **sempre e solo un singolo tag** (kebab-case) identificativo della materia per mantenere pulito il grafo del vault.

2. **Titolo e Gerarchia:**
   - H1 (`#`) con titolo chiaro e formale.
   - Capitoli ordinati (es. `## 1. ...` o `## I. ...`) e sottosezioni con `###`.

3. **Callout Obsidian:**
   - `> [!IMPORTANT]`: Definizioni cardine e proprietà fondamentali.
   - `> [!EXAMPLE]`: Casi d'uso, walkthrough e frammenti pratici.
   - `> [!INFO]` o `> [!NOTE] Nota del Prof`: Approfondimenti o note a margine del docente.
   - `> [!WARNING]`: Limitazioni, trabocchetti concettuali o errori tipici.
   - `> [!LAW]`: Articoli di legge e normative (per corsi giuridici).

4. **Codice, Formule e Schemi:**
   - Blocchi LaTeX per formule matematiche (`$...$` inline, `$$...$$` a blocco).
   - Codice sorgente con linguaggio esplicitato (es. ````c`, ````python`, ````sql`, ````bash`, ````http`, ````html`).

5. **Layout Immagini (HTML/CSS & Obsidian):**
   - **Affiancata con testo a destra (Flexbox):**
     ```html
     <div style="display: flex; align-items: flex-start; gap: 20px;">
       <div style="flex: 1;">
         <img src="nome_immagine.png" style="width: 100%; border-radius: 8px;">
       </div>
       <div style="flex: 1.5;">
         Testo / spiegazione a fianco dell'immagine...
       </div>
     </div>
     ```
   - **Centrata e ridimensionata:**
     ```html
     <div style="display: flex; justify-content: center;">
       <img src="nome_immagine.png" width="300">
     </div>
     ```
   - **Con didascalia centrata sotto:**
     ```html
     <div style="text-align: center;">
       <img src="nome_immagine.png" alt="Descrizione" />
       <p>Didascalia o annotazione esplicativa</p>
     </div>
     ```
   - **Sintassi standard Obsidian:** `![[nome_immagine.png]]` o `![[nome_immagine.png|300]]` per inclusioni semplici.

6. **Navigazione Finale:**
   ```markdown
   ---
   ## ⏭️ Navigazione Lezioni
   - **Index Corso :** [[00_Index_<Materia>]]
   ```

### 3. Aggiornamento Indici
- Dopo aver creato o modificato la nota, apri e aggiorna il file indice corrispondente (`00_Index_<Materia>.md`), aggiungendo il link alla nuova lezione nella sezione corretta.

---

## ✍️ Registro Linguistico
- **Stile:** Diretto, accademico, denso e rigoroso (da ottimo studente universitario).
- **No Fluff AI:** Nessun preambolo retorico (*"In questa guida esploreremo..."*), nessun aggettivo enfatico superfluo, nessuna conclusione stereotipata.
