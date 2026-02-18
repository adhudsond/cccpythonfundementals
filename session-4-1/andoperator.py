# Both conditions must be True
age = 25
has_license = True
# Can rent car if age >= 21 AND has license
if age >= 21 and has_license:
    print('You can rent a car')
else:
    print('Cannot rent car')
# Both must be True:
# age=25, license=True → Can rent
# age=18, license=True → Cannot (age fails)
# age=25, license=False → Cannot (license fails)
# and requires ALL conditions True!