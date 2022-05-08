# Task 30
# Every programmer should be able to write his/her own functions.
# We define new functions with a def command.
# Then we come up with a name of our new function Test the program and see what it does:

def moja_funkcja():
    print("moja funkcja")
    print("cos wypisuje")


def dzialania(a, b):
    S = a + b
    I = a * b
    D = a / b
    return [S, I, D]


moja_funkcja()
moja_funkcja()

wynik = dzialania(10, 5)
print(wynik)
