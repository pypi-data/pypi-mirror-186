from typing import Optional, Any


def search_params(
    search: Optional[str] = None,
    query: str = None,
    page: Optional[Any] = None,
    ordering: Optional[str] = None,
):
    return {
        "search": search,
        "query": query,
        "page": page,
        "ordering": ordering,
    }


__all__ = ['search_params']
