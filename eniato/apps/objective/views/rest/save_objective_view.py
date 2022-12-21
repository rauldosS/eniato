from rest_framework.response import Response
from rest_framework.views import APIView

from apps.objective.use_cases import SaveObjectiveUseCase
from apps.objective.serializers import ObjectiveSerializer


class SaveObjectiveView(APIView):
    permission_classes = ()
    authentication_classes = ()
    use_case = SaveObjectiveUseCase()
    serializer_class = ObjectiveSerializer

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(SaveObjectiveView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.use_case.execute(self.user, request.data)

        serializer = self.serializer_class(response)
        return Response(serializer.data)
