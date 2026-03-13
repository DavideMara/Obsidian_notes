---
date: 2026-02-25
tags:
  - "#sistemi-operativi"
  - teoriaSO
type: lezione
---

# Sistemi Operativi - Introduzione

## 1. Cos'è e quali sono i suoi compiti
 Un *sistema operativo (OS)* è fondamentalmente un programma (software) che ha il compito di controllare l'esecuzione di tutti gli altri programmi all'interno della macchina.
 Agisce come un'interfaccia diretta tra le applicazioni software e l'hardware fisico.
* Lo sviluppo e l'architettura di un OS mirano a tre obiettivi principali:
  * **Convenienza:** rendere l'utilizzo del sistema di elaborazione più semplice e fruibile per l'utente.
  * **Efficienza:** ottimizzare lo sfruttamento delle risorse hardware.
  * **Capacità di evolversi:** permettere lo sviluppo e l'integrazione di nuove funzionalità nel tempo.
  
>[!NOTA] 
>Il Firmware è un software a basso livello che fornisce istruzioni fondamentali per il loro funzionamento e controllo, agisce come ponta tra l'Hardware e il Sistema Operativo

---

## 2. Sistema Di Elaborazione
![[Pasted image 20260307133154.png]]

### Servizi del Sistema Operativo
L'OS eroga una serie di servizi fondamentali necessari al funzionamento dell'intero ecosistema informatico:
* **Creazione ed esecuzione dei programmi:** fornisce i meccanismi per compilare, caricare il codice in memoria e mandarlo in esecuzione.
* **Accesso ai dispositivi di I/O:** standardizza e gestisce l'interazione con periferiche esterne (es. stampanti, tastiere, reti).
* **Accesso controllato ai file:** organizza e protegge i dati persistenti.
  > [!IMPORTANT] Il File System
  > È il **File System** la componente specifica dell'OS che gestisce fisicamente la memoria secondaria (come gli hard disk - HDD) e i file.
* **Accesso al sistema:** regola l'autenticazione e l'uso delle risorse condivise.
* **Rilevazione degli errori e risposta:** monitora lo stato del sistema intervenendo in caso di anomalie. Questo include la gestione degli errori a livello hardware e la correzione/segnalazione in fase di compilazione o esecuzione.
* **Contabilità (Accounting):** traccia il consumo delle risorse condivise.
### Interfacce
Il sistema di elaborazione è strutturato a livelli, separati da interfacce standard che hanno livelli di complessità differente:
* **API (Application Programming Interface):** Interfaccia di programmazione utilizzata per i programmi applicativi e le librerie/utility.
* **ABI (Application Binary Interface):** Interfaccia binaria per le applicazioni, che funge da ponte tra le librerie e il sistema operativo stesso.
* **ISA (Instruction Set Architecture):** L'architettura del set di istruzioni, ovvero l'interfaccia di base tra il sistema operativo (software) e l'hardware di esecuzione.

---

## 3. La Gestione delle Risorse e il Controllo della CPU

![[Pasted image 20260310151159.png]]

>[!NOTE] Sebbene abbia un ruolo di supervisore nella gestione delle risorse, il sistema operativo è a tutti gli effetti un normale programma eseguito dal processore.

Per permettere alle applicazioni dell'utente di funzionare, l'OS deve necessariamente **cedere il controllo** (in quanto esso stesso un programma) della CPU. Una volta ceduto il controllo, l'OS dipende dall'hardware (in particolare dalla CPU) per poterlo riavere indietro. 

  > [!NOTE] Meccanismo di Ritorno
  > Se un processo ha bisogno di un servizio (es. I/O) o se si verifica un evento, l'hardware deve notificare l'OS tramite specifici meccanismi (come le interruzioni/interrupt) per restituirgli il controllo.

---

## 4. L'Evoluzione dei Sistemi Operativi (Fino a Slide 18)
I sistemi operativi si sono evoluti nel tempo per tre ragioni primarie: l'aggiornamento verso nuovi tipi di hardware, la richiesta di nuovi servizi da parte degli utenti e la necessità di correzione degli errori.

> [!NOTE] Nota
> L'evoluzione dei sistemi operativi è strettamente legata a quella dell'hardware: un cambio drastico nelle tecnologie hardware impone quasi sempre un cambio e un riadattamento nei sistemi operativi.

### Prima Generazione (1945–1955)
* **Tecnologia:** Basata sull'uso di tubi a vuoto (valvole).
* **Sistema Operativo:** Nessun sistema operativo presente.
* **Interazione:** L'elaboratore era controllato direttamente tramite interruttori fisici da una consolle.
* **Problemi principali:** L'enorme tempo di preparazione (setup) richiesto per ogni operazione e la totale inefficienza nella schedulazione dei lavori.

### Seconda Generazione (1955–1965): Sistemi a Lotti
* **Tecnologia:** Introduzione dei transistor.
* **Modello Operativo:** Nascono i sistemi a lotti (batch), fisicamente gestiti da un operatore dedicato.
* **Il Monitor:** I lavori (job) venivano raggruppati in lotti sul dispositivo di ingresso; un software primordiale chiamato **Monitor** ordinava in sequenza il caricamento dei programmi e delle utility necessarie. Al termine dell'esecuzione di un lavoro, il controllo della CPU torna automaticamente al Monitor.
* **JCL (Job Control Language):** Per dare istruzioni al Monitor venivano usate schede perforate con comandi e linguaggi di controllo specifici. 
* **Esempio pratico di Job:** Un lotto di schede iniziava tipicamente con comandi come `$JOB`, `$FORTRAN`, seguito da `$LOAD` per caricare il programma, `$RUN` per eseguirlo, fino alla chiusura con `$END`.

![[Pasted image 20260310151811.png]]

---



◀️ *Back to:* [[00_Index_Teoria_OS]]