from model.properties import Properties
from model.weapon import Weapon
import mongoengine
import pprint

def createItem(itemName):
    item = Weapon(name=itemName)
    properties = Properties()
    properties.value = "0.1"
    item.properties = properties
    item.save()

def selectByName(queryStr):
    print("[INFO] get document where name={}".format(queryStr))
    for item in Weapon.objects(name__contains=queryStr):
        print('ID: {}, name: {}, description: {}, position: {}, level: {}'.format(item.id, item.name, item.description, item.position, item.level))
        print('\t\tPROPERIES: damage: {}, health: {}, weight: {}, value: {}'.format(item.properties.damage, item.properties.health, item.properties.weight, item.properties.value))

def selectAll():
    print("[INFO] Select all")
    for item in Weapon.objects():
        print('ID: {}, name: {}, description: {}, position: {}, level: {}'.format(item.id, item.name, item.description, item.position, item.level))
        print('\t\tPROPERIES: damage: {}, health: {}, weight: {}, value: {}'.format(item.properties.damage, item.properties.health, item.properties.weight, item.properties.value))

def clearCollection():
    item = Weapon()
    item.drop_collection()

def printCollectionIndex():
    print("[INFO] Show indexes")
    item = Weapon()
    pprint.pprint(item.list_indexes())

def insertCollection():
    print("[INFO] Insert bulk")
    array = []
    for item in ('ax', 'bolt', 'club'):
        array.append( Weapon(name=item,properties=Properties()) )
    Weapon.objects.insert(array, load_bulk=False)
    selectAll()

def updateCollection():
    # Update EmbeddedDocumentField
    print("[INFO] Update EmbeddedDocumentField")
    p = Properties(damage="1")
    Weapon.objects(name__='pole').update_one(set__properties=p)
    selectAll()
    print("[INFO] Update DocumentField")
    # Update document
    Weapon.objects(name__='pole').update_one(set__description="pointy stick")
    selectAll()

def deleteCollection():
    print("[INFO] Delete document")
    Weapon.objects(name__contains='pole').delete()
    selectAll()

client = mongoengine.connect(host='db')

db = client.test

clearCollection()
print("[INFO] Before Create empty collection")
pprint.pprint(db.list_collection_names())

for value in ('pole', 'sword', 'hands'):
    createItem(value)

print("[INFO] After Create empty collection")
pprint.pprint(db.list_collection_names())

printCollectionIndex()

selectAll()

selectByName('pole')

updateCollection()

deleteCollection()

insertCollection()
