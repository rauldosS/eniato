from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.accounts.use_cases import DeleteAccountUseCase


class DeleteAccountView(APIView):
    permission_classes = ()
    authentication_classes = ()
    use_case = DeleteAccountUseCase()

    def post(self, request, account_id):
        self.use_case.execute(account_id)

        return Response(
            {'message': 'Delete Account successfully'},
            status=status.HTTP_200_OK
        )
