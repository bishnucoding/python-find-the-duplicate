from find_first import FindDuplicate

def test_small():
    dup_finder = FindDuplicate()
    actual_result = dup_finder.find_duplicate([4, 2, 1, 3, 1])

    assert actual_result == 1