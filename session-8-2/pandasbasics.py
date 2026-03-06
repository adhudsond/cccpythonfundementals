import pandas as pd

# Create DataFrame from dict
data = {
    'name': ['Alice', 'Bob', 'Carol'],
    'age': [25, 30, 28],
    'score': [95, 87, 92]
}

df = pd.DataFrame(data)
print(df)
#     name  age  score
# 0  Alice   25     95
# 1    Bob   30     87
# 2  Carol   28     92

# Access columns
print(df['name'])  # Alice, Bob, Carol

# Filter rows
high_scorers = df[df['score'] >= 90]
print(high_scorers)  # Alice and Carol