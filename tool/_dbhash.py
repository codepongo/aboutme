import dbm
class _dbm(object):
    def __init__(self, dbm):
        self.dbm = dbm
    def has_key(self, k):
        return self.dbm.has_key(k)
    def keys(self):
        return self.dbm.keys()
    def sync(self):
        pass
    def has_key(self, k):
        return self.dbm.has_key(k)
    def __getitem__(self, k):
        return self.dbm[k]
    def __setitem__(self, k, v):
        self.dbm[k] = v
    def __delitem__(self, k):
        del(self.dbm[k])
def open(filename, flag, mode=0666):
    return _dbm(dbm.open(filename, flag, mode))

