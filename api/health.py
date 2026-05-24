from django.db import connection
from django.db.utils import OperationalError
from django.http import JsonResponse

from .models import User


def liveness(request):
    return JsonResponse({"status": "alive"})


def readiness(request):
    try:
        connection.ensure_connection()

        table_name = User._meta.db_table

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name=%s;",
                [table_name]
            )

            result = cursor.fetchone()

        if not result:
            raise OperationalError(
                f"table '{table_name}' not found"
            )

        return JsonResponse({"status": "ready"})

    except Exception as exc:
        return JsonResponse(
            {"status": "not_ready", "error": str(exc)},
            status=503
        )