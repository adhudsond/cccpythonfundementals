numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6, 8, 10]
# Get numbers > 5
above_5 = list(filter(lambda x: x > 5, numbers))
print(above_5) # [6, 7, 8, 9, 10]
# Filter strings by length
words = ['hi', 'hello', 'hey', 'goodbye']
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words) # ['hello', 'goodbye']
# Same as: [x for x in numbers if x % 2 == 0]
# But filter is functional style