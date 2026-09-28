# Esercizi del Capitolo 1: Logica ed Insiemi

---
## 📚 Richiami di Teoria Essenziali

Prima di affrontare gli esercizi, ecco i concetti fondamentali del capitolo:

### Operazioni tra insiemi
| Operazione       | Simbolo         | Significato                                                  |
| ---------------- | --------------- | ------------------------------------------------------------ |
| **Unione**       | $A \cup B$      | Elementi che stanno in $A$ **oppure** in $B$ (o in entrambi) |
| **Intersezione** | $A \cap B$      | Elementi che stanno sia in $A$ **che** in $B$                |
| **Differenza**   | $A \setminus B$ | Elementi che stanno in $A$ **ma non** in $B$                 |
| **Sottoinsieme** | $A \subseteq B$ | Ogni elemento di $A$ appartiene anche a $B$                  |

### Valore assoluto
$$|x| = \begin{cases} x & \text{se } x \ge 0 \\ -x & \text{se } x < 0 \end{cases}$$
- $|x| < a \iff -a < x < a$ (intervallo aperto)
- $|x| > a \iff x < -a \text{ oppure } x > a$ (unione di semirette)
- **Disuguaglianza triangolare**: $|a + b| \le |a| + |b|$

### Potenze ($x > 0$, $a, b \in \mathbb{R}$)
- $x^{a+b} = x^a \cdot x^b$
- $(x^a)^b = x^{ab}$
- Se $x > 1$ e $a < b$, allora $x^a < x^b$ (funzione crescente)
- Se $0 < x < 1$ e $a < b$, allora $x^a > x^b$ (funzione decrescente)
- $x^{1/q} = \sqrt[q]{x}$

### Logaritmi ($b > 0$, $b \neq 1$, $x, y > 0$)
- $\log_b(xy) = \log_b x + \log_b y$
- $\log_b(x/y) = \log_b x - \log_b y$
- $\log_b(x^\alpha) = \alpha \cdot \log_b x$
- $b^{\log_b x} = x$ e $\log_b(b^a) = a$
- Cambio di base: $\log_a x = \frac{\log_b x}{\log_b a}$

---
## 📝 Testi degli Esercizi
---

### Esercizio 1.1
> 💡 **Suggerimento**: Usa la definizione di unione ($\cup$), intersezione ($\cap$) e sottoinsieme ($\subseteq$). Per dimostrare che due insiemi sono uguali, mostra che ciascuno è contenuto nell'altro.

Verificare le seguenti proprietà fondamentali della teoria degli insiemi:
1. $A \cup \emptyset = A$
2. $A \cap \emptyset = \emptyset$
3. $A \cup A = A$
4. $A \cap A = A$
5. $(A \cup B) \cup C = A \cup (B \cup C)$ (associatività dell'unione)
6. $(A \cap B) \cap C = A \cap (B \cap C)$ (associatività dell'intersezione)
7. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ (distributività dell'unione)
8. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ (distributività dell'intersezione)
9. $A \subseteq B \iff A \cup B = B$
10. $A \subseteq B \iff A \cap B = A$

---

### Esercizio 1.2
> 💡 **Suggerimento**: Pensa in modo concreto: le "donne" e gli "uomini coniugati" sono categorie che si escludono a vicenda? Possono sovrapporsi?

Sia $A$ l'insieme delle donne e $B$ l'insieme degli uomini coniugati. Descrivere a parole gli elementi dei seguenti insiemi:
* $A \cup B$
* $A \cap B$
* $A \setminus B$
* $B \setminus A$

---

### Esercizio 1.3
> 💡 **Suggerimento**: Riscrivi $x \in A \setminus (B \cap C)$ usando la definizione di differenza ($x \in A$ e $x \notin B \cap C$), poi applica la negazione logica (legge di De Morgan: $\neg(P \land Q) = \neg P \lor \neg Q$).

Dimostrare le leggi di De Morgan per la differenza di insiemi:
1. $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$
2. $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$

---

### Esercizio 1.4
> 💡 **Suggerimento**: Per risolvere una disequazione tipo $f(x) > 0$, trova gli zeri di $f$ e studia il segno nei vari intervalli usando una **tabella dei segni**.

Individuare gli elementi dei seguenti sottoinsiemi di $\mathbb{R}$:
* **a)** $A = \{x \in \mathbb{R} : x \cdot (x - 1) > 0\}$
* **b)** $A = \{x \in \mathbb{R} : x \cdot (x - 1) \le 0\}$
* **c)** $A = \{x \in \mathbb{R} : (x - 1) \cdot (x - 2) \cdot (x - 3) \ge 0\}$

---

### Esercizio 1.5
> 💡 **Suggerimento**: Scrivi esplicitamente gli elementi degli insiemi (o gli intervalli che li descrivono), poi confrontali.

Per ciascuna delle seguenti coppie di insiemi $A$ e $B$, stabilire se $A = B$, $A \subseteq B$ oppure $A \supseteq B$. Calcolare inoltre $A \cap B$, $A \cup B$, $A \setminus B$ e $B \setminus A$:
* **a)** $A = \{a \in \mathbb{R} : a < 0\}$, $\quad B = \{b \in \mathbb{R} : b \ne 0\}$
* **b)** $A = \{a : a = 3k \text{ con } k \in \mathbb{N}\}$, $\quad B = \{b : b = 7h \text{ con } h \in \mathbb{N}\}$
* **c)** $A = \{a : a = 3k \text{ con } k \in \mathbb{Z}\}$, $\quad B = \{b : b = 6h \text{ con } h \in \mathbb{Z}\}$
* **d)** $A = \{a : a \text{ numero primo e } a < 418 \text{ e } a > 3\}$, $\quad B = \{b : b \text{ numero primo e } b < \sqrt{171396} \text{ e } b^2 \ge 25\}$

---

### Esercizio 1.6
> 💡 **Suggerimento**: Ricorda che $|x| = x$ quando $x \ge 0$ e $|x| = -x$ quando $x < 0$. Inoltre $|-x| = |x|$ per ogni $x$.

Considerati i numeri reali $x, -x, -|x|, |x|, |-x|$, individuare quali di essi sono uguali tra loro e disporli in ordine crescente, distinguendo il caso $x \ge 0$ dal caso $x < 0$.

---

### Esercizio 1.7
> 💡 **Suggerimento**: Usa le regole del valore assoluto: $|x| < a \iff -a < x < a$ e $|x| > a \iff x < -a \lor x > a$. Per $|x - c| < r$ il risultato è l'intervallo centrato in $c$ con raggio $r$.

Individuare i sottoinsiemi di $\mathbb{R}$ caratterizzati dalle seguenti disuguaglianze:
* **a)** $|x| > 5$
* **b)** $|x| < 3$
* **c)** $|x - 4| < 3$
* **d)** $|x - 5| \ge 2$
* **e)** $|x \cdot (x - 1) \cdot (x + 2)| > 0$
* **f)** $|x + 1| + |x + 2| < 1$

---

### Esercizio 1.8
> 💡 **Suggerimento**: Ricorda che se la base è $> 1$, la potenza cresce al crescere dell'esponente. Se la base è tra 0 e 1, la potenza *decresce* al crescere dell'esponente. Può aiutare convertire tutto in forma decimale.

Disporre in ordine crescente le seguenti potenze:
* **a)** $2^{1/3}, \quad \left(\frac{1}{3}\right)^{-1/2}, \quad \left(\frac{3}{4}\right)^3, \quad \left(\frac{3}{5}\right)^4, \quad (0{,}3)^5, \quad (0{,}2)^6$
* **b)** $2^{1/3}, \quad 2^{3/4}, \quad 2^{-2}$
* **c)** $\left(\frac{1}{2}\right)^{1/3}, \quad \left(\frac{1}{2}\right)^{3/4}, \quad \left(\frac{1}{2}\right)^{-2}$

---

### Esercizio 1.9
> 💡 **Suggerimento**: Riscrivi entrambi i membri come potenze della stessa base. Poi uguaglia gli esponenti. Per l'equazione con il valore assoluto, distingui i casi.

Risolvere le seguenti equazioni:
* **a)** $2^{-x} = 32$
* **b)** $3^{4\sqrt{x}} - 4 \cdot 3^{2\sqrt{x}} + 3 = 0$
* **c)** $\left(\frac{3}{4}\right)^x = \left(\frac{4}{3}\right)^7$
* **d)** $3^{|x^2 - 3x + 2|} = 9^{x+1}$

---

### Esercizio 1.10
> 💡 **Suggerimento**: Le proprietà dei logaritmi derivano direttamente dalle proprietà delle potenze. Attenzione al dominio: $\log_b(x)$ è definito solo per $x > 0$.

Completare le proprietà fondamentali dei logaritmi seguendo la casistica dei segni di $x$ e $y$:
* $\log_b(xy) = \dots$
* $\log_b\left(\frac{x}{y}\right) = \dots$
* $\log_b(x^\alpha) = \dots$

---

### Esercizio 1.11
> 💡 **Suggerimento**: Per equazioni tipo $\log_b x = c$, usa la definizione: $x = b^c$. Attenzione alle condizioni sulla base del logaritmo ($b > 0$, $b \ne 1$) e sull'argomento ($x > 0$).

Risolvere le seguenti equazioni logaritmiche:
* **a)** $\log_x 64 = 6$
* **b)** $\log_{1/2} 16 = x$
* **c)** $\log_7 x = \frac{1}{3}$
* **d)** $\log_x x^2 = 1$
* **e)** $\log_{\sqrt{2}} x = \frac{2}{3}$
* **f)** $\log_{2x} x^2 = 3$

---

### Esercizio 1.12
> 💡 **Suggerimento**: La proprietà $\log(ab) = \log a + \log b$ vale solo se **entrambi** $a > 0$ e $b > 0$. Confronta i domini di definizione del membro sinistro e del membro destro.

Determinare i valori di $x$ per cui le seguenti uguaglianze sono corrette:
* **a)** $\log_2 \frac{x}{x-1} = \log_2 x - \log_2(x-1)$
* **b)** $\log(x+1)^2 = 2\log(x+1)$

---

### Esercizio 1.13
> 💡 **Suggerimento**: Per le equazioni logaritmiche, usa le proprietà per combinare i logaritmi, poi passa alla forma esponenziale. Controlla **sempre** le condizioni di esistenza alla fine!

Risolvere le seguenti equazioni logaritmiche:
* **a)** $\log(x-2) - \log(2x-1) = 0$
* **b)** $\log_{10} x + \log_{10}(2x) + \log_{10}(4x) = -3$
* **c)** $x^{\log_x(x+3)^2} = 16$
* **d)** $2\log_b^5 x = 5\log_b x - 3\log_b^3 x$
* **e)** $\log_2 x + \log_x 2 = 2$
* **f)** $\log\sqrt{x+1} + \log\sqrt{x-1} = 1$

---

### Esercizi di riepilogo del capitolo 1

#### 1.14
Determinare la scomposizione in fattori primi del numero $12^{12}$.

#### 1.15
Determinare la metà di $2^{12}$.

#### 1.16
> 💡 Esprimi tutti i numeri come potenze di 2 (quando possibile) per confrontarli.

Disporre in ordine crescente i seguenti numeri:
$$2^{1000}, \quad 2^{2002}, \quad 4^{1002}, \quad 6^{500}, \quad 8^{600}$$

#### 1.17
Determinare i valori di $a, b, c$ che rendono vere le seguenti uguaglianze:
1. $\sqrt[3]{\sqrt{5}} = \sqrt[a]{5}$
2. $\sqrt[3]{5\sqrt{5}} = \sqrt[b]{5}$
3. $\sqrt[5]{\sqrt[4]{3} \cdot \sqrt{3}} = \sqrt[c]{3}$

#### 1.18
Determinare i valori di $\alpha, \beta, \gamma$ che rendono vere le seguenti uguaglianze:
1. $(2^7)^\alpha = 2^{21}$
2. $2^7 + 2^7 = 2^\beta$
3. $2^7 \cdot 2^7 = 2^\gamma$

#### 1.19
Calcolare:
1. $\log_2(32 \cdot 8^4)$
2. $9^{\log_3 5}$
3. $5^{2 + \log_5 3}$

#### 1.20
Risolvere le seguenti equazioni:
1. $3^{2x-3} = 81$
2. $2^{(x^2)} = 1$
3. $2^{|x|} = 128^3$
4. $2^{-x} = -32$

#### 1.21
Siano $A = \{n \in \mathbb{N} \mid 1 \le n \text{ e } n \text{ pari}\}$, $B = \{n \in \mathbb{N} \mid 1 \le n \text{ e } n \text{ multiplo di } 3\}$, $C = \{n \in \mathbb{N} \mid 1 \le n \text{ e } n \text{ multiplo di } 4\}$.
Determinare:
* $A \cap C$
* $A \cap B$
* $A \setminus C$
* $B \cup C$

#### 1.22
Siano $A = \{x \in \mathbb{R} \mid -1 \le x \le 2\}$, $B = \{x \in \mathbb{R} \mid -2 < x < 2\}$, $C = [-2, -1)$.
Determinare:
* $A \setminus B$
* $C \cup B$
* $A \cap C$

---
---

## 🔑 Soluzioni Dettagliate

### Soluzione Esercizio 1.1
1. **$A \cup \emptyset = A$**: L'unione contiene gli elementi che appartengono ad $A$ o a $\emptyset$. Poiché $\emptyset$ non ha elementi, l'unione contiene solo gli elementi di $A$.
2. **$A \cap \emptyset = \emptyset$**: L'intersezione contiene gli elementi comuni ad $A$ e $\emptyset$. Poiché $\emptyset$ non contiene elementi, non vi sono elementi comuni.
3. **$A \cup A = A$** e **$A \cap A = A$**: Proprietà di idempotenza. Un elemento sta in "$A$ oppure $A$" se e solo se sta in $A$; un elemento sta in "$A$ e $A$" se e solo se sta in $A$.
4. **Associatività**: Per l'unione, $x \in (A \cup B) \cup C \iff x \in A \lor x \in B \lor x \in C \iff x \in A \cup (B \cup C)$, poiché il connettivo "oppure" è associativo. Analogo per l'intersezione con il connettivo "e".
5. **Distributività** ($A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$):
   * "$\subseteq$": Se $x \in A$, allora $x \in A \cup B$ e $x \in A \cup C$, quindi $x \in (A \cup B) \cap (A \cup C)$. Se $x \in B \cap C$, allora $x \in B$ e $x \in C$, quindi $x \in A \cup B$ e $x \in A \cup C$.
   * "$\supseteq$": Se $x \in (A \cup B) \cap (A \cup C)$, allora ($x \in A$ o $x \in B$) e ($x \in A$ o $x \in C$). Se $x \in A$ abbiamo finito. Se $x \notin A$, allora necessariamente $x \in B$ e $x \in C$, quindi $x \in B \cap C \subseteq A \cup (B \cap C)$. ✅
6. **Inclusioni**:
   * $A \subseteq B \iff A \cup B = B$: ($\Rightarrow$) Se $A \subseteq B$, ogni elemento di $A$ è già in $B$, quindi l'unione non aggiunge nulla: $A \cup B = B$. ($\Leftarrow$) Se $A \cup B = B$, ogni elemento di $A$ appartiene ad $A \cup B = B$, quindi $A \subseteq B$.
   * $A \subseteq B \iff A \cap B = A$: ($\Rightarrow$) Se $A \subseteq B$, ogni elemento di $A$ è anche in $B$, quindi gli elementi comuni sono tutti quelli di $A$. ($\Leftarrow$) Se $A \cap B = A$, allora ogni $x \in A$ appartiene ad $A \cap B$, dunque $x \in B$.

---

### Soluzione Esercizio 1.2
* **$A \cup B$**: L'insieme di tutte le persone che sono donne oppure uomini coniugati. Poiché le due categorie sono disgiunte (una donna non è un uomo e viceversa), equivale a "donne e uomini coniugati".
* **$A \cap B$**: L'insieme delle persone che sono contemporaneamente donne e uomini coniugati. Poiché un uomo non è una donna, $A \cap B = \emptyset$.
* **$A \setminus B$**: Le donne che non sono uomini coniugati. Poiché nessuna donna lo è, $A \setminus B = A$ (tutte le donne).
* **$B \setminus A$**: Gli uomini coniugati che non sono donne. Poiché nessuno lo è, $B \setminus A = B$ (tutti gli uomini coniugati).

---

### Soluzione Esercizio 1.3
1. **$A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$**:

   Partiamo dalla definizione di differenza e applichiamo la logica passo per passo:
   $$x \in A \setminus (B \cap C)$$
   $$\iff x \in A \quad\text{e}\quad x \notin (B \cap C)$$
   $$\iff x \in A \quad\text{e}\quad \neg(x \in B \text{ e } x \in C)$$
   Ora applichiamo la legge di De Morgan della logica: $\neg(P \land Q) = \neg P \lor \neg Q$:
   $$\iff x \in A \quad\text{e}\quad (x \notin B \text{ oppure } x \notin C)$$
   Distribuiamo la condizione "$x \in A$":
   $$\iff (x \in A \text{ e } x \notin B) \quad\text{oppure}\quad (x \in A \text{ e } x \notin C)$$
   $$\iff x \in (A \setminus B) \quad\text{oppure}\quad x \in (A \setminus C)$$
   $$\iff x \in (A \setminus B) \cup (A \setminus C) \quad\checkmark$$

2. **$A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$**:

   $$x \in A \setminus (B \cup C) \iff x \in A \text{ e } x \notin (B \cup C)$$
   $$\iff x \in A \text{ e } \neg(x \in B \text{ oppure } x \in C)$$
   De Morgan: $\neg(P \lor Q) = \neg P \land \neg Q$:
   $$\iff x \in A \text{ e } x \notin B \text{ e } x \notin C$$
   $$\iff (x \in A \text{ e } x \notin B) \text{ e } (x \in A \text{ e } x \notin C)$$
   $$\iff x \in (A \setminus B) \cap (A \setminus C) \quad\checkmark$$

---

### Soluzione Esercizio 1.4

* **a)** $x(x-1) > 0$

  **Passo 1**: troviamo gli zeri: $x = 0$ e $x = 1$.
  
  **Passo 2**: tabella dei segni:
  | Intervallo | $x$ | $x-1$ | Prodotto |
  |---|---|---|---|
  | $x < 0$ | $-$ | $-$ | $+$ ✅ |
  | $0 < x < 1$ | $+$ | $-$ | $-$ ❌ |
  | $x > 1$ | $+$ | $+$ | $+$ ✅ |
  
  **Risultato**: $A = (-\infty, 0) \cup (1, +\infty)$

* **b)** $x(x-1) \le 0$

  È l'insieme complementare del punto (a), con gli estremi inclusi (perché $\le$):
  $$A = [0, 1]$$

* **c)** $(x-1)(x-2)(x-3) \ge 0$

  **Zeri**: $x = 1, 2, 3$.
  
  **Tabella dei segni** (con tre fattori, il segno del prodotto si alterna):
  | Intervallo | $(x-1)$ | $(x-2)$ | $(x-3)$ | Prodotto |
  |---|---|---|---|---|
  | $x < 1$ | $-$ | $-$ | $-$ | $-$ ❌ |
  | $1 < x < 2$ | $+$ | $-$ | $-$ | $+$ ✅ |
  | $2 < x < 3$ | $+$ | $+$ | $-$ | $-$ ❌ |
  | $x > 3$ | $+$ | $+$ | $+$ | $+$ ✅ |
  
  Includendo i punti dove il prodotto è zero ($\ge$):
  $$A = [1, 2] \cup [3, +\infty)$$

---

### Soluzione Esercizio 1.5

* **a)** $A = (-\infty, 0)$ (numeri reali negativi) e $B = \mathbb{R} \setminus \{0\} = (-\infty, 0) \cup (0, +\infty)$ (numeri reali non nulli).
  * Ogni numero negativo è non nullo, quindi **$A \subseteq B$** (inclusione stretta: $A \subset B$).
  * $A \cap B = A = (-\infty, 0)$ (perché $A \subseteq B$).
  * $A \cup B = B = (-\infty, 0) \cup (0, +\infty)$ (perché $A \subseteq B$).
  * $A \setminus B = \emptyset$ (non ci sono elementi in $A$ che non stiano in $B$).
  * $B \setminus A = (0, +\infty)$ (i numeri positivi non nulli: stanno in $B$ ma non in $A$).

* **b)** $A = \{0, 3, 6, 9, 12, 15, 18, 21, \dots\}$ (multipli di 3) e $B = \{0, 7, 14, 21, \dots\}$ (multipli di 7).
  * Nessuna inclusione (es: $3 \in A \setminus B$ e $7 \in B \setminus A$).
  * $A \cap B = \{0, 21, 42, \dots\}$ = multipli di $\text{mcm}(3,7) = 21$.
  * $A \cup B = \{x \in \mathbb{N} : x \text{ è multiplo di 3 o di 7}\}$.
  * $A \setminus B = \{a \in A : a \text{ non è divisibile per 7}\}$ = es. $\{3, 6, 9, 12, 15, 18, 24, \dots\}$.
  * $B \setminus A = \{b \in B : b \text{ non è divisibile per 3}\}$ = es. $\{7, 14, 28, 35, \dots\}$.

* **c)** $A$ = multipli interi di 3, $B$ = multipli interi di 6.
  * Ogni multiplo di 6 è anche multiplo di 3 (perché $6h = 3 \cdot (2h)$), quindi **$B \subseteq A$**.
  * $A \cap B = B$
  * $A \cup B = A$
  * $A \setminus B = \{3, -3, 9, -9, 15, -15, \dots\}$ = multipli di 3 che non sono multipli di 6 (i "multipli dispari di 3").
  * $B \setminus A = \emptyset$

* **d)**
  * $A = \{a \text{ primo} : 3 < a < 418\} = \{5, 7, 11, 13, \dots, 409\}$.
  * Per $B$: calcoliamo $\sqrt{171396}$. Verifica: $414^2 = 171396$ ✅. Inoltre $b^2 \ge 25 \iff b \ge 5$ (dato che $b$ è primo, $b > 0$).
    Dunque $B = \{b \text{ primo} : 5 \le b < 414\}$.
  * Controlliamo se ci sono primi tra 414 e 417: $414$ pari, $415$ finisce per 5, $416$ pari, $417 = 3 \times 139$. **Nessun primo!**
  * L'insieme dei primi $\{5, 7, \dots, 409\}$ è lo stesso per $A$ e $B$. Quindi **$A = B$**.
  * Di conseguenza: $A \cap B = A$, $A \cup B = A$, $A \setminus B = \emptyset$, $B \setminus A = \emptyset$.

---

### Soluzione Esercizio 1.6
I cinque numeri sono $x,\; -x,\; -|x|,\; |x|,\; |-x|$.

Ricordiamo che $|-x| = |x|$ **sempre** (il valore assoluto "ignora" il segno).

* **Caso $x \ge 0$**: allora $|x| = x$ e $-|x| = -x$.
  * I valori distinti sono: $x$ e $-x$ (con $-x \le 0 \le x$).
  * Uguaglianze: $|x| = |-x| = x$ e $-|x| = -x$.
  * **Ordine crescente**: $-|x| = -x \le x = |x| = |-x|$

* **Caso $x < 0$**: allora $|x| = -x$ (positivo) e $-|x| = -(-x) = x$ (negativo).
  * I valori distinti sono: $x$ (negativo) e $-x$ (positivo).
  * Uguaglianze: $|x| = |-x| = -x$ e $-|x| = x$.
  * **Ordine crescente**: $x = -|x| \le -x = |x| = |-x|$

> In entrambi i casi, $|x| = |-x|$ e la disuguaglianza vale con $=$ solo quando $x = 0$.

---

### Soluzione Esercizio 1.7

* **a)** $|x| > 5$:
  Per definizione: $x < -5$ oppure $x > 5$.
  $$\boxed{(-\infty, -5) \cup (5, +\infty)}$$

* **b)** $|x| < 3$:
  Per definizione: $-3 < x < 3$.
  $$\boxed{(-3, 3)}$$

* **c)** $|x-4| < 3$:
  Significa "la distanza di $x$ da 4 è minore di 3", cioè $-3 < x - 4 < 3$, ovvero $1 < x < 7$.
  $$\boxed{(1, 7)}$$

* **d)** $|x-5| \ge 2$:
  Significa "la distanza di $x$ da 5 è almeno 2", cioè $x - 5 \le -2$ oppure $x - 5 \ge 2$, ovvero $x \le 3$ oppure $x \ge 7$.
  $$\boxed{(-\infty, 3] \cup [7, +\infty)}$$

* **e)** $|x(x-1)(x+2)| > 0$:
  Un valore assoluto è $> 0$ se e solo se l'argomento è $\ne 0$:
  $$x(x-1)(x+2) \ne 0 \iff x \ne 0,\; x \ne 1,\; x \ne -2$$
  $$\boxed{\mathbb{R} \setminus \{-2, 0, 1\}}$$

* **f)** $|x+1| + |x+2| < 1$:

  **Interpretazione geometrica**: $|x+1|$ è la distanza di $x$ dal punto $-1$; $|x+2|$ è la distanza di $x$ dal punto $-2$. La loro somma è la somma delle distanze di $x$ da $-1$ e da $-2$, che è **sempre** $\ge$ la distanza tra $-1$ e $-2$, cioè $1$.

  **Dimostrazione formale**: per la disuguaglianza triangolare,
  $$|x+1| + |x+2| \ge |(x+2) - (x+1)| = |1| = 1$$

  Quindi la somma è sempre $\ge 1$ e non può mai essere $< 1$.
  $$\boxed{\emptyset}$$

---

### Soluzione Esercizio 1.8

* **a)** Calcoliamo i valori approssimati:
  | Espressione | Calcolo | Valore |
  |---|---|---|
  | $(0{,}2)^6$ | $0.2^6$ | $\approx 0.000064$ |
  | $(0{,}3)^5$ | $0.3^5$ | $\approx 0.00243$ |
  | $(3/5)^4$ | $0.6^4$ | $= 0.1296$ |
  | $(3/4)^3$ | $0.75^3$ | $= 0.421875$ |
  | $2^{1/3}$ | $\sqrt[3]{2}$ | $\approx 1.260$ |
  | $(1/3)^{-1/2}$ | $\sqrt{3}$ | $\approx 1.732$ |

  **Ordine crescente**:
  $$(0{,}2)^6 < (0{,}3)^5 < \left(\frac{3}{5}\right)^4 < \left(\frac{3}{4}\right)^3 < 2^{1/3} < \left(\frac{1}{3}\right)^{-1/2}$$

* **b)** Base $2 > 1$: la funzione $2^x$ è **crescente**, quindi l'ordine segue quello degli esponenti.
  Esponenti: $-2 < \frac{1}{3} < \frac{3}{4}$.
  $$\boxed{2^{-2} < 2^{1/3} < 2^{3/4}}$$

* **c)** Base $\frac{1}{2} < 1$: la funzione $(1/2)^x$ è **decrescente**, quindi l'ordine è *invertito* rispetto agli esponenti.
  Esponenti: $-2 < \frac{1}{3} < \frac{3}{4}$, l'ordine delle potenze si inverte:
  $$\boxed{\left(\frac{1}{2}\right)^{3/4} < \left(\frac{1}{2}\right)^{1/3} < \left(\frac{1}{2}\right)^{-2}}$$

---

### Soluzione Esercizio 1.9

* **a)** $2^{-x} = 32$

  Riscriviamo: $32 = 2^5$, quindi $2^{-x} = 2^5 \implies -x = 5 \implies \boxed{x = -5}$.

* **b)** $3^{4\sqrt{x}} - 4 \cdot 3^{2\sqrt{x}} + 3 = 0$

  **Condizione di esistenza**: $x \ge 0$ (per la radice).

  **Sostituzione**: poniamo $t = 3^{2\sqrt{x}}$ (con $t > 0$). Notiamo che $3^{4\sqrt{x}} = (3^{2\sqrt{x}})^2 = t^2$.

  L'equazione diventa: $t^2 - 4t + 3 = 0$.

  Fattorizziamo: $(t-1)(t-3) = 0 \implies t = 1$ oppure $t = 3$.

  * $t = 1$: $3^{2\sqrt{x}} = 3^0 \implies 2\sqrt{x} = 0 \implies x = 0$ ✅
  * $t = 3$: $3^{2\sqrt{x}} = 3^1 \implies 2\sqrt{x} = 1 \implies \sqrt{x} = \frac{1}{2} \implies x = \frac{1}{4}$ ✅

  $$\boxed{x = 0 \quad\text{oppure}\quad x = \frac{1}{4}}$$

* **c)** $\left(\frac{3}{4}\right)^x = \left(\frac{4}{3}\right)^7$

  Riscriviamo: $\left(\frac{4}{3}\right)^7 = \left(\frac{3}{4}\right)^{-7}$, quindi $\left(\frac{3}{4}\right)^x = \left(\frac{3}{4}\right)^{-7} \implies \boxed{x = -7}$.

* **d)** $3^{|x^2 - 3x + 2|} = 9^{x+1}$

  Riscriviamo il membro destro: $9^{x+1} = 3^{2(x+1)} = 3^{2x+2}$.

  Uguagliando gli esponenti: $|x^2 - 3x + 2| = 2x + 2$.

  Poiché $|...| \ge 0$, serve $2x + 2 \ge 0 \implies x \ge -1$.

  Notiamo che $x^2 - 3x + 2 = (x-1)(x-2)$.

  **Caso 1**: $(x-1)(x-2) \ge 0$, cioè $x \le 1$ oppure $x \ge 2$:
  $$x^2 - 3x + 2 = 2x + 2 \implies x^2 - 5x = 0 \implies x(x-5) = 0$$
  $x = 0$ ✅ (soddisfa $x \le 1$ e $x \ge -1$) e $x = 5$ ✅ (soddisfa $x \ge 2$).

  **Caso 2**: $1 < x < 2$ (dove $(x-1)(x-2) < 0$):
  $$-(x^2 - 3x + 2) = 2x + 2 \implies -x^2 + 3x - 2 = 2x + 2 \implies x^2 - x + 4 = 0$$
  $\Delta = 1 - 16 = -15 < 0$: nessuna soluzione reale.

  $$\boxed{x = 0 \quad\text{oppure}\quad x = 5}$$

---

### Soluzione Esercizio 1.10

Nel dominio standard ($x > 0$ e $y > 0$):
* $\log_b(xy) = \log_b(x) + \log_b(y)$
* $\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)$
* $\log_b(x^\alpha) = \alpha \log_b(x)$

**Attenzione ai casi particolari** (quando $x$ o $y$ possono essere negativi):
* Se $x < 0$ e $y < 0$: $xy > 0$ e vale $\log_b(xy) = \log_b|x| + \log_b|y|$
* La proprietà $\log_b(x^\alpha) = \alpha \log_b(x)$ richiede $x > 0$. Se $\alpha$ è un intero pari e $x \ne 0$, si può scrivere $\log_b(x^\alpha) = \alpha \log_b|x|$

---

### Soluzione Esercizio 1.11

* **a)** $\log_x 64 = 6$

  Per definizione: $x^6 = 64$. Condizioni: $x > 0$ e $x \ne 1$.

  $x = \sqrt[6]{64} = \sqrt[6]{2^6} = \boxed{2}$ (e $2 > 0$, $2 \ne 1$ ✅).

* **b)** $\log_{1/2} 16 = x$

  Per definizione: $(1/2)^x = 16$.

  Riscriviamo: $2^{-x} = 2^4 \implies -x = 4 \implies \boxed{x = -4}$.

* **c)** $\log_7 x = \frac{1}{3}$

  Per definizione: $x = 7^{1/3} = \boxed{\sqrt[3]{7}}$.

* **d)** $\log_x x^2 = 1$

  Condizioni: $x > 0$ e $x \ne 1$.

  Usando la proprietà dei logaritmi: $\log_x x^2 = 2 \cdot \log_x x = 2 \cdot 1 = 2$.

  Quindi l'equazione diventa $2 = 1$, che è **falsa**. L'equazione **non ha soluzioni** ($\emptyset$).

* **e)** $\log_{\sqrt{2}} x = \frac{2}{3}$

  Per definizione: $x = (\sqrt{2})^{2/3} = (2^{1/2})^{2/3} = 2^{1/3} = \boxed{\sqrt[3]{2}}$.

* **f)** $\log_{2x} x^2 = 3$

  Condizioni: $2x > 0 \implies x > 0$, e $2x \ne 1 \implies x \ne 1/2$.

  Per definizione: $(2x)^3 = x^2 \implies 8x^3 = x^2$.

  Dividendo per $x^2$ (lecito perché $x > 0$): $8x = 1 \implies \boxed{x = \frac{1}{8}}$.

  Verifica: $x = 1/8 \ne 1/2$ ✅.

---

### Soluzione Esercizio 1.12

* **a)** $\log_2 \frac{x}{x-1} = \log_2 x - \log_2(x-1)$

  **Membro sinistro**: definito quando $\frac{x}{x-1} > 0$, cioè $x < 0$ oppure $x > 1$.

  **Membro destro**: richiede $x > 0$ **e** $x - 1 > 0$, cioè $x > 1$.

  Le due espressioni coincidono per il dominio comune: **$x > 1$**.

  > Per esempio, per $x = -1$: il membro sinistro vale $\log_2(1/2) = -1$ ed è definito, ma il membro destro richiede $\log_2(-1)$ che non esiste!

* **b)** $\log(x+1)^2 = 2\log(x+1)$

  **Membro sinistro**: definito quando $(x+1)^2 > 0$, cioè $x \ne -1$.

  **Membro destro**: richiede $x + 1 > 0$, cioè $x > -1$.

  L'uguaglianza è corretta per **$x > -1$**.

  > Per $x = -2$: il membro sinistro vale $\log((-1)^2) = \log 1 = 0$ ed è definito, ma il membro destro è $2\log(-1)$ che non esiste!

---

### Soluzione Esercizio 1.13

* **a)** $\log(x-2) - \log(2x-1) = 0$

  Condizioni: $x - 2 > 0$ e $2x - 1 > 0 \implies x > 2$.
  $$\log(x-2) = \log(2x-1) \implies x - 2 = 2x - 1 \implies -x = 1 \implies x = -1$$
  Ma $-1 \not> 2$. **Nessuna soluzione** ($\emptyset$).

* **b)** $\log_{10} x + \log_{10}(2x) + \log_{10}(4x) = -3$

  Condizioni: $x > 0$.

  Sommiamo i logaritmi:
  $$\log_{10}(x \cdot 2x \cdot 4x) = -3 \implies \log_{10}(8x^3) = -3 \implies 8x^3 = 10^{-3} = \frac{1}{1000}$$
  $$x^3 = \frac{1}{8000} \implies \boxed{x = \frac{1}{20}}$$

  Verifica: $x = 1/20 > 0$ ✅.

* **c)** $x^{\log_x(x+3)^2} = 16$

  Condizioni: $x > 0$, $x \ne 1$, e $(x+3)^2 > 0$ (vero per $x \ne -3$, automatico dato $x > 0$).

  Per la proprietà $b^{\log_b a} = a$:
  $$(x+3)^2 = 16 \implies x + 3 = \pm 4 \implies x = 1 \text{ oppure } x = -7$$

  Ma $x = 1$ viola $x \ne 1$ e $x = -7$ viola $x > 0$. **Nessuna soluzione** ($\emptyset$).

* **d)** $2\log_b^5 x = 5\log_b x - 3\log_b^3 x$

  Riscriviamo con $y = \log_b x$: $2y^5 + 3y^3 - 5y = 0$.

  Raccogliamo $y$: $y(2y^4 + 3y^2 - 5) = 0$.

  * $y = 0 \implies x = 1$

  * $2y^4 + 3y^2 - 5 = 0$: poniamo $z = y^2 \ge 0$:
    $2z^2 + 3z - 5 = 0 \implies (z-1)(2z+5) = 0 \implies z = 1$ (accettabile) oppure $z = -5/2$ (rifiutata).
    $z = 1 \implies y = \pm 1$:
    * $y = 1 \implies x = b$
    * $y = -1 \implies x = 1/b$

  $$\boxed{x \in \{1,\; b,\; 1/b\}}$$

* **e)** $\log_2 x + \log_x 2 = 2$

  Condizioni: $x > 0$, $x \ne 1$.

  Usando $\log_x 2 = \frac{1}{\log_2 x}$ e ponendo $y = \log_2 x$:
  $$y + \frac{1}{y} = 2 \implies y^2 - 2y + 1 = 0 \implies (y-1)^2 = 0 \implies y = 1$$
  $$\log_2 x = 1 \implies \boxed{x = 2}$$

* **f)** $\log\sqrt{x+1} + \log\sqrt{x-1} = 1$

  Condizioni: $x + 1 > 0$ e $x - 1 > 0 \implies x > 1$.

  Sommiamo (base 10):
  $$\log(\sqrt{x+1} \cdot \sqrt{x-1}) = 1 \implies \log\sqrt{x^2 - 1} = 1 \implies \sqrt{x^2-1} = 10$$
  $$x^2 - 1 = 100 \implies x^2 = 101 \implies \boxed{x = \sqrt{101}} \quad (\sqrt{101} \approx 10.05 > 1 \text{ ✅})$$

---

### Soluzioni Esercizi di Riepilogo

#### 1.14
$$12^{12} = (2^2 \cdot 3)^{12} = \boxed{2^{24} \cdot 3^{12}}$$

#### 1.15
$$\frac{2^{12}}{2} = 2^{12-1} = \boxed{2^{11}}$$

#### 1.16
Esprimiamo tutti i numeri come potenze di 2 (quando possibile):
* $2^{1000}$
* $4^{1002} = (2^2)^{1002} = 2^{2004}$
* $8^{600} = (2^3)^{600} = 2^{1800}$
* $2^{2002}$

Per $6^{500}$: $6^{500} = (2 \cdot 3)^{500} = 2^{500} \cdot 3^{500}$. Confrontiamolo con $2^{1800}$:
$6^{500} < 2^{1800} \iff 6 < 2^{1800/500} = 2^{3.6} \approx 12.13$ ✅.
E $6^{500} > 2^{1000} \iff 6 > 2^{1000/500} = 2^2 = 4$ ✅.

**Ordine crescente**:
$$\boxed{2^{1000} < 6^{500} < 8^{600} < 2^{2002} < 4^{1002}}$$

#### 1.17
1. $\sqrt[3]{\sqrt{5}} = (5^{1/2})^{1/3} = 5^{1/6} = \sqrt[6]{5} \implies \boxed{a = 6}$
2. $\sqrt[3]{5\sqrt{5}} = \sqrt[3]{5 \cdot 5^{1/2}} = \sqrt[3]{5^{3/2}} = (5^{3/2})^{1/3} = 5^{1/2} = \sqrt{5} \implies \boxed{b = 2}$
3. $\sqrt[5]{\sqrt[4]{3} \cdot \sqrt{3}} = \sqrt[5]{3^{1/4} \cdot 3^{1/2}} = \sqrt[5]{3^{3/4}} = (3^{3/4})^{1/5} = 3^{3/20} \implies \boxed{c = \frac{20}{3}}$

#### 1.18
1. $(2^7)^\alpha = 2^{7\alpha} = 2^{21} \implies 7\alpha = 21 \implies \boxed{\alpha = 3}$
2. $2^7 + 2^7 = 2 \cdot 2^7 = 2^1 \cdot 2^7 = 2^8 \implies \boxed{\beta = 8}$
3. $2^7 \cdot 2^7 = 2^{7+7} = 2^{14} \implies \boxed{\gamma = 14}$

#### 1.19
1. $\log_2(32 \cdot 8^4) = \log_2(2^5 \cdot 2^{12}) = \log_2(2^{17}) = \boxed{17}$
2. $9^{\log_3 5} = (3^2)^{\log_3 5} = 3^{2\log_3 5} = 3^{\log_3 25} = \boxed{25}$
3. $5^{2+\log_5 3} = 5^2 \cdot 5^{\log_5 3} = 25 \cdot 3 = \boxed{75}$

#### 1.20
1. $3^{2x-3} = 81 = 3^4 \implies 2x - 3 = 4 \implies x = \boxed{7/2}$
2. $2^{x^2} = 1 = 2^0 \implies x^2 = 0 \implies \boxed{x = 0}$
3. $2^{|x|} = 128^3 = (2^7)^3 = 2^{21} \implies |x| = 21 \implies \boxed{x = \pm 21}$
4. $2^{-x} = -32$: Un'esponenziale a base positiva è **sempre positiva**, quindi non può mai eguagliare un numero negativo. **Nessuna soluzione** ($\emptyset$).

#### 1.21
* $A = \{2, 4, 6, 8, \dots\}$ (pari), $B = \{3, 6, 9, 12, \dots\}$ (multipli di 3), $C = \{4, 8, 12, \dots\}$ (multipli di 4).

* **$A \cap C$**: I multipli di 4 sono tutti pari ($4 | n \implies 2 | n$), quindi $C \subseteq A$ e:
  $$A \cap C = C = \{4, 8, 12, 16, \dots\}$$

* **$A \cap B$**: I pari che sono anche multipli di 3 = multipli di $\text{mcm}(2,3) = 6$:
  $$A \cap B = \{6, 12, 18, 24, \dots\}$$

* **$A \setminus C$**: I pari che **non** sono multipli di 4, cioè i numeri della forma $4k+2$:
  $$A \setminus C = \{2, 6, 10, 14, 18, \dots\}$$

* **$B \cup C$**: I numeri che sono multipli di 3 **oppure** multipli di 4:
  $$B \cup C = \{3, 4, 6, 8, 9, 12, 15, 16, 18, 20, \dots\}$$

#### 1.22
* $A = [-1, 2]$, $B = (-2, 2)$, $C = [-2, -1)$.

* **$A \setminus B$**: Elementi in $[-1, 2]$ che **non** sono in $(-2, 2)$. L'intervallo $B$ esclude $2$, e l'intervallo $A$ include $2$. Tutti gli altri punti di $A$ (cioè $[-1, 2)$) appartengono anche a $B$. Quindi:
  $$A \setminus B = \{2\}$$

* **$C \cup B$**: $[-2, -1) \cup (-2, 2)$. L'intervallo $C$ aggiunge il punto $-2$ (incluso) che $B$ esclude. Tutti gli altri punti di $C$ sono già in $B$:
  $$C \cup B = [-2, 2)$$

* **$A \cap C$**: $[-1, 2] \cap [-2, -1)$. L'intervallo $A$ inizia da $-1$ (incluso), mentre $C$ finisce **prima** di $-1$ (escluso). Non ci sono punti in comune:
  $$A \cap C = \emptyset$$
