sentence = 'I love learning Python for ML'
# Split into words (creates a list)
words = sentence.split()
print(words)
# ['I', 'love', 'learning', 'Python', 'for', 'ML']
# Count words
word_count = len(words)
print(f'Word count: {word_count}') # 6
# Join words back together
rejoined = ' '.join(words)
print(rejoined)
# 'I love learning Python for ML'
# This is text analysis!