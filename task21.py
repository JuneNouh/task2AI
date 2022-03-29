# how to use these lists comands: len, append, [:], [3:], [-3:], [:-3], [1:-1]
languages = ['Python', 'Java', 'JavaScript']

# compute the length of languages
length = len(languages)
print(length)

# Output: 3




print(sum([1, 2, 3, 4, 5]))
# Output: 15





numbers = [9, 34, 11, -4, 27]

# find the smallest number
min_number = min(numbers)
print(min_number)

# Output: -4




numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)

# Output: 34




fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)
 # ['apple', 'banana', 'cherry', 'orange']





cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
    # ['BMW', 'Ford', 'Volvo']






fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
# 1






animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')


print(index)

# Output: 1





# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

print('Reversed List:', prime_numbers)

# Output: Reversed List: [7, 5, 3, 2]



# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)

# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]




# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# Output: 
# Removed Element: 5
# Updated List: [2, 3, 7]



# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')


print('List:', vowel)

# Output: List: ['a', 'e', 'i', 'o', 'u']








