from pyliquib.basechangeset import BaseChangeSet


class PyCallbackChangeSet(BaseChangeSet):
    def __init__(self, id, author, callback, comment, always=False):
        super(PyCallbackChangeSet, self).__init__(id, author, comment, always)
        self.callback = callback

    def _execute(self, db):
        self.callback(db)
