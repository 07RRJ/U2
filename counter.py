from collections import Counter

values = [1, 4, 6, 4, 8, 4, 4, 4]

most_common_numbers = Counter(values).most_common(2)
print(most_common_numbers)

most_common_letters = Counter("abcbadfbcb").most_common(3)
print(most_common_letters)