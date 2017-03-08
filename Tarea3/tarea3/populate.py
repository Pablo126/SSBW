from mongoengine import *
import datetime

db = connect('test')

# Esquema para la BD de pruebas de mongoDB

class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()   # añadido
    zipcode  = IntField()
    coord    = GeoPointField() # OJO, al BD de test estan a revés
                               # [long, lat] en vez de [lat, long]

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)              # en la misma collección
    grades           = ListField(EmbeddedDocumentField(likes))


dir = addr(street="Hermosa, 5 ", city="Granada", zipcode=18010, coord=[37.1766872, -3.5965171])  # así están bien
r2 = restaurants(name="Casa Julio", cuisine="AA", borough="Centro", address=dir)
r2.save()
dir = addr(street="Mi calle, 10 ", city="Granada", zipcode=18030, coord=[37.1763332, -3.2265171])  # así están bien
r3 = restaurants(name="DonPepe", cuisine="Granaina", borough="Centro", address=dir)
r3.save()
dir = addr(street="Otra, 15 ", city="Granada", zipcode=1802, coord=[37.1856872, -3.8865171])  # así están bien
r4 = restaurants(name="Mi casatelefno", cuisine="Granaina", borough="Centro", address=dir)
r4.save()
# Poner alguno más
# ...
# Consulta, los tres primeros
for r in restaurants.objects:
    print (r.name, r.address.coord)

# Hacer más consultas, probar las de geolocalización
# ...
aux = restaurants.objects(cuisine='AA')
for a in aux:
	print (a.name)
