import json

# Configuration data
config = {
'model_type': 'neural_network',
'learning_rate': 0.001,
'epochs': 100,
'layers': [128, 64, 32]
}
# Write to file
with open('config.json', 'w') as file:
    json.dump(config, file, indent=2)
# Creates config.json file:
# {
# "model_type": "neural_network",
# "learning_rate": 0.001,
# ...
# Now you can share this config!