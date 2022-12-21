from rest_framework.generics import ListAPIView

from apps.objective.repositories import ObjectiveRepository
from apps.objective.serializers import ObjectiveSerializer


class GetAllObjectivesByUserView(ListAPIView):
    repository = ObjectiveRepository()
    serializer_class = ObjectiveSerializer

    def get_queryset(self):
        return self.repository.get_all_by_user(self.request.user)
