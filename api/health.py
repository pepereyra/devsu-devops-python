from django.db import connection
from django.http import JsonResponse


def liveness(request):
    return JsonResponse({"status": "alive"})


def readiness(request):
    try:
        connection.ensure_connection()

        existing_tables = connection.introspection.table_names()

        if "api_user" not in existing_tables:
            return JsonResponse(
                {"status": "not_ready", "error": "table 'api_user' not found"},
                status=503
            )

        return JsonResponse({"status": "ready"})

    except Exception as exc:
        return JsonResponse(
            {"status": "not_ready", "error": str(exc)},
            status=503
        )