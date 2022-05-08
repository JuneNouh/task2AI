# The for command creates a loop and executes a command or a block of commands many times. It uses a special
# temporary variable (usually i or j) to iterate through all the objects in the list/range. Write this program down.
# Before you see the result, try to guess it.

print("Drukujemy liczby z zakresu:")
for i in range(1, 20, 3):
    print(i)
# 1,4,7,10,13,16,19
print("Drukujemy liczby z listy:")
for i in [4, 5, 10, 2, 5]:
    print(i)
# 4,5,10,2,5
print("Drukujemy wielokrotnie napis:")
for i in range(5):
    print("Hi!")
# five times Hi!
