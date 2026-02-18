email = 'sarah.johnson@techcompany.com'
# Find position of @
at_position = email.index('@')
# Result: 13
# Extract username (before @)
username = email[:at_position]
print(username) # 'sarah.johnson'
# Extract domain (after @)
domain = email[at_position+1:]
print(domain) # 'techcompany.com'
# This is data extraction!
# You're processing data like a pro!