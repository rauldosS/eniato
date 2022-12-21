from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.accounts.repositories import AccountRepository


class DeactivateAccountView(APIView):
    permission_classes = ()
    authentication_classes = ()
    repository = AccountRepository()

    def post(self, request, account_id):
        self.repository.update_account_activation(account_id, False)

        return Response(
            {'message': 'Deactivate Account successfully'},
            status=status.HTTP_200_OK
        )
