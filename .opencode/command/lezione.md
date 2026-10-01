---
description: "Pipeline completa di creazione nota. Recupera il materiale, delega la stesura all'agent appunti o materiale, poi aggiorna l'indice del corso."
agent: vault
---

Crea una nota definitiva a partire dal materiale indicato.

Argomenti: `$ARGUMENTS`

Primo elemento: `appunti` oppure `materiale`.
Secondo elemento: il percorso del file di partenza, oppure il corso se l'input sono piu` file.

Se il primo elemento manca, deducilo dal contenuto: se ci sono appunti personali, trascrizioni, bozze o note a voce, e` `appunti`. Se c'e` solo slide, PDF o dispense, e` `materiale`. Se non e` chiaro, chiedi.

## Sequenza

1. **Leggi il file di partenza** per capire il corso, la data della lezione e l'argomento. Non scriverne ancora una versione.

2. **Cerca i placeholder di recupero.** Se nell'appunto ci sono `// slide N //`, `// def ... //`, `// tabella ... //` o simili, delega a `@lettore` l'estrazione delle sezioni indicate dal materiale del corso (`materiale/`). Passa tutte le richieste in una sola delegazione, cosi` il materiale viene letto una volta sola. Se non ci sono placeholder, salta questo passo e non chiamare `lettore`.

3. **Delega la stesura** a `@appunti` oppure `@materiale`, passando: percorso del file di partenza, corso di destinazione, data della lezione, e il testo Recuperato al punto 2. Il writer produce la nota e non tocca l'indice.

4. **Delega l'indice** a `@indici` per registrare la nota nuova nel `00_Index_*.md` del corso. Se il file indice non esiste, crealo seguendo la struttura degli altri indici del vault.

5. **Riportami il risultato**: percorso della nota creata, che cosa hai recuperato dal materiale, che cosa non hai trovato, e che cosa hai lasciato nei raw notes. Non modificare mai i file in `raw_notes/`: sono input.
