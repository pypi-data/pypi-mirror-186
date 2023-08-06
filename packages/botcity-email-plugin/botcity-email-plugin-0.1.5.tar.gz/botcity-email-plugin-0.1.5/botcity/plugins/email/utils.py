from functools import wraps


def if_imap_configured(func):
    """
    Decorator which raises if imap_mail is None

    Args:
        func (callable): The function to be wrapped

    Returns:
        wrapper (callable): The decorated function
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._imap_mail is None:
            raise RuntimeError(f"An IMAP server must be configured. Cannot invoke {func.__name__}.")
        return func(self, *args, **kwargs)
    return wrapper


def if_smtp_configured(func):
    """
    Decorator which raises if smtp_mail is None

    Args:
        func (callable): The function to be wrapped

    Returns:
        wrapper (callable): The decorated function
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._smtp_mail is None:
            raise RuntimeError(f"An SMTP server must be configured. Cannot invoke {func.__name__}.")
        return func(self, *args, **kwargs)
    return wrapper
