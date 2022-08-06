from jasperlxjproject.lib import try_me

def test_try_me_length():
    assert len(try_me("Jasper")) != 0

def test_try_me_type():
    assert type(try_me("Mario")) == str
