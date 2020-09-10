from ..decorators import call_action


class CKANDatastore(object):
    def __init__(self, action):
        self.action = action

    @call_action
    def create(self, **kwargs):
        # TODO write out the arguments
        return locals()

    @call_action
    def info(self, id):
        return locals()

    @call_action
    def search(
        self,
        resource_id,
        filters=None,
        q=None,
        distinct=None,
        plain=None,
        language=None,
        limit=None,
        offset=None,
        fields=None,
        sort=None,
        include_total=None,
        total_estimation_threshold=None,
        records_format=None,
    ):
        return locals()

    @call_action
    def search_sql(self, sql_query):
        # TODO needs to call sql_query instead
        return locals()
