1◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]  

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

### Esercizio 5 Prova 15/01/26 (7 Punti)

#### 📝 Testo
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

### 🧠 Teoria e Regole di Risoluzione

1. **Little-Endian:** I byte di un dato multi-byte vengono memorizzati partendo dal **byte meno significativo (LSB)** all'indirizzo più basso (indice di byte minore), fino al **byte più significativo (MSB)** all'indirizzo più alto.
2. **Aritmetica dei Puntatori vs Offset in Byte:**
   $$\text{Offset Byte} = \text{Indice} \times \text{sizeof}(*\text{puntatore})$$
   - Accedere a `p[k]` significa accedere ai byte da $k \times 2$ a $k \times 2 + 1$.
   - Accedere a `q[k]` significa accedere al singolo byte $k \times 1$.
   - Accedere ad `a[k]` significa accedere agli 8 byte da $k \times 8$ a $k \times 8 + 7$.
3. **Complemento a Due:**
   - I numeri positivi si convertono direttamente in binario/esadecimale.
   - I numeri negativi $-v$ si ottengono invertendo tutti i bit del valore assoluto $+v$ ($\sim$) e sommando $1$.
4. **Sottrazione tra Puntatori vs Casting ad `int`:**
   - `&p[A] - &p[B]` produce la differenza in **numero di elementi** di tipo `short` $\implies A - B$.
   - `(int)(p + A) - (int)(a + B)` converte gli indirizzi in numeri interi (byte fisici) e ne fa la differenza in **byte**.

---

### 1️⃣ Dimensioni e Formule degli Offset

- L'array `a` è composto da 3 elementi `long long` da 8 byte ciascuno:
  $$\text{Dimensione Totale} = 3 \times 8 = \mathbf{24\text{ byte}}\quad (\text{Indici da Byte 0 a Byte 23})$$
- Formule per risalire alla posizione in memoria:
  - `a[i]` $\implies \text{Byte } i \times 8$
  - `p[i]` $\implies \text{Byte } i \times 2$
  - `q[i]` $\implies \text{Byte } i \times 1$

---

### 2️⃣ Calcoli e Spiegazione dell'Inizializzazione di `a[3]`

#### 🔹 Elemento `a[0] = 1536` (Byte 0..7)
- **Spiegazione:** $1536$ è un numero positivo. Lo scomponiamo in potenze di 2 per trovare la sua rappresentazione esadecimale su 8 byte (64 bit):
  $$1536 = 1024 + 512 = 2^{10} + 2^9 = \texttt{0x0400} + \texttt{0x0200} = \mathbf{\texttt{0x0600}}$$
  Su 64 bit: `0x0000000000000600`.
- **Disposizione Little-Endian:**
  - **Byte 0 (LSB):** `0x00` ($00000000_2$)
  - **Byte 1:** `0x06` ($00000110_2$, ovvero $2^1 + 2^2$)
  - **Byte 2..7:** tutti `0x00` (bit a 0)

#### 🔹 Elemento `a[1] = -2` (Byte 8..15)
- **Spiegazione:** $-2$ è negativo, quindi usiamo il complemento a due su 64 bit:
  1. Valore assoluto $+2$: `0x0000000000000002`
  2. Inversione bit ($\sim$): `0xFFFFFFFFFFFFFFFD`
  3. Aggiunta di $+1$: $\texttt{0xFFFFFFFFFFFFFFFD} + 1 = \mathbf{\texttt{0xFFFFFFFFFFFFFFFE}}$
- **Disposizione Little-Endian:**
  - **Byte 8 (LSB):** `0xFE` ($254_{10} = 11111110_2$, bit 0 a 0 e bit 1..7 a 1)
  - **Byte 9..15:** tutti `0xFF` ($255_{10} = 11111111_2$, tutti bit a 1 per estensione del segno)

#### 🔹 Elemento `a[2] = LLONG_MIN + 512` (Byte 16..23)
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

### 3️⃣ Calcoli e Spiegazione delle Modifiche Sequenziali

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

### 4️⃣ Mappa di Memoria Completa

> [!NOTE]
> **Convenzione di Scrittura dei Bit all'Esame:**
> Nei compiti d'esame le sequenze di 8 bit di ogni byte sono spesso scritte da sinistra a destra partendo dal **bit 0 (LSB)** fino al **bit 7 (MSB)**.
> - Esempio `0x06` ($2^1 + 2^2$): in notazione convenzionale è `00000110`, all'esame è scritto `01100000` (bit 0=0, bit 1=1, bit 2=1, bit 3..7=0).

| Byte | Puntatori Corrispondenti | Hex | Binario Standard (MSB $\to$ LSB) | Binario Esame (LSB $\to$ MSB) | Dettaglio / Operazione |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | `a`, `&p[0]`, `&q[0]` | `0x00` | `00000000` | `00000000` | Iniziale `a[0]` (LSB) |
| **1** | | `0x06` | `00000110` | `01100000` | Iniziale `a[0]` ($1536 / 256$) |
| **2** | `&p[1]` | `0x02` | `00000010` | `01000000` | Modificato da `p[1] = 4098` |
| **3** | | `0x10` | `00010000` | `00001000` | Modificato da `p[1] = 4098` |
| **4** | `&p[2]` | `0x00` | `00000000` | `00000000` | Iniziale `a[0]` |
| **5** | | `0x00` | `00000000` | `00000000` | Iniziale `a[0]` |
| **6** | `&p[3]` | `0xFD` | `11111101` | `10111111` | Modificato da `p[3] = 4093` |
| **7** | | `0x0F` | `00001111` | `11110000` | Modificato da `p[3] = 4093` |
| **8** | `a+1`, `&p[4]`, `&q[8]` | `0xFE` | `11111110` | `01111111` | Iniziale `a[1] = -2` |
| **9** | | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **10** | `p+5`, `&p[5]` | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **11** | | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **12** | `&p[6]` | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **13** | | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **14** | `&p[7]` | `0xFF` | `11111111` | `11111111` | Iniziale `a[1] = -2` |
| **15** | `q+15`, `&q[15]` | `0x49` | `01001001` | `10010010` | Modificato da `*(q+15) = 73` |
| **16** | `a+2`, `&p[8]` | `0x00` | `00000000` | `00000000` | Iniziale `a[2]` (LSB) |
| **17** | | `0x02` | `00000010` | `01000000` | Iniziale `a[2]` ($+512$) |
| **18** | `&p[9]`, `&q[18]` | `0x01` | `00000001` | `10000000` | Modificato da `p[9] = 16385` |
| **19** | | `0x40` | `01000000` | `00000010` | Modificato da `p[9] = 16385` |
| **20** | `&p[10]` | `0x00` | `00000000` | `00000000` | Iniziale `a[2]` |
| **21** | | `0x00` | `00000000` | `00000000` | Iniziale `a[2]` |
| **22** | `p+11`, `&p[11]` | `0x00` | `00000000` | `00000000` | Iniziale `a[2]` |
| **23** | | `0x80` | `10000000` | `00000001` | `LLONG_MIN` (MSB) |

---

### 5️⃣ Risoluzione Dettagliata delle Asserzioni

---

#### 🟢 Asserzione A: `(*(p + 5) - p[4]) % 2`

- **Spiegazione:**
  1. `*(p + 5)` (equivalente a `p[5]`) legge uno `short` (2 byte con segno) a partire dal Byte $5 \times 2 = 10$ (quindi **Byte 10 e 11**).
     - Byte 10: `0xFF`, Byte 11: `0xFF` $\implies$ parola a 16 bit: $\texttt{0xFFFF}$.
     - Trattandosi di un tipo con segno (`short`), $\texttt{0xFFFF}$ rappresenta il valore decimale **$-1$** ($65535 - 65536 = -1$).
  2. `p[4]` legge uno `short` a partire dal Byte $4 \times 2 = 8$ (quindi **Byte 8 e 9**).
     - Byte 8: `0xFE`, Byte 9: `0xFF` $\implies$ parola a 16 bit in Little-Endian: $\texttt{0xFFFE}$.
     - Valore con segno: $\texttt{0xFFFE} = \mathbf{-2}$ ($65534 - 65536 = -2$).
  3. **Calcolo:**
     $$*(p + 5) - p[4] = (-1) - (-2) = -1 + 2 = \mathbf{1}$$
     $$1 \pmod 2 = \mathbf{1}$$
- **Esito:** Poiché il risultato è $1 \ne 0$ (valore logico Vero), l'asserzione è **VERA**.

---

#### 🔴 Asserzione B: `(((int)(p + 11) - (int)(a + 2)) + q[18]) % 7`

- **Spiegazione:**
  1. `(int)(p + 11)` effettua un **cast esplicito ad intero** del puntatore: non si applica l'aritmetica dei puntatori (che dividerebbe per `sizeof`), ma si calcola l'**indirizzo assoluto in byte**.
     - Offset del puntatore `p + 11`: $11 \times \text{sizeof(short)} = 11 \times 2 = \mathbf{22\text{ byte}}$.
  2. `(int)(a + 2)` converte in byte l'indirizzo di `a + 2`:
     - Offset del puntatore `a + 2`: $2 \times \text{sizeof(long long)} = 2 \times 8 = \mathbf{16\text{ byte}}$.
  3. Differenza in byte:
     $$(int)(p + 11) - (int)(a + 2) = 22 - 16 = \mathbf{6}$$
  4. `q[18]` legge il valore come `char` (1 byte) al **Byte 18**:
     - Dalla mappa di memoria, Byte 18 vale $\texttt{0x01} = \mathbf{1}$.
  5. **Calcolo:**
     $$(6 + 1) \pmod 7 = 7 \pmod 7 = \mathbf{0}$$
- **Esito:** Il risultato numerico è $0$ (valore logico Falso), quindi l'asserzione è **FALSA**.

---

#### 🟢 Asserzione C: `((&p[9] - &p[2]) + p[8]) % 2`

- **Spiegazione:**
  1. `&p[9] - &p[2]` è una **sottrazione tra puntatori dello stesso tipo (`short*`)**:
     - In C, la sottrazione tra puntatori `ptr1 - ptr2` calcola il **numero di elementi** del tipo puntato compresi tra i due indirizzi:
       $$\&p[9] - \&p[2] = 9 - 2 = \mathbf{7}$$
       *(Verifica tramite byte: $\frac{\text{Offset}_9 - \text{Offset}_2}{\text{sizeof(short)}} = \frac{18 - 4}{2} = \frac{14}{2} = 7$)*
  2. `p[8]` legge uno `short` a 16 bit a partire dal Byte $8 \times 2 = 16$ (quindi **Byte 16 e 17**):
     - Byte 16: `0x00`, Byte 17: `0x02` $\implies$ valore $\texttt{0x0200}$.
     - In decimale: $\texttt{0x0200} = 2 \times 16^2 = 2 \times 256 = \mathbf{512}$.
  3. **Calcolo:**
     $$(7 + 512) \pmod 2 = 519 \pmod 2 = \mathbf{1}$$
- **Esito:** Poiché il risultato è $1 \ne 0$ (valore logico Vero), l'asserzione è **VERA**.