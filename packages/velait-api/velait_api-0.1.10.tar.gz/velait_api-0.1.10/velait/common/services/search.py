import json
from enum import Enum
from abc import abstractmethod, ABC
from typing import Optional, Any

from velait.common.services.exceptions import SearchError


class SearchOperator(Enum):
    LESS = "less"
    EQUAL = "equal"
    GREATER = "greater"
    CONTAINS = "contains"
    LESS_OR_EQUAL = "lessOrEqual"
    GREATER_OR_EQUAL = "greaterOrEqual"


class Search(ABC):
    DEFAULT_PAGE_SIZE: int = None

    def _parse_json(self, data, key_name: str):
        try:
            return json.loads(data)
        except (json.JSONDecodeError, TypeError, ValueError):
            if data is not None:
                raise SearchError(
                    name=key_name,
                    description=f"'{key_name}' cannot be parsed as JSON",
                )

    def __init__(self, search: Optional[str], query: str, page: Optional[Any], ordering: Optional[str], model):
        self.model = model
        self._search = search
        self._query = self._parse_json(data=query, key_name='query') or []

        parsed_page = self._parse_json(data=page, key_name='page') or {}
        self._page = {
            'offset': parsed_page.get('offset', 0) if page else 0,
            'size': parsed_page.get('size', self.DEFAULT_PAGE_SIZE) if page else self.DEFAULT_PAGE_SIZE,
        }

        self._ordering = tuple(map(str.strip, ordering.split(","))) if ordering else ()
        self.validate()

    def _validate_query_part(self, query_part: dict):
        name = query_part.get('fn')
        operation = query_part.get('op')

        if (name is None) or (operation is None):
            raise SearchError(
                name='query',
                description="All items in 'query' must have 'fn', 'op', 'fv' keys",
            )
        elif name not in self.model.queryable_fields:
            raise SearchError(
                name="query",
                description=f"{name} was not found as a value",
            )

    def validate(self):
        if isinstance(self._query, list):
            for query_part in self._query:
                self._validate_query_part(query_part)

        if not isinstance(self._page.get('offset'), int):
            raise SearchError(
                name='page',
                description="'offset' key must be a number in 'page' parameter",
            )

        ordering = []

        for field in self._ordering:
            if field.startswith('-'):
                ordering.append(field[1:])
            else:
                ordering.append(field)

        not_orderable_fields = set(ordering) - set(self.model.orderable_fields)

        if self._ordering and not_orderable_fields:
            parsed_fields = ' ,'.join(f"'{field}'" for field in not_orderable_fields)
            raise SearchError(
                name="ordering",
                description=f"Fields {parsed_fields} cannot be used in 'ordering'",
            )

    @abstractmethod
    def _parse_operator(self, field_name: str, operator: str, field_value: str):
        raise NotImplementedError("_parse_operator() is not implemented")

    def _parse_ordering(self):
        return self._ordering

    @abstractmethod
    def search(self):
        raise NotImplementedError("search() is not implemented")

    def parse_query_filters(self):
        if not isinstance(self._query, dict):
            return []

        return [self._parse_operator(
            field_name=query_part.get('fn'),
            operator=query_part.get('op'),
            field_value=query_part.get('fv'),
        ) for query_part in self._query]


__all__ = [
    'Search',
    'SearchError',
    'SearchOperator'
]
