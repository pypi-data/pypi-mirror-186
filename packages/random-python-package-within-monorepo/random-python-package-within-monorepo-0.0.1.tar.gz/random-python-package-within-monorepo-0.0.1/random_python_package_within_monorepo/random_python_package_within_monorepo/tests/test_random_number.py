from python_package_1 import random_number

def test_random_number():
    assert random_number.RandomNumberGenerator().run() >= 0
