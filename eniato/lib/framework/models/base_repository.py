import abc


class BaseRepository(abc.ABC):
    model = None
    domain_object = None
    factory = None

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or self.model
        self.domain_object = domain_object or self.domain_object
        self.factory = factory or self.factory

        if self.model is None:
            raise ValueError(
                '{}.model must be set'.format(self.__class__.__name__)
            )

        if not (self.domain_object or self.factory):
            raise ValueError(
                'You must set either {class_name}.domain_object'
                ' or {class_name}.factory'.format(
                    class_name=self.__class__.__name__
                )
            )

    def get_all(self):
        qs = self._get_queryset()
        return self._build_domain(qs)

    def get_by_id(self, id=id, fail_silently=False):
        try:
            item = self._get_queryset().get(id=id)
        except self.model.DoesNotExist as exception:
            if fail_silently:
                return None
            raise exception

        if self.factory:
            return self.factory.create_from_model(item)

        return self.domain_object.create_from_model(item)

    def _build_domain(self, qs):
        if self.factory:
            for domain_object in self.factory.build_from_queryset(qs):
                yield domain_object

        if self.domain_object:
            for item in qs:
                yield self.domain_object.create_from_model(item)

    def _get_queryset(self):
        return self.model.stored.all()
