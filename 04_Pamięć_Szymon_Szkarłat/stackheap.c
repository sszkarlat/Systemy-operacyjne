#include <stdio.h>
#include <stdlib.h>

void statyczna() {
    double tablica[1000000];
    printf("Funkcja statyczna: Zmienna lokalna o znacznym rozmiarze utworzona.\n");

    printf("Nacisnij Enter, aby kontynuowac...\n");
    getchar();
}

void dynamiczna() {
    double *tablica = (double *)malloc(1000000 * sizeof(double));
    if (tablica == NULL) {
        printf("Blad przy alokacji dynamicznej pamieci.\n");
        exit(EXIT_FAILURE);
    }
    printf("Funkcja dynamiczna: Zmienna lokalna o znacznym rozmiarze utworzona.\n");

    printf("Nacisnij Enter, aby kontynuowac...\n");
    getchar();

    free(tablica);
    printf("Pamiec zwolniona.\n");
}

int main() {
    statyczna();

    dynamiczna();

    return 0;
}

