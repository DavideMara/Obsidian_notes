◀️ *Back to:* [[00_Index_Programmazione_Procedurale]]  

# Strutture Autoreferenziali

Parliamo di strutture autoreferenziali quando contengono un **puntatore** che *punta* a una struttura dello **stesso tipo** 

~~~
struct node{
	int data;
	struct node *nextPtr;
}
~~~
Ad esempio questa definisce il tipo `struct node`.
- `int data;` -> rappresenta il membro intero
- `struct node *nextPrt;`-> è il puntatore ad un'altra struttura `struct node`
Per indicare la fine della struttura, nell'ultimo nodo il puntatore alla struct successiva và necessariamente messo a NULL.
## Gestione dinamic memory
E' necessario richiedere memoria in fase di esecuzione, utilizziamo quindi `malloc()`, `calloc()` e `free()`.
### Funzione malloc
Per la richiesta di memoria utilizziamo `malloc()`, passandogli il quantitativo di byte da allocare. In caso di **esito positivo** restituisce un puntatore a `void*` alla **memoria allocata** (può puntare ad una variabile di un qualsiasi tipo di puntatore).
~~~
newPtr = malloc(sizeof(struct node));
~~~
Facendo questo,  instanziamo un oggetto struct node (byte di dimenzione uguale). Andremmo ad allocare una nuova area nella memoria di quel num di byte e memorizziamo il puntatore alla memoria di newPtr



