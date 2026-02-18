# At least one condition must be True
is_weekend = True
is_holiday = False
# Can sleep in if weekend OR holiday
if is_weekend or is_holiday:
    print('Sleep in!')
else:
    print('Set alarm')
# Only one needs to be True:
# weekend=True, holiday=False → Sleep in!
# weekend=False, holiday=True → Sleep in!
# weekend=True, holiday=True → Sleep in!
# weekend=False, holiday=False → Set alarm
# or requires AT LEAST ONE True!
