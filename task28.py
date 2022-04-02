m = [3, -5, 2, 10, -14, 6, 8, 15, 9, 21]

sum_of_numbers_smaller_then_ten = 0

for num in m:
    if num > 0 and num < 10:
        print(num)
        sum_of_numbers_smaller_then_ten += num

print(f'The sum of numbers smaller then ten is: {sum_of_numbers_smaller_then_ten}.')