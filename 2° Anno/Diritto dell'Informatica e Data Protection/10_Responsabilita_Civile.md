---
date: 2026-03-16
subject: Diritto dell'Informatica e Data Protection
tags:
  - Diritto
  - appunti
  - lezione
type: lezione
---

# Responsabilità Civile per Illecito Trattamento dei Dati Personali

## Dinamiche del Processo Civile
In ambito civile, la richiesta di risarcimento del danno per un trattamento dei dati non adeguato segue regole procedurali rigorose. Il giudice valuta esclusivamente la fattispecie sottoposta alla sua attenzione, non adottando una visione "ampia" ma limitandosi alla cornice dettata dalle parti.

> [!INFO] Principio della domanda 
> Nel processo civile vige il principio della domanda (Art. 99 c.p.c.): l'autorità giudiziaria si pronuncia unicamente su quanto formalmente richiesto ed eccepito dai soggetti in causa.

All'interno di un processo civile si individuano le seguenti figure e componenti formali:
- **Attore**: colui che promuove l'azione in giudizio.
- **Convenuto**: il soggetto chiamato in giudizio a rispondere della pretesa dell'attore.
- **Chiamata in causa**: coinvolgimento di ulteriori soggetti terzi da parte del convenuto.
- **Petitum**: la domanda specifica rivolta al giudice (ciò che si chiede).
- **Causa petendi**: la spiegazione delle ragioni di fatto e di diritto che giustificano il petitum.

> [!INFO] Petitum e causa petendi 
> La corretta individuazione di *petitum* e *causa petendi* è il pilastro su cui si incardina l'intero impianto accusatorio per la violazione dei dati personali.

---

## L'Articolo 82 del GDPR: Diritto al Risarcimento

> [!LAW] **Art. 82 GDPR** 
>  "Chiunque subisca un danno materiale o immateriale a causa di una violazione del presente regolamento ha il diritto di ottenere il risarcimento del danno dal titolare del trattamento o dal responsabile del trattamento."

> [!INFO] 
> Il termine "chiunque subisca" fa stretto riferimento alla figura dell'[interessato], che nel perimetro del GDPR è sempre e solo una **persona fisica**.

Applicando le logiche processuali a questa norma:
- **Attore**: chiunque subisca la lesione (l'interessato).
- **Petitum**: la richiesta di risarcimento. Questo include sia il danno immateriale (es. danno morale/sofferenza) sia il danno materiale, comprendente il **lucro cessante** (il mancato guadagno derivante direttamente dall'illecito).
- **Causa petendi**: la violazione oggettiva delle disposizioni del Regolamento.

> [!INFO] La *causa petendi*
>  rappresenta il fondamento giuridico della domanda: senza l'allegazione e la dimostrazione delle ragioni fattuali dell'illecito, il petitum non può essere accolto.

Il danno lamentato deve essere provato in rapporto di causalità diretta con la violazione del GDPR.

> [!INFO] Esempio pratico (Phishing)
> In un attacco informatico andato a buon fine, i dati personali trattati in modo illecito o non protetti adeguatamente (es. nome utente e password sottratti) costituiscono la base materiale del danno su cui fondare la pretesa.

### Esempi Pratici di Illecito e Danno
1. **Phishing Bancario:** L'utente cade nel tranello, ma può citare la banca (es. Poste Italiane) se dimostra che il sistema di sicurezza (solo nome utente e password) era inadeguato rispetto allo stato dell'arte (mancanza di **MFA/OTP**).
2. **SIM Swap:** Duplicazione fraudolenta della SIM. La banca può rispondere se ha basato la sicurezza esclusivamente sul possesso del numero telefonico, ignorando rischi prevedibili.
3. **Carta Revolving:** Carta recapitata al soggetto sbagliato (es. a un supermercato) e attivata da terzi. Il titolare risponde delle carenze identificative e organizzative.
4. **Omonimia vs Omocodia:** L'errore dell'Agenzia delle Entrate (due codici fiscali uguali) può esentare il titolare (banca) che si è fidato di registri ufficiali. La semplice omonimia (stesso nome) invece non giustifica l'invio a indirizzi errati senza controllo del CF.

### Sicurezza e Responsabilizzazione (Accountability)
- **Art. 25 GDPR (Privacy by Design/Default):** La tutela deve essere incorporata nel sistema sin dalla progettazione. Il parametro è "mobile": bisogna aggiornarsi costantemente.
- **Art. 32 GDPR (Sicurezza del Trattamento):** Richiede misure adeguate allo "stato dell'arte" e al rischio. La sicurezza è un processo continuo, non un traguardo statico.
- **Vulnerabilità Zero-day:** Il titolare può liberarsi se prova che il danno deriva da un rischio non prevedibile e non evitabile con misure tecniche esigibili al momento del fatto (valutazione *ex ante*).

### Il Titolare del Trattamento e Oneri Probatori
Il destinatario principale dell'azione (il convenuto) è tipicamente il **Titolare del trattamento**, ovvero colui che detiene il potere decisionale e stabilisce i mezzi e le finalità (i "modi") del trattamento. All'interno di un'organizzazione rappresenta un'entità unitaria, la quale può però demandare parte del trattamento a soggetti esterni (i cosiddetti Responsabili del trattamento).

> [!INFO] Responsabile (Processor)
> Risponde se va oltre le istruzioni del titolare o viola obblighi diretti del GDPR. Se decide autonomamente (es. usa dati per profilazione propria), diventa Titolare e "paga di tasca sua".

> [!INFO] Onere della Prova
> L'attore deve provare la violazione, il danno e il nesso causale. Tuttavia, il titolare può esonerarsi solo dimostrando che l'evento non gli è in alcun modo imputabile (Art. 82.3 GDPR).

> [!INFO] Carico 
> La violazione a carico del Titolare deve essere rigorosamente dimostrata in corso di causa, quasi sempre mediante il supporto tecnico di una consulenza specializzata (CTU in ambito informatico).

---

## Responsabilità Civile e Codici di Condotta

> [!LAW] **Art. 24 GDPR e Art. 20 D.Lgs. 101/2018**
> Il comportamento contrario ai codici di condotta di settore costituisce presupposto diretto per la responsabilità civile e fonda il diritto al risarcimento del danno.

### Regole Deontologiche per l'Attività Giornalistica

Un ambito di forte scontro tra diritto alla riservatezza e altri diritti costituzionali (come la libertà di stampa) riguarda l'informazione giornalistica, soprattutto inerente alla salute.

> [!LAW] **Cassazione Civile, 21.06.2018, n. 16133**
> La Suprema Corte ha sanzionato l'illecita pubblicazione di notizie attinenti alla salute dell'interessato. Il caso riguardava un articolo di un quotidiano locale che esponeva nel dettaglio come due giovani fossero affetti dalla medesima sindrome che aveva già causato il decesso del fratello minore.

La pronuncia stabilisce un limite invalicabile: la divulgazione di notizie attinenti alla salute, in assenza del consenso dell'interessato, è consentita esclusivamente quando strettamente collegata all'essenzialità dell'informazione.

> [!INFO] 
> Il bilanciamento tra il diritto di cronaca e la Data Protection impone il divieto di divulgazione di dettagli clinici esuberanti rispetto alla finalità puramente informativa della notizia.

### Adeguatezza allo Stato dell'Arte
In chiusura, un principio cardine che permea tutto il diritto dell'informatica: le misure tecniche e organizzative adottate, così come le norme che le regolano, non sono concetti statici ma devono essere costantemente adeguate allo stato attuale della tecnica e dell'evoluzione tecnologica.

---
## ⏭️ Navigazione Lezioni

- **Index Corso Diritto:** [[00_Index_Diritto]]