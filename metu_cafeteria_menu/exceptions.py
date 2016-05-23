class RequestException(Exception):
    def __init__(self, parent_exception, message):
        self.parent_exception = parent_exception
        self.message = message

    def __str__(self):
        return self.message


class DateException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message