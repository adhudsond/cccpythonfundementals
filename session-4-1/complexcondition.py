# College admission logic
gpa = 3.8
test_score = 1350
has_recommendation = True
# Accept if:
# (High GPA AND good test) OR has recommendation
if (gpa >= 3.5 and test_score >= 1300) or has_recommendation:
    print('ACCEPTED!')
else:
    print('Not accepted')
# This student: Accepted!
# gpa=3.8 and test=1350 → both True → AND is True
# True OR anything → True
# Multiple paths to acceptance!