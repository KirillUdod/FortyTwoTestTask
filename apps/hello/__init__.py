try:
    import signals
    __all__ = ['signals']
except:
    from .signals import *
