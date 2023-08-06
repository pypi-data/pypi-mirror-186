#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'luigelo@ldvloper.com'

"""
    Modules
"""
import os
from functools import wraps
from inspect import iscoroutinefunction, getfile
from typing import Any, Callable, TypeVar, cast

"""
    Result4Utility Modules
"""
from result4utility.result import Result
from result4utility.result import ResultOperationType as resType


class Decorest:

    Fn = TypeVar('Fn', bound=Callable[..., Any])

    def __init__(self):
        pass

    def try_log(self, func: Fn):
        if iscoroutinefunction(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except Exception as exc:
                    return self.raise_exception(func, exc)
            return cast(self.Fn, wrapper)
        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    return self.raise_exception(func, exc)
            return wrapper

    def raise_exception(self, func, exc, result: Result = None) -> Result:
        if not result:
            result = Result()
        result.add_result(message=f'Error occurred in {func.__name__}: {str(exc)} in {get_filename(func)}',
                          result_type=resType.EXCEPTION)
        return result


def get_filename(func):
    if getfile(func):
        return os.path.split(getfile(func))[-1]
    return ''
