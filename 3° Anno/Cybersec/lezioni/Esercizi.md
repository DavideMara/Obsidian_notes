---
date: 2026-09-28
tags:
  - sicurezza-informatica
type: esercizi
---
# Esercizi e Domande per Casa - Sicurezza Informatica

---
## Registro Consegne

| #                                                              | Consegna                           | Lezione | Tipo    | Stato   |
| -------------------------------------------------------------- | ---------------------------------- | ------- | ------- | ------- |
| [E.1](#E.1%20-%20Versioning%20di%20HTTPS)                      | Versioning di HTTPS                | Lez. 02 | Teorica | Da fare |
| [E.2](#E.2%20-%20REST%20e%20Metodi%20HTTP)                     | REST e metodi HTTP                 | Lez. 02 | Teorica | Da fare |
| [E.3](#E.3%20-%20Encoding%20Base64)                            | Encoding base64                    | Lez. 02 | Teorica | Da fare |
| [E.4](#E.4%20-%20Verificare%20HTTP%20da%20Riga%20di%20Comando) | Verificare HTTP da riga di comando | Lez. 02 | Pratica | Da fare |
| [E.5](#E.5%20-%20Cookie%20e%20Cifratura%20del%20Canale)        | Cookie e cifratura                 | Lez. 02 | Pratica | Da fare |
| [E.6](#E.6%20-%20Esporre%20un%20Servizio%20Web%20con%20ngrok)  | Esporre un servizio web con ngrok  | Lez. 02 | Pratica | Da fare |
| [E.7](#E.7%20-%20Interazione%20SMTP%20via%20Telnet)            | Interazione SMTP via telnet        | Lez. 02 | Pratica | Da fare |

---

# Lezione 02 - Livello di Applicazione (28/09/2026)

Materiale di riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta]] (TCP/IP, HTTP, FTP, posta elettronica). Le 7 consegne si suddividono in 3 esercizi teorici e 4 pratici di laboratorio.

## E.1 - Versioning di HTTPS

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.3 Connessioni HTTP|5.3 Connessioni HTTP]]*

**Consegna.** Elencare e spiegare l'evoluzione del versioning di HTTPS, indicando per ogni versione le modifiche introdotte e le vulnerabilita risolte.

**Ambito della risposta.**

| Versione | Anno | Da approfondire |
|---|---|---|
| HTTP/1.0 | 1996 | Connessioni non persistenti, assenza di `Host`, nessun chunked transfer |
| HTTP/1.1 | 1997 | Connessioni persistenti, `Host` obbligatorio, `Cache-Control`, pipelining |
| TLS 1.0 / 1.1 | 1999 / 2006 | Debolezze crittografiche (BEAST, POODLE) e deprecazione |
| TLS 1.2 | 2008 | Algoritmi AEAD, `SNI`, `ALPN` |
| TLS 1.3 | 2018 | Handshake semplificato (1-RTT, 0-RTT), rimozione di cipher suite deboli |
| HTTP/2 | 2015 | Multiplexing su una connessione, header compression (HPACK), framing binario |
| HTTP/3 | 2022 | QUIC su UDP, header compression (QPACK), resistenza a version spoofing |

**Punti su cui insistere.**
* Perche HTTPS su HTTP/1.1 non ha eliminato il *head-of-line blocking*: HTTP/2 lo risolve a livello applicativo, ma lo **stream di trasporto** resta bloccato dalla perdita di un solo pacchetto TCP. HTTP/3 elimina il problema alla radice passando a QUIC, che implementa il multiplexing a livello di trasporto su UDP.
* La differenza tra **TLS** (protocollo) e **HTTPS** (HTTP su TLS): TLS opera tra il livello di trasporto e quello applicativo, quindi protegge qualunque protocollo applicativo, non solo HTTP.
* Perche TLS 1.3 ha ridotto il numero di round-trip (1-RTT, con 0-RTT come compromesso sull'attesa di conferma).

## E.2 - REST e Metodi HTTP

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.5 Metodi HTTP|5.5 Metodi HTTP]]*

**Consegna.** Elencare e spiegare la relazione tra il modello **REST** e i metodi HTTP `GET`, `POST`, `HEAD`, `PUT`, `DELETE`.

**Ambito della risposta.**

* **Corrispondenza CRUD / metodi HTTP:**

  | Operazione CRUD | Metodo HTTP | Idempotente | Sicuro |
  |---|---|---|---|
  | Create | `POST` | No | No |
  | Read | `GET` | Si | Si |
  | Update | `PUT` | Si | No |
  | Delete | `DELETE` | Si | No |
  | (parziale) Update | `PATCH` | Non necessariamente | No |

* **Le sei restrizioni di REST:** client-server, stateless, cacheable, uniform interface, layered system, code on demand. In particolare il vincolo **stateless** e la ragione per cui HTTP e stateless nonostante i cookie lo sembrino: lo stato e mantenuto dal client, non dal server.
* **Perche `GET` e `HEAD` sono idempotenti e sicuri**, mentre `POST` e `PUT` no.
* **Perche esiste `PATCH`** se `PUT` e gia idempotente: `PUT` rimpiazza l'intera risorsa, `PATCH` applica solo un delta.
* **Quando un metodo "sicuro" puo comunque essere dannoso:** un `GET` che innesca un'azione con effetto collaterale (es. link di disiscrizione via email) viola l'aspettativa del client, dei crawler e delle cache, e puo essere sfruttato per CSRF via `<img>` cross-origin.

> [!WARNING] Conseguenza di sicurezza
> I browser applicano protezioni diverse a metodi diversi: i form HTML emettono solo `GET` e `POST`, quindi `PUT`/`DELETE` non sono invocabili cross-site da un form. Al contrario, un `<img src="...">` puo innescare un `GET` cross-origin. E la ragione per cui le API che espongono azioni di stato via `GET` sono particolarmente esposte al **CSRF**.

## E.3 - Encoding Base64

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#7.4 MIME: estensioni per messaggi multimediali|7.4 MIME]]*

**Consegna.** Spiegare il significato e il funzionamento dell'encoding **base64**.

**Punti da coprire.**
* **Perche esiste:** SMTP e HTTP in forma originaria richiedono corpi in ASCII a 7 bit. I dati binari (immagini, PDF, eseguibili) contengono byte fuori dal range stampabile e non sono quindi trasportabili. Base64 risolve il problema trasformando dati arbitrari in una stringa ASCII sicura.
* **Come funziona:** l'alfabeto standard (`A-Z`, `a-z`, `0-9`, `+`, `/`) con 64 simboli, codificati **6 bit** per simbolo. Ogni tripletto di 8 bit (3 byte) produce 4 simboli da 6 bit, con padding `=` fino a completare l'ultimo gruppo. Un decodificatore deve poter ricavare esattamente i 6 bit per simbolo, il che spiega il vincolo di multipli di 3 byte.
* **Il rapporto con MIME:** corrisponde al valore `Content-Transfer-Encoding: base64` dell'intestazione MIME, che dichiara al destinatario come risolvere il corpo.
* **Non e cifratura.** Chiunque puo decodificare: e una **codifica** di trasporto, non un meccanismo di protezione. La risposta corretta a "come proteggo un allegato?" non e base64 ma cifratura (PGP/S/MIME, cifratura della cartella) o un canale cifrato come SMTPS/IMAPS.

> [!EXAMPLE] Verifica pratica
> Qualsiasi strumento di linea di comando permette di osservare la trasformazione:
> ```bash
> echo -n "Sicurezza" | base64
> echo "U2ljdXJyZXp6YQ==" | base64 -d
> ```
> Notare la relazione: 9 caratteri di input (`Sicurezza` sono 9 byte) producono 12 simboli base64, cio 3 gruppi da 4, senza padding. Provare con input di 1 e 2 byte per osservare il padding.

## E.4 - Verificare HTTP da Riga di Comando

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.4 Messaggi HTTP|5.4 Messaggi HTTP]]*

**Consegna.** Collegarsi via Telnet al proprio server web preferito e osservare le risposte reali del protocollo.

**Procedura.**

1. Aprire una connessione TCP sulla porta 80 (quella di default per un server HTTP):
   ```bash
   telnet cis.poly.edu 80
   ```
2. Digitare una richiesta `GET` minima ma completa:
   ```http
   GET /~ross/ HTTP/1.1
   Host: cis.poly.edu
   ```
   Premere due volte il tasto Invio: il primo CRLF chiude le intestazioni, il secondo invia la riga vuota che segnala la fine del messaggio.
3. Osservare il messaggio di risposta trasmesso dal server HTTP.

**Cosa osservare e annotare.**
* La differenza fra la risposta ricevuta e la struttura teorica della sezione 5.4: quali campi di intestazione sono presenti in realta e quali mancano.
* Il significato dei campi `Server`, `Content-Type`, `Content-Length`, `Last-Modified`, `Date`.
* Il valore del codice di stato e cosa comporta (confronto con la tabella dei codici).
* Il comportamento con `Connection: close` e con una richiesta `HEAD` (stesse intestazioni di un `GET`, corpo vuoto): utile per verificare quando il server decide di chiudere la connessione.

> [!NOTE] Perche Telnet e utile qui
> Telnet non effettua alcuna cifratura: la sessione serve a parlare HTTP in chiaro. E il modo piu rapido per vedere le intestazioni reali senza dover installare estensioni del browser (`curl -v` o gli strumenti di sviluppo fanno lo stesso lavoro in modo piu comodo, ma la lettura "a mano" del protocollo e il punto dell'esercizio).

## E.5 - Cookie e Cifratura del Canale

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.6 Cookie|5.6 Cookie]]*

**Consegna.** Verificare dove vengono salvati i cookie dal browser e individuare la presenza di cookie non cifrati.

**Procedura.**
1. Aprire i devtools del browser (F12), pannello **Application** (o **Storage**) e ispezionare `Cookies`.
2. Navigare un sito che imposta cookie, verificando in che posizione del filesystem vengono salvati:
   * Chrome/Chromium/Edge: profilo utente in `~/.config/google-chrome/Default/Cookies` (database **SQLite**, cifrato con la chiave di sistema su Linux/macOS con *Keychain*);
   * Firefox: `cookies.sqlite` nel profilo, in chiaro.
3. Nella tabella dei cookie verificare la presenza dei flag di sicurezza:

   | Flag | Effetto se assente |
   |---|---|
   | `Secure` | Il cookie viene inviato anche su HTTP in chiaro, intercettabile |
   | `HttpOnly` | Il cookie e leggibile da JavaScript, esfilturabile via XSS |
   | `SameSite` | Il cookie viene allegato a richieste cross-site, abilitando CSRF |

4. Nel pannello **Network** selezionare una richiesta e verificare in Request Headers la presenza dell'intestazione `Cookie` e in Response Headers di `Set-Cookie`.

**Domande di verifica.**
* Perche l'assenza del flag `Secure` su un cookie di sessione equivale a una password in chiaro sul canale?
* Che differenza c'e tra la cifratura **del canale** (HTTPS) e la cifratura **del dato memorizzato** (nel database del sito o nel file locale del browser)?
* Perche i cookie che contengono dati di autenticazione sono particolarmente critici, e come puo mitigarsi con `HttpOnly` + `Secure` + `SameSite=Strict`?

## E.6 - Esporre un Servizio Web con ngrok

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#5.7 Cache Web e Server Proxy|5.7 Cache web e server proxy]]*

**Consegna.** Mettere in piedi un servizio web raggiungibile dall'esterno per osservare le richieste e risposte HTTP reali, i cookie emessi e gli header di risposta.

**Procedura.**
1. Avviare un server web locale (qualsiasi server statico minimale e sufficiente):
   ```bash
   python3 -m http.server 8000
   ```
2. Esporlo su Internet tramite un tunnel:
   ```bash
   ngrok http 8000
   ```
   ngrok assegna un dominio pubblico (es. `https://abcd1234.ngrok-free.app`) che inoltra il traffico verso la porta locale.
3. Visitare l'URL pubblico e raccogliere, per ogni richiesta:
   * la **riga di richiesta** (metodo, percorso, versione) e tutte le intestazioni;
   * la **riga di stato** e il corpo della risposta;
   * i cookie emessi e il loro ciclo di vita (`Set-Cookie` con attributi `Max-Age`/`Expires`, `Path`, `SameSite`);
   * gli header `Cache-Control`, `ETag`, `Last-Modified` e il comportamento della cache del browser e dei proxy intermedi.

**Domande di verifica.**
* Che cosa cambia, dal punto di vista della sicurezza, nell'esporre un servizio su Internet: il bind su `0.0.0.0` vs `127.0.0.1` e il ruolo del firewall.
* Perche il tunnel espone il servizio anche se il server ascolta solo in locale.
* Cosa suggerisce il fatto che ngrok termini il traffico con TLS **a monte** del tunnel: in che punto del percorso il traffico e in chiaro.
* Che differenza c'e fra la risposta di un **server d'origine** e quella di una **cache**: provare a richiedere due volte la stessa risorsa e confrontare `Age`, `X-Cache` e i tempi.

## E.7 - Interazione SMTP via Telnet

*Riferimento: [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta#7.2 SMTP \[RFC 2821\]|7.2 SMTP]]*

**Consegna.** Provare un'interazione SMTP manualmente, senza utilizzare il client di posta.

**Procedura.**
1. Aprire la connessione:
   ```bash
   telnet servername 25
   ```
   Si riceve la risposta `220` dal server.
2. Immettere nell'ordine i comandi `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, `QUIT`:
   ```text
   S: 220 hamburger.edu
   C: HELO crepes.fr
   S: 250 Hello crepes.fr, pleased to meet you
   C: MAIL FROM: <alice@example.org>
   S: 250 alice@example.org... Sender ok
   C: RCPT TO: <bob@example.com>
   S: 250 bob@example.com ... Recipient ok
   C: DATA
   S: 354 Enter mail, end with "." on a line by itself
   C: Righe del messaggio
   C: .
   S: 250 Message accepted for delivery
   C: QUIT
   S: 221 hamburger.edu closing connection
   ```
3. Confrontare la sequenza ricevuta con l'esempio della slide.

**Cosa osservare e annotare.**
* La corrispondenza tra le **tre fasi** (handshaking, trasferimento, chiusura) e i comandi effettivamente inviati.
* Il fatto che ogni comando riceva una risposta con **codice di stato numerico a tre cifre** seguito da un'espressione: la stessa struttura di HTTP, ma qui il server **mantiene lo stato** della sessione.
* Il terminatore `CRLF.CRLF` usato dal server per individuare la fine del messaggio, coerente con il `.` singolo sulla riga propria che lato client manda in modalita `DATA`.
* Come il server reagisce a input anomali: `MAIL FROM` senza `HELO` preliminare, `RCPT TO` con indirizzo non valido, piu destinatari, `DATA` senza `RCPT TO`, dimensione del messaggio superiore al limite.

**Domande di verifica.**
* Quali controlli applica il server per mitigare lo **spam e l'abuso di relay**, e come si relazionano a SPF, DKIM e DMARC.
* Perche SMTP in chiaro sulla porta 25 e un problema, e quali sono le varianti cifrate (SMTPS, submission sulla 587, STARTTLS).
* Che cosa cambia se al posto di `HELO` si usa `EHLO`: la trattativa delle estensioni del protocollo.

> [!WARNING] Nota operativa
> La porta 25 in uscita e usata solo da server di posta autorizzati. La connessione diretta a un MX remoto puo essere rifiutata o throttled. Per il puro studio del protocollo e sufficiente l'interazione con il proprio server di posta di dominio universitario.

---

## ⏭️ Navigazione Lezioni
- **Index Corso :** [[00_Index_Cybersecurity]]
- **Teoria di riferimento :** [[02_Livello_Applicazione_TCPIP_HTTP_FTP_Posta]]
