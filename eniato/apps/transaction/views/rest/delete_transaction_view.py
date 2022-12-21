from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.transaction.repositories.transaction_repository import TransactionRepository


class DeleteTransactionView(APIView):
    permission_classes = ()
    authentication_classes = ()
    repository = TransactionRepository()

    def post(self, request, transaction_id):
        self.repository.delete_by_id(transaction_id)

        return Response(
            {'message': 'Delete Transaction successfully'},
            status=status.HTTP_200_OK
        )
