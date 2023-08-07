from unittest.mock import MagicMock

mock = MagicMock()
mock.__str__ = MagicMock(return_value='wheeeeee')
print(str(mock))
