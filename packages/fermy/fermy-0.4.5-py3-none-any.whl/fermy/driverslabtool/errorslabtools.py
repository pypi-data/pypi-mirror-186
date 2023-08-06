class CommunicationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MTPError(Exception):
    def __init__(self, message):
        super().__init__(message)
