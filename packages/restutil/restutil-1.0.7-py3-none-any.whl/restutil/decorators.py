#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'adions025@gmail.com'

import os
from functools import wraps
from inspect import iscoroutinefunction, getfile
from typing import Any, Callable, TypeVar, cast

from restutil.result import ResData
from restutil.result import ResOperationType as resType


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

    def raise_exception(self, func, exc, result: ResData = None) -> ResData:
        if not result:
            result = ResData()
        result.add_result(message=f'Error occurred in {func.__name__}: {str(exc)} in {get_filename(func)}',
                          res_type=resType.EXCEPTION)
        return result


def get_filename(func):
    if getfile(func):
        return os.path.split(getfile(func))[-1]
    return ''
