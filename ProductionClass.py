from unittest.mock import MagicMock

# Assuming ProductionClass is a real class you have defined in your code
class ProductionClass:
    def method(self, *args, **kwargs):
        # Some implementation here (not shown in the snippet)
        total_sum = sum(args)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        return total_sum

thing = ProductionClass()

# Mocking the method of the ProductionClass instance
thing.method = MagicMock(return_value=3)

# Calling the mocked method with specific arguments
result = thing.method(3, 4, 5, key='value')

# Assertion to check if the method was called with the specified arguments
thing.method.assert_called_with(3, 4, 5, key='value')

print(result)  # Output: 3

