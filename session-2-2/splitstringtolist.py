# Split sentence into words
sentence = 'I love learning Python for ML'
words = sentence.split()
print(words)
# ['I', 'love', 'learning', 'Python', 'for', 'ML']
# Count words
word_count = len(words)
print(f'Words: {word_count}') # 6
# Split on different character
csv_line = 'Alice,25,Engineer,Boston'
fields = csv_line.split(',')
print(fields)
# ['Alice', '25', 'Engineer', 'Boston']
# This is how CSV files work!