# text_analyzer.py
# Session 1.2 Project: Build a Text Analyzer (strings + cleaning + f-strings)

# 1) Takes any text input
raw_text = input("Enter text to analyze: ")

# 2) Cleans it (strip, lowercase)
clean_text = raw_text.strip().lower()

# Optional: ask what word(s) to search for
search_word = input("Enter a word to search for (optional): ").strip().lower()

# 3) Reports statistics (length, words, etc.)
total_chars_with_spaces = len(raw_text)
total_chars_clean_with_spaces = len(clean_text)

no_space_text = clean_text.replace(" ", "")
total_chars_no_spaces = len(no_space_text)

words = clean_text.split()
word_count = len(words)

# Average word length (letters only, ignoring punctuation)
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

# 4) Finds specific words
if search_word:
    occurrences = words.count(search_word)
    found = occurrences > 0
else:
    occurrences = 0
    found = False

# 5) Formats output professionally with f-strings
print("\n" + "=" * 40)
print("TEXT ANALYZER REPORT")
print("=" * 40)

print(f"Original text: {raw_text}")
print(f"Cleaned text:  {clean_text}")

print("\n--- Statistics ---")
print(f"Characters (original, incl. spaces): {total_chars_with_spaces}")
print(f"Characters (cleaned, incl. spaces):  {total_chars_clean_with_spaces}")
print(f"Characters (cleaned, no spaces):     {total_chars_no_spaces}")
print(f"Word count:                          {word_count}")
print(f"Average word length (letters only):  {avg_word_length:.2f}")

print("\n--- Case Versions ---")
print(f"UPPER: {raw_text.upper()}")
print(f"lower: {raw_text.lower()}")

print("\n--- Word Search ---")
if search_word:
    status = "FOUND ✅" if found else "NOT FOUND ❌"
    print(f"Search word: '{search_word}' -> {status} ({occurrences} time(s))")
else:
    print("No search word entered.")

print("\nKeep going — this is exactly how real text data gets cleaned and analyzed! 🚀")
print("=" * 40)
