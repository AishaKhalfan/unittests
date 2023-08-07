from unittest.mock import patch
from side_effects import side_effect

@patch('side_effects.side_effect')
# @patch('side_effects.ClassName1')
def test(MockClass1):
    side_effect("a")
    # module.ClassName2()
    assert MockClass1 is side_effect
    # assert MockClass2 is module.ClassName2
    assert MockClass1.called
    # assert MockClass2.called
    MockClass1.assert_called_once()

test()
