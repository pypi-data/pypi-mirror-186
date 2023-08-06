#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luigelo@ldvloper'

"""
    Modules
"""
from copy import deepcopy


class Tools(object):
    """
        Tool Class - For common functionalities
    """

    def __init__(self):
        """
            Basic constructor
        """
        self.__dictionary: dict = dict()
        pass

    def remove_property(self, target: dict, props: []) -> dict:
        """
            Method used for remove properties from a dictionary
            :rtype: object
            :param target: dict. Dictionary to apply changes
            :param props: []. Properties of dictionary that we will remove inside.
        """
        try:
            for p in props:
                del target[p]
                self.__dictionary = target
        except Exception:
            pass
        return self.__dictionary

    def dictionary_from_object(self, model: object) -> dict:
        """
            Method used for convert model into dictionary
            :rtype: dict
            :param model: object. Object over that we can do conversion to dictionary. Previously we do an copy and convert this copy.
        """
        try:
            bck_model = deepcopy(model)
            self.__dictionary = bck_model.__dict__
        except Exception:
            pass
        return self.__dictionary
