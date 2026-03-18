from my_funcs import odd_even, cal_mean, cal_max, cal_min


# TODO: 사용자 모듈 import
def test_odd_even():
    assert False is odd_even(5)
    assert True is odd_even(4)
    assert False is odd_even(7)
    assert True is odd_even(8)
    assert False is odd_even(3)


def test_cal_mean():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    c = [3, 4, 5, 6, 7]
    assert 3.0 == cal_mean(a)
    assert 4.0 == cal_mean(b)
    assert 5.0 == cal_mean(c)


def test_cal_max():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    c = [3, 4, 5, 6, 7]
    assert 5.0 == cal_max(a)
    assert 6.0 == cal_max(b)
    assert 7.0 == cal_max(c)


def test_cal_min():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    c = [3, 4, 5, 6, 7]
    assert 1.0 == cal_min(a)
    assert 2.0 == cal_min(b)
    assert 3.0 == cal_min(c)
