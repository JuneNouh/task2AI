num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in num_list:
    # print(num)
    if num == 1:
        continue
    if num == 2:
        print(f'Number {num} is a prime number.')
    else:
        if num % 2 != 0:
            for i in range(num_list.index(num)):

                if num / num_list[i] == 0:
                    break
            print(f'Number {num} is a prime number.')


