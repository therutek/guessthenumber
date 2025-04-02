import random

sekretna_liczba = random.randint(1, 100)

while True:  # Pętla działa, dopóki użytkownik nie zgadnie
    zgadnij = int(input("Wybierz liczbę od 1 do 100: "))
    print("Twoja liczba to: ", zgadnij)
    if zgadnij < sekretna_liczba:
        print("Za mało!")
    elif zgadnij > sekretna_liczba:
        print("Za dużo!")
    elif zgadnij == sekretna_liczba:
        print("Brawo! Zgadłeś liczbę!")
        break