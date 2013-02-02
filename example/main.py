from pymongo import MongoClient
from pyliquib import pycall, run, js

def __1(db):
	db.users.insert({'name': 'Henadzi Tsaryk'})
	db.users.insert({'name': 'Fast Turtle'})

def __2(db):
	for user in db.users.find():
		user['firstName'], user['lastName'] = user['name'].split()
		del user['name']
		db.users.save(user)

__3 = """
db.users.find().forEach(function(u) {
	u.initials = u.firstName[0] + u.lastName[0];
	db.users.save(u);
})
"""

if __name__ == '__main__':
	change_sets = (
		pycall('1', 'user@example.com', __1, 'It\'s a comment! The change set is executed with a python callback.'),
		pycall('2', 'user@example.com', __2),
		js('3', 'another.user@example.com', __3, 'This change set is an inline js which is executed by\
	     the MongoDB engine.')
	)

	run(MongoClient().test, change_sets)