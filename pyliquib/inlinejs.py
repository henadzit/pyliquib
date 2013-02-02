from pyliquib.basechangeset import BaseChangeSet

class InlineJsChangeSet(BaseChangeSet):
	def __init__(self, id, author, js, comment):
		super(InlineJsChangeSet, self).__init__(id, author, comment)
		self.js = js

	def _execute(self, db):
		db.eval(self.js)