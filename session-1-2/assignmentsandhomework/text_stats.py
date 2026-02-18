# text_stats.py

text = 'I am learning Python and I love it!'

# 1) Total characters (including spaces)
total_chars_with_spaces = len(text)

# 2) Total characters (without spaces)
total_chars_without_spaces = len(text.replace(" ", ""))

# 3) Number of words
words = text.split()
num_words = len(words)

# 4) Average word length (letters only, ignoring punctuation)
letters_only_words = []
for w in words:
    cleaned_word = ""
    for ch in w:
        if ch.isalpha():
            cleaned_word += ch
    if cleaned_word:
        letters_only_words.append(cleaned_word)

total_letters = sum(len(w) for w in letters_only_words)
avg_word_length = total_letters / len(letters_only_words) if letters_only_words else 0

# 5) Uppercase version
upper_text = text.upper()

# 6) Lowercase version
lower_text = text.lower()

print("Text:", text)
print("1. Total characters (including spaces):", total_chars_with_spaces)
print("2. Total characters (without spaces):", total_chars_without_spaces)
print("3. Number of words:", num_words)
print("4. Average word length:", round(avg_word_length, 2))
print("5. Uppercase version:", upper_text)
print("6. Lowercase version:", lower_text)
