---
description: "Audit strutturale deterministico del vault. Verifica link, immagini, frontmatter, tag canonici, indici, callout e caratteri vietati. Non modifica nulla."
agent: vault
---

Esegui l'audit strutturale del vault.

Ambito: `$1`

Se l'argomento e` vuoto, audita tutto il vault. Altrimenti e` il percorso di un corso (per esempio `3° Anno/Cybersec`) o di una cartella, e l'audit si limita a quel sottoalbero.

Esegui:

```
python3 .opencode/scripts/vault-audit.py $1
```

Lo script e` deterministico: non ricalcolare i suoi risultati con `grep` e non aggiungere controlli di esistenza tuoi. Riporta il suo output, riorganizzato per gravita' e per tipo di problema, e segnala esplicitamente i file con piu` rilievi.

Poi, in massimo cinque righe, indica gli interventi che merita la coda ERROR, quelli che merita la coda WARN, e lascia gli INFO come promemoria. Non correggere nulla e non lanciare `@revisore`: quello e' un controllo qualitativo, e i 9 check strutturali non gli competono piu`.
