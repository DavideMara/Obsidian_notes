---
date: 2026-03-18
tags:
  - Diritto
type: lezione
---

# Lezione 11: IA, Cybersecurity e Guerra Ibrida
**Data:** 18-03-2026

## IA nel Settore Militare e Guerra Ibrida
L'uso dell'IA in contesti bellici ("Guerra Ibrida") solleva questioni etiche e giuridiche fondamentali. 
**Guerra Ibrida:** Forma di conflitto permanente che coinvolge infrastrutture, propaganda, cyberattacchi e manipolazione dei social. Eisenhower denunciò il rischio del **complesso militare-industriale-accademico**, dove università e ricerca sono intrecciate con la difesa.

> [!EXAMPLE] Sistema Maven (Maven Smith System - Palantir)
> Utilizzato dall'esercito americano per attacchi di precisione. Integra modelli come **Claude (Anthropic)** per aggregare enormi quantità di dati. La decisione finale spetta all'uomo, ma l'analisi è gestita da LLM.

### Allineamento e Etica
L'**Allineamento (Alignment)** è l'obiettivo di progettare IA che non producano risultati pericolosi. Claude (Anthropic) usa la **Constitutional AI**: un sistema orientato da principi etici (una "costituzione" interna) ispirati ai diritti umani, ricordando le leggi della robotica di Asimov.

### Definizione di Intelligenza Artificiale
Viene definita IA ogni simulazione tramite computer di processi mentali umani:
- Apprendimento e ragionamento.
- Risoluzione di problemi e percezione.
- Processi decisionali e linguaggio.

**Storia ed Evoluzione Tecnica:**
- **Hardware:** Negli anni '70/'80 dominavano i supercomputer **Cray**. Oggi la potenza di calcolo è spostata sulle **GPU (NVIDIA)**, nate per i videogiochi (calcolo parallelo) e rivelatesi ideali per l'addestramento delle reti neurali.
- **Architetture:**
    - **Perceptron (1958):** Nato per fini militari (analisi foto aeree).
    - **Transformer (2017):** Base di tutti i LLM moderni (Google, *Attention Is All You Need*).
    - **GAN (Generative Adversarial Networks):** Un generatore sfida un discriminatore per creare immagini realistiche.
- **AGI (Artificial General Intelligence):** Ad oggi non esiste; è l'obiettivo di un'IA indistinguibile dall'uomo ma scalabile.

---

## Funzionamento dei Large Language Models (LLM)
### Il "Peccato Originale": Architettura di Von Neumann
Il problema strutturale degli LLM (e dell'informatica moderna) risiede nell'**Architettura di Von Neumann**, dove **dati e codice condividono lo stesso spazio logico**. Non essendoci separazione assoluta, un dato (il nostro prompt) può essere interpretato come comando (**Prompt Injection**). Le soluzioni attuali (*Guard rails*) sono come "epicicli tolemaici": aggiustamenti complessi che non risolvono il problema strutturale.

I LLM non "ricordano" nel senso umano e non "ragionano", ma effettuano una pura **analisi statistica** (un "autocomplete" avanzato).

### Architettura dell'Input
Non esiste una separazione netta tra codice e dati. L'input è composto da:
1. **System Prompt:** Istruzioni invisibili del produttore.
2. **Context Window:** La sequenza di prompt e output della sessione corrente (passata come input ad ogni turno).

> [!WARNING] Prompt Injection
> Poiché ogni parte dell'input ha lo stesso valore, un input esterno può sovrascrivere il *System Prompt* o le istruzioni dell'utente. Questo è un rischio critico per gli Agenti AI che hanno accesso a dati privati.

---

##  Crittografia e "Crypto Wars"
La crittografia è stata a lungo considerata tecnologia strategica (assimilata ad armi). Negli anni '90, per aggirare le restrizioni USA all'esportazione di software cifrato (come **PGP**), il codice venne stampato su libri o magliette: la legge vietava l'export di bit, ma non della carta stampata (protetta dal Primo Emendamento).

---

## I 6 Principi della Cybersecurity
La sicurezza dell'informazione si basa su una triade estesa (CIA+):

1. **Confidentiality (Riservatezza):** Solo chi è autorizzato legge i dati.
2. **Integrity (Integrità):** Impedire l'alterazione non autorizzata (*Tampering*).
3. **Availability (Disponibilità):** Il sistema deve essere accessibile (*Minaccia: DoS*).
4. **Authenticity (Autenticità):** Identificazione certa del mittente (*Minaccia: Spoofing*).
5. **Non-repudiability (Non-ripudiabilità):** Impossibilità di negare l'invio o la ricezione (concetto teorico legale).
6. **Authorization (Autorizzazione):** Livelli di accesso appropriati (*Minaccia: Elevation of privilege*).

> [!INFO] Il Fattore Umano
> **PEBKC** (*Problem Exists Between Keyboard and Chair*): L'anello debole è spesso l'utente (Social Engineering, Bad USB).
