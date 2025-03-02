def test_sum():
    assert sum(1, 1) == 2  # 1 + 1 = 2
    assert sum(-1, 1) == 0  # -1 + 1 = 0
    assert sum(-2, -3) == -5  # -2 + -3 = -5
    assert sum(0, 0) == 0  # 0 + 0 = 0
print(test_sum)