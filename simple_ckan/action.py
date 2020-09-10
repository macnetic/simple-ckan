from .get import CKANGet
from .ext.datastore import CKANDatastore


class CKANAction(object):
    def __init__(self, ckan):
        self.ckan = ckan
        self.get = CKANGet(self)
