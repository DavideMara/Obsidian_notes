---
titolo: "Analisi: Protezione dei Dati, Bias e Dati Neurali"
data: 2026-05-19
tags:
  - Diritto
  - AI
  - NeuroEtica
stato: completato
---
# Protezione dei Dati e Nuove Frontiere Digitali

## 1. Data Bias

> [!info] Definizione
> Una distorsione sistematica e non casuale all'interno di un insieme di dati, che porta a una rappresentazione della realtà parziale, inaccurata o soggettiva. Nell'ambito dell'IA, il bias non è un errore statistico isolato, ma una proprietà strutturale del dataset o del modello.

### 1.1 Tipi di Data Bias
- **Bias di Algoritmo (Algorithmic Biases):** Pregiudizio insito nel codice o nei pesi assegnati.
	-  **Caso Toeslagenaffaire (Olanda):** Algoritmo fiscale che discriminava le famiglie in base alla doppia cittadinanza.
	- **Caso SyRI (System Risk Indication):** Strumento di profilazione per frodi assistenziali, dichiarato illegittimo perché violava il bilanciamento tra efficienza amministrativa e privacy (Art. 8 CEDU).
- **Bias di Minoranza (Minority Bias):** Scarsa rappresentanza. Se il dataset riflette solo la maggioranza, il modello fallisce sulle "code" della distribuzione (outliers), marginalizzando ulteriormente gruppi già fragili.
- **Confirmation Bias (Bias di Conferma):** Tendenza a raccogliere dati che confermano preconcetti. Se un sistema di polizia predittiva viene addestrato su zone già storicamente più sorvegliate, genererà "profezie che si auto-avverano" (feedback loops).
- **Measurement Bias (Bias di Misurazione):** Errori negli strumenti o uso di variabili "proxy". Usare il CAP di residenza come parametro può essere un modo indiretto per discriminare in base al reddito o all'etnia (Redlining digitale).

### 1.2 Casi Studio e Impatto Giuridico
- [ ] **Caso 1: Amazon Recruiting (2015)**
	- *Fatto:* Amazon creò un'IA per selezionare CV. Il modello, addestrato sui successi dell'ultimo decennio (prevalentemente maschili), imparò a penalizzare i CV che contenevano la parola "femminile".
	- *Impatto sulla protezione dei dati:* Dimostra che la neutralità tecnologica è un mito. Viola il principio di **non discriminazione** e la necessità di controllo umano (Human-in-the-loop).
- [ ] **Caso 2: COMPAS (Justitia)**
	- *Fatto:* Algoritmo USA per valutare il rischio di recidiva. Assegnava punteggi di rischio più alti ai neri rispetto ai bianchi a parità di reato.
	- *Impatto sulla protezione dei dati:* Pone il problema dell'**opacità algoritmica** (Black Box). L'impossibilità di contestare la logica dietro una decisione lede il diritto alla difesa.
- [ ] **Caso 3: Algoritmo Grading A-Level (Regno Unito, 2020)**
	- *Fatto:* Durante il COVID-19, un algoritmo ha assegnato i voti scolastici basandosi sulla "performance storica" degli istituti. Risultato: penalizzati gli studenti brillanti di scuole povere e favoriti quelli di scuole private d'élite.
	- *Impatto:* Esempio di **bias socio-economico** istituzionalizzato. Il governo ha dovuto ritirare i voti dopo massicce proteste.
- [ ] **Caso 4: Algoritmo Optum/Impact Pro (Sanità USA)**
	- *Fatto:* Algoritmo usato per identificare pazienti ad alto rischio che necessitavano di cure extra. Usava la "spesa sanitaria storica" come proxy del bisogno di salute. Poiché i neri spendevano storicamente meno (per minor accesso alle cure), venivano classificati come "meno malati" di bianchi con le stesse patologie.
	- *Impatto:* **Proxy Bias**. L'uso di variabili economiche per decidere sulla salute crea discriminazioni sistemiche invisibili.
- [ ] **Caso 5: Apple Card / Goldman Sachs (Finanza)**
	- *Fatto:* Segnalazioni di algoritmi di scoring del credito che assegnavano fidi molto più bassi alle donne rispetto ai mariti, pur con redditi e beni co-intestati identici.
	- *Impatto:* Solleva il tema della **trasparenza algoritmica** nei servizi finanziari e della necessità di audit esterni.
- [ ] **Caso 6: Polizia Predittiva (PredPol / Geolitica)**
	- *Fatto:* Software che suggeriscono alle pattuglie dove dirigersi basandosi su dati storici di arresti. Risultato: le pattuglie vengono mandate sempre nelle stesse zone, effettuano più arresti lì, alimentando il dataset in un circolo vizioso.
	- *Impatto:* **Feedback Loop Bias**. Automatizza e "certifica" scientificamente pregiudizi storici di sorveglianza territoriale.

---

## 2. Dati Neurali (Neuro-dati)
> [!warning] La nuova frontiera della Privacy
> I dati neurali raccolgono l'attività del sistema nervoso. A differenza dei dati personali "classici" (nome, posizione), i neuro-dati possono rivelare intenzioni, stati emotivi e pensieri prima ancora che vengano esteriorizzati.

### 2.1 Tipologie di Dati Raccolti
- **Tracciati EEG (Elettroencefalogramma):** Analisi delle frequenze cerebrali per rilevare stress, attenzione o gradimento (Neuromarketing).
- **BCI (Brain-Computer Interfaces):** Dispositivi (es. Neuralink) che permettono il controllo di macchine tramite il pensiero, ma che fungono anche da "canali di output" di dati intimi.
- **Dati Involontari:** Reazioni subconsce che l'utente non può controllare o mascherare, rendendo nullo il concetto tradizionale di "volontà" nel consenso.

### 2.2 Implicazioni Giuridiche ed Etiche: I Neuro-diritti
La sfida è l'aggiornamento del GDPR verso i **Neurorights**:
1. **Privacy Mentale:** Impedire l'accesso ai dati cerebrali senza consenso esplicito e consapevole.
2. **Identità Personale:** Proteggere l'integrità del "Sé" da interferenze esterne.
3. **Libero Arbitrio:** Garantire che le decisioni non siano manipolate da impulsi indotti tecnologicamente.

> [!note] Il precedente del Cile
> Il Cile è stato il primo paese al mondo (2021) a inserire in Costituzione la tutela dell'integrità mentale e dei dati cerebrali come diritti umani fondamentali.

---

## 3. Potenziali Rischi

### 3.1 Rischi per l'Individuo (Micro-livello)
- **Manipolazione Cognitiva:** Sfruttamento di vulnerabilità psicologiche (es. dopamina tramite notifiche) per guidare il comportamento d'acquisto o politico.
- **Brain-jacking:** Accesso non autorizzato a dispositivi medici impiantabili (es. pacemaker neurali) con rischi per la vita stessa.

### 3.2 Rischi per la Società (Macro-livello)
- **Neuro-surveillance:** Aziende che monitorano l'attenzione dei dipendenti o scuole che misurano la concentrazione degli studenti tramite fasce EEG.
- **Digital Divide Cognitivo:** Il rischio che il potenziamento cognitivo (IA integrata nel cervello) crei una nuova divisione tra "umani aumentati" e "umani biologici", accentuando le disuguaglianze sociali.

---

## 4. Conclusioni e Punti Aperti
La protezione dei dati si sta evolvendo da un concetto di **tutela della libertà di agire** a una **tutela della libertà di pensare**. 
- **Punto Aperto 1:** Il GDPR è sufficiente per i dati neurali? Molti esperti suggeriscono che questi dati debbano essere considerati come **dati biometrici speciali** (Art. 9) o addirittura come "parte del corpo".
- **Punto Aperto 2:** Responsabilità Civile. Se un'IA neurale compie un'azione sbagliata basandosi su un mio impulso subconscio interpretato male, chi paga? L'utente o il produttore dell'interfaccia?
- **Punto Aperto 3:** L'IA Act dovrà integrare norme specifiche per vietare pratiche di IA che sfruttino la manipolazione neurale subliminale.
