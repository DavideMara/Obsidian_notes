Compito di Programmazione Orientata agli Oggetti - Simulazione Esame

## Esercizio 1
Si definisca una gerarchia di classi per rappresentare i dispositivi elettronici venduti in un negozio di tecnologia.
I dispositivi possono essere di due tipi: Smartphone e Notebook.
Per ogni dispositivo si rappresenti: la dimensione dello schermo in pollici (un valore double) e la quantità di memoria RAM in GB (un valore intero).
La quantità di memoria RAM non deve essere modificabile liberamente, ma solo attraverso un metodo "modificaRAM", disponibile a chiunque usi un oggetto dispositivo, che ne cambia il valore solo se il nuovo valore è maggiore di 0 ed è un valore valido (es. positivo).
Inoltre, per gli Smartphone si rappresenti se supportano la connettività 5G (un valore boolean), mentre per i Notebook si rappresenti il numero di porte USB disponibili (un valore intero).
Per entrambe le classi si definisca un metodo "calcolaPrezzo".
- Per gli Smartphone, il prezzo è calcolato come: 15.0 per ciascun pollice di dimensione dello schermo, più un costo aggiuntivo di 100.0 se il dispositivo supporta il 5G.
- Per i Notebook, il prezzo è calcolato come: 20.0 per ciascun pollice di dimensione dello schermo, più un costo aggiuntivo di 50.0 se la RAM è superiore a 8 GB.

Si definisca una classe "Negozio" che contiene come campo un array "inventario" in cui è possibile inserire sia Smartphone che Notebook.
Si definisca inoltre un costruttore della classe "Negozio" che prende due parametri n e m e che istanzia l'array "inventario" inserendo n Smartphone e m Notebook. I campi degli oggetti inseriti devono essere impostati in modo casuale (usando la classe Random).
Si definisca infine un metodo nella classe "Negozio" che, dato un intero "ramRichiesta", restituisce il massimo dei prezzi dei dispositivi con esattamente quella quantità di RAM presenti in "inventario".
Se nell'inventario non è presente alcun dispositivo con quella quantità di RAM, il metodo lancerà un'eccezione controllata (checked) di una classe "DispositivoNonTrovato" definita dall'utente.
Infine, si scriva il metodo main per testare le funzionalità della classe "Negozio".

## Esercizio 2
Si definisca una classe "Playlist" (che rappresenta una lista concatenata tramite riferimenti) utilizzata per memorizzare le canzoni in coda di riproduzione.
Per ciascuna canzone (rappresentata da una classe "ElementoCanzone" o "Canzone") si gestiscano: il titolo (String) e la durata in minuti (double).
Nella classe "Playlist" si definiscano:
- Un costruttore che, dato un intero n, costruisce una lista contenente n canzoni con titoli generati casualmente (es. "canzone" + un numero casuale) e durate casuali.
- Un metodo elastico/iterativo "cercaCanzone" che, dati una stringa "titoloCercato" e un double "durataLimite", verifica se nella playlist è presente una canzone con quel titolo e con durata inferiore a "durataLimite".
- La versione ricorsiva del metodo sopra ("cercaCanzoneRicorsiva").

Si realizzi infine una classe driver "Esercizio2" con un metodo main che:
- Costruisca una playlist di 150 canzoni.
- Stampi a video se nella playlist è presente una canzone con titolo "canzone1" e durata inferiore a 4.5 minuti usando il metodo iterativo.
- Stampi a video se nella playlist è presente una canzone con titolo "canzone2" e durata inferiore a 3.0 minuti usando il metodo ricorsivo.

## Esercizio 3
Si definisca un'applicazione client-server basata su socket.
Il server deve essere in grado di rispondere contemporaneamente a più client (multi-threaded).
Quando un client si connette, invia al server un numero casuale di righe di testo. Ciascuna riga è generata concatenando un numero casuale di volte la parola "java" (ad esempio: "java", "javajava", "javajavajava", ecc.).
La trasmissione si ritiene conclusa quando il client invia la stringa "QUIT".

Ogni volta che un client si disconnette, il server deve stampare sulla console:
- La media delle lunghezze delle stringhe ricevute finora da TUTTI i client connessi al server (stato globale condiviso).
- La media delle lunghezze delle stringhe ricevute specificamente da quel client disconnesso.
Si gestiscano opportunamente le problematiche di sincronizzazione per l'accesso ai dati condivisi tra i vari thread.