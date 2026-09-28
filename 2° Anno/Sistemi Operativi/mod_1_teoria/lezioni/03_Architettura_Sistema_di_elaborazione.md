---
date: 2026-03-04
tags:
  - sistemi-operativi
  - teoriaSO
type: lezione
---
# Architettura del Sistema di Elaborazione
## 1. Unità Centrale (CPU) e Componenti


![[Pasted image 20260310163023.png]]
L'unità centrale (CPU) è il cuore del sistema di elaborazione, interconnessa tramite il System Bus alla Main Memory e ai moduli di I/O.
* **Microprocessore:** Un processore realizzato su un singolo chip, spesso chiamato *core*.
* **Multiprocessore:** Architetture che integrano più processori **(core)** su un unico chip **(socket)** per parallelizzare le operazioni.
* **Memoria Cache:** Il processore è dotato di memoria cache interna.

> [!INFO]  Cache
> E' una memoria molto più veloce rispetto a quella principale. È la prima memoria a cui il processore accede per velocizzare il recupero delle informazioni più usate.

Oltre alla CPU standard, i sistemi moderni integrano processori specializzati:
* **GPU (Processore Grafico):** avendo a disposizione molti core computa su array di dati utilizzando la tecnica **SIMD** (Single-Instruction Multiple-Data). 
* **DSP (Processore di Segnale Digitale):** Si occupa specificamente della codifica e decodifica di segnali audio e video.
* **SoC (System on a Chip):** Un intero sistema su un singolo chip, dotato anche di supporto crittografico, tipicamente utilizzato per smartphone e palmari.
### Ciclo Fetch-Execute

![[Pasted image 20260310164508.png]]

Per l'esecuzione dei programmi Il processore segue un ciclo continuo chiamato **"Fetch-Execute"** (Estrai ed Esegui).

**Fetch Stage**: Il processore estrae la prossima istruzione da eseguire dalla memoria.
**Execute Stage:** Il processore esegue l'istruzione estratta.
	Le **istruzioni** elaborate in questo ciclo si dividono in diverse tipologie:
	    * Interazioni **Processore - Memoria**.
	    * Interazioni **Processore - I/O**.
	    * **Elaborazione dei dati** vera e propria.
	    * Istruzioni di **Controllo** (come i salti/goto).

---

## 3. Le Interruzioni (Interrupts)

In un ciclo fetch-execute a meno che che non sia disabilitato il **sistema d'interruzione** si passa al controllo delle interruzzioni, se c'è si salta da qualche altra parte del programma dove si gestisce **l'interruzzione** e si mette il programma in pausa.

Le interruzioni sono meccanismi fondamentali che permettono agli altri moduli del sistema (come le periferiche I/O) di interrompere il normale ciclo fetch-execute del processore.

> [!INFO] Vantaggi delle Interruzioni
> Grazie alle interruzioni, si evita di lasciare la CPU inattiva in attesa che un'operazione lenta di I/O finisca. Il processore può sospendere l'esecuzione di un programma corrente per gestire l'evento, ottimizzando l'uso delle proprie risorse.

Le interruzioni si dividono in quattro classi principali:
1. **Programma:** Generate da errori nell'esecuzione di un programma (es. overflow o eccezioni di indirizzo).
2. **Timer:** Permettono al sistema operativo di eseguire funzioni critiche a intervalli regolari.
3. **I/O:** Generate da un controllore I/O per segnalare il completamento di un'operazione o per notificare un errore.
4. **Errori HW:** Generate da problemi fisici dell'hardware.
### Gestione interruzioni

![[Pasted image 20260310170225.png]]

* **Interruzioni Multiple:** Quando si verificano più interruzioni contemporaneamente o in rapida sequenza, il sistema può adottare due approcci: mantenere le interruzioni disabilitate durante la gestione dell'interruzione corrente, oppure implementare uno schema a priorità di questo tipo :

*![[Pasted image 20260310170351.png]]

---
## ⏭️ Navigazione Lezioni

- **Index Corso :** [[00_Index_OS]]