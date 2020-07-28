from functools import wraps

def call_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        payload = func(*args, **kwargs)
        api_func = func.__name__
        caller = payload.pop("self")
        return caller.action.ckan.call_action(api_func, data=payload)
    return wrapper

class CKANGet(object):
    def __init__(self, action):
        self.action = action

    ###############################################################################
    # Methods below are wrappers for the get module in CKAN API                   #
    # Documentation for these is found here:                                      #
    # https://docs.ckan.org/en/latest/api/index.html#module-ckan.logic.action.get #
    ###############################################################################

    @call_action
    def site_read(self): 
        return locals()

    @call_action
    def package_list(self, limit:int=None, offset:int=None):
        # Not strictly necessary, the input will be checked server-side anyway.
        if (limit is not None) and (offset is None):
            raise ValueError("offset is undefined.")
        if (limit < 0) or (offset < 0):
            raise ValueError("limit and offset cannot be negative.")
        return locals()

    @call_action
    def current_package_list_with_resources(self, limit=None, offset=None, page=None):
        return locals()

    @call_action
    def member_list(self, id:str, object_type:str=None, capacity:str=None):
        return locals()

    @call_action
    def package_collaborator_list(self, id, capacity=None):
        return locals()

    @call_action
    def package_collaborator_list_for_user(self, id, capacity=None):
        return locals()
    
    @call_action
    def group_list(self, sort:str=None, limit:int=None, offset:int=None, groups=None, all_fields=False, include_dataset_count=False, include_extras=False, include_tags=False, include_users=False):
        return locals()

    @call_action
    def organization_list(self, *, order_by=None, sort=None, limit=None, offset=None, organizations=None, all_fields=None, include_dataset_count=None, include_extras=None, include_tags=None, include_groups=None, include_users=None):
        return locals()

    @call_action
    def tag_list(self, query=None, vocabulary=None, all_fields=None):
        return locals()

    @call_action
    def package_show(self, id, use_default_schema=None, include_tracking=None):
        return locals()

    @call_action
    def resource_show(self, id, include_tracking=None):
        return locals()

    @call_action
    def resource_view_show(self, id):
        return locals()

    @call_action
    def resource_view_list(self, id):
        return locals()

    @call_action
    def group_show(self, id, include_datasets=None, include_dataset_count=None, include_extras=None, include_users=None, include_groups=None, include_tags=None, include_followers=None):
        return locals()
    
    @call_action
    def organization_show(self, id, include_datasets=None, include_dataset_count=None, include_extras=None, include_users=None, include_groups=None, include_tags=None, include_followers=None):
        return locals()

    @call_action
    def tag_show(self, id, vocabulary_id=None, include_datasets=None):
        return locals()

    @call_action
    def package_autocomplete(self, q, limit=None):
        return locals()

    @call_action
    def user_autocomplete(self, q, limit=None):
        return locals()

    @call_action
    def group_autocomplete(self, q, limit=None):
        return locals()

    @call_action
    def organization_autocomplete(self, q, limit=None):
        return locals()

    @call_action
    def package_search(self, q, fq=None, fq_list=None, sort=None, rows=None, start=None, facet=None, facet_mincount=None, facet_limit=None, facet_field=None, include_drafts=None, include_private=None, use_default_schema=None):
        return locals()

    @call_action 
    def resource_search(self, q:str, order_by=None, limit=None, offset=None):
        # q is a string on the form f"{field}:{term}" or a list of string on the same form, e.g. "field1:term1"
        # It can probably be written a bit more elegantly
        return locals()

    @call_action
    def tag_search(self, query, vocabulary_id=None, limit=None, offset=None):
        return locals()

    @call_action
    def tag_autocomplete(self, query, vocabulary_id=None, limit=None, offset=None):
        return locals()

    @call_action
    def vocabulary_list(self):
        return locals()

    @call_action
    def vocabulary_show(self, id):
        return locals()

    @call_action
    def help_show(self, name):
        return locals()

    # There are many more to implement, but I'm tired of copy-paste work rn