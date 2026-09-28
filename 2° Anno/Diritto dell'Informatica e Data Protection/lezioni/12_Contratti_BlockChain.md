---
tags:
  - Diritto
  - Contratti
  - Blockchain
  - GDPR
---
◀️ *Torna a:* [[00_Index_Diritto.md]]

# Beni, Contratti e Blockchain

##  I Beni e il Contratto
Secondo il Codice Civile:
- **Beni (Art. 810 c.c.):** Cose che possono formare oggetto di diritti.
- **Beni Immobili vs Mobili (Art. 812 c.c.):** Gli immobili sono saldamente al suolo; le energie sono equiparate ai beni mobili (Art. 814 c.c.).

### Il Contratto (Art. 1321 c.c.)
L'accordo tra due o più parti per costituire, regolare o estinguere un rapporto giuridico **patrimoniale**.

**Requisiti Essenziali (Art. 1325 c.c.):**
1. Accordo delle parti.
2. Causa (funzione economico-sociale).
3. Oggetto (possibile, lecito, determinato).
4. Forma (se richiesta sotto pena di nullità).

> [!INFO] Pay-or-Consent (Dati come controprestazione)
> Il D.Lgs. 173/2021 riconosce che i **Dati Personali** possono essere una controprestazione patrimoniale. Il modello "Consenti o Paga" (es. Meta) è sotto esame dall'EDPB: il consenso deve essere libero e deve esistere un'alternativa equivalente.

---
##  Blockchain e Distributed Ledger Technology (DLT)
La blockchain nasce per risolvere il **Double Spending** senza intermediari centrali.

### Caratteristiche Tecniche e Nodi
- **Decentralizzazione:** Modello **Peer-to-Peer** (opposto al client-server), dove ogni nodo può essere sia client che server.
- **Nodi Completi (Full Nodes):** Conservano e verificano l'intera blockchain.
- **Nodi Light:** Consultano le informazioni senza scaricare tutto il registro.
- **Immutabilità:** Garantita da **Hash** e **Proof-of-Work (PoW)**.
- **Nonce:** Numero variabile che i miner cambiano per trovare un hash valido (difficoltà).
- **Ambiente Trustless:** La fiducia è spostata dal soggetto umano al protocollo tecnico.

### Meccanismi di Consenso
- **Proof-of-Work (PoW):** Basato sul lavoro computazionale (Mining, alto consumo energetico).
- **Proof-of-Stake (PoS):** Basato sulla partecipazione economica (asset vincolati).
- **Proof-of-Authority (PoA):** Validazione affidata a soggetti autorizzati (nodi identificati).

### Tipologie di Blockchain
- **Pubblica (Permissionless):** Aperta a chiunque (es. Bitcoin). Verificabilità totale.
- **Privata (Permissioned):** Accessibile solo a soggetti autorizzati. Verificabilità limitata.
*Nota: Blockchain e DLT (Distributed Ledger Technology) non sono sinonimi perfetti; la blockchain è una species del genus DLT.*

### Inquadramento Giuridico e Smart Contract
- **Validazione Temporale (Art. 8-ter d.l. 135/2018):** In Italia, la memorizzazione su DLT produce gli effetti giuridici della validazione temporale elettronica, utile per provare l'integrità e l'esistenza di un file a una certa data.
- **Smart Contract (Definizione):** Un programma per elaboratore la cui esecuzione vincola automaticamente le parti sulla base di effetti predefiniti.
- **La metafora del Distributore Automatico:** Lo smart contract è come una macchinetta del caffè; inserita la moneta e scelto il prodotto, l'esecuzione è automatica senza intervento umano.
- **Problemi Teorici:** Non sempre lo smart contract è un "contratto" civilistico. Può essere un mezzo di esecuzione di un accordo già concluso.
- **Forma Scritta:** La legge riconosce la forma scritta allo smart contract, ma solo previa **identificazione informatica** delle parti (requisiti AgID). Il codice da solo non prova il consenso valido, la causa o la liceità dell'oggetto.
- **Regolamento MiCA (2023/1114):** Disciplina le cripto-attività (ART, EMT, Utility Token) nell'UE.
- **DLT Pilot Regime:** Sperimentazione per strumenti finanziari tokenizzati.

> [!IMPORTANT] Blockchain e GDPR
 L'immutabilità della blockchain collide con il **Diritto alla Cancellazione** (Oblio). Le linee guida EDPB 2025 cercano di mediare tra architetture decentralizzate e responsabilità del titolare.
