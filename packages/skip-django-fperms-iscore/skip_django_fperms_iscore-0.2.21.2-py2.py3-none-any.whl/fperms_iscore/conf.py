from django.conf import settings as django_settings


DEFAULTS = {
    'IS_CORE_PERM_USE_CACHE': False,
    'IS_CORE_PERM_CACHE_NAME': 'default',
    'IS_CORE_PERM_CACHE_TIMEOUT': 60 * 10,  # 10 min
}


class Settings:

    def __getattr__(self, attr):
        if attr not in DEFAULTS:
            raise AttributeError('Invalid fperms_iscore setting: "{}"'.format(attr))

        default = DEFAULTS[attr]
        return getattr(django_settings, attr, default(self) if callable(default) else default)


settings = Settings()
