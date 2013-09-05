import datetime

from constants import *


class BaseChangeSet(object):
    def __init__(self, id, author, comment='', always=False):
        self.id = id
        self.author = author
        self.comment = comment
        self.always = always

    def execute(self, db):
        if self.always or not self._executed(db):
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
        db[LIQUIB_LOG].update({'id': self.id}, log_record, upsert=True)
