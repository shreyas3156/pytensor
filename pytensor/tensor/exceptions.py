class ShapeError(Exception):
    """Raised when the shape cannot be computed."""


class NotScalarConstantError(Exception):
    """
    Raised by get_underlying_scalar_constant if called on something that is
    not a scalar constant.
    """


class AdvancedIndexingError(TypeError):
    """
    Raised when Subtensor is asked to perform advanced indexing.

    """
