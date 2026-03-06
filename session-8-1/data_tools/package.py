# Import from package
from data_tools import readers
from data_tools import writers
# Use modules
data = readers.read_csv('file.csv')
writers.write_csv('out.csv', data)
# Or import specific functions
from data_tools.readers import read_csv
from data_tools.writers import write_csv
data = read_csv('file.csv')
write_csv('out.csv', data)
# Organized and professional!
# Each module has single responsibility