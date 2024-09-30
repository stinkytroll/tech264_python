# Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset(["hello", "world"])

# Try to add "!" to frozen_set. What happens?
# frozen_set.add("!")  # Raises attribute error.
print(frozen_set)

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)

# Print normal_set.
print(normal_set)

# Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set?
# The order changes because they are unordered collections.


# What makes a frozen set different to a normal set? Explain.
# Frozen sets freeze a list and make it unchangeable, meaning they are immutable - unlike regular sets, which
# are mutable.

