class Field: pass

class IntField(Field):
    def __init__(self, column, min_value=None, max_value=None):
        self.column    = column
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        val = int(value)

        if self.min_value is not None:
            if val < self.min_value:
                raise ValueError('value must be between min_value and max_value')
        if self.max_value is not None:
            if val > self.max_value:
                raise ValueError('value must be between min_value and max_value')

        self.value = value


class CharField(Field):
    def __init__(self, column, max_length=None):
        self.column     = column
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if len(value) > self.max_length:
            raise ValueError('value length exceeds max_length')

        self.value = value
