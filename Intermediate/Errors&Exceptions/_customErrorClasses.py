# MAKING Custom ERROR Classes

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 1000:
       raise ValueTooHighError('TOO HIGH! X greater than 1000')
    if x < 0:
        raise  ValueTooSmallError('TOO SMALL! X less than 0', x)

try:
    # test_value(1010)
    test_value(-10)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
else:
    print('Everything went fine!')
finally:
    print('Cleaning up....')