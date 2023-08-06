from os import getenv, environ
from sys import stdin
from urllib.parse import parse_qs
from json import loads
from typing import Dict, Callable, Any

from .types import QueryType, HeadersType


CONTENT_TYPE_PARSER_MAP: Dict[str, Callable[[str], Any]] = {
    'application/json': loads,
    'application/x-www-form-urlencoded': parse_qs,
    'multipart/form-data': parse_qs
}

def parse_query() -> QueryType:
    return parse_qs(getenv('QUERY_STRING'))


def parse_headers() -> HeadersType:
    def format_key(k: str):
        return '-'.join([p.capitalize() for p in k.split('_')][1:])

    return {
        'Content-Type': getenv('CONTENT_TYPE', ''),
        'Content-Length': getenv('CONTENT_LENGTH', ''),
        **{format_key(k): v for k, v in environ.items() if k.startswith('HTTP_')}
    }


def parse_body(headers: HeadersType) -> str:
    if not(length := int(headers.get('Content-Length') or 0)):
        return str()

    raw_data = stdin.read(length)

    if not (content_type := headers.get('Content-Type')):
        return raw_data

    if not (parser := CONTENT_TYPE_PARSER_MAP.get(content_type)):
        return raw_data
    
    return parser(raw_data)

    
    
