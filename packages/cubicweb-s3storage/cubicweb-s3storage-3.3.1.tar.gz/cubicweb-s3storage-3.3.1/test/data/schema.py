from yams.buildobjs import EntityType, String, Bytes


class Image(EntityType):
    title = String()
    data = Bytes(required=True)
    thumbnail = Bytes()
