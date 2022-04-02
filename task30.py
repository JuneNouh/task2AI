def moja_funkcja():
    print("Moja funkcja")
    print("cos wypisuje")

def dzialania(a, b):
    s = a + b
    i = a * b
    d = a / b

    return [s, i, d]

moja_funkcja()
moja_funkcja()

wynik = dzialania(10, 5)
print(wynik)
