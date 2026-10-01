#!/usr/bin/env python3
"""Audit strutturale deterministico del vault Obsidian.

Sostituisce i controlli esistenziali che un LLM esegue inaffidabilmente con grep
(frontmatter, link risolti, immagini, callout, indici). Non valuta la qualita' della
prosa: quello resta compito dell'agent revisore.

Uso:
    python3 .opencode/scripts/vault-audit.py [percorso-ambito]

Senza argomento audita tutto il vault. Con un percorso limita l'audit al sottoalbero.
"""

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VAULT = ROOT

# ---------------------------------------------------------------- configurazione

# (prefisso cartella, tag canonico, file indice, mostra footer Navigazione)
COURSES = [
    ("1\u00b0 Anno/Analisi", "Analisi", "00_Index_Analisi.md", False),
    ("1\u00b0 Anno/OOP", "OOP", "00_Index_OOP.md", False),
    ("1\u00b0 Anno/PRP", "ProceduralProgramming", "00_Index_Programmazione_Procedurale.md", False),
    ("2\u00b0 Anno/Algoritmi", "Algoritmi", "00_Index_Algoritmi.md", True),
    ("2\u00b0 Anno/Diritto dell'Informatica e Data Protection", "Diritto", "00_Index_Diritto.md", True),
    ("2\u00b0 Anno/Ingegneria Software", "IngegneriaSoftware", "00_Index_Ingegneria_Software.md", True),
    ("2\u00b0 Anno/Linguaggi Formali", "linguaggi-formali", "00_Index_Linguaggi_Formali.md", True),
    ("2\u00b0 Anno/Sistemi Operativi", "sistemi-operativi", "00_Index_OS.md", True),
    ("3\u00b0 Anno/Base di Dati", "base-di-dati", "00_Index_Base_di_Dati.md", True),
    ("3\u00b0 Anno/Cybersec", "sicurezza-informatica", "00_Index_Cybersecurity.md", True),
    ("3\u00b0 Anno/Introduzione AI", "intelligenza-artificiale", "00_Index_Introduzione_AI.md", True),
    ("3\u00b0 Anno/Programmazione Web", "programmazione-web", "00_Index_Programmazione_Web.md", True),
    ("3\u00b0 Anno/Reti", "reti", "00_Index_Reti.md", True),
    ("Erasmus_Spagna/data-structure", "DataStructure", "00_Index_Data_Structure_Erasmus.md", False),
    ("Erasmus_Spagna/introduction-computer-network", "IntroductionComputerNetwork", "00_Index_Introduction_Computer_Network_Erasmus.md", False),
    ("Erasmus_Spagna/software-engineering", "SoftwareEngineering", "00_Index_Software_Engineering_Erasmus.md", False),
]

# Tag non-corso ammessi, piu' i sotto-tag tematici del corso di Diritto.
EXTRA_TAGS = {
    "appunti", "Erasmus", "Index", "LectureNotes", "lezione",
    "AI", "NeuroEtica", "GDPR", "Blockchain", "Contratti",
    "teoriaSO", "labSO",
}

# Frontmatter ammesso sulle note di contenuto.
NOTE_KEYS = {"date", "tags", "type", "subject", "updated"}
LEGACY_KEYS = {"data", "titolo", "stato"}
NOTE_TYPES = {"lezione", "esercizi", "riferimento"}

# Unica eccezione all'obbligo di indicizzazione: appunti provvisori, non note di
# lezione. Elenco dichiarato, non dedotto dal nome.
AUX_NOTES = {"OS_Lab_quick_notes"}

# Tipi di callout nativi di Obsidian, in minuscolo: il confronto e' case-insensitive
# perche' Obsidian accetta `[!Info]`, `[!INFO]` e `[!info]` identici. Un tipo fuori
# da questo elenco non e' un errore: Obsidian renderizza anche i callout personalizzati
# (qui `[!LAW]` per il diritto, `[!nota]` per le note a voce).
CALLOUT_TYPES = {
    "note", "abstract", "summary", "tldr", "info", "todo", "tip", "hint",
    "important", "success", "check", "done", "question", "help", "faq",
    "warning", "caution", "attention", "failure", "fail", "missing",
    "danger", "error", "bug", "example", "quote", "cite",
}

# Punteggiatura Unicode vietata dalle regole del vault.
FORBIDDEN = {
    "\u2014": "em-dash", "\u2013": "en-dash", "\u2192": "freccia ->",
    "\u2190": "freccia <-", "\u2194": "freccia <->", "\u21d2": "freccia =>",
    "\u201c": "smart quote doppia", "\u201d": "smart quote doppia",
    "\u2018": "smart quote singola", "\u2019": "smart quote singola",
    "\u2026": "ellipsis", "\u2713": "checkmark", "\u2705": "check",
    "\u274c": "X", "\u2022": "bullet", "\u00a0": "spazio unificatore",
}

# Documentazione tecnica: contiene placeholder come nome_immagine.png per
# costruzione, non sono riferimenti rotti.
DOCS = {"AGENTS.md", "Guida_Opencode.md", "opencode.json"}
DOCS_PREFIX = ("prompts/", ".opencode/")

# ---------------------------------------------------------------- raccolta file


def all_files():
    """Tutti i file del vault, esclusi .git e .obsidian."""
    out = []
    for dirpath, dirnames, filenames in os.walk(VAULT):
        rel = os.path.relpath(dirpath, VAULT)
        parts = [] if rel == "." else rel.split(os.sep)
        if parts and parts[0] in (".git", ".obsidian"):
            continue
        dirnames[:] = [d for d in dirnames if d not in (".git", ".obsidian")]
        for name in filenames:
            out.append(os.path.normpath(os.path.join(rel, name)))
    return out


def is_markdown(path):
    return path.endswith(".md")


def is_doc(path):
    name = os.path.basename(path)
    return name in DOCS or path.startswith(DOCS_PREFIX)


def is_index(path):
    return os.path.basename(path).startswith("00_Index")


def is_raw(path):
    return os.path.sep + "raw_notes" + os.path.sep in path


def is_meta_root(path):
    """File .md alla radice del vault: documenti di servizio, senza frontmatter."""
    return os.path.dirname(path) == "" and is_markdown(path)


def is_lesson(path):
    """Nota di contenuto: dentro lezioni/, fuori da raw_notes e dagli indici."""
    if not is_markdown(path) or is_index(path) or is_raw(path) or is_meta_root(path):
        return False
    return os.path.sep + "lezioni" + os.path.sep in path


def course_of(path):
    for prefix, tag, index, footer in COURSES:
        if path == prefix or path.startswith(prefix + os.sep):
            return prefix, tag, index, footer
    return None


# ------------------------------------------------------------------- mascheramento


def mask_code(text):
    """Sostituisce con spazi fence e inline code, conservando offset e righe.

    Serve a non scambiare la sintassi condizionale Bash [[ -f x ]] e gli esempi
    inline come <img src="..."> per riferimenti rotti.
    """
    out = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        # Un fence puo' stare dentro un blockquote (`> ```bash`), che e' il modo
        # normale di mettere codice in un callout. Togliendo i marcatori di
        # blockquote prima di controllare, si riconoscono anche quelli: altrimenti
        # il contenuto del callout non viene mascherato e `if [[ -f x ]]` viene
        # scambiato per un wikilink.
        probe = re.sub(r"^[ \t]*(?:>[ \t]?)+", "", line).lstrip()
        if probe.startswith("```") or probe.startswith("~~~"):
            in_fence = not in_fence
            out.append(" " * (len(line.rstrip("\n"))) + line[len(line.rstrip("\n")):])
            continue
        if in_fence:
            out.append(" " * (len(line.rstrip("\n"))) + line[len(line.rstrip("\n")):])
            continue
        masked = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), line)
        out.append(masked)
    return "".join(out)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


# -------------------------------------------------------------------- findings

findings = []


def add(severity, check, path, line, message):
    findings.append((severity, check, path, line, message))


def parse_frontmatter(text):
    """Ritorna (dict, riga_chiusura) o (None, 0) se non c'e' frontmatter."""
    if not text.startswith("---"):
        return None, 0
    match = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", text, re.S)
    if not match:
        return None, 0
    body = match.group(1)
    data = {}
    key = None
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^([A-Za-z0-9_-]+):[ \t]*(.*)$", line)
        if item:
            key = item.group(1)
            data[key] = item.group(2).strip()
        elif key is not None and line.lstrip().startswith("- "):
            data.setdefault("__list__", []).append(line.lstrip()[2:].strip())
    if "tags" in data and data.get("__list__"):
        data["tags"] = data.pop("__list__")
    else:
        data.pop("__list__", None)
    return data, text.count("\n", 0, match.end())


# --------------------------------------------------------------- i nove controlli


def check_frontmatter(md):
    for path in md:
        text = read(path)
        data, _ = parse_frontmatter(text)
        info = course_of(path)

        if data is None:
            # I raw_notes sono input del processo, mai note da completare: segnalare
            # che non hanno frontmatter sarebbe un invito a modificarli.
            if not is_meta_root(path) and not is_raw(path):
                add("INFO", "frontmatter", path, 0, "nessun frontmatter")
            continue

        tags = data.get("tags")
        tag_list = tags if isinstance(tags, list) else ([tags] if tags else [])
        tag_list = [t for t in tag_list if t]

        for key in LEGACY_KEYS:
            if key in data:
                add("WARN", "frontmatter", path, 0,
                    "chiave legacy `%s` (usare `date`)" % key)

        for key in data:
            if key not in NOTE_KEYS and key not in LEGACY_KEYS:
                add("INFO", "frontmatter", path, 0, "chiave non standard `%s`" % key)

        if is_index(path):
            extra = set(data) - {"tags"}
            if extra:
                add("WARN", "frontmatter", path, 0,
                    "indice con campi extra: %s (solo `tags`)" % ", ".join(sorted(extra)))
            continue

        if not tag_list:
            add("ERROR", "frontmatter", path, 0, "nessun tag")
        if "type" in data and data["type"] not in NOTE_TYPES:
            add("WARN", "frontmatter", path, 0,
                "type `%s` non in %s" % (data["type"], sorted(NOTE_TYPES)))
        # Una chiave assente non e' la stessa cosa di una chiave sbagliata: le date
        # di alcune note non sono ricostruibili (l'unica data in git e' quella
        # d'importazione del vault, che non e' la data della lezione). Si segnala
        # come INFO da compilare, non come WARN: inventare una data e' peggio.
        for key in ("date", "type"):
            if key not in data:
                add("INFO", "frontmatter", path, 0,
                    "manca `%s` nel frontmatter (da compilare)" % key)
        if "date" in data and not re.match(r"^\d{4}-\d{2}-\d{2}$", data["date"]):
            add("WARN", "frontmatter", path, 0, "date `%s` non in YYYY-MM-DD" % data["date"])

        if info and info[1] not in tag_list:
            add("ERROR", "tag", path, 0,
                "manca il tag canonico `%s` (presenti: %s)"
                % (info[1], ", ".join(tag_list) or "nessuno"))


def check_links(md, stems, headings, by_stem):
    patterns = [
        ("wikilink", re.compile(r"(?<!!)\[\[([^\]\n]*)\]\]")),
    ]
    for path in md:
        text = read(path)
        masked = mask_code(text)
        for kind, pattern in patterns:
            for match in pattern.finditer(masked):
                raw = match.group(1)
                target = raw.split("|")[0].strip()
                line = line_of(masked, match.start())
                if not target:
                    add("ERROR", "link", path, line, "wikilink vuoto")
                    continue
                # `[[File]]`, `[[File#ancora]]` e `[[#ancora]]` sono tre casi distinti.
                # Ridurre tutto al nome del file faceva fallire i 35 link con ancora
                # verso un'altra nota, che sono tutti legittimi.
                where, _, anchor = target.partition("#")
                where = where.strip()
                anchor = anchor.strip().lower()
                if not where:
                    if anchor and anchor not in (headings.get(path) or set()):
                        add("ERROR", "link", path, line,
                            "ancora `#%s` inesistente in questo file" % target[1:])
                    continue
                stem = os.path.splitext(os.path.basename(where))[0]
                if stem not in stems:
                    add("ERROR", "link", path, line, "wikilink rotto `%s`" % where)
                    continue
                if not anchor:
                    continue
                # L'ancora si puo' verificare solo se il nome punta a un file
                # univoco: con due file omonimi l'ancora e' ambigua e il confronto
                # produrrebbe falsi positivi.
                dest = by_stem.get(stem)
                if dest and anchor not in (headings.get(dest) or set()):
                    add("WARN", "link", path, line,
                        "ancora `#%s` non trovata in %s" % (anchor, dest))


def check_images(md, files, stems):
    referenced = set()
    embed = re.compile(r"!\[\[([^\]\n|]+?)(?:\|[^\]\n]*)?\]\]|<img\s[^>]*src=[\"']([^\"']+)[\"']")
    for path in md:
        text = read(path)
        masked = mask_code(text)
        for match in embed.finditer(masked):
            name = (match.group(1) or match.group(2) or "").strip()
            if not name:
                continue
            stem = os.path.splitext(os.path.basename(name))[0]
            referenced.add(stem)
            if stem not in stems:
                add("ERROR", "immagine", path, line_of(masked, match.start()),
                    "embed verso file inesistente `%s`" % name)

    exts = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp")
    orphans = sorted(
        p for p in files
        if p.lower().endswith(exts)
        and os.path.splitext(os.path.basename(p))[0] not in referenced
    )
    # Le immagini dentro materiale/ sono state estratte dai PDF del docente: non
    # sono da indicizzare, sono il materiale stesso, e AGENTS.md lo dice esplicitamente.
    # Elencarle una per una produce 75 righe di rumore. Solo le immagini in
    # attachments/ sono state incollate dall'utente, e li' un orphan e' un sospetto.
    pasted = [p for p in orphans if p.startswith("attachments" + os.sep)]
    for path in pasted:
        add("INFO", "immagine", path, 0, "immagine incollata ma non usata in nessuna nota")
    if len(orphans) > len(pasted):
        add("INFO", "immagine", "(riassunto)", 0,
            "%d immagini sotto materiale/ non sono referenziate da nessuna nota "
            "(atteso: sono estratte dai PDF, non vanno indicizzate)"
            % (len(orphans) - len(pasted)))


def check_footer(md):
    for path in md:
        info = course_of(path)
        if not info or not info[3] or not is_lesson(path):
            continue
        if "## \u23ed\ufe0f Navigazione Lezioni" not in read(path):
            add("WARN", "footer", path, 0, "manca `## Navigazione Lezioni`")


# Check e croci compaiono solo in 1° Anno/Analisi/lezioni/Esercizi_Capitolo_1.md, dove
# marcano la risposta corretta o sbagliata di ogni esercizio. E' una convenzione
# didattica, non fluff: si segnala come INFO, non come violazione.
CONVENTIONAL = {"\u2705", "\u274c"}


def check_chars(md):
    # Non si maschera il codice: secondo le regole del vault i caratteri vietati
    # sono vietati anche dentro esempi e output di terminale.
    for path in md:
        # I raw_notes sono input: segnalare caratteri vietati dentro le trascrizioni
        # non serve a nulla, perche' l'unico modo di risolverli e'.modificarli.
        if is_raw(path):
            continue
        for num, line in enumerate(read(path).splitlines(), 1):
            for char, name in FORBIDDEN.items():
                if char not in line:
                    continue
                if char in CONVENTIONAL:
                    add("INFO", "caratteri", path, num,
                        "%s U+%04X (convenzione didattica, valutare a mano)"
                        % (name, ord(char)))
                else:
                    add("WARN", "caratteri", path, num, "%s U+%04X" % (name, ord(char)))


def check_callouts(md):
    """Due soli controlli precisi: il `>` attaccato al marker e il tipo inesistente.

    Non si segnala una riga che contiene semplicemente `[!...]`: dentro un
    blockquote quella e' la forma valida `> [!INFO]`, e `![[immagine]]` non e'
    un callout.
    """
    bad_marker = re.compile(r"^>\[!(\w+)\]")
    typed = re.compile(r"^>\s*\[!(\w+)\]")
    for path in md:
        if is_raw(path):
            continue
        masked = mask_code(read(path))
        for num, line in enumerate(masked.splitlines(), 1):
            if bad_marker.match(line):
                add("WARN", "callout", path, num,
                    "`>%s` senza spazio: Obsidian non lo renderizza come callout"
                    % line[1:].strip())
                continue
            match = typed.match(line)
            if match and match.group(1).lower() not in CALLOUT_TYPES:
                add("INFO", "callout", path, num,
                    "callout personalizzato `[!%s]` (renderizza, non e' nativo)"
                    % match.group(1))


def check_indices(md, stems, files):
    for prefix, tag, index_name, footer in COURSES:
        index_path = os.path.join(prefix, index_name)
        if not os.path.isfile(os.path.join(VAULT, index_path)):
            add("WARN", "indice", index_path, 0, "file indice mancante")
            continue
        text = read(index_path)
        masked = mask_code(text)

        entries = defaultdict(int)
        listed = set()
        for match in re.finditer(r"\[\[([^\]\n]*)\]\]", masked):
            raw = match.group(1)
            full = raw.split("|")[0].strip()
            target = full.split("#")[0].strip()
            if not target:
                add("ERROR", "indice", index_path, line_of(masked, match.start()),
                    "voce `- [[]]` vuota")
                continue
            stem = os.path.splitext(os.path.basename(target))[0]
            # Solo `00_` e' un indice. Le lezioni iniziano con `01_`-`99_`, quindi la
            # vecchia euristica "inizia con 0 seguito da una cifra" le scartava come
            # se fossero altri indici, e poi le segnalava come non indicizzate.
            if stem.startswith("00_"):
                continue  # rimando a altro indice o hub
            listed.add(stem)
            # La chiave e' il link integrale, alias compreso. Un PDF unico citato
            # come "Parte 18", "Parte 19", ... e' la struttura normale di un
            # dispense spezzata, non una voce duplicata: conta solo il link identico.
            entries[raw.strip()] += 1
            if stem not in stems:
                add("ERROR", "indice", index_path, line_of(masked, match.start()),
                    "voce punta a file inesistente `%s`" % target)

        for raw, count in sorted(entries.items()):
            if count > 1:
                add("WARN", "indice", index_path, 0,
                    "`%s` listato %d volte" % (raw, count))

        on_disk = {
            os.path.splitext(os.path.basename(p))[0]
            for p in files
            if p.startswith(prefix + os.sep) and is_lesson(p)
        }
        # Ogni nota di lezioni/ va indicizzata, con o senza numerazione:
        # `Appunti_Completi_Diritto` non ha numero ma e' una raccolta di lezioni
        # vera e propria, quindi la si indexa come tutte le altre. L'unica
        # eccezione sono i file di appoggio elencati in AUX_NOTES, che sono
        # dichiarati uno per uno perche' non sono note di lezione.
        for stem in sorted(on_disk - listed - AUX_NOTES):
            add("WARN", "indice", index_path, 0,
                "nota `%s.md` presente ma non indicizzata" % stem)


# ------------------------------------------------------------------------- main

_cache = {}


def read(path):
    full = os.path.join(VAULT, path)
    if full not in _cache:
        with open(full, encoding="utf-8", errors="replace") as handle:
            _cache[full] = handle.read()
    return _cache[full]


def main():
    scope = sys.argv[1] if len(sys.argv) > 1 else None
    files = all_files()
    if scope:
        scope = scope.rstrip("/")
        files = [p for p in files if p == scope or p.startswith(scope + os.sep)]

    md = [p for p in files if is_markdown(p) and not is_doc(p)]
    stems = {os.path.splitext(os.path.basename(p))[0] for p in files}
    # stem -> percorso, solo per gli stem univoci. Con due file omonimi la
    # corrispondenza e' ambigua, quindi non la si usa per validare le ancore.
    first_seen = {}
    ambiguous = set()
    for p in files:
        stem = os.path.splitext(os.path.basename(p))[0]
        if stem in first_seen:
            ambiguous.add(stem)
        else:
            first_seen[stem] = p
    by_stem = {s: p for s, p in first_seen.items() if s not in ambiguous}
    headings = {}
    for path in md:
        text = read(path)
        found = set()
        for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*$", mask_code(text)):
            found.add(re.sub(r"[#*`]", "", match.group(1)).strip().lower())
        headings[path] = found

    check_frontmatter(md)
    check_links(md, stems, headings, by_stem)
    check_images(md, files, stems)
    check_footer(md)
    check_chars(md)
    check_callouts(md)
    check_indices(md, stems, files)

    if not findings:
        print("Nessun problema rilevato su %d file markdown." % len(md))
        return

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda f: (order[f[0]], f[1], f[2], f[3]))

    counts = defaultdict(int)
    for severity, check, path, line, message in findings:
        counts[severity] += 1

    print("=" * 72)
    print("AUDIT STRUTTURALE DEL VAULT")
    print("ambito: %s" % (scope or "vault intero"))
    print("file markdown analizzati: %d" % len(md))
    print("ERROR %d   WARN %d   INFO %d" % (counts["ERROR"], counts["WARN"], counts["INFO"]))
    print("=" * 72)

    per_check = defaultdict(list)
    for finding in findings:
        per_check[finding[1]].append(finding)

    labels = {
        "link": "Link rotti o vuoti",
        "immagine": "Immagini",
        "indice": "Indici",
        "tag": "Tag canonici",
        "frontmatter": "Frontmatter",
        "callout": "Callout",
        "footer": "Footer di navigazione",
        "caratteri": "Caratteri vietati",
    }
    for check in sorted(per_check, key=lambda c: order[per_check[c][0][0]]):
        group = per_check[check]
        print()
        print("--- %s (%d) ---" % (labels.get(check, check), len(group)))
        shown = 0
        for severity, _, path, line, message in group:
            if shown >= 15:
                print("    ... altri %d non mostrati (passa il path come argomento perli)"
                      % (len(group) - shown))
                break
            where = "%s:%d" % (path, line) if line else path
            print("  [%s] %s" % (severity, where))
            print("        %s" % message)
            shown += 1

    print()
    print("I controlli su prosa, struttura argomentativa e fluff restano all'agent revisore.")


if __name__ == "__main__":
    main()
