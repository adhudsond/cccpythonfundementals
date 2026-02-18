# Very frequent in real workflows:
# Keep only emails that look valid and convert to lowercase
raw_emails = ["alice@company.com", "bob@home", "charlie@gmail.com", "", "DAVE@WORK.COM "]
valid_emails = []
for email in raw_emails:
 cleaned = email.strip().lower()
 if "@" in cleaned and "." in cleaned.split("@")[-1]:
    valid_emails.append(cleaned)
print(valid_emails)
# ['alice@company.com', 'charlie@gmail.com', 'dave@work.com'] 