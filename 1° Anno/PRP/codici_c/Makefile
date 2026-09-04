CC = gcc
CFLAGS = -g3 -O0 -Wall -Wextra -std=c99

TARGETS = 01_conversioni 02_flusso 03_mappa_memoria 04_liste 05_matrici 06_multifile

all: $(TARGETS)

01_conversioni: 01_conversioni.c
	$(CC) $(CFLAGS) -o 01_conversioni 01_conversioni.c

02_flusso: 02_flusso_sequence_points.c
	$(CC) $(CFLAGS) -o 02_flusso 02_flusso_sequence_points.c

03_mappa_memoria: 03_mappa_memoria.c
	$(CC) $(CFLAGS) -o 03_mappa_memoria 03_mappa_memoria.c

04_liste: 04_liste_dinamiche.c
	$(CC) $(CFLAGS) -o 04_liste 04_liste_dinamiche.c

05_matrici: 05_matrici_dinamiche.c
	$(CC) $(CFLAGS) -o 05_matrici 05_matrici_dinamiche.c

06_multifile: 06_multifile_main.c 06_multifile_aux.c
	$(CC) $(CFLAGS) -o 06_multifile 06_multifile_main.c 06_multifile_aux.c

clean:
	rm -f $(TARGETS) *.o
