from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from cryton_core.cryton_app import util, exceptions, serializers
from cryton_core.lib.util import util as core_util


class LogViewSet(util.BaseViewSet):
    """
    Log ViewSet.
    """
    http_method_names = ["get"]
    serializer_class = serializers.LogSerializer

    @extend_schema(
        description="Get Cryton Core app logs.",
        parameters=[
            OpenApiParameter("offset", OpenApiTypes.NUMBER, OpenApiParameter.QUERY),
            OpenApiParameter("limit", OpenApiTypes.NUMBER, OpenApiParameter.QUERY),
            OpenApiParameter("filter", OpenApiTypes.STR, OpenApiParameter.QUERY),
            OpenApiParameter("page", exclude=True)
        ],
        responses={
            200: serializers.LogSerializer,  # 'next'/'previous' parameters are inherited by default
            500: serializers.DetailStringSerializer,
        }
    )
    def list(self, request: Request):
        filter_param = request.query_params.get("filter")
        try:
            offset = int(request.query_params.get("offset", 0))
            limit = int(request.query_params.get("limit", 0))
        except ValueError as ex:
            raise exceptions.ValidationError(ex)

        all_logs = core_util.get_logs()

        if filter_param is not None:
            filtered_logs = []
            for log in all_logs:
                if filter_param in log:
                    filtered_logs.append(log)
        else:
            filtered_logs = all_logs

        filtered_logs_count = len(filtered_logs)
        if limit > 0 or offset > 0:
            logs_to_show = filtered_logs[offset:offset + limit if limit > 0 else filtered_logs_count]
        else:
            logs_to_show = filtered_logs

        msg = {"count": filtered_logs_count, "results": logs_to_show, "next": "", "previous": ""}
        return Response(msg, status=status.HTTP_200_OK)
