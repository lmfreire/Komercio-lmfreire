class MixinSerializer:
    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method)