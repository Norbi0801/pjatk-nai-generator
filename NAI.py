import random


def generuj_zadanie_perceptron():
    """
    Generuje przykładowe zadanie o perceptronie dyskretnym unipolarnym
    z losowo dobranymi liczbami dla wektora wejściowego, wag i progu.
    """
    p = tuple(random.randint(-3, 3) for _ in range(3))  # wektor p
    q = tuple(random.randint(-3, 3) for _ in range(3))  # wektor wag q
    r = random.randint(0, 3)  # próg r

    zadanie = f"""Zadanie - perceptron dyskretny unipolarny

Dany jest wektor wejściowy p = {p} oraz wektor wag perceptronu q = {q} 
i próg r = {r} dyskretnego perceptronu unipolarnego.

a) Oblicz wyjście tego perceptronu.
b) Zakładając, że uzyskane wyjście jest nieprawidłowe, oblicz - używając reguły 
   uczenia delta ze stałą uczenia a=1 - zmodyfikowany wektor wag.
c) Powiedz, czy wartość progu powinna się podnieść, czy obniżyć, aby poprawić działanie perceptronu.
"""
    return zadanie


def generuj_zadanie_kNN():
    """
    Generuje przykładowe zadanie dotyczące klasyfikatora k-NN.
    Tworzymy kilka wektorów treningowych i prosimy o klasyfikację nowego wektora.
    """
    klasy = ["A", "B", "C"]

    wektory = {}
    for klasa in klasy:
        wektory[klasa] = []
        for i in range(2):
            vec = tuple(random.randint(-2, 3) for _ in range(3))
            wektory[klasa].append(vec)

    x = tuple(random.randint(-2, 4) for _ in range(3))

    k = 3

    zadanie = "Zadanie - klasyfikator k-NN\n\n"
    zadanie += "Mając podane wektory należące do kilku klas:\n"
    for klasa in klasy:
        for i, v in enumerate(wektory[klasa], start=1):
            zadanie += f"klasa {klasa}:  {klasa.lower()}{i} = {v}\n"
    zadanie += f"\nZaklasyfikuj wektor x = {x} używając algorytmu k-NN " \
               f"(k = {k}) i zwykłej odległości euklidesowej.\n" \
               f"Zademonstruj wszystkie potrzebne obliczenia.\n"

    return zadanie


def generuj_zadanie_ewaluacja_klasyfikatora():
    """
    Generuje przykładowe zadanie z ewaluacji klasyfikatora
    (macierz omyłek, precyzja, pełność, F-miara itp.).
    """
    n = random.randint(40, 80)

    pCount = random.randint(n // 2, n)
    tp = random.randint(pCount // 2, pCount)
    tn = random.randint(0, n - pCount)

    fp = pCount - tp
    fn = (n - pCount) - tn

    zadanie = f"""Zadanie - ewaluacja klasyfikatora

Mamy zbiór testowy zawierający {n} przypadków (obserwacji). 
Każdy przypadek należy do klasy "pozytywnej" (wyzdrowiał) lub "negatywnej" (nie wyzdrowiał).

Klasyfikator przewidział, że kuracja będzie skuteczna (klasa pozytywna) w {pCount} przypadkach, 
przy czym faktycznie (True Positive) było wśród nich {tp}. Dodatkowo klasyfikator poprawnie 
przewidział nieskuteczność kuracji (True Negative) w {tn} przypadkach.

a) Zbuduj macierz omyłek (confusion matrix).
b) Oblicz wartości: TP, FP, TN, FN.
c) Oblicz i przedstaw (w postaci możliwie uproszczonego ułamka):
   - dokładność (accuracy)
   - precyzję (precision)
   - pełność (recall)
   - F-miara (F1 score)

Uwaga: Załóż, że klasa "pozytywna" to "wyzdrowiał(a)". 
"""
    return zadanie


def generuj_zadanie_k_means():
    """
    Generuje przykładowe zadanie z algorytmu k-średnich.
    """

    data_points = []
    for _ in range(4):
        vec = tuple(random.randint(-1, 3) for _ in range(3))
        data_points.append(vec)

    c1 = tuple(random.randint(-1, 3) for _ in range(3))
    c2 = tuple(random.randint(-1, 3) for _ in range(3))

    zadanie = "Zadanie - algorytm k-średnich (k-means)\n\n"
    zadanie += "Dany jest zbiór danych składający się z następujących wektorów:\n"
    for i, dp in enumerate(data_points, start=1):
        zadanie += f"{chr(96 + i)} = {dp}\n"
    zadanie += f"\nPoczątkowe wartości centroidów dwóch grup:\n"
    zadanie += f"c1 = {c1}\n"
    zadanie += f"c2 = {c2}\n"
    zadanie += (
        "\nWykonaj obliczenia dla algorytmu k-średnich (k = 2). "
        "W każdej iteracji przypisz wektory do najbliższego centroidu "
        "(w razie remisu wybierz grupę o mniejszym numerze), "
        "oblicz nowe wartości centroidów, i kontynuuj aż do stabilizacji przypisań. "
        "Podaj końcowy podział na grupy oraz końcowe położenie centroidów.\n"
    )

    return zadanie


def generuj_zestaw_zadan():
    """
    Funkcja generuje cały zestaw zadań (perceptron, k-NN, ewaluacja, k-means).
    Możesz oczywiście dostosować, które zadania chcesz wylosować.
    """
    zadania = [
        generuj_zadanie_perceptron(),
        generuj_zadanie_kNN(),
        generuj_zadanie_ewaluacja_klasyfikatora(),
        generuj_zadanie_k_means()
    ]

    print( "\n---\n".join(zadania))
    print("-----------------------------------------------------------------------------------------------------------")


def main():
    generuj_zestaw_zadan()

if __name__ == "__main__":
    main()
