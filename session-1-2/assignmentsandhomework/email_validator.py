# email_validator.py

email1 = 'user@company.com'
email2 = 'invalid.email'
email3 = ' USER@EMAIL.COM '

emails = [email1, email2, email3]

for email in emails:
    # 1) Remove spaces + 2) Convert to lowercase
    cleaned = email.strip().lower()

    # 3) Check if contains '@' and '.'
    is_valid = ('@' in cleaned) and ('.' in cleaned)

    # 4) Print 'Valid' or 'Invalid'
    if is_valid:
        print(f"{cleaned} -> Valid")

        # Bonus: Extract username and domain
        username, domain = cleaned.split('@', 1)
        print(f"  Username: {username}")
        print(f"  Domain:   {domain}")
    else:
        print(f"{cleaned} -> Invalid")
