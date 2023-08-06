#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'adions025@gmail.com'

from enum import Enum


class ResOperation(object):
    def __init__(self, message, res_type):
        self.__message = message
        self.__result_type = res_type

    @property
    def message(self):
        return self.__message

    @property
    def result_type(self):
        return self.__result_type


class ResOperationType(Enum):
    ERROR = 0
    INFO = 1
    WARNING = 2
    SUCCESS = 3
    EXCEPTION = 4
