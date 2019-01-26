class FlaskUnsignWordlistException(Exception):
    """Base exception class"""


class NoSuchWordlist(FlaskUnsignWordlistException):
    """Raised when no such wordlist exists"""
