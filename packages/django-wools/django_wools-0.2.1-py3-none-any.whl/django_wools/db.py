from functools import wraps
from typing import Text, Union

from django.apps import apps
from django.db.models import Model

LOCK_MODES = (
    "ACCESS SHARE",
    "ROW SHARE",
    "ROW EXCLUSIVE",
    "SHARE UPDATE EXCLUSIVE",
    "SHARE",
    "SHARE ROW EXCLUSIVE",
    "EXCLUSIVE",
    "ACCESS EXCLUSIVE",
)


def require_lock(model: Union[Text, Model], lock: Text):
    """
    Decorator for PostgreSQL's table-level lock functionality

    Example:
        @atomic
        @require_lock(MyModel, 'ACCESS EXCLUSIVE')
        def myview(request)
            ...

    PostgreSQL's LOCK Documentation:
    http://www.postgresql.org/docs/8.3/interactive/sql-lock.html
    """

    def require_lock_decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if lock not in LOCK_MODES:
                raise ValueError("%s is not a PostgreSQL supported lock mode.")
            from django.db import connection

            if not isinstance(model, Model):
                true_model = apps.get_model(model)
            else:
                true_model = model

            cursor = connection.cursor()
            # noinspection PyProtectedMember
            cursor.execute(
                "LOCK TABLE %s IN %s MODE" % (true_model._meta.db_table, lock)
            )
            return view_func(*args, **kwargs)

        return wrapper

    return require_lock_decorator
