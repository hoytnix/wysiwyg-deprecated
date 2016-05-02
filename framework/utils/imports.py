"""Because writing imports is redundant."""

import importlib
import inspect


def all_models():
    """A list of model-class objects."""

    namespace = __import__('framework').models

    modules = []
    for name, obj in inspect.getmembers(namespace):
        if inspect.ismodule(obj):
            modules.append(obj)

    classes = []
    for module in modules:
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                classes.append(obj)

    models = []
    for _class in classes:
        try:
            if _class.__tablename__:
                if _class not in models:  # IDK why there are duplicates.
                    models.append(_class)
        except:
            pass

    return models
