"""Singleton metaclass."""


class SingletonMeta(type):
    """Metaclass for singleton objects."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Execute the metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]
