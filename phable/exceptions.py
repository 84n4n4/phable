from dataclasses import dataclass


@dataclass
class UnknownRecError(Exception):
    help_msg: str


@dataclass
class NotFoundError(Exception):
    help_msg: str


@dataclass
class IncorrectHttpStatus(Exception):
    help_msg: str


@dataclass
class InvalidCloseError(Exception):
    help_msg: str


@dataclass
class ServerSignatureNotEqualError(Exception):
    """Raised when the ServerSignature value sent by the server does not equal the
    ServerSignature computed by the client."""

    pass
