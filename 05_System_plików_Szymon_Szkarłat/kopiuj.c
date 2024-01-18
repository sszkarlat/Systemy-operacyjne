#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // sprawdź liczbę argumentów
    if (argc != 4) {
        printf("Nieprawidłowa liczba argumentów, spróbuj:\n./kopiuj N FILE FILE");
        return -1;
    }

    // konwertuj argument z rozmiarem bufora na liczbę całkowitą
    int buffer = atoi(argv[1]);
    if (buffer <= 0) {
        printf("Rozmiar bufora musi być dodatnią liczbą całkowitą.\n");
        return -1;
    }

    char temp[buffer];

    // otwórz plik do odczytu
    FILE *fr = fopen(argv[2], "r");
    if (fr == NULL) {
        printf("Nie udało się otworzyć pliku %s\n", argv[2]);
        return -1;
    }

    // otwórz plik do zapisu
    FILE *fw = fopen(argv[3], "w");
    if (fw == NULL) {
        printf("Nie udało się otworzyć pliku %s\n", argv[3]);
        fclose(fr); // zamknij otwarty plik
        return -1;
    }

    // zapisz zawartość do tablicy temp i zapisz ją ponownie do innego pliku
    while (fgets(temp, buffer, fr) != NULL) {
        fwrite(temp, sizeof(char), buffer - 1, fw);
    }

    // zamknij pliki
    fclose(fr);
    fclose(fw);

    return 0;
}
