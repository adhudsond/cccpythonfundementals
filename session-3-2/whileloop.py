# Count to 5 with while
count = 0
while count < 5:
    print(count)
count += 1 # MUST update condition!
# Output:
# 0
# 1
# 2
# 3
# 4
# If you forget 'count += 1':
# Infinite loop! (Ctrl+C to stop)
# Always update the condition variable!