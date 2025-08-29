from collections import Counter

numbers = [1, 4, 6, 4, 8, 4, 4, 4]
most_common_numbers = Counter(numbers).most_common(2)
print(most_common_numbers)

# letters = "abcbadfbcb"
letters = input(": ")
most_common_letters = Counter(letters).most_common(3)
print(most_common_letters)