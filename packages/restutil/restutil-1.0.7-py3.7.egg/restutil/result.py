#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'adions025@gmail.com'

from typing import List, Any
from restutil.operations import ResOperation

from restutil.operations import ResOperationType


class ResData(object):

    def __init__(self):
        self.__content: Any = None
        self.__has_errors: bool = False
        self.__result_operations: List = []

    @property
    def result_operations(self) -> List:
        return self.__result_operations

    def add_result(self, message: str, res_type: ResOperationType) -> None:
        try:
            self.__result_operations.append(ResOperation(message, res_type))
            if res_type == ResOperationType.ERROR or res_type == ResOperationType.EXCEPTION:
                self.__has_errors = True
        except Exception as ex:
            raise ValueError(str(ex))

    def add_result_range(self, result_range: list) -> None:
        for res in result_range:
            self.add_result(res.message, res.result_type)

    def format_result_operations(self):
        message = ""
        for x in self.__result_operations:
            message = '%s %s - %s,' % (message, x.result_type.name, x.message)
        return message

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def has_errors(self):
        return self.__has_errors
