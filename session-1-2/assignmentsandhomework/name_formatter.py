# name_formatter.py

# Messy names
name1 = 'john smith'
name2 = ' ALICE JOHNSON '
name3 = 'bob JONES'

# 1) Clean (remove extra spaces) + 2) Title case
clean1 = name1.strip().title()
clean2 = name2.strip().title()
clean3 = name3.strip().title()

# 3) Print formatted names
print(clean1)
print(clean2)
print(clean3)
