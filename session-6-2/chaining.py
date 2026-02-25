# Mixed positive/negative numbers
numbers = [-5, 3, -1, 8, -2, 10, 0]
# Pipeline: filter positives → square them
result = list(
map(
lambda x: x**2,
filter(lambda x: x > 0, numbers)
)
)
print(result) # [9, 64, 100]
# Step by step:
# 1. filter: [3, 8, 10] (only positive)
# 2. map: [9, 64, 100] (squared)
# Functional programming pipeline!
# Very readable once you get used to it