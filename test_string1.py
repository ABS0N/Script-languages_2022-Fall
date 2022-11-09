from utils import donuts, both_ends, fix_start, mix_up

def test_donuts():
    assert donuts(4) == 'Fánkok száma: 4'
    assert donuts(9) == 'Fánkok száma: 9'
    assert donuts(10) == 'Fánkok száma: sok'
    assert donuts(99) == 'Fánkok száma: sok'

def test_both_ends():
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')