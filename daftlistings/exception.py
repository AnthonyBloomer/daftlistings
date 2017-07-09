class DaftRequestException(Exception):
    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def __str__(self):
        return "Error: Status code: %s Reason: %s" % (self.status_code, self.reason)


class DaftInputException(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Error: " + self.reason
