import datetime

from constants import *

class BaseChangeSet(object):
	def __init__(self, id, author, comment=''):
		self.id = id
		self.author = author
		self.comment = comment

	def execute(self, db):
		if not self._executed(db):
			self._execute(db)
			self._log(db)

	def _execute(self, db):
		raise NotImplementedError()

	def _executed(self, db):
		return db[LIQUIB_LOG].find_one({'id': self.id})

	def _log(self, db):
		log_record = {'id': self.id,
		              'author': self.author,
		              'comment': self.comment,
		              'executed': datetime.datetime.utcnow()}
		db[LIQUIB_LOG].insert(log_record)
