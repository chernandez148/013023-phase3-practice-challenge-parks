class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and (0 < len(name) < 15):
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        name