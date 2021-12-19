"""
Global constant to add method to every Constant that inherits it
"""
class GlobalConstant(object):

    class Meta:
        abstract = True

    FieldStr = {}
    @classmethod
    def get_choices(cls):
        return cls.FieldStr.items()
