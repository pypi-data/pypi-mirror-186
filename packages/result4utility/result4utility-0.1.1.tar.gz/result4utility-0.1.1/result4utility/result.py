#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luigelo@ldvloper.com'

"""
    Modules
"""
from typing import List, Any

"""
    Result4Utility Modules
"""
from result4utility.operations import ResultOperation
from result4utility.operations import ResultOperationType


class Result(object):

    def __init__(self):
        self.__content: Any = None
        self.__has_errors: bool = False
        self.__result_operations: List = []

    @property
    def result_operations(self) -> List:
        return self.__result_operations

    def add_result(self, message: str, result_type: ResultOperationType) -> None:
        try:
            self.__result_operations.append(ResultOperation(message, result_type))
            if result_type == ResultOperationType.ERROR or result_type == ResultOperationType.EXCEPTION:
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
