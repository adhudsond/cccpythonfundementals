# config_manager.py
# ML Configuration Manager (save -> load -> update -> save)

import json

# 1) Create ML config dictionary
config = {
    "model": {"type": "CNN", "layers": [64, 128, 256]},
    "training": {"lr": 0.001, "epochs": 50},
    "data": {"batch_size": 32, "split": 0.8}
}

config_file = "ml_config.json"

# 2) Save to 'ml_config.json'
with open(config_file, "w") as file:
    json.dump(config, file, indent=2)

print("=" * 60)
print("CONFIG MANAGER")
print("=" * 60)
print(f"Saved initial config to: {config_file}")

# 3) Read it back
with open(config_file, "r") as file:
    loaded_config = json.load(file)

print("\nLoaded config from file successfully.")

# 4) Modify training epochs to 100
loaded_config["training"]["epochs"] = 100

# 5) Save updated config
with open(config_file, "w") as file:
    json.dump(loaded_config, file, indent=2)

print("Updated epochs to 100 and saved updated config.")

# 6) Print all settings nicely formatted
print("\n--- CURRENT ML CONFIG SETTINGS ---")
print(json.dumps(loaded_config, indent=2))
print("=" * 60)
