# Grade pass/fail
grade = 75
if grade >= 60:
    print('PASSED')
    status = 'pass'
else:
    print('FAILED')
    status = 'fail'
print(f'Status: {status}')
# One of these ALWAYS runs
# If grade is 75: prints 'PASSED'
# If grade is 45: prints 'FAILED'
# else catches everything if doesn't match!