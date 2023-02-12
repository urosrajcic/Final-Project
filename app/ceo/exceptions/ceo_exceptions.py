class CEONotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CEOAlreadyExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
