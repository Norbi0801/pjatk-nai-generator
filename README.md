# Repozytorium NAI

To repozytorium zawiera kod w języku Python, który generuje losowe zadania z zakresu sieci neuronowych i uczenia maszynowego (NAI). Główne zadania obejmują:

- **Perceptron dyskretny unipolarny** – obliczenia związane z działaniem perceptronu, w tym obliczenie wyjścia, korektę wag metodą reguły delta oraz analizę zmiany progu.
- **Klasyfikator k-NN** – zadanie polegające na klasyfikacji nowego wektora przy użyciu algorytmu k-NN z wykorzystaniem odległości euklidesowej.
- **Ewaluacja klasyfikatora** – zadanie obejmujące budowę macierzy omyłek oraz obliczanie miar oceny, takich jak dokładność, precyzja, pełność i F-miara.
- **Algorytm k-średnich (k-means)** – zadanie, w którym przydziela się dane do grup i oblicza nowe centroidy, aż do osiągnięcia stabilnego podziału.

## Zawartość repozytorium

- `NAI.py` – główny plik zawierający kod generujący zadania. Znajdziesz w nim funkcje:
  - `generuj_zadanie_perceptron()` – generuje zadanie dotyczące perceptronu.
  - `generuj_zadanie_kNN()` – generuje zadanie związane z klasyfikatorem k-NN.
  - `generuj_zadanie_ewaluacja_klasyfikatora()` – generuje zadanie dotyczące ewaluacji klasyfikatora.
  - `generuj_zadanie_k_means()` – generuje zadanie związane z algorytmem k-średnich.
  - `generuj_zestaw_zadan()` – łączy powyższe zadania w jeden zestaw i wypisuje je w konsoli.
  - `main()` – funkcja główna, która uruchamia generowanie zestawu zadań.

## Wymagania

- Python 3.x

## Jak uruchomić

1. **Sklonuj repozytorium**
2. **Uruchom skrypt**
   ```bash
   python NAI.py
   ```
3. **W konsoli pokaże się wygenerowany zestaw**
   
