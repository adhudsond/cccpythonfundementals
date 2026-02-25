# All three types of parameters
def process_data(operation, *args, **kwargs):
    print(f'Operation: {operation}')
    print(f'Data: {args}')
    print(f'Options: {kwargs}')
# Call with all types
process_data(
'analyze', # regular
10, 20, 30, # *args
method='mean', # **kwargs
precision=2
)
# Output:
# Operation: analyze
# Data: (10, 20, 30)
# Options: {'method': 'mean', 'precision': 2}
# Super flexible!