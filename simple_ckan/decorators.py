from functools import wraps


def call_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        payload = func(*args, **kwargs)
        api_func = func.__name__
        caller = payload.pop("self")
        return caller.action.ckan.call_action(api_func, data=payload)

    return wrapper
