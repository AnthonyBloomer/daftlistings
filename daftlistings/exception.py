class DaftException(Exception):
    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.text = reason

    def __str__(self):
        return "Error: Status code: %s Message: %s" % (self.status_code, self.text)
