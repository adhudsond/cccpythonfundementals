# Old way (DON'T use this)
name = 'Sarah'
age = 32
message = 'My name is ' + name + ' and I am ' + str(age)
# F-STRING way (USE THIS!)
message = f'My name is {name} and I am {age}'
# Python handles everything automatically!
# Notice the 'f' before the quote
# Variables go in {curly braces}
# F-strings can even do math:
score = 87
print(f'You scored {score}% which is {score/100:.2f}')
# Output: You scored 87% which is 0.87