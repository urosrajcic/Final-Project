class ArtistNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ArtistAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
