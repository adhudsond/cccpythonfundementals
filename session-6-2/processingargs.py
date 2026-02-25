# *args is a tuple - loop through it
def find_max(*args):
    if not args:
        return None
    max_val = args[0]
    for num in args:
        if num > max_val:
            max_val = num
    return max_val
print(find_max(5, 2, 9, 1, 7)) # 9
print(find_max(100, 50, 75)) # 100
# Or just use max():
def find_max(*args):
    return max(args) if args else None