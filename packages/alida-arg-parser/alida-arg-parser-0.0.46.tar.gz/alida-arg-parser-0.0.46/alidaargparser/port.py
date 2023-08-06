


class Port:
    def __init__(self, name=None, description=None, number=None, http_model=None):
        self.name = name
        self.description = description
        self.number = number
        self.http_model = http_model

    def __getattr__(self, attr):
        return self.__dict__

