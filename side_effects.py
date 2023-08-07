from unittest.mock import MagicMock

# Create an instance of MagicMock
mock = MagicMock()

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

# Assign the side_effect function to the mock object
mock.side_effect = side_effect
# Call the mock object with arguments 'a', 'b', and 'c'
print(mock('a'), mock('b'), mock('c'))

# Now, we change the side_effect to a list of return values
mock.side_effect = [5, 4, 3, 2, 1]

# Call the mock object without any arguments
print(mock(), mock(), mock(), mock(), mock())

