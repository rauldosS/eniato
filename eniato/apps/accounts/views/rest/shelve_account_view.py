from rest_framework.generics import GenericAPIView

from rest_framework.response import Response


class ShelveAccountView(GenericAPIView):
    use_case = ''
    serializer_class = ''

    def post(self, request, **kwargs):
        print('chegou')
        data = {'teste': 'ok'}
        return Response(data)
