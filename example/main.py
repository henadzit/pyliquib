from pymongo import MongoClient
from pyliquid import pycall, run

def __1(db):
	db.collection1.insert({'successful': True})

def __2(db):
	db.collection2.insert({'msg': 'Hello World!'})

if __name__ == '__main__':
	change_sets = (
		pycall('1', 'user@example.com', __1),
	    pycall('2', 'user@example.com', __2)
	)

	run(MongoClient().test, change_sets)