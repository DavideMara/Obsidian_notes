---
date: 2026-10-01
tags:
  - reti
type: lezione
---
# Internetworking: Le Reti di Reti

Il concetto di **Internetworking** fa riferimento all'interconnessione di reti distinte per formare una rete più ampia, creando delle vere e proprie "autostrade elettroniche" per collegare tra loro isole di connettività.

> [!IMPORTANT] Definizione di Internetworking
> L'Internetworking consiste nella capacità di interconnettere reti di calcolatori eterogenee (diverse per architettura, tecnologia, protocollo e ambito geografico) in modo da permettere la comunicazione end-to-end tra nodi appartenenti a reti differenti, dando vita a un'unica infrastruttura logica globale.

## I. Principi Fondamentali dell'Internetworking

L'interconnessione di più reti presenta diverse sfide tecniche che devono essere risolte per garantire un funzionamento trasparente:

- **Eterogeneità delle reti:** Le reti da interconnettere possono utilizzare tecnologie diverse (Ethernet, Wi-Fi, ATM, fibra ottica, ecc.).
- **Indipendenza amministrativa:** Ogni rete può avere una propria amministrazione e policy di gestione.
- **Scalabilità:** Il sistema deve poter crescere senza compromettere le prestazioni globali.
- **Trasparenza:** L'utente finale deve percepire l'intera infrastruttura come una singola rete unificata.

## II. Dispositivi di Interconnessione

Per realizzare l'interconnessione tra reti differenti, vengono utilizzati apparati specifici operanti a diversi livelli dello stack protocollare:

| Dispositivo | Livello OSI | Funzione |
|---|---|---|
| **Repeater** | Livello 1 (Fisico) | Rigenera e amplifica il segnale, estendendo la portata del mezzo fisico. Non opera a livello logico. |
| **Hub** | Livello 1 (Fisico) | Ripete il segnale su tutte le porte. Oggi in disuso a favore degli switch. |
| **Bridge** | Livello 2 (Data Link) | Connettono segmenti di rete dello stesso tipo, filtrando il traffico in base agli indirizzi MAC. |
| **Switch** | Livello 2 (Data Link) | Evoluzione dei bridge, con commutazione per porta e maggiore efficienza. Può operare anche a Livello 3 (Switch multilayer). |
| **Router** | Livello 3 (Network) | Dispositivo chiave per l'Internetworking. Instrada i pacchetti tra reti diverse, basandosi sugli indirizzi logici (IP) e sulle tabelle di routing. |
| **Gateway** | Livello 4+ (Trasporto/App) | Può operare a livelli superiori, traducendo protocolli o formati tra ambienti eterogenei. |

> [!IMPORTANT] Il Ruolo del Router
> Il **router** rappresenta l'elemento fondamentale dell'Internetworking: analizza l'indirizzo IP di destinazione di ciascun pacchetto, consulta la propria tabella di instradamento e decide il percorso ottimale per inoltrarlo verso la rete di destinazione.

## III. Il Concetto di Rete di Reti

L'Internet stesso rappresenta l'esempio paradigmatico di Internetworking: un insieme globale di migliaia di reti autonome (Autonomous Systems - AS) interconnesse tra loro, che comunicano utilizzando un protocollo comune (IP) e formano un'unica infrastruttura logica planetaria.

> [!INFO] Internet come Internetwork
> Il termine "Internet" deriva proprio da *Inter-Network*, ovvero "rete di reti". Non è una singola rete, ma la sovrapposizione logica di innumerevoli reti fisicamente distinte, unite dal protocollo IP.

---
## ⏭️ Navigazione Lezioni
- **Modulo 1 - Lezione precedente :** [[01_Introduzione_Architettura_Reti]]
- **Index Corso :** [[00_Index_Reti]]