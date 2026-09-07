◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]  

# Conversioni
### Esercizio 1 - prova Esame 
```c
double f(float a) {
    return (a - 1); // quà il valore di a è 3, a -1 = 2
    // faremo il return di una variabile float con valore 2
}

int main(void) {
    unsigned a = 3LL; // convertito da long long a unsigned int (valore 3)         
    int b = -1U;  // da unsigned -1 (4294967295) in int (con valore -1)    
    
    // int b viene convertito in unsigned quindi diventa 4294967295
    // a rimane insigned 
    // b<a risulta falsa, passiamo alla funzione f quindi a convertito a float 
    // con quindi valore 3
    float c = f((b < a) ? b : a); // float c = 2 
    float d = UINT_MAX + c - 7; // tutti i valori sono promossi a float 
    //il valore di float d sarà infine 4294967290.0
}
```

### Esercizio 1 Prova 15/01/26

```c
long int g2(unsigned long p){
	return p + 'e' - 'a';//'e' e 'a' convertiti in unsigned long
	// viene poi convertito 65542 in long int da unsigned long
}
// il valore di ritorno da g2 viene convertito (quindi da long int) in int 
int g1(int p){
	char c = 'k'; // 'k' vale cone ASCII 107, quindi temporary char c = int 107
	
	return g2(p + c - 'd'); // 65531 + 107 - 100 = 65538
	// vengono tutti promossi a int 	
	// passiamo poi p come un unsigned long p
}

int main(void) {
	unsigned short x = -5L; // da long int (-5L) a unShort x = 65531
	// da unsigned short a int 
	double b = g1(x);  // da int si passa a double 
	printf("%f\n", b); // verrà stampato 65542.000000
}
```

### Esercizio 4 Prova 30/01/26

```c

int i = -1
unsigned int limit = 200U;

if (i<limit){
	printf("%d", i);	
}
// la variabile i in quanto int (rank minore di unsigned int quindi limit)
// viene convertita int int unsigned per permettere l'operazione dentro l'IF 
// avendo quindi i due operandi allo stesso livello avremmo il limite di 
// unsigned int a confronto con 200, risultando in un FALSE 

```
### Esercizio 1

```c 
long int f(unsigned int a) {
    return (a - 5);
}

int main(void) {
    short x = -10S;  
    unsigned int y = 20U;
    double z = f((x > y) ? x : y); 
    float d = USHRT_MAX + z - 12;
}

```

- il valore di short x è -10
- quello di unsigned int y  è 20
- convertiamo short x into unsigned int, il valore diventa 4294967286
- x>y = TRUE 
- passiamo alla funzione f x, dovendolo così convertire a unsigned int (quindi  4294967286 )
	- dentro la funzione f il return sarà a-5 =4294967281
	- convertito poi a long int 
- il valore di long int f viene poi convertito in double in modo da poter esser assegnato a z
- double z con valore quindi di 4294967281
- per fload d convertiamo tutto a double , avremmo quindi 4294967295 + 4294967281 -12
- convertito poi a float d avremmo = 8589934564.0

---

# Mappe di Memoria, Puntatori e Little-Endian

### Esercizio 5 Prova 15/01/26

####  Testo
```c
long long a[3] = {1536, -2, LLONG_MIN + 512};
short int *p = (short*) a;
char *q = (char*) a;
p[1] = 4098, p[3] = 4095 - 2, *(q + 15) = 73, p[9] = 4096 * 4 + 1;
```
- **Dimensioni tipi:** `long long` = 8 byte, `short int` = 2 byte, `char` = 1 byte.
- **Costante:** $4096 = 2^{12}$.
- Valori rappresentati in **Little-Endian** e **Complemento a Due**.

**Affermazioni da verificare (Vere o False):**
- **A.** `(*(p + 5) - p[4]) % 2`
- **B.** `(((int)(p + 11) - (int)(a + 2)) + q[18]) % 7`
- **C.** `((&p[9] - &p[2]) + p[8]) % 2`

---
#### 1️⃣ Dimensioni, Puntatori e Formule degli Offset

- L'array `a` è composto da 3 elementi `long long` da 8 byte ciascuno:
  $$\text{Dimensione Totale} = 3 \times 8 = \mathbf{24\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 23})$$

> [!NOTE]
> **Relazione tra i Puntatori `p`, `q` e l'Array `a` (Sovrapposizione di Memoria / Aliasing):**
> - **Stessa Memoria Fisica:** In C non c'è "ereditarietà". `p` e `q` puntano all'inizio della stessa identica area di memoria di `a` (`(void*)p == (void*)q == (void*)a`). Non c'è copia di dati: modificare `p[i]` altera direttamente i byte sottostanti dell'array `a`.
> - **Diversa Risoluzione di Lettura (`sizeof`):** I puntatori cambiano solo la "griglia" con cui interpretano i byte:
>   - **`a` (`long long`, 8 byte):** vede la memoria a blocchi di 8 byte $\implies \text{Byte } i \times 8$
>   - **`p` (`short`, 2 byte):** vede la stessa memoria a blocchi di 2 byte $\implies \text{Byte } i \times 2$
>   - **`q` (`char`, 1 byte):** vede la stessa memoria a singoli byte $\implies \text{Byte } i \times 1$

```text
Byte:   0   1 | 2   3 | 4   5 | 6   7 | 8   9 | 10 11 | 12 13 | 14 15 | 16 17 | 18 19 | 20 21 | 22 23
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
a   : [             a[0]              |              a[1]             |              a[2]             ]
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
p   : [  p[0] |  p[1] |  p[2] |  p[3] |  p[4] |  p[5] |  p[6] |  p[7] |  p[8] |  p[9] | p[10] | p[11] ]
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
q   : [q0][q1]|[q2]...                                                                       ...|[q23]]
```

---

#### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione dell'array

##### 🔹 Elemento `a[0] = 1536` (Byte 0..7)
- **Spiegazione:** $1536$ è un numero positivo. Lo scomponiamo in potenze di 2 per trovare la sua rappresentazione esadecimale su 8 byte (64 bit):
  $$1536 = 1024 + 512 = 2^{10} + 2^9 = \texttt{0x0400} + \texttt{0x0200} = \mathbf{\texttt{0x0600}}$$
  Su 64 bit: `0x0000000000000600`.
- **Disposizione Little-Endian:**
  - **Byte 0 (LSB):** `0x00` ($00000000_2$)
  - **Byte 1:** `0x06` ($00000110_2$, ovvero $2^1 + 2^2$)
  - **Byte 2..7:** tutti `0x00` (bit a 0)

##### 🔹 Elemento `a[1] = -2` (Byte 8..15)
- **Spiegazione:** $-2$ è negativo, quindi usiamo il complemento a due su 64 bit:
  1. Valore assoluto $+2$: `0x0000000000000002`
  2. Inversione bit ($\sim$): `0xFFFFFFFFFFFFFFFD`
  3. Aggiunta di $+1$: $\texttt{0xFFFFFFFFFFFFFFFD} + 1 = \mathbf{\texttt{0xFFFFFFFFFFFFFFFE}}$
- **Disposizione Little-Endian:**
  - **Byte 8 (LSB):** `0xFE` ($254_{10} = 11111110_2$, bit 0 a 0 e bit 1..7 a 1)
  - **Byte 9..15:** tutti `0xFF` ($255_{10} = 11111111_2$, tutti bit a 1 per estensione del segno)

##### 🔹 Elemento `a[2] = LLONG_MIN + 512` (Byte 16..23)
- **Spiegazione:**
  - `LLONG_MIN` è il valore minimo a 64 bit con segno ($-2^{63}$): solo il bit 63 (più significativo) è a 1 $\implies \texttt{0x8000000000000000}$.
  - $+512 = 2^9 = \texttt{0x0000000000000200}$.
  - Somma: $\texttt{0x8000000000000000} + \texttt{0x0000000000000200} = \mathbf{\texttt{0x8000000000000200}}$.
- **Disposizione Little-Endian:**
  - **Byte 16 (LSB):** `0x00`
  - **Byte 17:** `0x02` ($2^1 = 2$)
  - **Byte 18..22:** `0x00`
  - **Byte 23 (MSB):** `0x80` ($2^7 = 128$)

---

#### 3️⃣ Mappa di Memoria di Base (Array Iniziale `a[3]` prima delle modifiche)

Questa è la mappa esatta di memoria prodotta dalla sola inizializzazione `long long a[3] = {1536, -2, LLONG_MIN + 512};`:

|  Byte  | Puntatori Iniziali |  Hex   | Binario Esame (LSB $\to$ MSB) | Elemento / Significato Iniziale |
| :----: | :----------------- | :----: | :---------------------------: | :------------------------------ |
| **0**  | `a`, `&p[0]`, `&q[0]` | `0x00` |          `00000000`           | `a[0]` (LSB $= 0$)              |
| **1**  |                    | `0x06` |          `01100000`           | `a[0]` ($1536 / 256 = 6$)       |
| **2**  | `&p[1]`            | `0x00` |          `00000000`           | `a[0]`                          |
| **3**  |                    | `0x00` |          `00000000`           | `a[0]`                          |
| **4**  | `&p[2]`            | `0x00` |          `00000000`           | `a[0]`                          |
| **5**  |                    | `0x00` |          `00000000`           | `a[0]`                          |
| **6**  | `&p[3]`            | `0x00` |          `00000000`           | `a[0]`                          |
| **7**  |                    | `0x00` |          `00000000`           | `a[0]` (MSB)                    |
| **8**  | `a+1`, `&p[4]`, `&q[8]` | `0xFE` |          `01111111`           | `a[1]` (LSB $= -2$)             |
| **9**  |                    | `0xFF` |          `11111111`           | `a[1]` (estensione segno $-2$)  |
| **10** | `p+5`, `&p[5]`     | `0xFF` |          `11111111`           | `a[1]`                          |
| **11** |                    | `0xFF` |          `11111111`           | `a[1]`                          |
| **12** | `&p[6]`            | `0xFF` |          `11111111`           | `a[1]`                          |
| **13** |                    | `0xFF` |          `11111111`           | `a[1]`                          |
| **14** | `&p[7]`            | `0xFF` |          `11111111`           | `a[1]`                          |
| **15** | `q+15`, `&q[15]`   | `0xFF` |          `11111111`           | `a[1]` (MSB)                    |
| **16** | `a+2`, `&p[8]`     | `0x00` |          `00000000`           | `a[2]` (LSB)                    |
| **17** |                    | `0x02` |          `01000000`           | `a[2]` ($+512 / 256 = 2$)       |
| **18** | `&p[9]`, `&q[18]`  | `0x00` |          `00000000`           | `a[2]`                          |
| **19** |                    | `0x00` |          `00000000`           | `a[2]`                          |
| **20** | `&p[10]`           | `0x00` |          `00000000`           | `a[2]`                          |
| **21** |                    | `0x00` |          `00000000`           | `a[2]`                          |
| **22** | `p+11`, `&p[11]`   | `0x00` |          `00000000`           | `a[2]`                          |
| **23** |                    | `0x80` |          `00000001`           | `a[2]` (`LLONG_MIN` MSB)        |

---

#### 4️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

1. **`p[1] = 4098;`**
   - **Spiegazione:** `p` punta ad elementi `short` (2 byte). `p[1]` punta all'indice $1 \times 2 = \text{Byte } \mathbf{2}$ e sovrascrive i **Byte 2 e 3**.
   - $4098 = 4096 + 2 = 2^{12} + 2^1 = \texttt{0x1000} + \texttt{0x0002} = \mathbf{\texttt{0x1002}}$.
   - Little-Endian a 16 bit:
     - **Byte 2 (LSB):** `0x02`
     - **Byte 3 (MSB):** `0x10`

2. **`p[3] = 4095 - 2 = 4093;`**
   - **Spiegazione:** `p[3]` punta all'indice $3 \times 2 = \text{Byte } \mathbf{6}$ e sovrascrive i **Byte 6 e 7**.
   - $4093 = 4096 - 3 = \texttt{0x1000} - 3 = \mathbf{\texttt{0x0FFD}}$ (in decimale: $15 \times 256 + 15 \times 16 + 13 = 4093$).
   - Little-Endian a 16 bit:
     - **Byte 6 (LSB):** `0xFD` ($11111101_2$)
     - **Byte 7 (MSB):** `0x0F` ($00001111_2$)

3. **`*(q + 15) = 73;`**
   - **Spiegazione:** `q` è `char*` (1 byte). `*(q + 15)` equivale a `q[15]` e modifica solo il singolo **Byte 15**.
   - $73 = 64 + 8 + 1 = 2^6 + 2^3 + 2^0 = \texttt{0x40} + \texttt{0x08} + \texttt{0x01} = \mathbf{\texttt{0x49}}$.
   - **Byte 15:** `0x49` ($01001001_2$).

4. **`p[9] = 4096 * 4 + 1 = 16385;`**
   - **Spiegazione:** `p[9]` punta all'indice $9 \times 2 = \text{Byte } \mathbf{18}$ e sovrascrive i **Byte 18 e 19**.
   - $16385 = 16384 + 1 = 2^{14} + 2^0 = \texttt{0x4000} + \texttt{0x0001} = \mathbf{\texttt{0x4001}}$.
   - Little-Endian a 16 bit:
     - **Byte 18 (LSB):** `0x01`
     - **Byte 19 (MSB):** `0x40` ($64_{10} = 2^6$)

---

#### 5️⃣ Mappa di Memoria Finale (dopo tutte le modifiche)

> [!NOTE]
> **Convenzione di Scrittura dei Bit all'Esame (LSB $\to$ MSB):**
> Nei compiti d'esame le sequenze di 8 bit di ogni byte sono scritte da sinistra a destra partendo dal **bit 0 ($2^0$)** fino al **bit 7 ($2^7$)**.

|  Byte  | Puntatori Corrispondenti |  Hex   | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione               |
| :----: | :----------------------- | :----: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]`    | `0x00` |          `00000000`           | Iniziale `a[0]` (LSB)                |
| **1**  |                          | `0x06` |          `01100000`           | Iniziale `a[0]` ($1536 / 256$)       |
| **2**  | `&p[1]`                  | `0x02` |          `01000000`           | **Modificato da `p[1] = 4098`**      |
| **3**  |                          | `0x10` |          `00001000`           | **Modificato da `p[1] = 4098`**      |
| **4**  | `&p[2]`                  | `0x00` |          `00000000`           | Iniziale `a[0]`                      |
| **5**  |                          | `0x00` |          `00000000`           | Iniziale `a[0]`                      |
| **6**  | `&p[3]`                  | `0xFD` |          `10111111`           | **Modificato da `p[3] = 4093`**      |
| **7**  |                          | `0x0F` |          `11110000`           | **Modificato da `p[3] = 4093`**      |
| **8**  | `a+1`, `&p[4]`, `&q[8]`  | `0xFE` |          `01111111`           | Iniziale `a[1] = -2`                 |
| **9**  |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **10** | `p+5`, `&p[5]`           | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **11** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **12** | `&p[6]`                  | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **13** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **14** | `&p[7]`                  | `0xFF` |          `11111111`           | Iniziale `a[1] = -2`                 |
| **15** | `q+15`, `&q[15]`         | `0x49` |          `10010010`           | **Modificato da `*(q+15) = 73`**     |
| **16** | `a+2`, `&p[8]`           | `0x00` |          `00000000`           | Iniziale `a[2]` (LSB)                |
| **17** |                          | `0x02` |          `01000000`           | Iniziale `a[2]` ($+512$)             |
| **18** | `&p[9]`, `&q[18]`        | `0x01` |          `10000000`           | **Modificato da `p[9] = 16385`**     |
| **19** |                          | `0x40` |          `00000010`           | **Modificato da `p[9] = 16385`**     |
| **20** | `&p[10]`                 | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **21** |                          | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **22** | `p+11`, `&p[11]`         | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **23** |                          | `0x80` |          `00000001`           | `LLONG_MIN` (MSB)                    |

---

#### 6️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🟢 Asserzione A: `(*(p + 5) - p[4]) % 2`

**Spiegazione:**
1. **`*(p + 5)`** (equivalente a `p[5]`) legge uno `short` (2 byte con segno) a partire dal Byte $5 \times 2 = 10$ (**Byte 10 e 11**):
   - Byte 10: `0xFF`, Byte 11: `0xFF` $\implies$ parola a 16 bit: $\texttt{0xFFFF}$.
   - Trattandosi di un tipo con segno (`short`), $\texttt{0xFFFF}$ rappresenta il valore decimale **$-1$** ($65535 - 65536 = -1$).
2. **`p[4]`** legge uno `short` a partire dal Byte $4 \times 2 = 8$ (**Byte 8 e 9**):
   - Byte 8: `0xFE`, Byte 9: `0xFF` $\implies$ parola a 16 bit in Little-Endian: $\texttt{0xFFFE}$.
   - Valore con segno: $\texttt{0xFFFE} = \mathbf{-2}$ ($65534 - 65536 = -2$).
3. **Calcolo finale:**
   - $(*(p + 5) - p[4]) \pmod 2 = (-1 - (-2)) \pmod 2 = (-1 + 2) \pmod 2 = 1 \pmod 2 = \mathbf{1}$.

**Esito:** Poiché il risultato è $1 \ne 0$ (valore logico Vero), l'asserzione è **VERA**.

---

#### 🔴 Asserzione B: `(((int)(p + 11) - (int)(a + 2)) + q[18]) % 7`

**Spiegazione:**
1. **`(int)(p + 11)`** effettua un **cast esplicito ad intero** del puntatore $\implies$ offset in byte: $11 \times \text{sizeof(short)} = 11 \times 2 = \mathbf{22\text{ byte}}$.
2. **`(int)(a + 2)`** converte in byte l'indirizzo di `a + 2` $\implies$ offset in byte: $2 \times \text{sizeof(long long)} = 2 \times 8 = \mathbf{16\text{ byte}}$.
3. **Differenza in byte:**
   - $(int)(p + 11) - (int)(a + 2) = 22 - 16 = \mathbf{6}$.
4. **`q[18]`** legge il valore come `char` (1 byte) al **Byte 18**:
   - Dalla mappa di memoria, Byte 18 vale $\texttt{0x01} = \mathbf{1}$.
5. **Calcolo finale:**
   - $((6 + 1) \pmod 7) = 7 \pmod 7 = \mathbf{0}$.

**Esito:** Il risultato numerico è $0$ (valore logico Falso), quindi l'asserzione è **FALSA**.

---

#### 🟢 Asserzione C: `((&p[9] - &p[2]) + p[8]) % 2`

**Spiegazione:**
1. **`&p[9] - &p[2]`** è una **sottrazione tra puntatori dello stesso tipo (`short*`)**:
   - In C, la sottrazione tra puntatori calcola il numero di elementi puntati: $\&p[9] - \&p[2] = 9 - 2 = \mathbf{7}$.
2. **`p[8]`** legge uno `short` a 16 bit a partire dal Byte $8 \times 2 = 16$ (**Byte 16 e 17**):
   - Byte 16: `0x00`, Byte 17: `0x02` $\implies$ valore $\texttt{0x0200} = 2 \times 256 = \mathbf{512}$.
3. **Calcolo finale:**
   - $(((\&p[9] - \&p[2]) + p[8]) \pmod 2) = (7 + 512) \pmod 2 = 519 \pmod 2 = \mathbf{1}$.

**Esito:** Poiché il risultato è $1 \ne 0$ (valore logico Vero), l'asserzione è **VERA**.

---

### Esercizio 7 Prova 30/01/26

#### Testo
```c
long long a[3] = {1537, -67, (LLONG_MAX + 1) + 512};
int *p = (int*) a;
char *q = (char*) a;
p[1] = INT_MAX, p[4] += 2048, q[19] = ~q[19];
```
- **Dimensioni tipi:** `long long` = 8 byte, `int` = 4 byte, `char` = 1 byte.
- Valori rappresentati in **Little-Endian** e **Complemento a Due**.

**Affermazioni da verificare (Vere o False):**
- **A.** `(~(p[3] & p[1])) == p[5]`
- **B.** `*((long long*)(&p[1])) < *((long long*)(&p[2]))`
- **C.** `((long long*)(&p[1])) < ((short int*)(&p[2]))`

---

#### 1️⃣ Dimensioni, Puntatori e Formule degli Offset

- L'array `a` contiene 3 elementi `long long` da 8 byte ciascuno:
  $$\text{Dimensione Totale} = 3 \times 8 = \mathbf{24\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 23})$$

> [!NOTE]
> **Relazione tra i Puntatori `p`, `q` e l'Array `a`:**
> - `a` (`long long*`, 8 byte): blocchi da 8 byte $\implies \text{Offset} = i \times 8$ (Byte $0, 8, 16$).
> - `p` (`int*`, 4 byte): blocchi da 4 byte $\implies \text{Offset} = i \times 4$ (Byte $0, 4, 8, 12, 16, 20$).
> - `q` (`char*`, 1 byte): singoli byte $\implies \text{Offset} = i \times 1$ (Byte $0, 1, 2, \dots, 23$).

```text
Byte:   0   1   2   3 | 4   5   6   7 | 8   9  10  11 | 12  13  14  15 | 16  17  18  19 | 20  21  22  23
      +---------------+---------------+---------------+----------------+----------------+----------------+
a   : [              a[0]             |              a[1]              |              a[2]               ]
      +---------------+---------------+---------------+----------------+----------------+----------------+
p   : [      p[0]     |      p[1]     |      p[2]     |      p[3]      |      p[4]      |      p[5]      ]
      +---------------+---------------+---------------+----------------+----------------+----------------+
q   : [q0][q1][q2][q3]|[q4]...                                                                  ...|[q23]]
```

---

#### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione dell'array

##### 🔹 Elemento `a[0] = 1537` (Byte 0..7)
- **Scomposizione in potenze di 2:**
  $$1537 = 1024 + 512 + 1 = 2^{10} + 2^9 + 2^0 = \texttt{0x0400} + \texttt{0x0200} + \texttt{0x0001} = \mathbf{\texttt{0x0000000000000601}}$$
- **Disposizione Little-Endian (64 bit):**
  - **Byte 0 (LSB):** `0x01` ($00000001_2$)
  - **Byte 1:** `0x06` ($00000110_2$, ovvero $2^1 + 2^2$)
  - **Byte 2..7:** tutti `0x00` ($00000000_2$)

##### 🔹 Elemento `a[1] = -67` (Byte 8..15)
- **Complemento a due su 64 bit per $-67$:**
  1. Valore assoluto $+67 = 64 + 2 + 1 = \texttt{0x0000000000000043}$
  2. Inversione bit ($\sim$): `0xFFFFFFFFFFFFFFBC`
  3. Aggiunta di $+1$: $\texttt{0xFFFFFFFFFFFFFFBC} + 1 = \mathbf{\texttt{0xFFFFFFFFFFFFFFBD}}$
  *(Verifica LSB: $256 - 67 = 189 = \texttt{0xBD}$)*
- **Disposizione Little-Endian:**
  - **Byte 8 (LSB):** `0xBD` ($10111101_2$)
  - **Byte 9..15:** tutti `0xFF` ($11111111_2$, per estensione del segno)

##### 🔹 Elemento `a[2] = (LLONG_MAX + 1) + 512` (Byte 16..23)
- **Overflow a 64 bit e somma:**
  - `LLONG_MAX` su 64 bit vale $2^{63} - 1 = \texttt{0x7FFFFFFFFFFFFFFF}$.
  - `(LLONG_MAX + 1)` va in overflow a 64 bit e produce esattamente `LLONG_MIN` $= -2^{63} = \texttt{0x8000000000000000}$.
  - $+512 = +2^9 = \texttt{0x0000000000000200}$.
  - Somma: $\texttt{0x8000000000000000} + \texttt{0x0000000000000200} = \mathbf{\texttt{0x8000000000000200}}$.
- **Disposizione Little-Endian:**
  - **Byte 16 (LSB):** `0x00`
  - **Byte 17:** `0x02` ($00000010_2$, $2^1 = 2$)
  - **Byte 18..22:** `0x00`
  - **Byte 23 (MSB):** `0x80` ($10000000_2$, bit 7 a 1)

---

#### 3️⃣ Mappa di Memoria di Base (Array Iniziale `a[3]` prima delle modifiche)

Questa è la mappa esatta di memoria prodotta dalla sola inizializzazione `long long a[3] = {1537, -67, (LLONG_MAX + 1) + 512};`:

|  Byte  | Puntatori Iniziali |  Hex   | Binario Esame (LSB $\to$ MSB) | Elemento / Significato Iniziale      |
| :----: | :----------------- | :----: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]` | `0x01` |          `10000000`           | `a[0]` (LSB $= 1$)                   |
| **1**  |                    | `0x06` |          `01100000`           | `a[0]` ($1536 / 256 = 6$)            |
| **2**  |                    | `0x00` |          `00000000`           | `a[0]`                               |
| **3**  |                    | `0x00` |          `00000000`           | `a[0]`                               |
| **4**  | `&p[1]`, `&q[4]`   | `0x00` |          `00000000`           | `a[0]`                               |
| **5**  |                    | `0x00` |          `00000000`           | `a[0]`                               |
| **6**  |                    | `0x00` |          `00000000`           | `a[0]`                               |
| **7**  |                    | `0x00` |          `00000000`           | `a[0]` (MSB)                         |
| **8**  | `a+1`, `&p[2]`, `&q[8]` | `0xBD` |          `10111101`           | `a[1]` (LSB $= 256 - 67 = 189$)      |
| **9**  |                    | `0xFF` |          `11111111`           | `a[1]` (estensione segno $-67$)      |
| **10** |                    | `0xFF` |          `11111111`           | `a[1]`                               |
| **11** |                    | `0xFF` |          `11111111`           | `a[1]`                               |
| **12** | `&p[3]`, `&q[12]`  | `0xFF` |          `11111111`           | `a[1]`                               |
| **13** |                    | `0xFF` |          `11111111`           | `a[1]`                               |
| **14** |                    | `0xFF` |          `11111111`           | `a[1]`                               |
| **15** |                    | `0xFF` |          `11111111`           | `a[1]` (MSB)                         |
| **16** | `a+2`, `&p[4]`, `&q[16]` | `0x00` |          `00000000`           | `a[2]` (LSB)                         |
| **17** |                    | `0x02` |          `01000000`           | `a[2]` ($+512 / 256 = 2$)            |
| **18** |                    | `0x00` |          `00000000`           | `a[2]`                               |
| **19** | `&q[19]`           | `0x00` |          `00000000`           | `a[2]`                               |
| **20** | `&p[5]`, `&q[20]`  | `0x00` |          `00000000`           | `a[2]`                               |
| **21** |                    | `0x00` |          `00000000`           | `a[2]`                               |
| **22** |                    | `0x00` |          `00000000`           | `a[2]`                               |
| **23** |                    | `0x80` |          `00000001`           | `a[2]` (`LLONG_MIN` MSB)             |

---

#### 4️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

1. **`p[1] = INT_MAX;`**
   - `p` è `int*` (4 byte). `p[1]` sovrascrive i **Byte 4..7** (offset $1 \times 4 = \text{Byte } 4$).
   - `INT_MAX` su 32 bit con segno è $2^{31} - 1 = \mathbf{\texttt{0x7FFFFFFF}}$.
   - Little-Endian su 32 bit:
     - **Byte 4:** `0xFF` ($11111111_2$)
     - **Byte 5:** `0xFF` ($11111111_2$)
     - **Byte 6:** `0xFF` ($11111111_2$)
     - **Byte 7 (MSB):** `0x7F` ($01111111_2$, bit 7 a 0)

2. **`p[4] += 2048;`**
   - `p[4]` occupa i **Byte 16..19** (offset $4 \times 4 = \text{Byte } 16$).
   - Valore iniziale di `p[4]` nei Byte 16..19: `0x00, 0x02, 0x00, 0x00` $\implies \texttt{0x00000200} = 512_{10}$.
   - Somma: $512 + 2048 = 2560_{10} = 2048 + 512 = 2^{11} + 2^9 = \texttt{0x0800} + \texttt{0x0200} = \mathbf{\texttt{0x00000A00}}$.
   - Little-Endian nei Byte 16..19:
     - **Byte 16:** `0x00`
     - **Byte 17:** `0x0A` ($00001010_2$, ovvero $10_{10}$)
     - **Byte 18:** `0x00`
     - **Byte 19:** `0x00`

3. **`q[19] = ~q[19];`**
   - `q` è `char*` (1 byte). `q[19]` modifica unicamente il **Byte 19**.
   - Valore attuale di Byte 19 prima dell'operazione: `0x00` ($00000000_2$).
   - Negazione bit a bit (NOT): $\sim(\texttt{0x00}) = \mathbf{\texttt{0xFF}}$ ($11111111_2$).
   - **Byte 19 diventa:** `0xFF`.

---

#### 5️⃣ Mappa di Memoria Finale (dopo tutte le modifiche)

|  Byte  | Puntatori Corrispondenti |  Hex   | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione               |
| :----: | :----------------------- | :----: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]`    | `0x01` |          `10000000`           | Iniziale `a[0]` (LSB $= 1$)          |
| **1**  |                          | `0x06` |          `01100000`           | Iniziale `a[0]` ($1536 / 256$)       |
| **2**  |                          | `0x00` |          `00000000`           | Iniziale `a[0]`                      |
| **3**  |                          | `0x00` |          `00000000`           | Iniziale `a[0]`                      |
| **4**  | `&p[1]`, `&q[4]`         | `0xFF` |          `11111111`           | **Modificato da `p[1] = INT_MAX`**   |
| **5**  |                          | `0xFF` |          `11111111`           | **Modificato da `p[1] = INT_MAX`**   |
| **6**  |                          | `0xFF` |          `11111111`           | **Modificato da `p[1] = INT_MAX`**   |
| **7**  |                          | `0x7F` |          `11111110`           | **Modificato da `p[1] = INT_MAX`**   |
| **8**  | `a+1`, `&p[2]`, `&q[8]`  | `0xBD` |          `10111101`           | Iniziale `a[1] = -67` (LSB)          |
| **9**  |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **10** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **11** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **12** | `&p[3]`, `&q[12]`        | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **13** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **14** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **15** |                          | `0xFF` |          `11111111`           | Iniziale `a[1] = -67`                |
| **16** | `a+2`, `&p[4]`, `&q[16]` | `0x00` |          `00000000`           | Iniziale `a[2]` (LSB)          |
| **17** |                          | `0x0A` |          `01010000`           | **Modificato da `p[4] += 2048`**     |
| **18** |                          | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **19** | `&q[19]`                 | `0xFF` |          `11111111`           | **Modificato da `q[19] = ~q[19]`**   |
| **20** | `&p[5]`, `&q[20]`        | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **21** |                          | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **22** |                          | `0x00` |          `00000000`           | Iniziale `a[2]`                      |
| **23** |                          | `0x80` |          `00000001`           | `LLONG_MIN` (MSB di `a[2]`)          |

---

#### 6️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🟢 Asserzione A: `(~(p[3] & p[1])) == p[5]`

**Spiegazione:**
1. `p[3]` è l'`int` a 32 bit situato ai **Byte 12..15**:
   - I byte sono tutti `0xFF` $\implies \texttt{0xFFFFFFFF} = -1_{10}$.
2. `p[1]` è l'`int` a 32 bit situato ai **Byte 4..7**:
   - Byte: `0xFF, 0xFF, 0xFF, 0x7F` $\implies \texttt{0x7FFFFFFF} = \text{INT\_MAX}$.
3. Operazione AND bit a bit (`p[3] & p[1]`):
   - $\texttt{0xFFFFFFFF} \ \& \ \texttt{0x7FFFFFFF} = \texttt{0x7FFFFFFF}$.
4. Negazione bit a bit NOT ($\sim$):
   - $\sim(\texttt{0x7FFFFFFF}) = \mathbf{\texttt{0x80000000}} = \text{INT\_MIN} = -2147483648_{10}$.
5. `p[5]` è l'`int` a 32 bit situato ai **Byte 20..23**:
   - Byte 20..22: `0x00, 0x00, 0x00`, Byte 23: `0x80` $\implies \mathbf{\texttt{0x80000000}} = \text{INT\_MIN}$.
6. **Confronto:**
   - $\texttt{0x80000000} == \texttt{0x80000000} \implies \mathbf{\text{VERO}}$.

**Esito:** L'asserzione è **VERA**.

---

#### 🟢 Asserzione B: `*((long long*)(&p[1])) < *((long long*)(&p[2]))`

**Spiegazione:**
1. `&p[1]` è l'indirizzo del **Byte 4**. Il cast a `long long*` legge 8 byte a partire dal Byte 4 (**Byte 4..11**):
   - Byte 4..7 (`p[1]`): `0xFF, 0xFF, 0xFF, 0x7F`
   - Byte 8..11 (`p[2]`): `0xBD, 0xFF, 0xFF, 0xFF`
   - Valore a 64 bit risultante in Little-Endian: $V_1 = \texttt{0xFFFFFFBD7FFFFFFF}$ (numero negativo).
2. `&p[2]` è l'indirizzo del **Byte 8**. Il cast a `long long*` legge 8 byte a partire dal Byte 8 (**Byte 8..15**):
   - Byte 8..11 (`p[2]`): `0xBD, 0xFF, 0xFF, 0xFF`
   - Byte 12..15 (`p[3]`): `0xFF, 0xFF, 0xFF, 0xFF`
   - Valore a 64 bit risultante: $V_2 = \texttt{0xFFFFFFFFFFFFFFBD} = -67_{10}$.
3. **Confronto tra i due numeri con segno ($V_1 < V_2$):**
   - $V_1 \approx -2.8 \times 10^{11} < -67 = V_2 \implies \mathbf{\text{VERO}}$.

**Esito:** Poiché $V_1 < V_2$, l'asserzione è **VERA**.

---

#### 🟢 Asserzione C: `((long long*)(&p[1])) < ((short int*)(&p[2]))`

**Spiegazione:**
1. `&p[1]` è l'indirizzo in memoria dell'elemento `p[1]`, situato all'**offset Byte 4** (`a + 4`).
2. `&p[2]` è l'indirizzo in memoria dell'elemento `p[2]`, situato all'**offset Byte 8** (`a + 8`).
3. I cast a tipi puntatore differenti convertono solo il tipo di dato, ma **non modificano l'indirizzo fisico in memoria**.
4. Poiché l'indirizzo del Byte 4 precede numericamente nello spazio di indirizzamento l'indirizzo del Byte 8:
   - $\text{Indirizzo}(\&p[1]) < \text{Indirizzo}(\&p[2]) \iff 4 < 8 \implies \mathbf{\text{VERO}}$.

**Esito:** L'asserzione è **VERA**.

---

### Esercizio 5 Prova 22/06/26

#### Testo
```c
int a[4] = {5 + 2 * 32, INT_MIN + 21, [2] = 65540, 262144 / 2 + 99};
short int *p = (short*) a;
char *q = (char*) a;
*(q + 3) = -1;
*((short int*)&q[5]) = 257;
```
- **Dimensioni tipi:** `int` = 4 byte, `short int` = 2 byte, `char` = 1 byte.
- **Costante:** $262144 = 2^{18}$.
- Valori rappresentati in **Little-Endian** e **Complemento a Due**.

**Affermazioni da verificare (Vere o False):**
- **A.** `((&a[4] - a) + p[5]) % 2`
- **B.** `(((int)(a + 2) - (int)&q[2]) + q[14]) % 2`
- **C.** `((q[12] >> 4) | q[4]) >= 35`

---

#### 1️⃣ Dimensioni, Puntatori e Formule degli Offset

- L'array `a` contiene 4 elementi `int` da 4 byte ciascuno:
  $$\text{Dimensione Totale} = 4 \times 4 = \mathbf{16\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 15})$$

> [!NOTE]
> **Relazione tra i Puntatori `p`, `q` e l'Array `a`:**
> - `a` (`int*`, 4 byte): blocchi da 4 byte $\implies \text{Offset} = i \times 4$ (Byte $0, 4, 8, 12$).
> - `p` (`short*`, 2 byte): blocchi da 2 byte $\implies \text{Offset} = i \times 2$ (Byte $0, 2, 4, 6, 8, 10, 12, 14$).
> - `q` (`char*`, 1 byte): singoli byte $\implies \text{Offset} = i \times 1$ (Byte $0, 1, 2, \dots, 15$).

```text
Byte:   0   1 | 2   3 | 4   5 | 6   7 | 8   9 | 10 11 | 12 13 | 14 15
      +-------+-------+-------+-------+-------+-------+-------+-------+
a   : [      a[0]     |      a[1]     |      a[2]     |      a[3]     ]
      +-------+-------+-------+-------+-------+-------+-------+-------+
p   : [  p[0] |  p[1] |  p[2] |  p[3] |  p[4] |  p[5] |  p[6] |  p[7] ]
      +-------+-------+-------+-------+-------+-------+-------+-------+
q   : [q0][q1]|[q2]...                                        ...|[q15]]
```

---

#### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione dell'array

##### 🔹 Elemento `a[0] = 5 + 2 * 32` (Byte 0..3)
- **Calcolo:** $5 + 2 \times 32 = 5 + 64 = 69_{10}$.
- **Scomposizione in potenze di 2:**
  $$69 = 64 + 4 + 1 = 2^6 + 2^2 + 2^0 = \texttt{0x40} + \texttt{0x04} + \texttt{0x01} = \mathbf{\texttt{0x00000045}}$$
- **Disposizione Little-Endian (32 bit):**
  - **Byte 0 (LSB):** `0x45` ($01000101_2$)
  - **Byte 1..3:** tutti `0x00` ($00000000_2$)

##### 🔹 Elemento `a[1] = INT_MIN + 21` (Byte 4..7)
- **Calcolo:**
  - `INT_MIN` su 32 bit con segno è $-2^{31} = \texttt{0x80000000}$.
  - $+21 = 16 + 4 + 1 = 2^4 + 2^2 + 2^0 = \texttt{0x00000015}$.
  - Somma: $\texttt{0x80000000} + \texttt{0x00000015} = \mathbf{\texttt{0x80000015}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 4 (LSB):** `0x15` ($00010101_2$)
  - **Byte 5..6:** `0x00` ($00000000_2$)
  - **Byte 7 (MSB):** `0x80` ($10000000_2$, bit di segno a 1)

##### 🔹 Elemento `a[2] = 65540` (Byte 8..11)
- **Calcolo tramite Designated Initializer `[2] = 65540`:**
  - $65540 = 65536 + 4 = 2^{16} + 2^2 = \texttt{0x00010000} + \texttt{0x00000004} = \mathbf{\texttt{0x00010004}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 8 (LSB):** `0x04` ($00000100_2$)
  - **Byte 9:** `0x00` ($00000000_2$)
  - **Byte 10:** `0x01` ($00000001_2$, $2^{16} / 2^{16} = 1$)
  - **Byte 11 (MSB):** `0x00` ($00000000_2$)

##### 🔹 Elemento `a[3] = 262144 / 2 + 99` (Byte 12..15)
- **Calcolo:**
  - $262144 / 2 = 2^{18} / 2 = 2^{17} = 131072 = \texttt{0x00020000}$.
  - $+99 = 64 + 32 + 2 + 1 = 2^6 + 2^5 + 2^1 + 2^0 = \texttt{0x00000063}$.
  - Somma: $131072 + 99 = 131171_{10} = \mathbf{\texttt{0x00020063}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 12 (LSB):** `0x63` ($01100011_2$)
  - **Byte 13:** `0x00` ($00000000_2$)
  - **Byte 14:** `0x02` ($00000010_2$, $2^{17} / 2^{16} = 2$)
  - **Byte 15 (MSB):** `0x00` ($00000000_2$)

---

#### 3️⃣ Mappa di Memoria di Base (Array Iniziale `a[4]` prima delle modifiche)

Questa è la mappa esatta di memoria prodotta dalla sola inizializzazione `int a[4] = {5 + 2 * 32, INT_MIN + 21, [2] = 65540, 262144 / 2 + 99};`:

|  Byte  | Puntatori Iniziali |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Elemento / Significato Iniziale |
| :----: | :----------------- | :----: | :---------------------: | :---------------------------: | :------------------------------ |
| **0**  | `a`, `&p[0]`, `&q[0]` | `0x45` |       `01000101`        |          `10100010`           | `a[0]` (LSB $= 69$)             |
| **1**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[0]`                          |
| **2**  | `&p[1]`, `&q[2]`   | `0x00` |       `00000000`        |          `00000000`           | `a[0]`                          |
| **3**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[0]` (MSB)                    |
| **4**  | `a+1`, `&p[2]`, `&q[4]` | `0x15` |       `00010101`        |          `10101000`           | `a[1]` (LSB $= 21$)             |
| **5**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[1]`                          |
| **6**  | `&p[3]`, `&q[6]`   | `0x00` |       `00000000`        |          `00000000`           | `a[1]`                          |
| **7**  |                    | `0x80` |       `10000000`        |          `00000001`           | `a[1]` (`INT_MIN` MSB)          |
| **8**  | `a+2`, `&p[4]`, `&q[8]` | `0x04` |       `00000100`        |          `00100000`           | `a[2]` (LSB $= 4$)              |
| **9**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[2]`                          |
| **10** | `&p[5]`, `&q[10]`  | `0x01` |       `00000001`        |          `10000000`           | `a[2]` ($2^{16} / 2^{16} = 1$)  |
| **11** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[2]` (MSB)                    |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0x63` |       `01100011`        |          `11000110`           | `a[3]` (LSB $= 99$)             |
| **13** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[3]`                          |
| **14** | `&p[7]`, `&q[14]`  | `0x02` |       `00000010`        |          `01000000`           | `a[3]` ($2^{17} / 2^{16} = 2$)  |
| **15** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[3]` (MSB)                    |

---

#### 4️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

1. **`*(q + 3) = -1;`**
   - **Spiegazione:** `q` è `char*` (1 byte). `*(q + 3)` equivale a `q[3]` e modifica unicamente il **Byte 3**.
   - `-1` in complemento a due su 1 byte con segno (`char`) vale $\mathbf{\texttt{0xFF}}$ ($11111111_2$).
   - **Byte 3 diventa:** `0xFF`.
   - *Effetto collaterale su `p[1]` (Byte 2..3):* Byte 2 vale `0x00` e Byte 3 vale `0xFF`, quindi come intero `short` a 16 bit con segno in Little-Endian abbiamo $\texttt{0xFF00} = \mathbf{-256_{10}}$ ($65280 - 65536 = -256$).

2. **`*((short int*)&q[5]) = 257;`**
   - **Spiegazione:** `&q[5]` è l'indirizzo del **Byte 5**. Il cast `(short int*)` scrive un intero a 16 bit (2 byte) sui **Byte 5 e 6**.
   - $257 = 256 + 1 = 2^8 + 2^0 = \texttt{0x0100} + \texttt{0x0001} = \mathbf{\texttt{0x0101}}$.
   - Disposizione Little-Endian a 16 bit:
     - **Byte 5 (LSB):** `0x01` ($00000001_2$)
     - **Byte 6 (MSB):** `0x01` ($00000001_2$)
   - **Byte 5 diventa:** `0x01` *(era `0x00`)*.
   - **Byte 6 diventa:** `0x01` *(era `0x00`)*.
   - *Effetto collaterale sugli `short`:*
     - `p[2]` (Byte 4..5): Byte 4 è `0x15` ($21$), Byte 5 è `0x01` $\implies \texttt{0x0115} = 256 + 21 = \mathbf{277_{10}}$.
     - `p[3]` (Byte 6..7): Byte 6 è `0x01`, Byte 7 è `0x80` $\implies \texttt{0x8001} = -32768 + 1 = \mathbf{-32767_{10}}$.

---

#### 5️⃣ Mappa di Memoria Finale (dopo tutte le modifiche)

|  Byte  | Puntatori Corrispondenti |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione               |
| :----: | :----------------------- | :----: | :---------------------: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]`    | `0x45` |       `01000101`        |          `10100010`           | Iniziale `a[0]` (LSB $= 69$) $\to p[0] = 69$ |
| **1**  |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[0]`                      |
| **2**  | `&p[1]`, `&q[2]`         | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[0]` $\to p[1] = -256$    |
| **3**  | `&q[3]`                  | `0xFF` |       `11111111`        |          `11111111`           | **Modificato da `*(q+3) = -1`**      |
| **4**  | `a+1`, `&p[2]`, `&q[4]`  | `0x15` |       `00010101`        |          `10101000`           | Iniziale `a[1]` (LSB $= 21$) $\to p[2] = 277$ |
| **5**  | `&q[5]`                  | `0x01` |       `00000001`        |          `10000000`           | **Modificato da `*((short*)&q[5])`** |
| **6**  | `&p[3]`, `&q[6]`         | `0x01` |       `00000001`        |          `10000000`           | **Modificato da `*((short*)&q[5])`** $\to p[3] = -32767$ |
| **7**  |                          | `0x80` |       `10000000`        |          `00000001`           | Iniziale `a[1]` (`INT_MIN`)          |
| **8**  | `a+2`, `&p[4]`, `&q[8]`  | `0x04` |       `00000100`        |          `00100000`           | Iniziale `a[2]` (LSB $= 4$) $\to p[4] = 4$ |
| **9**  |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[2]`                      |
| **10** | `&p[5]`, `&q[10]`        | `0x01` |       `00000001`        |          `10000000`           | Iniziale `a[2]` ($2^{16} / 2^{16} = 1$) $\to p[5] = 1$ |
| **11** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[2]`                      |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0x63` |       `01100011`        |          `11000110`           | Iniziale `a[3]` (LSB $= 99$) $\to p[6] = 99$ |
| **13** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[3]`                      |
| **14** | `&p[7]`, `&q[14]`        | `0x02` |       `00000010`        |          `01000000`           | Iniziale `a[3]` ($2^{17} / 2^{16} = 2$) $\to p[7] = 2$ |
| **15** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[3]`                      |

---

#### 6️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🟢 Asserzione A: `((&a[4] - a) + p[5]) % 2`

**Spiegazione:**
1. **`&a[4] - a`** è una **sottrazione tra puntatori del tipo `int*`**:
   - $\&a[4] - a = 4 - 0 = \mathbf{4}$ *(conta il numero di elementi di tipo `int` tra i due indirizzi)*.
2. **`p[5]`** legge un intero `short` a 16 bit a partire dall'offset $5 \times 2 = \text{Byte } 10$ (**Byte 10 e 11**):
   - Byte 10: `0x01`, Byte 11: `0x00` $\implies$ valore in Little-Endian: $\texttt{0x0001} = \mathbf{1}$.
3. **Calcolo finale:**
   - $(((\&a[4] - a) + p[5]) \pmod 2) = (4 + 1) \pmod 2 = 5 \pmod 2 = \mathbf{1}$.

**Esito:** Il risultato numerico è $1 \ne 0$ (valore logico Vero), quindi l'asserzione è **VERA**.

---

#### 🔴 Asserzione B: `(((int)(a + 2) - (int)&q[2]) + q[14]) % 2`

**Spiegazione:**
1. **`(int)(a + 2)`** effettua il cast a intero dell'indirizzo `a + 2` $\implies$ offset in byte: $2 \times \text{sizeof(int)} = 2 \times 4 = \mathbf{8\text{ byte}}$.
2. **`(int)&q[2]`** calcola l'indirizzo assoluto in byte di `q[2]` $\implies 2 \times \text{sizeof(char)} = 2 \times 1 = \mathbf{2\text{ byte}}$.
3. **Differenza in byte:**
   - $(int)(a + 2) - (int)\&q[2] = 8 - 2 = \mathbf{6}$.
4. **`q[14]`** legge il singolo **Byte 14** come `char`:
   - Dalla mappa di memoria, Byte 14 vale $\texttt{0x02} = \mathbf{2}$.
5. **Calcolo finale:**
   - $((6 + 2) \pmod 2) = 8 \pmod 2 = \mathbf{0}$.

**Esito:** Il risultato numerico è $0$ (valore logico Falso), quindi l'asserzione è **FALSA**.

---

#### 🔴 Asserzione C: `((q[12] >> 4) | q[4]) >= 35`

**Spiegazione:**
1. **`q[12]`** legge il singolo **Byte 12** come `char`:
   - Dalla mappa di memoria, Byte 12 vale $\texttt{0x63} = 6 \times 16 + 3 = \mathbf{99_{10}}$.
   - In binario: $99_{10} = \texttt{01100011}_2$.
2. **Shift a destra `q[12] >> 4`:**
   - Spostando i bit di 4 posizioni a destra: $\texttt{01100011}_2 \gg 4 = \texttt{00000110}_2 = \mathbf{6_{10}}$ *(equivalente alla divisione intera $\lfloor 99 / 16 \rfloor = 6$)*.
3. **`q[4]`** legge il singolo **Byte 4** come `char`:
   - Dalla mappa di memoria, Byte 4 vale $\texttt{0x15} = 1 \times 16 + 5 = \mathbf{21_{10}} = \texttt{00010101}_2$.
4. **OR bit a bit (`(q[12] >> 4) | q[4]`):**
   ```text
     0 0 0 0 0 1 1 0   (6)
   | 0 0 0 1 0 1 0 1   (21)
   -----------------
     0 0 0 1 0 1 1 1   (23)
   ```
   Il risultato dell'OR bit a bit è **$23_{10}$**.
5. **Confronto:**
   - $23 \ge 35 \implies \mathbf{\text{FALSO}}\ (0)$.

**Esito:** Poiché $23 \ge 35$ non è verificata, l'asserzione è **FALSA**.

---

### Esercizio 5 Prova 08/07/26

#### Testo
```c
int a[4] = {3 + 2 * 64, INT_MIN + 9, [2] = 131076, 524288 / 4 + 33};
short int *p = (short*) a;
char *q = (char*) a;
*(q + 2) = -1;
*((short int*)&q[9]) = 513;
```
- **Dimensioni tipi:** `int` = 4 byte, `short int` = 2 byte, `char` = 1 byte.
- **Costante:** $524288 = 2^{19}$.
- Valori rappresentati in **Little-Endian** e **Complemento a Due**.

**Affermazioni da verificare (Vere o False):**
- **A.** `((&a[3] - a) + p[5]) % 2`
- **B.** `(((int)(a + 3) - (int)&q[6]) + q[10]) % 4`
- **C.** `((q[12] >> 2) | q[4]) >= 9`

---

#### 1️⃣ Dimensioni, Puntatori e Formule degli Offset

- L'array `a` contiene 4 elementi `int` da 4 byte ciascuno:
  $$\text{Dimensione Totale} = 4 \times 4 = \mathbf{16\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 15})$$

> [!NOTE]
> **Relazione tra i Puntatori `p`, `q` e l'Array `a`:**
> - `a` (`int*`, 4 byte): blocchi da 4 byte $\implies \text{Offset} = i \times 4$ (Byte $0, 4, 8, 12$).
> - `p` (`short*`, 2 byte): blocchi da 2 byte $\implies \text{Offset} = i \times 2$ (Byte $0, 2, 4, 6, 8, 10, 12, 14$).
> - `q` (`char*`, 1 byte): singoli byte $\implies \text{Offset} = i \times 1$ (Byte $0, 1, 2, \dots, 15$).

```text
Byte:   0   1 | 2   3 | 4   5 | 6   7 | 8   9 | 10 11 | 12 13 | 14 15
      +-------+-------+-------+-------+-------+-------+-------+-------+
a   : [      a[0]     |      a[1]     |      a[2]     |      a[3]     ]
      +-------+-------+-------+-------+-------+-------+-------+-------+
p   : [  p[0] |  p[1] |  p[2] |  p[3] |  p[4] |  p[5] |  p[6] |  p[7] ]
      +-------+-------+-------+-------+-------+-------+-------+-------+
q   : [q0][q1]|[q2]...                                        ...|[q15]]
```

---

#### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione dell'array

##### 🔹 Elemento `a[0] = 3 + 2 * 64` (Byte 0..3)
- **Calcolo:** $3 + 2 \times 64 = 3 + 128 = 131_{10}$.
- **Scomposizione in potenze di 2:**
  $$131 = 128 + 2 + 1 = 2^7 + 2^1 + 2^0 = \texttt{0x80} + \texttt{0x02} + \texttt{0x01} = \mathbf{\texttt{0x00000083}}$$
- **Disposizione Little-Endian (32 bit):**
  - **Byte 0 (LSB):** `0x83` ($10000011_2$)
  - **Byte 1..3:** tutti `0x00` ($00000000_2$)

##### 🔹 Elemento `a[1] = INT_MIN + 9` (Byte 4..7)
- **Calcolo:**
  - `INT_MIN` su 32 bit con segno è $-2^{31} = \texttt{0x80000000}$.
  - $+9 = 8 + 1 = 2^3 + 2^0 = \texttt{0x00000009}$.
  - Somma: $\texttt{0x80000000} + \texttt{0x00000009} = \mathbf{\texttt{0x80000009}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 4 (LSB):** `0x09` ($00001001_2$)
  - **Byte 5..6:** `0x00` ($00000000_2$)
  - **Byte 7 (MSB):** `0x80` ($10000000_2$, bit di segno a 1)

##### 🔹 Elemento `a[2] = 131076` (Byte 8..11)
- **Calcolo tramite Designated Initializer `[2] = 131076`:**
  - $131076 = 131072 + 4 = 2^{17} + 2^2 = \texttt{0x00020000} + \texttt{0x00000004} = \mathbf{\texttt{0x00020004}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 8 (LSB):** `0x04` ($00000100_2$)
  - **Byte 9:** `0x00` ($00000000_2$)
  - **Byte 10:** `0x02` ($00000010_2$, $2^1 = 2$)
  - **Byte 11 (MSB):** `0x00` ($00000000_2$)

##### 🔹 Elemento `a[3] = 524288 / 4 + 33` (Byte 12..15)
- **Calcolo:**
  - $524288 / 4 = 2^{19} / 2^2 = 2^{17} = 131072 = \texttt{0x00020000}$.
  - $+33 = 32 + 1 = 2^5 + 2^0 = \texttt{0x00000021}$.
  - Somma: $131072 + 33 = 131105_{10} = \mathbf{\texttt{0x00020021}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 12 (LSB):** `0x21` ($00100001_2$)
  - **Byte 13:** `0x00` ($00000000_2$)
  - **Byte 14:** `0x02` ($00000010_2$)
  - **Byte 15 (MSB):** `0x00` ($00000000_2$)

---

#### 3️⃣ Mappa di Memoria di Base (Array Iniziale `a[4]` prima delle modifiche)

Questa è la mappa esatta di memoria prodotta dalla sola inizializzazione `int a[4] = {3 + 2 * 64, INT_MIN + 9, [2] = 131076, 524288 / 4 + 33};`:

|  Byte  | Puntatori Iniziali |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Elemento / Significato Iniziale |
| :----: | :----------------- | :----: | :---------------------: | :---------------------------: | :------------------------------ |
| **0**  | `a`, `&p[0]`, `&q[0]` | `0x83` |       `10000011`        |          `11000001`           | `a[0]` (LSB $= 131$)            |
| **1**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[0]`                          |
| **2**  | `&p[1]`, `&q[2]`   | `0x00` |       `00000000`        |          `00000000`           | `a[0]`                          |
| **3**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[0]` (MSB)                    |
| **4**  | `a+1`, `&p[2]`, `&q[4]` | `0x09` |       `00001001`        |          `10010000`           | `a[1]` (LSB $= 9$)              |
| **5**  |                    | `0x00` |       `00000000`        |          `00000000`           | `a[1]`                          |
| **6**  | `&p[3]`, `&q[6]`   | `0x00` |       `00000000`        |          `00000000`           | `a[1]`                          |
| **7**  |                    | `0x80` |       `10000000`        |          `00000001`           | `a[1]` (`INT_MIN` MSB)          |
| **8**  | `a+2`, `&p[4]`, `&q[8]` | `0x04` |       `00000100`        |          `00100000`           | `a[2]` (LSB $= 4$)              |
| **9**  | `&q[9]`            | `0x00` |       `00000000`        |          `00000000`           | `a[2]`                          |
| **10** | `&p[5]`, `&q[10]`  | `0x02` |       `00000010`        |          `01000000`           | `a[2]` ($2^{17} / 2^{16} = 2$)  |
| **11** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[2]` (MSB)                    |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0x21` |       `00100001`        |          `10000100`           | `a[3]` (LSB $= 33$)             |
| **13** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[3]`                          |
| **14** | `&p[7]`, `&q[14]`  | `0x02` |       `00000010`        |          `01000000`           | `a[3]` ($2^{17} / 2^{16} = 2$)  |
| **15** |                    | `0x00` |       `00000000`        |          `00000000`           | `a[3]` (MSB)                    |

---

#### 4️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

1. **`*(q + 2) = -1;`**
   - **Spiegazione:** `q` è `char*` (1 byte). `*(q + 2)` equivale a `q[2]` e modifica unicamente il **Byte 2**.
   - `-1` in complemento a due su 1 byte con segno (`char`) vale $\mathbf{\texttt{0xFF}}$ ($11111111_2$).
   - **Byte 2 diventa:** `0xFF`.
   - *Effetto collaterale su `p[1]` (Byte 2..3):* Byte 2 vale `0xFF` e Byte 3 vale `0x00`, quindi in Little-Endian `p[1] = 0x00FF = 255_{10}`.

2. **`*((short int*)&q[9]) = 513;`**
   - **Spiegazione:** `&q[9]` è l'indirizzo del **Byte 9**. Il cast `(short int*)` scrive un intero a 16 bit (2 byte) sui **Byte 9 e 10**.
   - $513 = 512 + 1 = 2^9 + 2^0 = \texttt{0x0200} + \texttt{0x0001} = \mathbf{\texttt{0x0201}}$.
   - Disposizione Little-Endian a 16 bit:
     - **Byte 9 (LSB):** `0x01` ($00000001_2$)
     - **Byte 10 (MSB):** `0x02` ($00000010_2$)
   - **Byte 9 diventa:** `0x01` *(era `0x00`)*.
   - **Byte 10 diventa:** `0x02` *(era già `0x02`)*.

---

#### 5️⃣ Mappa di Memoria Finale (dopo tutte le modifiche)

|  Byte  | Puntatori Corrispondenti |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione               |
| :----: | :----------------------- | :----: | :---------------------: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]`    | `0x83` |       `10000011`        |          `11000001`           | Iniziale `a[0]` (LSB $= 131$)        |
| **1**  |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[0]`                      |
| **2**  | `&p[1]`, `&q[2]`         | `0xFF` |       `11111111`        |          `11111111`           | **Modificato da `*(q+2) = -1`**      |
| **3**  |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[0]`                      |
| **4**  | `a+1`, `&p[2]`, `&q[4]`  | `0x09` |       `00001001`        |          `10010000`           | Iniziale `a[1]` (LSB $= 9$)          |
| **5**  |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[1]`                      |
| **6**  | `&p[3]`, `&q[6]`         | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[1]`                      |
| **7**  |                          | `0x80` |       `10000000`        |          `00000001`           | Iniziale `a[1]` (`INT_MIN`)          |
| **8**  | `a+2`, `&p[4]`, `&q[8]`  | `0x04` |       `00000100`        |          `00100000`           | Iniziale `a[2]` (LSB $= 4$)          |
| **9**  | `&q[9]`                  | `0x01` |       `00000001`        |          `10000000`           | **Modificato da `*((short*)&q[9])`** |
| **10** | `&p[5]`, `&q[10]`        | `0x02` |       `00000010`        |          `01000000`           | **Modificato da `*((short*)&q[9])`** |
| **11** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[2]`                      |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0x21` |       `00100001`        |          `10000100`           | Iniziale `a[3]` (LSB $= 33$)         |
| **13** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[3]`                      |
| **14** | `&p[7]`, `&q[14]`        | `0x02` |       `00000010`        |          `01000000`           | Iniziale `a[3]`                      |
| **15** |                          | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[3]`                      |

---

#### 6️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🟢 Asserzione A: `((&a[3] - a) + p[5]) % 2`

**Spiegazione:**
1. **`&a[3] - a`** è una **sottrazione tra puntatori del tipo `int*`**:
   - $\&a[3] - a = 3 - 0 = \mathbf{3}$ *(conta il numero di elementi di tipo `int` tra i due indirizzi)*.
2. **`p[5]`** legge un intero `short` a 16 bit a partire dall'offset $5 \times 2 = \text{Byte } 10$ (**Byte 10 e 11**):
   - Byte 10: `0x02`, Byte 11: `0x00` $\implies$ valore in Little-Endian: $\texttt{0x0002} = \mathbf{2}$.
3. **Calcolo finale:**
   - $(((\&a[3] - a) + p[5]) \pmod 2) = (3 + 2) \pmod 2 = 5 \pmod 2 = \mathbf{1}$.

**Esito:** Il risultato numerico è $1 \ne 0$ (valore logico Vero), quindi l'asserzione è **VERA**.

---

#### 🔴 Asserzione B: `(((int)(a + 3) - (int)&q[6]) + q[10]) % 4`

**Spiegazione:**
1. **`(int)(a + 3)`** effettua il cast a intero dell'indirizzo `a + 3` $\implies$ offset in byte: $3 \times \text{sizeof(int)} = 3 \times 4 = \mathbf{12\text{ byte}}$.
2. **`(int)&q[6]`** calcola l'indirizzo assoluto in byte di `q[6]` $\implies 6 \times \text{sizeof(char)} = 6 \times 1 = \mathbf{6\text{ byte}}$.
3. **Differenza in byte:**
   - $(int)(a + 3) - (int)\&q[6] = 12 - 6 = \mathbf{6}$.
4. **`q[10]`** legge il singolo **Byte 10** come `char`:
   - Dalla mappa di memoria, Byte 10 vale $\texttt{0x02} = \mathbf{2}$.
5. **Calcolo finale:**
   - $((6 + 2) \pmod 4) = 8 \pmod 4 = \mathbf{0}$.

**Esito:** Il risultato numerico è $0$ (valore logico Falso), quindi l'asserzione è **FALSA**.

---

#### 🟢 Asserzione C: `((q[12] >> 2) | q[4]) >= 9`

**Spiegazione:**
1. **`q[12]`** legge il singolo **Byte 12** come `char`:
   - Dalla mappa di memoria, Byte 12 vale $\texttt{0x21} = 2 \times 16 + 1 = \mathbf{33_{10}}$.
   - In binario: $33_{10} = \texttt{00100001}_2$.
2. **Shift a destra `q[12] >> 2`:**
   - Spostando i bit di 2 posizioni a destra: $\texttt{00100001}_2 \gg 2 = \texttt{00001000}_2 = \mathbf{8_{10}}$ *(equivalente alla divisione intera $\lfloor 33 / 4 \rfloor = 8$)*.
3. **`q[4]`** legge il singolo **Byte 4** come `char`:
   - Dalla mappa di memoria, Byte 4 vale $\texttt{0x09} = \mathbf{9_{10}} = \texttt{00001001}_2$.
4. **OR bit a bit (`(q[12] >> 2) | q[4]`):**
   ```text
     0 0 0 0 1 0 0 0   (8)
   | 0 0 0 0 1 0 0 1   (9)
   -----------------
     0 0 0 0 1 0 0 1   (9)
   ```
   Il risultato dell'OR bit a bit è **$9$**.
5. **Confronto:**
   - $9 \ge 9 \implies \mathbf{\text{VERO}}\ (1)$.

**Esito:** Poiché $9 \ge 9$ è verificata, l'asserzione è **VERA**.

---

### Esercizio 5 Prova 13/01/25

#### Testo
```c
int a[5] = {INT_MAX - 7, 1287, INT_MIN + 528, -10, 312};
short int *p = (short int*) a;
char *q = (char*) a;
p[3] = SHRT_MAX;
p[5] += 2048;
q[18] = ~q[19];
```
- **Dimensioni tipi:** `int` = 4 byte, `short int` = 2 byte, `char` = 1 byte.
- Valori rappresentati in **Little-Endian** e **Complemento a Due**.

**Affermazioni da verificare (Vere o False):**
- **A.** `(q[0] | q[1]) + q[17]`
- **B.** `*((short*)&q[17]) < 0`
- **C.** `(((int)(q + 13) - (int)(a + 1)) - q[1]) % 3`

---

#### 1️⃣ Dimensioni, Puntatori e Formule degli Offset

- L'array `a` contiene 5 elementi `int` da 4 byte ciascuno:
  $$\text{Dimensione Totale} = 5 \times 4 = \mathbf{20\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 19})$$

> [!NOTE]
> **Relazione tra i Puntatori `p`, `q` e l'Array `a`:**
> - `a` (`int*`, 4 byte): blocchi da 4 byte $\implies \text{Offset} = i \times 4$ (Byte $0, 4, 8, 12, 16$).
> - `p` (`short*`, 2 byte): blocchi da 2 byte $\implies \text{Offset} = i \times 2$ (Byte $0, 2, 4, 6, 8, 10, 12, 14, 16, 18$).
> - `q` (`char*`, 1 byte): singoli byte $\implies \text{Offset} = i \times 1$ (Byte $0, 1, 2, \dots, 19$).

```text
Byte:   0   1 | 2   3 | 4   5 | 6   7 | 8   9 | 10 11 | 12 13 | 14 15 | 16 17 | 18 19
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
a   : [      a[0]     |      a[1]     |      a[2]     |      a[3]     |      a[4]     ]
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
p   : [  p[0] |  p[1] |  p[2] |  p[3] |  p[4] |  p[5] |  p[6] |  p[7] |  p[8] |  p[9] ]
      +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
q   : [q0][q1]|[q2]...                                                        ...|[q19]]
```

---

#### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione dell'array

##### 🔹 Elemento `a[0] = INT_MAX - 7` (Byte 0..3)
- **Calcolo:**
  - $\text{INT\_MAX}$ a 32 bit con segno è $2^{31} - 1 = \texttt{0x7FFFFFFF}$.
  - $\text{INT\_MAX} - 7 = \texttt{0x7FFFFFFF} - 7 = \mathbf{\texttt{0x7FFFFFF8}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 0 (LSB):** `0xF8` ($11111000_2$)
  - **Byte 1:** `0xFF` ($11111111_2$)
  - **Byte 2:** `0xFF` ($11111111_2$)
  - **Byte 3 (MSB):** `0x7F` ($01111111_2$)

##### 🔹 Elemento `a[1] = 1287` (Byte 4..7)
- **Calcolo:**
  - $1287 = 1024 + 256 + 7 = 2^{10} + 2^8 + 7 = \texttt{0x0400} + \texttt{0x0100} + \texttt{0x0007} = \mathbf{\texttt{0x00000507}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 4 (LSB):** `0x07` ($00000111_2$)
  - **Byte 5:** `0x05` ($00000101_2$)
  - **Byte 6:** `0x00` ($00000000_2$)
  - **Byte 7 (MSB):** `0x00` ($00000000_2$)

##### 🔹 Elemento `a[2] = INT_MIN + 528` (Byte 8..11)
- **Calcolo:**
  - $\text{INT\_MIN}$ a 32 bit con segno è $-2^{31} = \texttt{0x80000000}$.
  - $+528 = 512 + 16 = 2^9 + 2^4 = \texttt{0x0200} + \texttt{0x0010} = \texttt{0x00000210}$.
  - Somma: $\texttt{0x80000000} + \texttt{0x00000210} = \mathbf{\texttt{0x80000210}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 8 (LSB):** `0x10` ($00010000_2$)
  - **Byte 9:** `0x02` ($00000010_2$)
  - **Byte 10:** `0x00` ($00000000_2$)
  - **Byte 11 (MSB):** `0x80` ($10000000_2$)

##### 🔹 Elemento `a[3] = -10` (Byte 12..15)
- **Complemento a due su 32 bit per $-10$:**
  1. Valore assoluto $+10 = \texttt{0x0000000A}$
  2. Inversione bit ($\sim$): `0xFFFFFFF5`
  3. Aggiunta di $+1$: $\texttt{0xFFFFFFF5} + 1 = \mathbf{\texttt{0xFFFFFFF6}}$ *(Verifica LSB: $256 - 10 = 246 = \texttt{0xF6}$)*
- **Disposizione Little-Endian (32 bit):**
  - **Byte 12 (LSB):** `0xF6` ($11110110_2$)
  - **Byte 13..15:** tutti `0xFF` ($11111111_2$, per estensione del segno)

##### 🔹 Elemento `a[4] = 312` (Byte 16..19)
- **Calcolo:**
  - $312 = 256 + 56 = 256 + 32 + 16 + 8 = 2^8 + 2^5 + 2^4 + 2^3 = \texttt{0x0100} + \texttt{0x0038} = \mathbf{\texttt{0x00000138}}$.
- **Disposizione Little-Endian (32 bit):**
  - **Byte 16 (LSB):** `0x38` ($00111000_2$)
  - **Byte 17:** `0x01` ($00000001_2$)
  - **Byte 18..19:** tutti `0x00` ($00000000_2$)

---

#### 3️⃣ Mappa di Memoria di Base (Array Iniziale `a[5]` prima delle modifiche)

Questa è la mappa esatta di memoria prodotta dalla sola inizializzazione `int a[5] = {INT_MAX - 7, 1287, INT_MIN + 528, -10, 312};`:

|  Byte  | Puntatori Iniziali |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Elemento / Significato Iniziale |
| :----: | :----------------- | :----: | :---------------------: | :---------------------------: | :------------------------------ |
| **0**  | `a`, `&p[0]`, `&q[0]` | `0xF8` |       `11111000`        |          `00011111`           | `a[0]` (LSB $= \text{INT\_MAX}-7$) |
| **1**  | `&q[1]`            | `0xFF` |       `11111111`        |          `11111111`           | `a[0]`                          |
| **2**  | `&p[1]`, `&q[2]`   | `0xFF` |       `11111111`        |          `11111111`           | `a[0]`                          |
| **3**  | `&q[3]`            | `0x7F` |       `01111111`        |          `11111110`           | `a[0]` (MSB)                    |
| **4**  | `a+1`, `&p[2]`, `&q[4]` | `0x07` |       `00000111`        |          `11100000`           | `a[1]` (LSB $= 7$)              |
| **5**  | `&q[5]`            | `0x05` |       `00000101`        |          `10100000`           | `a[1]` ($5 \times 256 = 1280$)  |
| **6**  | `&p[3]`, `&q[6]`   | `0x00` |       `00000000`        |          `00000000`           | `a[1]`                          |
| **7**  | `&q[7]`            | `0x00` |       `00000000`        |          `00000000`           | `a[1]` (MSB)                    |
| **8**  | `a+2`, `&p[4]`, `&q[8]` | `0x10` |       `00010000`        |          `00001000`           | `a[2]` (LSB $= 16$)             |
| **9**  | `&q[9]`            | `0x02` |       `00000010`        |          `01000000`           | `a[2]` ($2 \times 256 = 512$)   |
| **10** | `&p[5]`, `&q[10]`  | `0x00` |       `00000000`        |          `00000000`           | `a[2]`                          |
| **11** | `&q[11]`           | `0x80` |       `10000000`        |          `00000001`           | `a[2]` (`INT_MIN` MSB)          |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0xF6` |       `11110110`        |          `01101111`           | `a[3]` (LSB $= -10$)            |
| **13** | `q+13`, `&q[13]`   | `0xFF` |       `11111111`        |          `11111111`           | `a[3]` (estensione segno)       |
| **14** | `&p[7]`, `&q[14]`  | `0xFF` |       `11111111`        |          `11111111`           | `a[3]`                          |
| **15** | `&q[15]`           | `0xFF` |       `11111111`        |          `11111111`           | `a[3]` (MSB)                    |
| **16** | `a+4`, `&p[8]`, `&q[16]` | `0x38` |       `00111000`        |          `00011100`           | `a[4]` (LSB $= 56$)             |
| **17** | `&q[17]`           | `0x01` |       `00000001`        |          `10000000`           | `a[4]` ($1 \times 256 = 256$)   |
| **18** | `&p[9]`, `&q[18]`  | `0x00` |       `00000000`        |          `00000000`           | `a[4]`                          |
| **19** | `&q[19]`           | `0x00` |       `00000000`        |          `00000000`           | `a[4]` (MSB)                    |

---

#### 4️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

1. **`p[3] = SHRT_MAX;`**
   - **Spiegazione:** `p` è `short*` (2 byte). `p[3]` si trova all'offset $3 \times 2 = \text{Byte } \mathbf{6}$ e sovrascrive i **Byte 6 e 7**.
   - `SHRT_MAX` su 16 bit con segno è $2^{15} - 1 = 32767 = \mathbf{\texttt{0x7FFF}}$.
   - Little-Endian su 16 bit:
     - **Byte 6 (LSB):** `0xFF` ($11111111_2$)
     - **Byte 7 (MSB):** `0x7F` ($01111111_2$)

2. **`p[5] += 2048;`**
   - **Spiegazione:** `p[5]` si trova all'offset $5 \times 2 = \text{Byte } \mathbf{10}$ (occupa i **Byte 10 e 11**).
   - Valore iniziale di `p[5]`: Byte 10 è `0x00`, Byte 11 è `0x80` $\implies \texttt{0x8000} = -32768_{10}$.
   - $2048 = 2^{11} = \texttt{0x0800}$.
   - Somma: $\texttt{0x8000} + \texttt{0x0800} = \mathbf{\texttt{0x8800}} = -32768 + 2048 = -30720_{10}$.
   - Little-Endian nei Byte 10..11:
     - **Byte 10 (LSB):** `0x00`
     - **Byte 11 (MSB):** `0x88` ($10001000_2$)

3. **`q[18] = ~q[19];`**
   - **Spiegazione:** `q` è `char*` (1 byte). `q[19]` è il singolo **Byte 19** e vale attualmente `0x00`.
   - Negazione bit a bit NOT ($\sim$): $\sim(\texttt{0x00}) = \mathbf{\texttt{0xFF}}$ ($11111111_2$).
   - Assegnazione: **Byte 18 diventa `0xFF`** *(era `0x00`)*.
   - Il Byte 19 rimane inalterato (`0x00`).

---

#### 5️⃣ Mappa di Memoria Finale (dopo tutte le modifiche)

|  Byte  | Puntatori Corrispondenti |  Hex   | Binario (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione               |
| :----: | :----------------------- | :----: | :---------------------: | :---------------------------: | :----------------------------------- |
| **0**  | `a`, `&p[0]`, `&q[0]`    | `0xF8` |       `11111000`        |          `00011111`           | Iniziale `a[0]` (LSB)                |
| **1**  | `&q[1]`                  | `0xFF` |       `11111111`        |          `11111111`           | Iniziale `a[0]`                      |
| **2**  | `&p[1]`, `&q[2]`         | `0xFF` |       `11111111`        |          `11111111`           | Iniziale `a[0]`                      |
| **3**  | `&q[3]`                  | `0x7F` |       `01111111`        |          `11111110`           | Iniziale `a[0]` (MSB)                |
| **4**  | `a+1`, `&p[2]`, `&q[4]`  | `0x07` |       `00000111`        |          `11100000`           | Iniziale `a[1]` (LSB)                |
| **5**  | `&q[5]`                  | `0x05` |       `00000101`        |          `10100000`           | Iniziale `a[1]`                      |
| **6**  | `&p[3]`, `&q[6]`         | `0xFF` |       `11111111`        |          `11111111`           | **Modificato da `p[3] = SHRT_MAX`**  |
| **7**  | `&q[7]`                  | `0x7F` |       `01111111`        |          `11111110`           | **Modificato da `p[3] = SHRT_MAX`**  |
| **8**  | `a+2`, `&p[4]`, `&q[8]`  | `0x10` |       `00010000`        |          `00001000`           | Iniziale `a[2]` (LSB)                |
| **9**  | `&q[9]`                  | `0x02` |       `00000010`        |          `01000000`           | Iniziale `a[2]`                      |
| **10** | `&p[5]`, `&q[10]`        | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[2]`                      |
| **11** | `&q[11]`                 | `0x88` |       `10001000`        |          `00010001`           | **Modificato da `p[5] += 2048`**     |
| **12** | `a+3`, `&p[6]`, `&q[12]` | `0xF6` |       `11110110`        |          `01101111`           | Iniziale `a[3]` (LSB $= -10$)        |
| **13** | `q+13`, `&q[13]`         | `0xFF` |       `11111111`        |          `11111111`           | Iniziale `a[3]`                      |
| **14** | `&p[7]`, `&q[14]`        | `0xFF` |       `11111111`        |          `11111111`           | Iniziale `a[3]`                      |
| **15** | `&q[15]`                 | `0xFF` |       `11111111`        |          `11111111`           | Iniziale `a[3]` (MSB)                |
| **16** | `a+4`, `&p[8]`, `&q[16]` | `0x38` |       `00111000`        |          `00011100`           | Iniziale `a[4]` (LSB $= 312$)        |
| **17** | `&q[17]`                 | `0x01` |       `00000001`        |          `10000000`           | Iniziale `a[4]`                      |
| **18** | `&p[9]`, `&q[18]`        | `0xFF` |       `11111111`        |          `11111111`           | **Modificato da `q[18] = ~q[19]`**   |
| **19** | `&q[19]`                 | `0x00` |       `00000000`        |          `00000000`           | Iniziale `a[4]` (MSB)                |

---

#### 6️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🔴 Asserzione A: `(q[0] | q[1]) + q[17]`

**Spiegazione:**
1. **`q[0]`** legge il singolo **Byte 0** come `char` con segno:
   - Dalla mappa di memoria, Byte 0 vale $\texttt{0xF8}$ ($11111000_2$).
   - Con la promozione intera (integral promotion), diventa l'intero con segno $-8_{10}$ ($\texttt{0xFFFFFFF8}$).
2. **`q[1]`** legge il singolo **Byte 1** come `char` con segno:
   - Dalla mappa di memoria, Byte 1 vale $\texttt{0xFF}$ ($11111111_2$).
   - Con la promozione intera, vale $-1_{10}$ ($\texttt{0xFFFFFFFF}$).
3. **OR bit a bit `(q[0] | q[1])`:**
   - $\texttt{0xFFFFFFF8} \mid \texttt{0xFFFFFFFF} = \texttt{0xFFFFFFFF} = \mathbf{-1_{10}}$.
4. **`q[17]`** legge il singolo **Byte 17** come `char`:
   - Dalla mappa di memoria, Byte 17 vale $\texttt{0x01} = \mathbf{1_{10}}$.
5. **Calcolo finale:**
   - $(q[0] \mid q[1]) + q[17] = -1 + 1 = \mathbf{0}$.

**Esito:** Il risultato numerico è $0$ (valore logico Falso), quindi l'asserzione è **FALSA**.

---

#### 🟢 Asserzione B: `*((short*)&q[17]) < 0`

**Spiegazione:**
1. **`&q[17]`** è l'indirizzo di memoria del **Byte 17**.
2. Il cast **`(short*)`** interpreta l'indirizzo come puntatore a intero a 16 bit con segno (`short`), leggendo i 2 byte a partire da Byte 17 (**Byte 17 e Byte 18**):
   - Byte 17 (LSB): `0x01`
   - Byte 18 (MSB): `0xFF`
3. Ricostruendo il valore a 16 bit in Little-Endian:
   $$\text{Valore a 16 bit} = \texttt{0xFF01}$$
4. Poiché si tratta di un tipo con segno (`short`), il bit più significativo (bit 15) è a $1$, identificando un **numero negativo**:
   $$\texttt{0xFF01} = 65281 - 65536 = \mathbf{-255_{10}}$$
5. **Confronto:**
   - $-255 < 0 \implies \mathbf{\text{VERO}}\ (1)$.

**Esito:** Poiché il valore è strettamente minore di zero, l'asserzione è **VERA**.

---

#### 🟢 Asserzione C: `(((int)(q + 13) - (int)(a + 1)) - q[1]) % 3`

**Spiegazione:**
1. **`(int)(q + 13)`** converte a intero l'indirizzo del puntatore `q + 13`:
   - Poiché `q` parte dal Byte 0 con passi da 1 byte (`char`), l'indirizzo corrisponde esattamente all'offset **Byte 13**.
2. **`(int)(a + 1)`** converte a intero l'indirizzo del puntatore `a + 1`:
   - Poiché `a` è di tipo `int*` (`sizeof(int) = 4`), `a + 1` si trova all'offset $1 \times 4 = \mathbf{\text{Byte } 4}$.
3. **Differenza in byte:**
   - $(int)(q + 13) - (int)(a + 1) = 13 - 4 = \mathbf{9}$.
4. **`q[1]`** legge il singolo **Byte 1** come `char`:
   - Dalla mappa di memoria, Byte 1 vale $\texttt{0xFF} = \mathbf{-1_{10}}$.
5. **Calcolo finale:**
   - $((9 - (-1)) \pmod 3) = (9 + 1) \pmod 3 = 10 \pmod 3 = \mathbf{1}$.

**Esito:** Il risultato numerico è $1 \ne 0$ (valore logico Vero), quindi l'asserzione è **VERA**.