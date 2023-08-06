from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, extend_schema_view

from cryton_core.cryton_app import util, serializers, exceptions
from cryton_core.cryton_app.models import WorkerModel
from cryton_core.lib.util import exceptions as core_exceptions, creator
from cryton_core.lib.models.worker import Worker


@extend_schema_view(
    list=extend_schema(description="List Workers.", parameters=[serializers.ListSerializer]),
    retrieve=extend_schema(description="Get existing Worker."),
)
class WorkerViewSet(util.InstanceFullViewSet):
    """
    Worker ViewSet.
    """
    queryset = WorkerModel.objects.all()
    http_method_names = ["get", "post", "delete"]
    serializer_class = serializers.WorkerSerializer

    @extend_schema(
        description="Create new Worker.",
        request=serializers.WorkerCreateSerializer,
        responses={
            201: serializers.CreateDetailSerializer,
            400: serializers.DetailStringSerializer,
        }
    )
    def create(self, request: Request):
        try:
            params = {key: request.data.get(key, "") for key in ['name', 'description']}
            force = request.data.get("force", False)
            worker_obj_id = creator.create_worker(force=force, **params)
        except core_exceptions.WrongParameterError as ex:
            raise exceptions.ParseError(ex)

        msg = {'id': worker_obj_id, 'detail': 'Worker created.'}
        return Response(msg, status=status.HTTP_201_CREATED)

    @extend_schema(
        description="Check if Worker is responding.",
        request=None,
        responses={
            200: serializers.DetailStringSerializer,
        }
    )
    @action(methods=["post"], detail=True)
    def healthcheck(self, _, **kwargs):
        worker_id = kwargs.get('pk')
        try:
            worker_obj = Worker(worker_model_id=worker_id)
        except core_exceptions.WorkerObjectDoesNotExist:
            raise exceptions.NotFound()
        worker_obj.healthcheck()

        msg = {'detail': f"Worker with ID {worker_id} is {worker_obj.state}."}
        return Response(msg, status=status.HTTP_200_OK)

    @extend_schema(
        description="Delete Worker.",
        responses={
            204: serializers.DetailStringSerializer,
            404: serializers.DetailStringSerializer,
        }
    )
    def destroy(self, request: Request, *args, **kwargs):
        worker_id = kwargs.get('pk')
        try:
            Worker(worker_model_id=worker_id).delete()
        except core_exceptions.WorkerObjectDoesNotExist:
            raise exceptions.NotFound()

        return Response({'detail': 'Deleted.'}, status=status.HTTP_204_NO_CONTENT)
