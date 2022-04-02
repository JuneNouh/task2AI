def christmass(deco):
    a = 7
    n = 7
    for i in range(7):
        if i > 0:
            cristmas_row = " " * a + "^" * (2 * i + 1)
            cs_list = list(cristmas_row)
            index_range = range(i)
            z = 1
            for n in index_range:
                cs_list[a + z] = deco
                z += 2
            cristmas_row = "".join(cs_list)
            print(cristmas_row)
            a -= 1
        else:
            cristmas_row = " " * a + "^" * (2 * i + 1)
            print(cristmas_row)
            a -= 1

    for b in range(n // 2):
        print("     ####")

christmass("o")