from django.urls import path

from .get_all_objectives_by_user_view import GetAllObjectivesByUserView
from .save_objective_view import SaveObjectiveView
# from .active_objective_view import ActivateObjectiveView
# from .deactivate_objective_view import DeactivateObjectiveView
# from .delete_objective_view import DeleteObjectiveView

urlpatterns = [
    path(
        'objetivos/usuario',
        GetAllObjectivesByUserView.as_view(),
        name='get_objective_list_by_user'
    ),
    path(
        'salvar',
        SaveObjectiveView.as_view(),
        name='save_objective'
    ),
    # path(
    #     'ativar/<int:objective_id>',
    #     ActivateObjectiveView.as_view(),
    #     name='activate_objective_view'
    # ),
    # path(
    #     'desativar/<int:objective_id>',
    #     DeactivateObjectiveView.as_view(),
    #     name='delete_objective_view'
    # ),
    # path(
    #     'apagar/<int:objective_id>',
    #     DeleteObjectiveView.as_view(),
    #     name='delete_objective_view'
    # )
]
