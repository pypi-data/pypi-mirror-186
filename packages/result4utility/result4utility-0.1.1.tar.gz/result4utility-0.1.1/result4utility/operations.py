#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luigelo@ldvloper.com'

"""
    Modules
"""
from enum import Enum


class ResultOperation(object):
    def __init__(self, message, result_type):
        self.__message = message
        self.__result_type = result_type

    @property
    def message(self):
        return self.__message

    @property
    def result_type(self):
        return self.__result_type


class ResultOperationType(Enum):
    ERROR = 0
    INFO = 1
    WARNING = 2
    SUCCESS = 3
    EXCEPTION = 4
