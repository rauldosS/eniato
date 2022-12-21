from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.accounts.repositories import AccountRepository


class DeleteAccountView(APIView):
    permission_classes = ()
    authentication_classes = ()
    repository = AccountRepository()

    def post(self, request, account_id):
        self.repository.delete_by_id(account_id)

        return Response(
            {'message': 'Delete Account successfully'},
            status=status.HTTP_200_OK
        )
