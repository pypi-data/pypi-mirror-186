#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'adions025@gmail.com'


class DictReader(object):

    def __init__(self, keys_dic=None, config_file=()):
        self.__config_file = config_file
        if keys_dic is None:
            self.__keys = ()
        else:
            self.__keys = keys_dic
        self.__result = None

    def __getattr__(self, attribute):
        try:
            result = DictReader(keys_dic=self.__keys + (attribute,), config_file=self.__config_file)
        except Exception as ex:
            raise ValueError(str(ex))
        return result

    def get(self, value_dict=None):
        try:
            if value_dict is None:
                dictionary_search = self.__config_file
            else:
                dictionary_search = value_dict
            for k in self.__keys:
                value = dictionary_search.get(k)
                if value is not None:
                    if isinstance(value, dict):
                        self.get(value_dict=value)
                    else:
                        if self.__result is None:
                            self.__result = value
        except Exception as ex:
            raise ValueError(str(ex))
        return self.__result
