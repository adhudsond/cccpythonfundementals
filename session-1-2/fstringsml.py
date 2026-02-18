# Simulating ML training progress
epoch = 1 # Current full pass through dataset
total_epochs = 100
loss = 0.456 # Average prediction error
accuracy = 0.892 # 89.2% of correct predictions
# Professional logging (this is what real ML code looks like!)
print(f'Epoch {epoch}/{total_epochs}:')
print(f' Loss: {loss:.3f}')
print(f' Accuracy: {accuracy:.1%}')
# Output:
# Epoch 1/100:
# Loss: 0.456
# Accuracy: 89.2%
# This is professional ML output!