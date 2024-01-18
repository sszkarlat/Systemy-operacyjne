#include <stdio.h>
#include <stdlib.h>

#define ROWS_INITIAL 10000
#define COLS_INITIAL 10000

int main() {
    int rows = ROWS_INITIAL;
    int cols = COLS_INITIAL;

    double ***array = (double ***)malloc(rows * sizeof(double **));
    if (array == NULL) {
        fprintf(stderr, "Blad alokacji pamięci.\n");
        return 1;
    }

    for (int i = 0; i < rows; i++) {
        array[i] = (double **)malloc(cols * sizeof(double *));
        if (array[i] == NULL) {
            fprintf(stderr, "Blad alokacji pamieci.\n");
            return 1;
        }

        for (int j = 0; j < cols; j++) {
            array[i][j] = (double *)malloc(sizeof(double));
            if (array[i][j] == NULL) {
                fprintf(stderr, "Blad alokacji pamieci.\n");
                return 1;
            }
        }
    }

    printf("Alokacja pamieci zakonczona. Nacisnij dowolny klawisz, aby zakonczyc...\n");
    getchar(); // Czekaj na nacisniecie klawisza

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            free(array[i][j]);
        }
        free(array[i]);
    }
    free(array);
    printf("Zwolnienie pamieci zakonczone.\n");
    
    return 0;
}

