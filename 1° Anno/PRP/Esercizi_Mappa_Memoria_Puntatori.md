---
tags:
  - ProceduralProgramming
  - ExamPrep
  - MemoryMap
  - Pointers
---
◀️ *Torna al:* [[01_Guida_Tipologie_Esami_PRP]] | *Riferimento Note:* [[PRP_Complete_Notes#10-pointers]] | [[PRP_Complete_Notes#21-data-representation--computer-arithmetic-c-context]] | [[PRP_Complete_Notes#15-memory-definitions-duration-and-layout]]

# 🧠 Tipologia 5: Mappa di Memoria, Little-Endian, Puntatori e Bitwise (7 Punti)

Questa è la tipologia di esercizio più importante e corposa di tutto l'esame (vale ben **7 punti** ed è presente in **tutti gli appelli**).

---

## 📐 Teoria e Regole di Riferimento (`PRP_Complete_Notes.md`)

I riferimenti teorici fondamentali nelle note si trovano in **[[PRP_Complete_Notes#21-data-representation--computer-arithmetic-c-context]]**, **[[PRP_Complete_Notes#10-pointers]]** e **[[PRP_Complete_Notes#15-memory-definitions-duration-and-layout]]**.

### 1. Architettura Little-Endian e Complemento a Due
* **Little-Endian:** In un sistema Little-Endian, il **byte meno significativo (LSB)** viene memorizzato all'indirizzo di memoria **più basso**, mentre il **byte più significativo (MSB)** si trova all'indirizzo più alto.
  * *Esempio:* Il valore `2048` (esadecimale `0x00000800`, a 16 bit: `0000 1000 0000 0000` cioè byte `0x08` e `0x00`):
    - Byte 0 (indirizzo basso): `00000000` (`0x00`)
    - Byte 1 (indirizzo alto): `00001000` (`0x08`)
* **Complemento a Due (Numeri Negativi):**
  - $-1$ in complemento a due ha tutti i bit a `1` (`0xFF` su 8 bit, `0xFFFF` su 16 bit, `0xFFFFFFFF` su 32 bit).
  - $-2$ ha bit `11111110_2` (`0xFE`).
  - `LLONG_MIN` a 64 bit ha il bit di segno a `1` seguito da 63 zeri (`0x8000000000000000`).

### 2. Aritmetica dei Puntatori e Cast dei Tipi
* **Aritmetica dei Puntatori (`ptr + k`):**
  L'incremento `ptr + k` sposta l'indirizzo di $k \times \text{sizeof}(*ptr)$ byte!
  - Se `p` è `short*` ($\text{sizeof} = 2$), `p[1]` accede ai byte 2 e 3. `p[9]` accede ai byte 18 e 19.
  - Se `q` è `char*` ($\text{sizeof} = 1$), `q[15]` accede esattamente al byte 15.
  - Se `a` è `long long a[3]` ($\text{sizeof} = 8$), `a+2` sposta l'indirizzo di $2 \times 8 = 16$ byte.
* **Sottrazione tra Puntatori dello Stesso Tipo:**
  `&p[9] - &p[2]` misura la distanza in **numero di elementi del tipo puntato** (`short`), non in byte!
  $$\&p[9] - \&p[2] = 9 - 2 = 7$$
* **Sottrazione con Cast a Intero (`(int)(p+11) - (int)(a+2)`):**
  Quando si converte un puntatore a tipo intero `(int)` prima di sottrarre, si calcola la differenza **diretta in byte**!
  - `p+11` corrisponde al byte $11 \times 2 = 22$.
  - `a+2` corrisponde al byte $2 \times 8 = 16$.
  - Differenza: $22 - 16 = 6$ byte.

---

## 📝 Algoritmo di Risoluzione Passo-Passo per l'Esame

1. **Disegna la Griglia di Memoria Byte per Byte:**
   - Prepara una tabella con le colonne: `Indice Byte | Offset Pointer (p[k], q[k]) | Contenuto Binario/Hex`.
   - Popola inizialmente l'array di partenza `a[...]` espandendo ciascun valore in Little-Endian.
2. **Applica le Modifiche Sovrapposte via Puntatore in Ordine:**
   - Applica le sovrascritture di `p[...]`, `q[...]` ed eventuali cast.
   - Converti i numeri da assegnare in binario/hex e scrivi i byte nelle rispettive celle Little-Endian.
3. **Valuta le 3 Affermazioni (A, B, C):**
   - Sostituisci i valori numerici dereferenziati ed esegui i calcoli aritmetici/bitwise.
   - Rispondi indicando **VERA** o **FALSA** con la giustificazione completa.

---

## 📑 Analisi Completa degli Esercizi dai Mock Exam (Pdfs)

### 📌 Caso 1: Esame 3 Giugno 2026 (Esercizio 5)
**Dati dell'Esercizio:**
- `long long a[3] = {2048, -3, LLONG_MIN + 768};`
- `short int *p = (short*) a; char *q = (char*) a;`
- Modifiche: `p[1]=4098`, `p[3]=4095-2`, `*(q+15)=73`, `p[9]=4096*4+1;`
- Dimensioni: `long long` = 8 byte, `short` = 2 byte, `char` = 1 byte. $4096 = 2^{12}$.

**Tabella Mappa di Memoria Risultante (in 16 bit / byte):**
* `p[0]` (byte 0-1): $2048 = 0x0800 \rightarrow$ `p[0]` resta $2048$.
* `p[1]` (byte 2-3): sovrascritto con $4098 = 4096 + 2 = 0x1002$.
* `p[2]` (byte 4-5): $0$.
* `p[3]` (byte 6-7): sovrascritto con $4095 - 2 = 4093 = 0x0FFD$.
* `p[4]` (byte 8-9): parte di `-3` $\rightarrow$ `-3`.
* `p[5]` (byte 10-11): $-1$.
* `p[6]` (byte 12-13): $-1$.
* `p[7]` (byte 14-15): `*(q+15)=73` (byte 15 diventa $73$). `p[7]` diventa $18943$.
* `p[8]` (byte 16-17): $768$.
* `p[9]` (byte 18-19): sovrascritto con $4096 \times 4 + 1 = 16385$.
* `p[10]` (byte 20-21): $0$.
* `p[11]` (byte 22-23): parte di `LLONG_MIN` $\rightarrow -32768$.

**Valutazione delle Affermazioni:**

#### **A. `(*(p + 7) - p[8]) % 2`**
* `*(p+7)` equivale a `p[7]`, che vale $18943$.
* `p[8]` vale $768$.
* Risultato: $(18943 - 768) \% 2 = 18175 \% 2 = 1$.
* **Risultato A: VERA (valore 1)**.

#### **B. `(((int)(p + 11) - (int)(a + 2)) + q[18]) % 7`**
* `(int)(p + 11)` si trova al byte offset $11 \times 2 = 22$.
* `(int)(a + 2)` si trova al byte offset $2 \times 8 = 16$.
* Differenza in byte: $22 - 16 = 6$.
* `q[18]` corrisponde al LSB di `p[9]` ($16385 = 0x4001 \rightarrow$ LSB = $1$).
* Somma: $6 + 1 = 7$.
* Modulo: $7 \% 7 = 0$.
* **Risultato B: FALSA (valore 0)**.

#### **C. `((&p[9] - &p[2]) + p[8]) % 2`**
* `&p[9] - &p[2]` = differenza tra puntatori `short*` = $9 - 2 = 7$.
* `p[8]` = $768$.
* Somma: $7 + 768 = 775$.
* Modulo: $775 \% 2 = 1$.
* **Risultato C: VERA (valore 1)**.

---

### 📌 Caso 2: Esame 22 Giugno 2026 (Esercizio 5)
**Dati dell'Esercizio:**
- `int a[4] = {5+2*32, INT_MIN + 21, [2]=65540, 262144/2+99};`
- `short int *p = (short*) a; char *q = (char*) a;`
- Modifiche: `*(q+3)=-1; *((short int*)&q[5])=257;`

**Valutazione delle Affermazioni:**
- **A. `((&a[4] - a) + p[5]) % 2`**
  - `&a[4] - a` = $4$ (differenza di 4 elementi `int`).
  - `p[5]` = $1$.
  - $(4 + 1) \% 2 = 5 \% 2 = 1 \rightarrow$ **VERA**.
- **B. `(((int)(a + 2) - (int)&q[2]) + q[14]) % 2`**
  - `(int)(a + 2)` al byte 8. `(int)&q[2]` al byte 2 $\rightarrow 8 - 2 = 6$ byte.
  - `q[14]` = $2$.
  - $(6 + 2) \% 2 = 8 \% 2 = 0 \rightarrow$ **FALSA**.
- **C. `((q[12] >> 4) | q[4]) >= 35`**
  - `q[12]` = $99 = 01100011_2$. Shift a destra di 4: $99 >> 4 = 6$.
  - `q[4]` = $21 = 00010101_2$.
  - Bitwise OR: $6 \ | \ 21 = 23$.
  - $23 \ge 35 \rightarrow$ **FALSA**.

---

## 💡 Checklist per l'Esame

- [ ] Ho ordinato i byte in **Little-Endian** (LSB prima a indirizzi bassi)?
- [ ] Ho distinto la sottrazione tra puntatori tipizzati (es. `p[9] - p[2]` = elementi) dalla sottrazione con cast a `(int)` (byte)?
- [ ] Ho controllato se l'operazione di modulo `% 2` restituisce $1$ (dispari/VERA) o $0$ (pari/FALSA)?
