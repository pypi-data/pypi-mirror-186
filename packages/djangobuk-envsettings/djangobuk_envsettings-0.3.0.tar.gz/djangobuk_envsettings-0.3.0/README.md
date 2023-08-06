# envsettings

* Update django settings from environment variables by updating `sys.modules`
* Mostly using `ast.literal_eval` to convert string to python object.
* Tested by converting all default django settings to string and back to python object and then running django command.

## todo
* simplify code
* verify settings after they are casted to python object

1. Usage:
    - in `myproject.settings`:
        ```python
        import os
        import sys
        import ast
        
        from djangobuk_envsettings import update_from_env
        
        update_from_env(
            sys.modules[__name__],
            # default prefix for all variables
            pre='DJANGO_',
            # settings that can be updated from env
            # by default all settings are allowed (this option overrides)
            allowed=[
                'SECRET_KEY',
                'SITE_ID',
            ],
            # optional
            # extra settings and their types (to be used with extra_allowed)
            extra_mapping={
                'DATABASE_PATH': ast.literal_eval,
            },
            # optional
            # extra settings that can be updated from env
            extra_allowed=[
                'DATABASE_PATH',
            ]
        )
        
        # nothing more required
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': DATABASE_PATH,
            }
        }

       ```
