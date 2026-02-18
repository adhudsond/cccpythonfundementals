# Raw sensor data (Fahrenheit)
temps_f = [98.6, 105.2, -999, 72.1, -999, 101.3, 98.9]
# Clean and convert in ONE line!
# Remove -999, convert to Celsius, round
temps_c = [
round((temp - 32) * 5/9, 1)
for temp in temps_f
if temp > 0 # Filter out errors
]
print(temps_c)
# [37.0, 40.7, 22.3, 38.5, 37.2]
# Clean data in one comprehension!
# This is professional data cleaning!