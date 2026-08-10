---
tags:
  - ProceduralProgramming
  - ExamPrep
  - CodeTracing
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#06-expressions--operators]] | [[PRP_Complete_Notes#07-statements]]

# 🔄 Tipologia 2: Tracing di Codice C, Cicli e Precedenza degli Operatori

Questa tipologia di esercizio (presente in tutti i testi d'esame con punteggio da 6 punti) richiede di simulare l'esecuzione passo-passo di un programma C complesso e determinare **esattamente l'output stampato a schermo**.

---

## 📐 Teoria e Regole di Riferimento (`PRP_Complete_Notes.md`)

I riferimenti teorici principali nelle note si trovano in **[[PRP_Complete_Notes#06-expressions--operators]]** e **[[PRP_Complete_Notes#07-statements]]**.

### 1. Basi Numeriche e Letterali Interi
* **Ottale:** Prefisso `0` (es. `073` = $7 \times 8^1 + 3 \times 8^0 = 59$; `025` = $2 \times 8 + 5 = 21$; `012` = $1 \times 8 + 2 = 10$).
* **Esadecimale:** Prefisso `0x` o `0X` (es. `0x1E` = $1 \times 16 + 14 = 30$; `0x1A` = $26$; `0x0F` = $15$; `0xa` = $10$).

### 2. Operatori Bitwise e Shift
* `&` (AND bit a bit): $1 \ \& \ 1 = 1$, altrimenti $0$.
* `|` (OR bit a bit): $0 \ | \ 0 = 0$, altrimenti $1$.
* `^` (XOR bit a bit): bit diversi $\rightarrow 1$, uguali $\rightarrow 0$.
* `>>` (Shift a destra): `a >>= 1` equivale a dividere `a` per $2$ (divisione intera).
* `<<` (Shift a sinistra): `a <<= 1` equivale a moltiplicare `a` per $2$.

### 3. Operatori Logici e Short-Circuit Evaluation
* `&&` (AND logico): Valuta il primo operando. Se è $0$ (falso), il secondo operando **non viene valutato** (corto circuito).
* `||` (OR logico): Valuta il primo operando. Se è diverso da $0$ (vero), il secondo operando **non viene valutato**.

### 4. Operatore Virgola `,` ed Operatore Ternario `?:`
* **Operatore Virgola (`,`):** Valuta l'espressione di sinistra, scarta il risultato, valuta l'espressione di destra e restituisce il valore di quest'ultima. Garantisce un *sequence point*.
* **Operatore Ternario (`cond ? expr1 : expr2`):** Valuta `cond`. Se diversa da 0 valuta solo `expr1`, altrimenti valuta solo `expr2`.

### 5. Incremento / Decremento (`++a`, `a++`, `--a`, `a--`)
* Prefisso (`++a`, `--a`): Modifica il valore della variabile **prima** che l'espressione in cui compare venga valutata.
* Postfisso (`a++`, `a--`): Restituisce il valore originale della variabile nell'espressione e incrementa/decrementa la variabile **dopo** (entro il prossimo sequence point).

---

## 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

1. **Converti tutte le costanti in decimale:**
   - Converti immediatamente ottali e esadecimali in decimale su un foglio di brutta.
2. **Crea una tabella di tracciamento dello stato (Trace Table):**
   - Colonne: `Iterazione | Variabile a | Condizione Ciclo | Modifiche Intermedie | Output Stampa`.
3. **Fai molta attenzione al cortocircuito (`||` e `&&`):**
   - In `if (a == 6 || a-- == 10)`, se `a == 6` è VERO, `a-- == 10` NON viene eseguito e `a` NON viene decrementato!
4. **Traccia attentamente gli incrementi e le istruzioni di salto (`break`, `continue`, `goto`):**
   - Ricorda che `continue` salta il resto del corpo del ciclo e passa all'incremento/test successivo.
   - `break` interrompe ed esce immediatamente dal ciclo.

---

## 📑 Analisi degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 3 Giugno 2026 (Esercizio 2)
**Codice:**
```c
int a = 0x1E & 073;
printf("%d\n", a);
while (a % 2 == 0 ? (a >>= 1, a) : (a += 3, 1)) {
    printf("%d\n", a);
    if (a == 6 || a-- == 10) {
        a *= 2;
        break;
    }
    a -= 1;
}
printf("a: %d\n", a);
```

**Tracciamento Passo-Passo:**
1. **Inizializzazione:**
   - `0x1E` = $30 = 00011110_2$.
   - `073` = $59 = 00111011_2$.
   - `a = 30 & 59`:
     ```text
       00011110 (30)
     & 00111011 (59)
     --------------
       00011010 (26)
     ```
   - **Stampa 1:** `26`

2. **Ciclo `while`:**
   - **Iterazione 1:**
     - Test `while`: `a % 2 == 0` ($26 \% 2 == 0$, VERO).
     - Esegue raggio VERO del ternario: `(a >>= 1, a)`. `a >>= 1` $\rightarrow a = 13$. Restituisce `13` (diverso da 0 $\rightarrow$ VERO).
     - **Stampa 2:** `13`
     - Test `if`: `a == 6` (FALSO). Esegue `a-- == 10` ($13 == 10$, FALSO, poi `a` diventa `12`).
     - Esegue `a -= 1` $\rightarrow a = 11$.
   - **Iterazione 2:**
     - Test `while`: `a % 2 == 0` ($11 \% 2 == 0$, FALSO).
     - Esegue raggio FALSO del ternario: `(a += 3, 1)`. `a += 3` $\rightarrow a = 14$. Restituisce `1` (VERO).
     - **Stampa 3:** `14`
     - Test `if`: `a == 6` (FALSO). Esegue `a-- == 10` ($14 == 10$, FALSO, poi `a` diventa `13`).
     - Esegue `a -= 1` $\rightarrow a = 12$.
   - **Iterazione 3:**
     - Test `while`: `a % 2 == 0` ($12 \% 2 == 0$, VERO).
     - Esegue `(a >>= 1, a)` $\rightarrow a = 6$. Restituisce `6` (VERO).
     - **Stampa 4:** `6`
     - Test `if`: `a == 6` (VERO! Cortocircuito: `a-- == 10` non viene eseguito!).
     - Esegue corpo `if`: `a *= 2` $\rightarrow a = 12$.
     - `break`: esce dal ciclo `while`.

3. **Stampa Finale:**
   - `printf("a: %d\n", a);` $\rightarrow$ **Stampa 5:** `a: 12`

**Output Finale Completo:**
```text
26
13
14
6
a: 12
```

---

### 📌 Caso 2: Esame 15 Gennaio 2026 (Esercizio 2)
**Codice:**
```c
int a = 025 + 0x1A;
printf("%d\n", a);
while (a % 2 ? --a : (a >>= 1, 1)) {
    printf("%d\n", a);
    if (a == 3 || a-- == 4) {
        a <<= 1;
        break;
    }
    a /= 2;
}
printf("a: %d\n", a);
```

**Tracciamento Passo-Passo:**
1. **Inizializzazione:**
   - `025` = $21$, `0x1A` = $26$.
   - `a = 21 + 26 = 47`.
   - **Stampa 1:** `47`

2. **Ciclo `while`:**
   - **Iterazione 1:**
     - Test `while`: `a % 2` ($47 \% 2 = 1$, VERO). Esegue `--a` $\rightarrow a = 46$. Restituisce $46$ (VERO).
     - **Stampa 2:** `46`
     - Test `if`: `a == 3` (FALSO). `a-- == 4` ($46 == 4$, FALSO, poi `a` diventa $45$).
     - Esegue `a /= 2` $\rightarrow a = 45 / 2 = 22$.
   - **Iterazione 2:**
     - Test `while`: `a % 2` ($22 \% 2 = 0$, FALSO). Esegue `(a >>= 1, 1)` $\rightarrow a = 11$, restituisce $1$ (VERO).
     - **Stampa 3:** `11`
     - Test `if`: `a == 3` (FALSO). `a-- == 4` ($11 == 4$, FALSO, poi `a` diventa $10$).
     - Esegue `a /= 2` $\rightarrow a = 10 / 2 = 5$.
   - **Iterazione 3:**
     - Test `while`: `a % 2` ($5 \% 2 = 1$, VERO). Esegue `--a` $\rightarrow a = 4$. Restituisce $4$ (VERO).
     - **Stampa 4:** `4`
     - Test `if`: `a == 3` (FALSO). `a-- == 4` ($4 == 4$, VERO! Poi `a` diventa $3$).
     - Esegue corpo `if`: `a <<= 1` $\rightarrow a = 3 \times 2 = 6$.
     - `break`: esce dal ciclo.

3. **Stampa Finale:**
   - **Stampa 5:** `a: 6`

**Output Finale Completo:**
```text
47
46
11
4
a: 6
```

---

### 📌 Caso 3: Esame 30 Gennaio 2026 (Esercizio 5 - Undefined Behavior)
**Codice:**
```c
int a= 0x1b, i= 3, *b= &a;
for (int *p= &i; (a-=1) ? (*p++, --a) : ((*p)+=2, a); *p++) {
    a= (a - i);
    printf("%d %d OK\n", a, *p);
    if (a <= 0) {
        a= 1;
        continue;
    }
}
printf("%d %p\n", a, ((short*)b) + 1);
```

> [!WARNING]
> **Trap Esercizio Esame:** Notare che il puntatore `p` parte puntando a `i`. Tuttavia, nell'incremento del ciclo `for` fa `*p++` (incrementa l'indirizzo memorizzato in `p` per puntare alla locazione di memoria successiva).
> Dopo il primo ciclo, `p` non punta più a `i` ma ad una locazione di memoria indefinita fuori dall'oggetto!
> L'accesso a memoria fuori dall'oggetto d'origine è un **Undefined Behavior (UB)** in C.

**Output Teorico Atteso all'Esame:**
```text
22 _ OK
17 _ OK
12 _ OK
7 _ OK
2 _ OK
0 0x7ffee439a000
```
*(Dove i valori `_` sono indefiniti in quanto `*p` dereferenzia memoria non valida).*

---

## 💡 Checklist per l'Esame

- [ ] Ho convertito tutti i numeri ottali (`0...`) ed esadecimali (`0x...`) in decimale prima di iniziare?
- [ ] Ho ricordato che l'operatore virgola `,` restituisce sempre il valore dell'espressione a DESTRA?
- [ ] Ho verificato il corto-circuito negli `if` con `||` e `&&` per non applicare decrementi non eseguiti?
- [ ] Ho gestito correttamente la differenza tra prefisso (`--a`) e postfisso (`a--`)?
