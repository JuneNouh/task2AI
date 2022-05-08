def max_sum(a, b, c):
    return a + b + c - min([a, b, c])


def return_even(x):
    list_number = []
    for i in x:
        if i % 2 == 0:
            list_number.append(i)
    return list_number


def trapezoid_area(a, b, h):
    return ((a + b) / 2) * h


def christmass(deco):
    print('    ^')
    print('   ^^^')
    print(f'  ^{deco}^^^')
    print(f' ^^^^^{deco}^')
    print('  ^^^^^')
    print(f' ^^{deco}^^^^')
    print(f'^^^^^^{deco}^^')
    print('   ###')


# max_sum
result = max_sum(17, 15, 18)
print(result)

# return even
list_result = return_even([3, 2, 10, 6, 8, 15, 9, 21])
print(list_result)

# trapezoid_area
area = trapezoid_area(5, 8, 3)
print(area)

christmass("o")
