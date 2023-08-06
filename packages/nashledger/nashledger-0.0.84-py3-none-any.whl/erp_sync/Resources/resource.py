
from erp_sync.APIs.api_format import API
import json
from erp_sync.APIs.utils.generate_code import get_code

# This a super class used to hold methods that are used by all ERP/Client's entities
# This will be the default method behaviours to be used, incase the inheriting class chooses not override them

# Every ERP/Client entities/apis operate as 'CRUDly'. 
# The methods are:
# A Create/New method - a method to make a new entry
# A Read method - a method to read entries
# A Update/Edit method - a method to update an entry
# A Delete method - a method to delete an entry

# An import method - a method to import entries

# This class will also have 'support variables'. These are variables used/set to enable the above CRUD methods work 
# This class will also have 'support methods'. These are the getter and setter methods to 'support variables'

# It also has two methods that have to be overriden by inheriting classes,
# 1. payload - This method is used to return the default payload expected by the inheriting class 
# 2. serialize - This method is used to convert the standardized CRUD operations payloads to the expected client/erp structure.

# Methods that do not return results i.e. return void, they instead return an instance of themselves. This is to allow for chaining of methods
class Resource(API):
    # a variable to hold the erp/client ID 
    _client_id = None
    
    # a variable to hold the user/developer ID
    _user_id = -1
    
    # a variable to hold the company ID of the client/erp
    _company_id = 1
    
    # a variable to hold the ID of the type of erp/client being interacted with e.g. Zoho, Odoo
    _client_type = -1
    
    # a variable to hold responses returned, it will hold the response of the last operation/method executed
    _response = {}
    
    # a variable to hold the URL used to create a new entry
    _new_url = ""
    
    # a variable to hold the URL used to edit an entry
    _edit_url = ""
    
    # a variable to hold the URL used to read entries
    _read_url = ""
    
    # a variable to hold the URL used to delete an entry
    _delete_url = ""
    
    # a variable to hold the URL used to import entries
    _import_url = ""
    
    # These are the ids of each type client/erp
    QBO = 1
    ZOHO = 2
    SAP = 3
    XERO = 4
    ODOO = 5
    MS_DYNAMICS = 6
    ERP_NEXT = 8
    
    # a variable to hold the entity/resource ID, you can choose to give each entity an ID
    _resource_id = -1

    # below are property variables to be used in inheriting classes as markers i.e. what to do in that class
    # if the you want to read, create or update an entry.

    @property
    def READ(self):
        return 0

    @property
    def NEW(self):
        return 1

    @property
    def UPDATE(self):
        return 2

    def set_company_id(self, company_id):
        self._company_id = company_id
        return self    

    def set_client_type(self, client_type):
        self._client_type = client_type
        return self        
    
    def set_client_id(self, client_id):
        self._client_id = client_id
        return self        
    
    def set_user_id(self, user_id):
        self._user_id = user_id
        return self

    def set_urls(self,urls):
        self.set_new_url(urls.get("new",""))
        self.set_edit_url(urls.get("edit",""))
        self.set_read_url(urls.get("read",""))
        self.set_delete_url(urls.get("delete",""))
        self.set_import_url(urls.get("import",""))
        return self

    # method to make a new entry
    def new(self, payload = None, method='POST',endpoint=None, files = None):
        if endpoint is None:
            endpoint = self.get_new_url()

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = self._exec(payload, method, endpoint, files = files)

        # set response here
        return self

    # method to update an entry
    def edit(self, payload = None, method='PUT',endpoint=None, files = None):
        if endpoint is None:
            endpoint = self.get_edit_url()
        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = self._exec(payload, method, endpoint, files = files)
        return self

    # method to read entries
    def read(self, payload = None, method='GET',endpoint=None):
        if endpoint is None:
            endpoint = self.get_read_url()

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = self._exec(payload, method, endpoint)
        return self

    # method to delete an entry
    def delete(self, payload = None, method='DELETE',endpoint=None):
        if endpoint is None:
            endpoint = self.get_delete_url()

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = self._exec(payload, method, endpoint)
        return self

    # method to import entries
    def import_data(self, payload = None, method='GET',endpoint=None):
        if endpoint is None:
            endpoint = self.get_import_url()

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = self._exec(payload, method, endpoint)
        return self


    # This method is used to return the default payload expected by the inheriting class
    def payload(self):
        return {}


    # This method is used to convert the standardized CRUD operations payloads. It serves two functions
    # 1. It will take the standardized payloads and return the expected client/erp specific payload 
    # 2. It will get responses from READ operations and standardize the responses
    def serialize(self):
        return self

    def response(self):
        return self._response

    def set_response(self,response={}):
        self._response = response
        return self
    
    def set_new_url(self,new_url):
        self._new_url = new_url
        return self
    
    def set_edit_url(self,edit_url):
        self._edit_url = edit_url
        return self
    
    def set_read_url(self,read_url):
        self._read_url = read_url
        return self
    
    def set_delete_url(self,delete_url):
        self._delete_url = delete_url
        return self
    
    def set_import_url(self,import_url):
        self._import_url = import_url
        return self
    
    def get_new_url(self):
        return self._new_url
    
    def get_edit_url(self):
        return self._edit_url
    
    def get_read_url(self):
        return self._read_url
    
    def get_delete_url(self):
        return self._delete_url
    
    def get_import_url(self):
        return self._import_url

    def get_client_id(self):
        return self._client_id
    
    def get_company_id(self):
        return self._company_id
    
    def get_client_type(self):
        return self._client_type
    
    def get_user_id(self):
        return self._user_id
    
    def generate_code(self, length = 6):
        return get_code(length)
    
    # This is the method that will be called execute an A.P.I. request. 
    # Since most of the A.P.I. calls methods are similar, they are to be placed inside this method to avoid code duplication.
    # 
    # It will only accept parameters unique to each A.P.I. request. 
    def _exec(self, payload = None, method='POST', endpoint = "", files = None):
                
        if files is None:
            payload=json.dumps(payload)
        else:
            payload=payload

        # Call the iPay A.P.I. url by passing the variables to the super class method responsible for making requests to A.P.I. endpoints
        # The super class method returns a response that is returned by this method
        return super().api_request(url=f"{super().get_base_url()}{endpoint}", payload=payload, method=method, files=files)