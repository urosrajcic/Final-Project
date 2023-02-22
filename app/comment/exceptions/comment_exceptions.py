class CommentNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CommentAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
