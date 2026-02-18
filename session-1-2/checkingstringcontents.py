filename = 'model_data.csv'
# Check if ends with .csv
if filename.endswith('.csv'):
    print('This is a CSV file!')
# Check if contains 'data'
if 'data' in filename:
    print('This file contains data')
# Check if starts with 'model'
if filename.startswith('model'):
    print('This is a model file')
# All three conditions are True!
# You're validating data programmatically!