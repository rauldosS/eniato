from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.use_cases import SaveAccountUseCase
from apps.accounts.serializers import AccountSerializer


class SaveAccountView(APIView):
    permission_classes = ()
    authentication_classes = ()
    use_case = SaveAccountUseCase()
    serializer_class = AccountSerializer

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(SaveAccountView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.use_case.execute(self.user, request.data)

        serializer = self.serializer_class(response)
        return Response(serializer.data)
