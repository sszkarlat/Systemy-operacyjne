#include <iostream>
#include <fstream>

int main(int args, char *argv[])
{
    // sprawdzenie liczby argumentow
    if (args != 4)
    {
        std::cout << "Error! Bledne dane wejsciowe\n./kopiuj liczba_kopii kopiowanyPlik plikWynikowy" << std::endl;
        return -1;
    }

    // konwersja rozmiaru bufora na liczbe calkowita
    int rozmiar_bufora = std::stoi(argv[1]);
    if (rozmiar_bufora <= 0)
    {
        std::cout << "Rozmiar bufora musi byc dodatnia liczba calkowita." << std::endl;
        return -1;
    }

    char bufor_tymczasowy[rozmiar_bufora];

    // otwarcie pliku do odczytu
    std::ifstream czytaj(argv[2]);
    if (!czytaj.is_open())
    {
        std::cout << "Otwarcie pliku sie nie powiodlo " << argv[2] << std::endl;
        return -1;
    }

    // otwarcie pliku do zapisu
    std::ofstream zapisz(argv[3]);
    if (!zapisz.is_open())
    {
        std::cout << "Otwarcie pliku sie nie powiodlo " << argv[3] << std::endl;
        czytaj.close();
        return -1;
    }

    // zapisanie zawartosci do tablicy bufor_tymczasowy
    while (czytaj.getline(bufor_tymczasowy, rozmiar_bufora))
    {
        zapisz.write(bufor_tymczasowy, rozmiar_bufora - 1);
    }

    // zamykanie plikow
    czytaj.close();
    zapisz.close();

    return 0;
}
