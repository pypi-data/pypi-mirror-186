from djangobuk_envsettings.conversion import MAPPING


def get_mapping(extra_map: dict = None) -> dict:
    mapping = MAPPING.copy()
    if extra_map:
        mapping.update(extra_map)
    return mapping


def settings_to_dict(settings_module=None) -> dict:
    """
    Convert Django settings module into dict.
    """
    return {
        k: type(getattr(settings_module, k)) for k in dir(settings_module) if
        not k.startswith('_') and
        k.upper() == k
    }


def eval_settings(settings: dict, mapping=None) -> dict:
    """
    Given settings map ex. {SECRET_KEY: "asdasd"}
    evaulate values into coresponding Python types.
    """
    if not mapping:
        return {}
    # for opt, value in settings.items():
    #     print(opt, value)
    #     print(type(mapping[opt](value)))
    return {
        opt: mapping[opt](value) for (opt, value) in settings.items()
    }


def gather_settings(pre='DJANGO_') -> dict:
    """
    Collect dict of settings from env variables.
    """
    import os
    if pre:
        return {
            k[len(pre):]: v for (k, v) in os.environ.items() if
            k.startswith(pre)
        }
    return {
        k: v for (k, v) in os.environ.items()
    }
