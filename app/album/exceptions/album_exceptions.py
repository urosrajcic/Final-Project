class AlbumNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class AlbumAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
