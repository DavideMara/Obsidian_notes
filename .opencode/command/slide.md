---
description: Lookup puntuale in una slide o pagina di PDF. Restituisce il testo fedele di quella pagina, per verificare cosa dice davvero il materiale.
agent: lettore
---

Estrai il testo di una singola pagina di PDF.

Numero pagina: `$1`
File: `$2`

Se il file non e` specificato, cerca il PDF plausibile nel `materiale/` del corso e chiedi conferma prima di procedere.

Estrai la pagina con `pdftotext -f N -l N -layout` e riporta il testo fedele. Segnala esplicitamente la parte illeggibile o assente, invece di ricostruirla.
