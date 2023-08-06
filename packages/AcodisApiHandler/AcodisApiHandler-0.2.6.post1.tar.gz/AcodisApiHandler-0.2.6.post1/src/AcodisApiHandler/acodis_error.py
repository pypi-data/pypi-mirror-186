class AcodisError(Exception):
    def __init__(self, message):
        """General class for Acodis-related errors"""
        super().__init__(message)


class AcodisApiError(AcodisError):
    def __init__(self, message):
        """Class for Acodis API-related errors"""
        super().__init__(message)


class AcodisAuthError(AcodisApiError):
    def __init__(self, message):
        """Class for Acodis API authentication errors"""
        super().__init__(message)

    def __str__(self):
        return f"API Authentication error: {self.message}"


class AcodisParsingError(AcodisError):
    def __init__(self, message):
        """Class for Acodis result parsing errors"""
        super().__init__(message)
