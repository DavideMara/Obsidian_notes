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