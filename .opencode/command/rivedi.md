---
description: "Revisione qualitativa di note o modifiche: prosa, registro, struttura, callout, formule, terminologia, allineamento col materiale. Produce un report senza modificare nulla."
agent: revisore
---

Esegui la revisione qualitativa.

Cosa rivedere: `$ARGUMENTS`

Puo` essere:
- un percorso di note (per esempio `3° Anno/Cybersec/lezioni`)
- un file singolo
- `diff`, per rivedere solo le modifiche non ancora committate
- `ultime N`, per rivedere le ultime N lezioni di un corso

Se l'argomento e` vuoto, chiedi cosa rivedere invece di indovinare.

Per `diff`, usa `git diff` e `git diff --staged`. Non eseguire mai comandi git che scrivono: niente `add`, `commit`, `checkout`, `restore`, `reset`, `stash`.

Valuta solo cio` che rientra nel tuo mandato: prosa, registro, struttura, callout, terminologia, formule, allineamento col materiale. I controlli di esistenza li fa `/revisione`, non rifarli.
