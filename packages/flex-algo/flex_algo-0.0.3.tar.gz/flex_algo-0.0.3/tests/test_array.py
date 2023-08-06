from flex_algo import array


def test_two_sum():
    """Test two sum"""
    expected = array.two_sum([2, 7, 11, 15], 9)
    actual = [0, 1]
    assert actual == expected, "two sum incorrectly"
