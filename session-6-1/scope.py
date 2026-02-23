# Global variable
global_var = 'I am global'
def my_function():
# Local variable
    local_var = 'I am local'
    print(global_var) # Can access global
    print(local_var) # Can access local
my_function()
# I am global
# I am local
print(global_var) # Works
# print(local_var) # ERROR! local_var doesn't exist here
# Local variables only live inside function!
# They're created when function runs,
# deleted when function ends
