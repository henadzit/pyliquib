from pyliquib.basechangeset import BaseChangeSet


class InlineJsChangeSet(BaseChangeSet):
    def __init__(self, id, author, js, comment, always=False):
        super(InlineJsChangeSet, self).__init__(id, author, comment, always)
        self.js = js

    def _execute(self, db):
        db.eval(self.js)