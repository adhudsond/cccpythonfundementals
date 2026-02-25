# config_builder.py
# Build ML config function with **kwargs

def create_ml_config(**kwargs):
    # Default config
    config = {
        "learning_rate": 0.01,
        "epochs": 100,
        "batch_size": 32
    }

    # Update with kwargs
    config.update(kwargs)
    return config


# Tests
print(create_ml_config())
print(create_ml_config(epochs=150, lr=0.001))