import anydbm
import os

class DB(object):
    def __init__(self, file_loc):
        self.file_loc = os.path.expanduser(file_loc)
        self._db = anydbm.open(self.file_loc, 'c')

    def __del__(self):
        try:
            self._db.close()
        except Exception:
            pass

    def __contains__(self, nzb):
        return self.in_db(nzb)

    def add_nzb(self, nzb):
        self._db[str(nzb.guid)] = '1'

    def in_db(self, nzb):
        return str(nzb.guid) in self._db

    def close(self):
        self._db.close()
