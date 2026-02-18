students = ['Alice', 'Bob', 'Carol', 'David']
# With enumerate
for index, name in enumerate(students):
    print(f'Student #{index + 1}: {name}')
# Output:
# Student #1: Alice
# Student #2: Bob
# Student #3: Carol
# Student #4: David
# Can also start from different number:
for index, name in enumerate(students, start=1):
    print(f'{index}. {name}')
# Automatic numbering!

# Imagine you’re processing user input and want to number invalid entries for better error messages:
responses = ["yes", "no", "maybe", "42", "banana", "yesss"]
print("Invalid answers (with line numbers):")
for idx, answer in enumerate(responses, start=1):
    if answer.lower() not in ["yes", "no"]:
        print(f" Line {idx:2d}: '{answer}' ← not allowed")
#Output:
 #Invalid answers (with line numbers):
 #Line 3: 'maybe' ← not allowed
 #Line 4: '42' ← not allowed
 #Line 5: 'banana' ← not allowed
 #Line 6: 'yesss' ← not allowed