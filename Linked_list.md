# Strutture Autoreferenziali

Parliamo di strutture autoreferenziali quando contengono un **puntatore** che *punta* a una struttura dello **stesso tipo** 

~~~
struct node{
	int data;
	struct node *nextPtr;
}
~~~
Ad esempio questa definisce il tipo struct node