class ErrorDecodingPDFLabel(Exception):
    pass


class MissingData(Exception):
    """Have a field with the name of the missing field."""

    def __init__(self, field):
        super(MissingData, self).__init__(field)
        self.field = field


class UndefinedCredentials(Exception):
    pass


class UnknownApiResponse(Exception):
    """The response is not ok or status code different of 200."""

    def __init__(self, field):
        super(UnknownApiResponse, self).__init__(field)
        self.message = field


class InvalidApiResponse(Exception):
    """Can't extract required information from the response."""

    def __init__(self, field):
        super(InvalidApiResponse, self).__init__(field)
        self.message = field
