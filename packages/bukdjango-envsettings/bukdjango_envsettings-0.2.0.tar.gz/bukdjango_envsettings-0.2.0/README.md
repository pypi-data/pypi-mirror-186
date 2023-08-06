# envsettings

Allows updating all django settings from `env` variables.

1. Usage:
    - in `myproject.settings`:
        ```python
        import os
        import sys
        
        from bukdjango_envsettings import update_from_env
        
        update_from_env(
            sys.modules[__name__],
            pre='DJANGO_',
            allowed=[
                'SECRET_KEY',
                'SITE_ID',
            ],
            extra_mapping={
                'EXTRA_KEY': str,
                'EXTRA_KEY2': str,
                'ENGINE_NAME': str,
            },
            extra_allowed=[
                'EXTRA_KEY',
                'ENGINE_NAME',
            ]
        )
        
        
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ENGINE_NAME,
            }
        }

       ```
    - all settings should be prefixed with `DJANGO_` by default, see 