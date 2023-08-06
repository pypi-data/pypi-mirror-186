
import sys

class Field():

    def __init__(self, name = None, default = None):
        self.__name = name
        self.__default = default

    @property
    def default(self):
        return self.__default

    @property
    def name(self):
        return self.__name

    def to_python(self, value):
        return value

class ListField(Field):

    def __init__(self, subfield = Field(), name = None, default = None):
        #super(ListField, self).__init__(name = name)
        Field.__init__(self, name = name, default = default)
        self.__subfield = subfield

    def to_python(self, values):
        if values:
            return [self.__subfield.to_python(value) for value in values]
        return None

class BooleanField(Field):

    def to_python(self, value):
        if value:
            value = value.lower()
            #if not(value in ["0", "false"]): return True
            if value in ["1", "true"]: return True

        return False
            

class StringField(Field): pass

class LongField(Field):

    def to_python(self, value):
        if value:
            if sys.version_info.major > 2:
                return int(value)
            else:
                return long(value)
        return None

class IntField(Field):

    def to_python(self, value):
        if value:
            return int(value)
        return None

class FloatField(Field):

    def to_python(self, value):
        if value:
            return float(value)
        return None


FIELD_LIST = [Field, ListField, BooleanField, StringField, LongField, IntField, FloatField]
