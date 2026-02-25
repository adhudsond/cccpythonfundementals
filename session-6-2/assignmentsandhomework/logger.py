# logger.py
# Flexible logger using **details

def log(level, message, **details):
    print(f"[{level}] {message}")
    if details:
        print("Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    print()  # blank line for readability


# Tests
log("INFO", "Training started")
log("ERROR", "Failed", code=404, file="data.csv")