name = ' sarah johnson '
# Remove spaces from ends
clean = name.strip()
print(clean) # 'sarah johnson'
# Make uppercase
upper = clean.upper()
print(upper) # 'SARAH JOHNSON'
# Make title case (First Letter Capital)
title = clean.title()
print(title) # 'Sarah Johnson'
# Replace text
new = clean.replace('sarah', 'Sarah')
print(new) # 'Sarah johnson'