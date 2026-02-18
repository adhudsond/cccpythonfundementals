# Categorize people by age
ages = [5, 25, 15, 67, 45, 12, 70, 30, 8, 55]
children = []
adults = []
seniors = []
for age in ages:
    if age < 18:
        children.append(age)
    elif age < 65:
        adults.append(age)
else:
    seniors.append(age)
print(f'Children: {children}') # [5, 15, 12, 8]
print(f'Adults: {adults}') # [25, 45, 30, 55]
print(f'Seniors: {seniors}') # [67, 70]
# Data segmentation!