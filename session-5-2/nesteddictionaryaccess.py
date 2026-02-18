company = {
'engineering': {
'employees': 50,
'manager': 'Alice',
'budget': 5000000
},
'marketing': {
'employees': 20,
'manager': 'Bob',
'budget': 2000000
}
}
# Access department info
eng_manager = company['engineering']['manager']
print(eng_manager) # Alice
# Calculate total employees
total = company['engineering']['employees'] + \
company['marketing']['employees']
print(f'Total employees: {total}') # 70