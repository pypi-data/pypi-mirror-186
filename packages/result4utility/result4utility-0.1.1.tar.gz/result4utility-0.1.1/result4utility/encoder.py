#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luigelo@ldvloper.com'

"""
    Modules
"""
from inspect import getmembers
from json import JSONEncoder, loads, dumps
from multiprocessing import Pool, cpu_count


class Encoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        if hasattr(obj, '__dict__'):
            return {key: val for key, val in getmembers(obj)
                    if not any((key.startswith('_'), callable(val), key == 'metadata'))}
        if hasattr(obj, 'isoformat'):
            return f"{obj.isoformat(timespec='milliseconds')}Z"
        return super(Encoder, self).default(obj)


def jsonize(data, rel=False):
    result = []
    data = tuple(data) if isinstance(data, list) else (data,)
    for entity in data:
        if hasattr(entity, '__table__'):
            columns = [x.name for x in entity.__table__.columns]
            relations = [x.key for x in entity.__mapper__.relationships]
            obj = {}
            for col in columns:
                attr = getattr(entity, col)
                obj[col] = (f"{attr.isoformat(timespec='milliseconds')}Z" if hasattr(attr, 'isoformat') else attr)
            for relation in relations:
                obj[relation] = jsonize(getattr(entity, relation), True)
            result.append(obj)
        elif not rel:
            result.append(loads(dumps(entity, cls=Encoder)))
    return result


def get_response(result):
    limit = 24_000_000
    content, result.content = result.content, None
    response = loads(dumps(result, cls=Encoder))
    if isinstance(content, list):
        if len(str(content)) > limit:
            with Pool(cpu_count()) as pool:
                response['content'] = pool.map(jsonize, content)
            pool.join()
        else:
            response['content'] = jsonize(content)
    else:
        response['content'] = jsonize(content)[0]
    return response
