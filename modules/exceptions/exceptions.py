class InvalidInput(Exception):
    def __init__(self):
        self.message_text = ''

    def message(self):
        return self.message_text

class IntInvalidInput(InvalidInput):
    def __init__(self):
        super(IntInvalidInput, self).__init__()
        self.message_text = 'Будь ласка, введіть ціле значення.'

class FloatInvalidInput(InvalidInput):
    def __init__(self):
        super(FloatInvalidInput, self).__init__()
        self.message_text = 'Будь ласка, введіть числове значення.'

if __name__ == '__main__':
    try:
        a = int('d')
    except ValueError:
        print(IntInvalidInput().message())