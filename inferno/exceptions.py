"""Contains inferno-specific exceptions."""


class InfernoException(BaseException):
    """Base inferno exception."""


class NotInitializedError(InfernoException):
    """Module is not initialized, please call the `.initialize`
    method or train the model by calling `.fit(...)`.

    """
