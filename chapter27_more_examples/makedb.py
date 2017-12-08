from person import Person, Manager
bob = Person('bob smith')
sue = Person('sue jones', job='dev', pay=100000)
tom = Manager('tom jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
	db[object.name] = object
db.close()