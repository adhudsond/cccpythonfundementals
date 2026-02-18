# Join words with spaces
words = ['I', 'love', 'Python']
sentence = ' '.join(words)
print(sentence) # 'I love Python'
# Join with different separator
words = ['apple', 'banana', 'cherry']
csv = ','.join(words)
print(csv) # 'apple,banana,cherry'
# Join with newlines
lines = ['Line 1', 'Line 2', 'Line 3']
text = '\n'.join(lines)
print(text)
# Line 1
# Line 2
# Line 3
# Essential for file writing!