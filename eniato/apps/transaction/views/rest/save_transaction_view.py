from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transaction.use_cases import SaveTransactionUseCase
from apps.transaction.serializers import TransactionSerializer


class SaveTransactionView(APIView):
    permission_classes = ()
    authentication_classes = ()
    use_case = SaveTransactionUseCase()
    serializer_class = TransactionSerializer

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(SaveTransactionView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.use_case.execute(self.user, request.data)

        serializer = self.serializer_class(response)
        return Response(serializer.data)
