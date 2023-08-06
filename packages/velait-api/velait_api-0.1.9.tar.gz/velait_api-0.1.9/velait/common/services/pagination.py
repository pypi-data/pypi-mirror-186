from velait.common.services.exceptions import PaginationLimitsError


def get_page_limits(page: int, page_size: int):
    if page_size <= 0 or page < 0:
        raise PaginationLimitsError()

    offset = page * page_size
    return offset, offset + page_size


def get_offset_limits(offset: int, page_size: int):
    if page_size <= 0 or offset < 0:
        raise PaginationLimitsError()

    return offset, page_size


__all__ = ['get_page_limits', 'get_offset_limits']
