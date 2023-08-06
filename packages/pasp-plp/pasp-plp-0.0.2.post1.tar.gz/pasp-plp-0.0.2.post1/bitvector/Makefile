CC=gcc
CFLAGS=-Wall -Wextra -pedantic
DEBUG=

main: bitvector tests
	$(CC) $(CFLAGS) $(DEBUG) -o a.out bitvector.o tests.o

debug: DEBUG += -g
debug: main

bitvector: bitvector.c bitvector.h
	$(CC) $(CFLAGS) $(DEBUG) -c bitvector.c

tests:
	$(CC) $(CFLAGS) $(DEBUG) -c tests.c

clean:
	rm -f *.o *.out *.h.gch
