class InvalidInput(Exception):
    def __init__(self):
        self.message = ''

    def message(self):
        return self.message()

class IntInvalidInput(InvalidInput):
    def __init__(self):
        super(IntInvalidInput, self).__init__()
        self.message = 'Будь ласка, введіть ціле значення.'

class FloatInvalidInput(InvalidInput):
    def __init__(self):
        super(FloatInvalidInput, self).__init__()
        self.message = 'Будь ласка, введіть числове значення.'
