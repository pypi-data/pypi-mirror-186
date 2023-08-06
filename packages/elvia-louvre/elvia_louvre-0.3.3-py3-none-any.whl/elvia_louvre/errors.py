
class LouvreException(Exception):
    """
    Base Louvre exception class.
    """    
    pass


class LouvreImageNotFound(LouvreException):
    pass


class LouvreKeyError(LouvreException):
    pass


class LouvreQueryError(LouvreException):
    pass


class LouvreValueError(LouvreException):
    pass


class LouvreVaultConnError(LouvreException):
    pass


class LouvreSecretError(LouvreException):
    pass


class LouvreInvalidImageVariant(LouvreException):
    pass
