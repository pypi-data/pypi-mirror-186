from erp_sync.Resources.clients import Client
from erp_sync.Resources.users import Users
from erp_sync.Resources.resource import Resource

# This class is responsible for configuring and checking of developer credentials.
# It's the class that will be called first before a developer accesses Nash Framework - Nash's API resources

# This class is also a Resource class
class Nash(Resource):
    # Since all classes are going to be called from this class,
    # You can use this class to set attributes of other classes/resources
    _headers = {
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    _params = {}

    _response = {}

    _is_logged_in = False

    _client = None

    _access_token = None

    _user_id = -1

    # When intializing this class, set the default request headers and params
    def __init__(self):
        super().__init__("NashAPI", self._headers, self._params)

    # Use this method to login a user into the nash framework
    def login(self, payload=None, method='POST', endpoint="/auth/login"):
        # authenticate and provide user credentials
        # set response here

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = Users(self).login(
            payload, method, endpoint).response()

        if self._response["status"] == 200:

            super().set_user_id(self._response["id"])

            if 'access_token' in self._response:

                self._set_access_token(self._response["access_token"])
                self._is_logged_in = True

                self._headers["Authorization"] = f"Bearer {self.get_access_token()}"

        return self

    # Use this method to sign up a user into the nash framework
    def sign_up(self, payload=None, method='POST', endpoint="/users", log_in_user=True):
        # authenticate and provide user credentials
        # set response here

        # Call the method exec to make the request to A.P.I. endpoint and return the data that will be returned in this method
        self._response = Users(self).new(payload, method, endpoint).response()

        if log_in_user:
            if 'created_at' in self._response:

                self.login(payload={"username": payload.get(
                    "username"), "password": payload.get("password")}).response()

        return self

    # Use this method to get access to the ERP/Client class, this is the gateway to the ERP Resources/Entities and 
    def client(self, client_id=-1):

        if self._client is None:
            self._client = Client(self, client_id)

        return self._client

    def user(self):
        return Users(self)

    # Method to check if a user is logged in
    def is_logged_in(self):
        return self._is_logged_in

    # Method to set user log in access token
    def _set_access_token(self, access_token):
        self._access_token = access_token
        return self

    # Method to get user log in access token
    def get_access_token(self):
        return self._access_token
