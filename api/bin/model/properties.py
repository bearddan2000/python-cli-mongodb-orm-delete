from mongoengine import *

class Properties(EmbeddedDocument):
    """docstring for Properties."""
    damage = StringField()
    health = StringField()
    weight = StringField()
    value = StringField()
