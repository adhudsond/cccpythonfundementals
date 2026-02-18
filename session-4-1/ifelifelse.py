# Convert number to letter grade
score = 87
if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'
print(f'Score {score} = Grade {letter}')
# Output: Score 87 = Grade B
# Checks in order, stops at first True
# 87 >= 90? No. >= 80? Yes! → 'B', done!