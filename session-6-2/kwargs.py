# Function accepts any keyword arguments
def create_profile(**kwargs):
    print('Profile created:')
    for key, value in kwargs.items():
        print(f' {key}: {value}')
# Call with different fields
create_profile(name='Alice', age=25)
# Profile created:
# name: Alice
# age: 25
create_profile(name='Bob', age=30, city='NYC', job='Engineer')
# Profile created:
# name: Bob
# age: 30
# city: NYC
# job: Engineer
# Flexible key-value pairs!