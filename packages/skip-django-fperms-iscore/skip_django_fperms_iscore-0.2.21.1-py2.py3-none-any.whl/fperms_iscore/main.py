from is_core.main import DjangoUiRestCore

from fperms_iscore.mixins import PermCoreMixin


class PermDjangoUiRestCore(PermCoreMixin, DjangoUiRestCore):

    abstract = True
