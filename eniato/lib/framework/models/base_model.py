from .mixins.softdelete_model import SoftDeleteMixin
from .mixins.timestamped_model import TimeStampedModel
from django.forms.models import model_to_dict


class BaseModel(SoftDeleteMixin, TimeStampedModel):

    class Meta:
        abstract = True

    def to_dict(self):
        exclude = 'deleted', 'deleted_by'
        return model_to_dict(self, exclude=exclude)
