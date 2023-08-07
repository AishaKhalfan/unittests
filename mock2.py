from unittest.mock import Mock

mock = Mock()
mock.side_effect = [3, 2, 1]
mock(), mock(), mock()

mock = Mock(return_value=3)
def side_effect(*args, **kwargs):
    return DEFAULT

mock.side_effect = side_effect
mock()
