import json
# Read config file
with open('config.json', 'r') as file:
    config = json.load(file)
# Use as normal Python dict
print(f"Model: {config['model_type']}")
print(f"Learning rate: {config['learning_rate']}")
# Access nested data
layers = config['layers']
print(f'Network layers: {layers}')
# Modify and save back
config['epochs'] = 150
with open('config.json', 'w') as file:
    json.dump(config, file, indent=2)
# Full CRUD operations on files!