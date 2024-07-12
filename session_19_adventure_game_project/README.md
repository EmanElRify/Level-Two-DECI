# Session 19: Adventure Game Project


### Randomness 
> Add randomness to the story events. For example, when the player go deep into the forest at first they find a strange creature.
 When they play again and go deep to the forest they find something else, maybe a wand stick
- add randomness using `random` module
- use `random.choice(items)` , where `items` is a list of possible events that could happen
For example:
```python
import random

# Example list
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Choose a random item from the list
random_item = random.choice(items)

print(f"The randomly selected item is: {random_item}")
```