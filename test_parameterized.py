from parameterized import parameterized, param

# A list of tuples
@parameterized([
    (2, 3, 5),
    (3, 5, 8),
])
def test_add(a, b, expected):
    assert_equal(a + b, expected)

# A list of params
@parameterized([
    param("10", 10),
    param("10", 16, base=16),
])
def test_int(str_val, expected, base=10):
    assert_equal(int(str_val, base=base), expected)

# An iterable of params
@parameterized(
    param.explicit(*json.loads(line))
    for line in open("testcases.jsons")
)
def test_from_json_file(...):
    ...

# A callable which returns a list of tuples
def load_test_cases():
    return [
        ("test1", ),
        ("test2", ),
    ]
@parameterized(load_test_cases)
def test_from_function(name):
    ...
