tasks = ['email', 'meeting', 'lunch']
# Add to end
tasks.append('report')
print(tasks) # ['email', 'meeting', 'lunch', 'report']
# Add at specific position
tasks.insert(1, 'coffee')
print(tasks) # ['email', 'coffee', 'meeting', 'lunch', 'report']
# Remove specific item
tasks.remove('lunch')
print(tasks) # ['email', 'coffee', 'meeting', 'report']
# Remove last item
last = tasks.pop()
print(last) # 'report'
print(tasks) # ['email', 'coffee', 'meeting']