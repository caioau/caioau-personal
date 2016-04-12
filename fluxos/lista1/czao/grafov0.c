/*

Objetivo: implementar em czao um "lib" para grafos



*/

#include <stdio.h>
#include <stdlib.h>


struct cel{
	int prox;
	double peso;
	struct cel *prox;
};

typedef struct cel cel;

struct grafo{
	int nn; // numero de nos
	int na; // numero de arcos (estamos usando apenas arestas por enquanto)
	cel **eds; // lista de adjacencias , representando os arcos
};

typedef struct grafo grafo;

/* Prototipos de funcoes*/

int main(){ // fazer o maic num main.c separado



	return 0;
}
