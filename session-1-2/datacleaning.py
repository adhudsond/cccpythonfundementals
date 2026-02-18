# Messy data from spreadsheet
raw_data = [
' JOHN SMITH ',
' alice JOHNSON',
'BOB jones'
]
# Clean it up!
clean_data = []
for name in raw_data:
# Remove spaces, make title case
    clean = name.strip().title()
    clean_data.append(clean)
print(clean_data)
# ['John Smith', 'Alice Johnson', 'Bob Jones']
# You just processed data professionally!