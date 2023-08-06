from django.core.cache import caches
from django.core.exceptions import ImproperlyConfigured

from fperms import get_perm_model

from fperms_iscore import enums
from fperms_iscore.conf import settings

from is_core.auth.permissions import IsAuthenticated


Perm = get_perm_model()


permissions = {}


GENERAL_CACHE_NAME = '__all__'


def _get_perm_slug_from_data(perm_type, perm_codename, object_ct_id=None, object_id=None):
    slug = '{}|{}'.format(perm_type, perm_codename)
    if object_ct_id and object_id:
        return '{}|{}|{}'.format(slug, object_ct_id, object_id)
    return slug


def _get_perm_slug_from_obj(perm_type, perm_codename, obj=None):
    from django.contrib.contenttypes.models import ContentType

    object_ct_id = object_id = None
    if obj is not None:
        object_ct_id = ContentType.objects.get_for_model(obj).pk
        object_id = obj.pk
    return _get_perm_slug_from_data(perm_type, perm_codename, object_ct_id, object_id)


def _get_perm_slug(perm):
    return _get_perm_slug_from_data(perm.type, perm.codename, perm.content_type_id, perm.object_id)


def get_cache(request):
    if not hasattr(request, 'session') or not settings.IS_CORE_PERM_USE_CACHE:
        return None
    return caches[settings.IS_CORE_PERM_CACHE_NAME]


def get_all_user_perm_slugs(request):
    if hasattr(request.user, '_fperms_is_core_user_perm_slugs'):
        return request.user._fperms_is_core_user_perm_slugs

    cache_key = None
    perm_slugs = None
    cache = get_cache(request)

    if cache:
        cache_key = f'fperms_is_core-{request.user.pk}-{request.session.session_key}'
        perm_slugs = cache.get(cache_key)

    if perm_slugs is None:
        perm_slugs = set(_get_perm_slug(p) for p in request.user.fperms.all_perms())
        if cache:
            cache.set(cache_key, perm_slugs, settings.IS_CORE_PERM_CACHE_TIMEOUT)

    request.user._fperms_is_core_user_perm_slugs = perm_slugs
    return perm_slugs


class BaseFPermPermission(IsAuthenticated):

    def __init__(self, check_object_permission=False):
        self._check_object_permission = check_object_permission

    def _get_name(self, name, request, view, obj=None):
        raise NotImplementedError

    def has_permission(self, name, request, view, obj=None):
        """
        Return `True` if user has set permission of is superuser
        """
        if not super().has_permission(name, request, view, obj):
            return False

        user = request.user
        if user.is_superuser:
            return True

        permission_name = self._get_name(name, request, view, obj)

        user_perm_slugs = get_all_user_perm_slugs(request)
        return (
            _get_perm_slug_from_obj(enums.PERM_TYPE_CORE, permission_name) in user_perm_slugs
            or (
                self._check_object_permission
                and obj is not None
                and _get_perm_slug_from_obj(enums.PERM_TYPE_CORE, permission_name, obj=obj) in user_perm_slugs
            )
        )


class FPermPermission(BaseFPermPermission):

    def __init__(self, name, verbose_name=None, register=True, check_object_permission=False):
        """
        :param name: name of the permission stored as codename in `Perm` model
        :param verbose_name: verbose name of the permission
        """
        super().__init__(check_object_permission=check_object_permission)
        self.name = name
        self.verbose_name = verbose_name
        if register:
            self._register()

    def _register(self):
        if self.name in permissions:
            raise ImproperlyConfigured('Duplicite permission with name {}'.format(self.name))
        permissions[self.name] = self

    def _get_name(self, name, request, view, obj=None):
        return self.name
