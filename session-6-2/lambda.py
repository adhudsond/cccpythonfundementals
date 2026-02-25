# Regular function
def square(x):
    return x ** 2
result = square(5)
print(result) # 25
# Lambda function (same thing)
square_lambda = lambda x: x ** 2
result = square_lambda(5)
print(result) # 25
# Or use inline (no variable):
result = (lambda x: x ** 2)(5)
print(result) # 25
# Lambda = quick throwaway function