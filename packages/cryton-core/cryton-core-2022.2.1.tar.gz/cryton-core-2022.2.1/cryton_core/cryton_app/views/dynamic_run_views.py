# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action
#
# from drf_spectacular.utils import extend_schema
#
# from cryton_core.cryton_app import util, serializers, exceptions
# from cryton_core.cryton_app.views import run_views
# from cryton_core.lib.util import exceptions as core_exceptions
# from cryton_core.lib.models.run import Run
#
# TODO: do not inherit from run views since only some methods are needed, pause/resume are unnecessary for example
# class DynamicRunViewSet(run_views.RunViewSet):
#     """
#     Dynamic Run ViewSet.
#     """
#
#     @action(methods=["post"], detail=True)
#     def finish(self, _, **kwargs):
#         run_id = kwargs.get("pk")
#         try:
#             run_obj = Run(run_model_id=run_id)
#         except core_exceptions.RunObjectDoesNotExist:
#             raise exceptions.NotFound()
#
#         # TODO: create method `mark_as_finished` that will set state and time, and also check is stages/steps have
#         #  finished; maybe even create such a method for StageEx
#         # run_obj.state = states.FINISHED
#         return Response({"detail": 'Marked Run as Finished'}, status=status.HTTP_200_OK)
