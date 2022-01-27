from model.properties import Properties
from mongoengine import *

class Weapon(Document):
    """docstring for Weapon."""
    name = StringField(required=True)
    description = StringField()
    position = StringField(default="right")
    level = IntField(default=1)
    properties = EmbeddedDocumentField(Properties)
    meta = {'indexes': ['name']}
