# Generate all combinations
colors = ['red', 'blue', 'green']
sizes = ['small', 'medium', 'large']
products = []
for color in colors:
    for size in sizes:
        product = f'{size} {color} shirt'
        products.append(product)
print(products)
# ['small red shirt', 'medium red shirt', 'large red shirt',
# 'small blue shirt', 'medium blue shirt', 'large blue shirt',
# 'small green shirt', 'medium green shirt', 'large green shirt']
# 3 colors × 3 sizes = 9 products
# Automatic combinations!