def get_model_name(serializer_class):
    return serializer_class.Meta.model.__name__.lower()
