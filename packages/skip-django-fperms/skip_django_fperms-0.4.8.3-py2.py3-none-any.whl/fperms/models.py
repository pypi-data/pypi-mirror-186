from fperms.base import BasePerm, Group  # noqa: F401
from fperms.managers import RelatedPermManager


class Perm(BasePerm):

    related_manager = RelatedPermManager()

    class Meta:
        base_manager_name = 'related_manager'
