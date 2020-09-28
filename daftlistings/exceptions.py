class DaftException(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Error: " + self.reason
