from assimilator.alchemy.database import AlchemyRepository as BaseAlchemyRepository
from velait.common.exceptions import AlreadyDeletedError


class VelaitRepository(BaseAlchemyRepository):
    def delete(self, obj):
        if obj.is_removed:
            raise AlreadyDeletedError()

        obj.is_removed = True


__all__ = [
    'VelaitRepository',
]
