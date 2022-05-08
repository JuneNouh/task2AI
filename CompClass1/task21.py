list_number = [5, 10, 15, 20, 25, 30]
# We can reverse a list also in this way: listReversed = list[::-1]
list_number.reverse()
print('The list reversed is: ', list_number)
# Remove the middle element from the list using pop, i removed the third index because the list has an even length
list_number.pop(3)
print(list_number)
# calculate the sum of the list
sumList = sum(list_number)
print('The sum of the values of the list is: ', sumList)
# calculate the max of the list
max_value = max(list_number)
print('The maximum value of the list is: ', max_value)
# calculate the average of the list
average = sum(list_number) / len(list_number)
print('The average of the list is: ', average)
