from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transaction.use_cases import CreateTransactionUseCase
from apps.transaction.serializers import TransactionSerializer


class CreateTransactionView(APIView):
    permission_classes = ()
    authentication_classes = ()
    use_case = CreateTransactionUseCase()
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        print('data', request.data)

        response = self.use_case.execute(request.data)

        serializer = self.serializer_class(response)
        return Response(serializer.data)
