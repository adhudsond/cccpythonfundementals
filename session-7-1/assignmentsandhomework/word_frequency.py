# word_frequency.py
# Real text analysis: count word frequencies and show top 5

# Create test file
with open("words.txt", "w") as f:
    f.write("Python is great Python is powerful Python is fun")

# 1) Read file content
with open("words.txt", "r") as f:
    content = f.read()

# 2) Split into words
words = content.split()

# 3) Count frequency of each word (dict)
freq = {}
for w in words:
    # normalize to lowercase for consistent counting
    w = w.lower()
    freq[w] = freq.get(w, 0) + 1

# 4) Print top 5 most common words
# Convert dict to list of (word, count) pairs, sort by count desc, then word asc
sorted_words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

print("=" * 50)
print("WORD FREQUENCY REPORT (TOP 5)")
print("=" * 50)

top_n = 5
for word, count in sorted_words[:top_n]:
    print(f"{word}: {count}")

print("=" * 50)