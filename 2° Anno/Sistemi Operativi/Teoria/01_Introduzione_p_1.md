---
date: 2026-02-25
tags:
  - "#sistemi-operativi"
  - teoriaSO
type: lezione
---

# Sistemi Operativi - Introduzione

## 1. Cos'è e quali sono i suoi compiti

### Ruolo di Interfaccia
```mermaid
graph LR
    APP["<b>Applicazioni</b>"] -- "Richiedono Servizi" --> OS["<b>Sistema Operativo</b>"]
    OS -- "Gestisce Risorse" --> HW["<b>Hardware</b>"]
    HW -- "Risponde / Notifica" --> OS
    OS -- "Ritorna Risultati" --> APP
```

### Obiettivi Principali
```mermaid
graph TD
    OBJ["<b>Sviluppo OS</b>"]
    OBJ -- "Punta alla" --> OBJ1["<b>Convenienza</b><br/>(Facilità per l'utente)"]
    OBJ -- "Punta alla" --> OBJ2["<b>Efficienza</b><br/>(Ottimizzazione HW)"]
    OBJ -- "Punta alla" --> OBJ3["<b>Evoluzione</b><br/>(Nuove funzioni/HW)"]
```

### Posizionamento Firmware
```mermaid
graph TD
    OS["<b>OS</b>"] -- "Si appoggia a" --> FW["<b>Firmware</b>"]
    FW -- "Controlla / Inizializza" --> HW["<b>Hardware</b>"]
```

<div style="page-break-after: always;"></div>

---

## 2. Sistema Di Elaborazione

### Servizi Erogati
```mermaid
graph TD
    S["<b>L'OS Eroga:</b>"]
    S -- "Caricamento/Run" --> S1["Esecuzione Programmi"]
    S -- "Driver/Standard" --> S2["Gestione I/O"]
    S -- "Protezione/Organizzazione" --> S3["File System"]
    S -- "Login/Permessi" --> S4["Sicurezza"]
    S -- "Debug/Monitoring" --> S5["Gestione Errori"]
    S -- "Tracciamento Consumi" --> S6["Accounting"]
```

### Gerarchia delle Interfacce
```mermaid
graph BT
    ISA["<b>ISA</b><br/>(Hardware)"] -- "Definisce Set Istruzioni" --> ABI["<b>ABI</b><br/>(Linguaggio Binario)"]
    ABI -- "Espone ai Programmatori" --> API["<b>API</b><br/>(Librerie/Utility)"]
```

<div style="page-break-after: always;"></div>

---

## 3. La Gestione delle Risorse e il Controllo della CPU

### Ciclo del Controllo CPU
```mermaid
graph LR
    OS["<b>Sistema Operativo</b>"] -- "Context Switch" --> APP["<b>App / Processo</b>"]
    APP -- "Sospensione / System Call" --> HW["<b>Hardware</b>"]
    HW -- "Segnale di Interrupt" --> OS
```

### Meccanismo di Ritorno
```mermaid
graph TD
    HWS["<b>Hardware (CPU)</b>"] -- "Rileva Anomalia/Task" --> INT["<b>INTERRUPT</b>"]
    INT -- "Forza il Salto a" --> OSR["<b>Codice OS</b>"]
```

<div style="page-break-after: always;"></div>

---

## 4. L'Evoluzione dei Sistemi Operativi

### Prima Generazione (1945-1955)
```mermaid
graph TD
    T1["<b>Valvole</b>"] -- "Causano" --> T2["<b>Nessun OS</b>"]
    T2 -- "Richiede" --> T3["<b>Controllo Manuale</b><br/>(Interruttori fisici)"]
```

### Seconda Generazione (1955-1965)
```mermaid
graph TD
    direction TB
    TECH["<b>Transistor</b>"] -- "Permettono" --> SYS["<b>Sistemi a Lotti</b>"]
    SYS -- "Gestiti dal" --> MON["<b>MONITOR</b><br/>(Primo Software OS)"]
    MON -- "Riceve Comandi da" --> CMD["<b>JCL</b><br/>(Schede Perforate)"]
```

---

◀️ *Back to:* [[00_Index_OS]]
