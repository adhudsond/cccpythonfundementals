# age_validator.py
# Age validation + category system (with edge-case testing)

def categorize_age(age):
    # 2) Validate + categorize
    if age < 0 or age > 120:
        category = "Invalid age"
        message = "Please enter an age between 0 and 120."
    elif age < 13:
        category = "Child"
        message = "You are classified as a child."
    elif age < 18:
        category = "Teen"
        message = "You are classified as a teen."
    elif age < 65:
        category = "Adult"
        message = "You are classified as an adult."
    else:
        category = "Senior"
        message = "You are classified as a senior."

    # 3) Print category with message
    print(f"Age {age} -> {category}")
    print(f"Message: {message}\n")


# 1) Get age (use age = 25 for testing)
age = 25
categorize_age(age)

# Test edge cases: -1, 0, 13, 18, 65, 121
test_ages = [-1, 0, 13, 18, 65, 121]
for a in test_ages:
    categorize_age(a)
