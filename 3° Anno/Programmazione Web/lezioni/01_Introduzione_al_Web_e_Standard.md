---
date: 2026-09-21
tags:
  - programmazione-web
type: lezione
---
# Introduzione al Web, Architetture e Standard (HTML, HTTP, URL)

> [!INFO] Informazioni sul Corso e Modalità d'Esame
> * **Docente:** Carlo Taticchi
> * **Email:** `carlo.taticchi@unipg.it`
> * **Pagina Web:** [www.carlotaticchi.it](https://www.carlotaticchi.it)
> * **Ricevimento:** Su appuntamento.
> * **Modalità d'Esame:**
>   * **Progetto Pratico:** Da concordare con il docente, svolto obbligatoriamente in modalità **singola** (nessun gruppo di lavoro). Il completamento del progetto è vincolante per l'ammissione all'orale.
>   * **Prova Orale:** Discussione critica del progetto realizzato e verifica delle conoscenze teoriche sull'intero programma del corso.

---

## I. Il World Wide Web e gli Standard Fondamentali

Il **World Wide Web (WWW)** è un servizio applicativo distribuito operante sull'infrastruttura di Internet, concepito per consentire la navigazione, la condivisione e la fruizione di risorse eterogenee collegate tramite **ipertesti** (documenti contenenti rimandi e collegamenti bidirezionali ad altre risorse informative).

```
                      ┌─────────────────────────────────────────┐
                      │          WORLD WIDE WEB (WWW)           │
                      └────────────────────┬────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐             ┌──────────────────┐
│       HTML       │             │       HTTP       │             │       URL        │
│ Struttura dei    │             │ Protocollo di    │             │ Identificazione  │
│ Documenti Web    │             │ Comunicazione    │             │ Univoca Risorse  │
└──────────────────┘             └──────────────────┘             └──────────────────┘
```

I tre pilastri architetturali del Web sono:
* **HTML (HyperText Markup Language):** Linguaggio di markup standard per la definizione strutturale e semantica delle pagine web.
* **HTTP (HyperText Transfer Protocol):** Protocollo di comunicazione di livello applicativo per lo scambio efficiente di messaggi client-server.
* **URL (Uniform Resource Locator):** Schema globale e univoco di indirizzamento e localizzazione delle risorse in rete.

### 1. HTML (HyperText Markup Language)
* Standardizzato dal **W3C (World Wide Web Consortium)** per garantire uniformità e interoperabilità multipiattaforma.
* Definisce la gerarchia semantica dei contenuti (testi, immagini, collegamenti, form) interpretata dai motori di rendering.
* L'ultima raccomandazione formale dello standard è **HTML 5.3** (rilasciata il 28 gennaio 2021).

### 2. Il Browser Web
Il **Browser** è l'applicazione client responsabile dell'acquisizione, interpretazione, composizione visiva e navigazione delle risorse web:
* Agisce come **client HTTP**, traducendo le interazioni dell'utente (click, digitazione URL) in richieste di rete verso i server web remoti.
* Costruisce e mantiene l'albero **DOM (Document Object Model)** parsando il markup HTML e combinandolo con le regole di stile **CSS** e la logica **JavaScript**.
* L'ecosistema attuale presenta un'elevata uniformità di conformità agli standard W3C ed ECMAScript tra i principali vendor (con Google Chrome che detiene la quota di mercato prevalente).

---

## II. Architettura Client-Server nel Web

Il Web è strutturato secondo il paradigma architetturale **Client-Server**:

```
 ┌──────────────┐                                ┌──────────────┐
 │    Client    │────── HTTP Request (URL) ─────>│    Server    │
 │  (Browser)   │<───── HTTP Response (HTML) ────│ (Always-On)  │
 └──────────────┘                                └──────────────┘
```

* **Client:** Dispositivi eterogenei (computer desktop, smartphone, tablet, Smart TV) che avviano le sessioni di comunicazione inviando query e richieste puntuali per recuperare o modificare dati.
* **Server:** Macchine dedicate ad alta affidabilità, tipicamente operanti in modalità *always-on*, preposte alla centralizzazione delle risorse, all'elaborazione della logica di business, alla memorizzazione persistente su database e al controllo degli accessi.

---

## III. Il Protocollo HTTP (HyperText Transfer Protocol)

**HTTP** è un protocollo di livello applicativo (nello stack ISO/OSI e TCP/IP) basato su uno schema a scambio di messaggi di tipo **Request-Response**.

### 1. Livello di Trasporto e Sicurezza
* **TCP (Transmission Control Protocol):** HTTP si appoggia sul protocollo TCP per garantire un canale di trasporto bidirezionale affidabile, orientato alla connessione, con consegna ordinata e priva di errori dei pacchetti (*three-way handshake*).
* **TLS (Transport Layer Security - HTTPS):** Cifra il canale di trasporto tra client e server, garantendo confidenzialità, autenticità e integrità dei dati.

> [!WARNING] Rischio di Sicurezza Pre-HTTPS: Man-in-the-Middle (MitM)
> Nelle comunicazioni HTTP in chiaro (porta 80), pacchetti non cifrati possono essere facilmente intercettati, manipolati o falsificati da nodi intermedi malevoli (*attacco Man-in-the-Middle*). L'adozione di TLS/HTTPS (porta 443) è oggi lo standard obbligatorio per proteggere credenziali e payload sensibili, pur introducendo un costo computazionale aggiuntivo per l'handshake crittografico.

### 2. Funzionalità Avanzate del Protocollo
* **Caching:** Memorizzazione locale o intermedia di risposte statiche per abbattere la latenza e ridurre il consumo di banda.
* **CORS (Cross-Origin Resource Sharing):** Meccanismo di sicurezza che consente a un server di specificare quali origini esterne (domini, schemi o porte) sono autorizzate ad accedere alle sue risorse tramite richieste asincrone.
* **Autenticazione:** Negoziazione di credenziali tramite header dedicati (`Authorization`, Bearer Token, Basic Auth).
* **Proxy & Gateway:** Nodi intermedi usati per routing, bilanciamento del carico, filtro di sicurezza e ispezione dei pacchetti.
* **Sessioni:** Mantenimento dello stato applicativo continuo attraverso scambi successivi.

> [!IMPORTANT] Natura Stateless di HTTP e Gestione dello Stato
> HTTP è un protocollo intrinsecamente **stateless** (privo di stato): ciascuna coppia richiesta-risposta è completamente indipendente e il server non conserva memoria delle interazioni precedenti.
> * **Soluzione Applicativa:** Per gestire l'autenticazione persistente, carrelli elettronici e preferenze, si impiegano i **Cookie** (piccole stringhe di testo inviate dal server via header `Set-Cookie` e ritrasmesse automaticamente dal client via header `Cookie`) oppure token di sessione (es. JWT).

---

## IV. Struttura dei Messaggi HTTP: Richiesta e Risposta

### 1. Richiesta HTTP (HTTP Request)
Una richiesta HTTP è composta da quattro parti fondamentali:
1. **Request Line:** Specifica il **Metodo**, il **Path (URI)** della risorsa e la **Versione del Protocollo**.
2. **Headers:** Coppie chiave-valore contenenti metadati sul client, codifiche supportate, cookie e host.
3. **Linea Vuota:** Separatore obbligatorio (`\r\n`) tra header e payload.
4. **Body (opzionale):** Payload contenente dati inviati al server (es. JSON in chiamate API o dati di form).

```http
POST /api/v1/users HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64)
Content-Type: application/json
Content-Length: 42

{"username": "mario_rossi", "role": "admin"}
```

#### Tassonomia dei Metodi HTTP: Sicurezza e Idempotenza
* **Metodo Sicuro (Safe):** Un metodo si definisce *sicuro* se la sua esecuzione è di sola lettura e non altera lo stato delle risorse sul server.
* **Metodo Idempotente (Idempotent):** Un metodo si definisce *idempotente* se l'effetto prodotto sul server dall'esecuzione di $N \ge 1$ richieste identiche consecutive è esattamente equivalente a quello di una singola richiesta.

| Metodo HTTP | Scopo Principale | Sicuro? | Idempotente? |
| :--- | :--- | :---: | :---: |
| **`GET`** | Recupero in sola lettura di una risorsa | **Sì** | **Sì** |
| **`HEAD`** | Recupera solo gli header identici a una `GET` | **Sì** | **Sì** |
| **`OPTIONS`**| Interroga i metodi/capacità supportati dal server | **Sì** | **Sì** |
| **`TRACE`** | Esegue un loop-back diagnostico lungo la rotta | **Sì** | **Sì** |
| **`PUT`** | Sostituzione completa o creazione di una risorsa | **No** | **Sì** |
| **`DELETE`** | Eliminazione della risorsa specificata | **No** | **Sì** |
| **`POST`** | Invio di dati da elaborare (creazione entità) | **No** | **No** |
| **`PATCH`** | Modifica parziale di una risorsa esistente | **No** | **No** |
| **`CONNECT`**| Istituisce un tunnel bidirezionale (es. proxy SSL) | **No** | **No** |

### 2. Risposta HTTP (HTTP Response)
Una risposta HTTP è composta da:
1. **Status Line:** Versione del protocollo, **Status Code** (codice numerico a 3 cifre) e **Reason Phrase** testuale.
2. **Headers:** Metadati sulla risposta (tipo MIME del contenuto, lunghezza, policy di caching, impostazione cookie).
3. **Linea Vuota:** Separatore.
4. **Body (opzionale):** La risorsa restituita (documento HTML, immagine binaria, array JSON).

```http
HTTP/1.1 200 OK
Date: Mon, 21 Sep 2026 10:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 156

<!DOCTYPE html>
<html lang="it">
<head><title>Home</title></head>
<body><h1>Benvenuto nel Web!</h1></body>
</html>
```

### 3. Evoluzione delle Versioni di HTTP
* **HTTP/1.1:** Protocollo testuale basato su connessioni persistenti (`Keep-Alive`) e pipeline seriale delle richieste.
* **HTTP/2:** Introduce il multiplexing su singola connessione TCP, la compressione degli header (HPACK) e l'incapsulamento dei messaggi in **frame binari** non leggibili direttamente come testo puro.
* **HTTP/3:** Abbandona TCP in favore di **QUIC** (protocollo di trasporto operante sopra **UDP**), eliminando l'overhead di connessione e il problema del blocco di testa della linea (*Head-of-Line Blocking* a livello di trasporto).

---

## V. Struttura dell'URL e Risoluzione DNS

### 1. Anatomia di un URL (Uniform Resource Locator)
L'URL identifica univocamente la posizione di una risorsa sulla rete e il protocollo necessario per recuperarla:

$$\underbrace{\text{https}}_{\text{Protocollo / Scheme}} :// \underbrace{\text{www}}_{\text{Sottodominio}} . \underbrace{\text{dmi}}_{\text{2° Livello}} . \underbrace{\text{unipg}}_{\text{Dominio}} . \underbrace{\text{it}}_{\text{TLD}} : \underbrace{\text{443}}_{\text{Porta}} / \underbrace{\text{didattica/corsi}}_{\text{Path (Percorso)}} ? \underbrace{\text{anno=2026\&sem=1}}_{\text{Query String}} \# \underbrace{\text{programma}}_{\text{Fragment / Anchor}}$$

* **Scheme/Protocollo:** Specifica il protocollo di comunicazione (es. `http`, `https`, `ftp`).
* **Host / Fully Qualified Domain Name (FQDN):**
  * *Top-Level Domain (TLD):* Suffisso di primo livello (es. `.it`, `.org`, `.com`).
  * *Dominio di secondo livello:* Nome registrato dell'organizzazione (es. `unipg`).
  * *Sottodomini:* Struttura gerarchica interna (es. `dmi`, `www`).
* **Porta:** Numero di porta del socket (opzionale se coincidente con il default: porta 80 per HTTP, 443 per HTTPS).
* **Path:** Percorso logico del file o della risorsa sul server.
* **Query String:** Insieme di coppie `chiave=valore` separate da `&` per passare parametri al backend.
* **Fragment / Anchor:** Riferimento interno a una specifica sezione o elemento con `id` identificativo nella pagina.

### 2. Risoluzione da URL a Indirizzo IP tramite DNS
Il **Domain Name System (DNS)** funge da rubrica distribuita e gerarchica di Internet, traducendo nomi a dominio mnemonici in indirizzi IP numerici:

> [!EXAMPLE] Flusso di Risoluzione DNS e Connessione
> Esempio di risoluzione per l'URL `https://www.dmi.unipg.it`:
> 1. **Controllo Cache Locale:** Il browser verifica la presenza dell'IP nella propria cache e in quella del sistema operativo.
> 2. **Interrogazione DNS Resolver / TLD Server:** In assenza di riscontro locale, contatta il DNS Resolver che interroga il server radice (Root DNS) e il server **TLD (`.it`)**.
> 3. **Individuazione Server Autoritativo:** Il server TLD restituisce l'indirizzo del **DNS Autoritativo** per la zona `unipg.it`.
> 4. **Estrazione Indirizzo IP:** Il server autoritativo risponde con l'indirizzo IP univoco associato a `www.dmi.unipg.it` (es. `141.250.197.175`).
> 5. **Connessione Socket:** Il browser apre la connessione TCP/TLS verso l'IP ottenuto ed emette la richiesta HTTP.

---

## VI. Ciclo di Vita della Pagina e Architettura Frontend

### 1. Flusso di Elaborazione nel Browser
Una volta stabilita la connessione:
1. Il client invia la `GET` HTTP per la risorsa radice.
2. Il server restituisce il markup HTML (eventualmente generato dinamicamente lato server, es. tramite PHP o framework backend).
3. Il motore di parsing del browser analizza l'HTML e genera il **DOM (Document Object Model)**.
4. Vengono individuate e scaricate le risorse collegate (fogli di stile CSS, script JavaScript, immagini, font).
5. Il browser calcola il **Render Tree**, esegue il calcolo del layout (*Reflow*) e disegna i pixel sullo schermo (*Painting*).

```
  HTML Source ────────> DOM Tree ─────┐
                                      ├───> Render Tree ───> Layout (Reflow) ───> Paint
  CSS Files   ────────> CSSOM Tree ───┘
```

### 2. I Tre Componenti Fondamentali della Pagina Web
Lo sviluppo frontend moderno si fonda sul principio della **Separazione delle Competenze (Separation of Concerns)**:

1. **Struttura e Contenuti (HTML):**
   * Definisce la gerarchia logica dei dati e il significato semantico degli elementi (`<header>`, `<nav>`, `<article>`, `<section>`, `<footer>`).
2. **Rappresentazione Visiva e Stile (CSS - Cascading Style Sheets):**
   * Regola layout (Flexbox, Grid), tipografia, colori, animazioni e responsività adattiva per dispositivi mobili (*media queries*).
3. **Funzionalità e Dinamismo (JavaScript):**
   * Manipola programmaticamente il DOM in tempo reale, intercetta gli eventi dell'interfaccia e gestisce comunicazioni asincrone con il backend tramite **AJAX** (con l'API `fetch` o `XMLHttpRequest`) senza dover ricaricare l'intera pagina.

> [!NOTE] Disaccoppiamento Struttura/Presentazione
> Il progetto storico [CSS Zen Garden](https://csszengarden.com) dimostra il potere della separazione delle competenze: un unico identico file HTML acquisisce layout e stili grafici radicalmente diversi modificando esclusivamente il foglio di stile CSS associato, senza alterare una sola riga di codice markup.

---

## VII. Evoluzione Storica del Web (Web 1.0, Web 2.0, Web 3.0)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       EVOLUZIONE DEL WEB                                                │
├─────────────────────────────┬───────────────────────────────────────────┬───────────────────────────────┤
│          Web 1.0            │                  Web 2.0                  │            Web 3.0            │
│        (1990 - 2000)        │               (2000 - 2010)               │        (2010 - Presente)      │
├─────────────────────────────┼───────────────────────────────────────────┼───────────────────────────────┤
│ • "Read-Only Web"           │ • "Read-Write Web"                        │ • "Read-Write-Execute Web"    │
│ • Pagine statiche HTML      │ • Pagine dinamiche e interattive          │ • Web Semantico e Ontologie   │
│ • Contenuti fissi aziendali │ • Contenuti generati dagli utenti (UGC)   │ • Integrazione AI / ML        │
│ • Navigazione ipertestuale  │ • Piattaforme Social e collaborative      │ • Dati strutturati collegati  │
│   unidirezionale            │   (Wikipedia, YouTube, Facebook, blog)    │ • Sistemi decentralizzati     │
└─────────────────────────────┴───────────────────────────────────────────┴───────────────────────────────┘
```

* **Web 1.0 (1990-2000) — The Static Web:** Architettura informativa statica; siti creati da programmatori e aziende con ruoli rigidi: gli editori pubblicano, gli utenti fruiscono passivamente in sola lettura.
* **Web 2.0 (2000-2010) — The Social & Interactive Web:** Introduzione del web dinamico e interattivo; l'utente diventa co-creatore attivo di contenuti (*User-Generated Content*). Sviluppo delle tecnologie asincrone (AJAX) e nascita dei social media.
* **Web 3.0 (2010-Presente) — The Semantic & Intelligent Web:** Elaborazione semantica dei contenuti mediante metadati strutturati e ontologie (consentendo ai computer di comprendere il significato dei dati). Personalizzazione avanzata guidata da intelligenza artificiale, servizi decentralizzati e interoperabilità pervasiva tra piattaforme.

---

## VIII. Panorama Tecnologico dello Sviluppo Web Moderno

La complessità del web moderno richiede uno stack articolato di linguaggi, framework e strumenti operativi:

* **Linguaggi di Base:** HTML5, CSS3, JavaScript (ES6+), TypeScript, PHP, Python, SQL.
* **Frontend Frameworks:** React, Vue.js, Angular, Svelte, Next.js, Nuxt.js.
* **CSS Frameworks & Tooling:** Tailwind CSS, Bootstrap, Sass, PostCSS.
* **Backend Frameworks & Runtime:** Node.js (Express, NestJS), Python (Django, FastAPI, Flask), PHP (Laravel), Java (Spring Boot), ASP.NET Core.
* **Database & ORM:** PostgreSQL, MySQL, SQLite, MongoDB; Prisma, TypeORM, SQLAlchemy, Hibernate.
* **Architetture API:** RESTful API, GraphQL, WebSockets, gRPC.
* **Ambienti di Sviluppo (IDE):** Visual Studio Code, Sublime Text, IntelliJ IDEA, WebStorm.

---

## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_Programmazione_Web]]
