import json
import requests
from datetime import datetime,timezone,timedelta
from rest_framework import status
try:
    from django.conf import settings
except Exception as e:
    pass

# This is a class that is designed to include all methods and functions one needs to make an A.P.I. call
# It holds native python api request calls
class API(object):

    _base_url = 'https://dev.ledger.nashglobal.co'

    _auth_token_url = None
    _oauth2_client_id = None
    _client_secret = None
    _identity_token = None
    _auth_scope = None

    global_session = requests.Session()

    try:
        _oauth2_client_id = getattr(
            settings, 'OAUTH2_CLIENT_ID', _oauth2_client_id)
        _client_secret = getattr(
            settings, 'CLIENT_SECRET', _client_secret)
        _auth_token_url = getattr(
            settings, 'OAUTH2_TOKEN_URL', _auth_token_url)
        _auth_scope = getattr(
            settings, 'OAUTH2_SCOPE', _auth_scope)
    except Exception as e:
        pass

    # Most API calls require headers, params and payloads
    _headers = None
    _params = None
    _payload = None

    # You always expect a response from A.P.I. calls
    _response = {}

    # When using this class to create an A.P.I. class, each API should have an optional name and code
    # but must have headers and any required parameters
    def __init__(self, name=None, headers=None, params=None, code=None):
        self._name = name
        self._code = code

        self._headers = headers
        self._params = params       

        try:
            self._base_url=getattr(settings, 'LEDGER_URL', self._base_url)
        except Exception as e:
            pass

        requests.packages.urllib3.disable_warnings()

    def set_identity_token(self,identity_token):
        self._identity_token = identity_token
        return self

    def refresh_identity_token(self):
        refresh_token=False
        # check if an Authorization header was set in the global token
        if self.global_session.headers.get('Authorization'):
            # check when it was set to expire which is set in '%H:%M:%S'
            auth_expires_in=self.global_session.headers.get('auth_expires_in')
            # convert the string '%H:%M:%S' to time
            auth_expires_in=datetime.strptime(auth_expires_in, '%H:%M:%S').time()
            # get the current time and add ten minutes to it, so that we refresh the token 10 minutes before its expiry
            current_time=(datetime.now(timezone.utc) + timedelta(minutes=5)).time()
            # if current time plus 10 minutes is more than when the auth needs to expire
            # refresh the token
            if current_time > auth_expires_in:
                # first set the Authorization to an empty string
                self.global_session.headers.update({'Authorization': ''})
                refresh_token=True
        # If the Authorization header was not set in the global token
        else:
            refresh_token=True
            
        if refresh_token:
            _payload = {
                'grant_type': 'client_credentials',
                'scope': self._auth_scope,
                'client_id': self._oauth2_client_id,
                'client_secret': self._client_secret
            }
            self._identity_token = requests.request(
                "POST", self._auth_token_url, data=_payload)             
                
            if self._identity_token.status_code == 200:                
                self.global_session.headers.update({
                    'Authorization':f"{self._identity_token.json().get('access_token',None)}",
                    'auth_expires_in':(datetime.now(timezone.utc) + timedelta(seconds=self._identity_token.json().get('expires_in',0))).strftime("%H:%M:%S")
                })  
                

    # There are 3 types of API requests that most APIs use, POST, GET, PUT and DELETE
    # This method will take the payload or data to be sent and send it to the required API url
    # using the desired method and returns the response
    def api_request(self, url, payload, method, verify = False, files = None):
        # Authenticate this service on the Nash Identity Server
        self.refresh_identity_token()
        
        if payload == "null":
            self._payload=json.dumps({})
        else:
            self._payload = payload
        
        if self._headers is not None and self.global_session.headers.get('Authorization'):
            self._headers.update({
                'Authorization':f"Bearer {self.global_session.headers.get('Authorization')}"
            })
        
        try:
            if method == 'POST':
                self._response = requests.post(url, headers=self._headers, params=self._params,
                                           data=self._payload, json=self._payload, verify=verify,files=files)
            elif method == 'PUT':
                self._response = requests.put(url, headers=self._headers, params=self._params,
                                           data=self._payload, json=self._payload, verify=verify)
            elif method == 'GET':
                self._response = requests.get(url, headers=self._headers, params=self._params,
                                           data=self._payload, json=self._payload, verify=verify)
            elif method == 'DELETE':
                self._response = requests.delete(url, headers=self._headers, params=self._params,
                                           data=self._payload, json=self._payload, verify=verify)

            try:
                if self._response.status_code == status.HTTP_200_OK:
                    self._response = json.loads(self._response.text)
                else:
                    if status.is_server_error(self._response.status_code):
                        self._response['error'] = f'ERP Core Server Error: HTTP Error Code {self._response.status_code}'
                    elif status.is_client_error(self._response.status_code):
                        self._response['error'] = f'ERP Sync Service Server Error: HTTP Error Code {self._response.status_code}'
            except ValueError as e:
                self._response['error'] = self._response.text


            # try:
            #     self._response = json.loads(self._response.text)
            # except ValueError as e:
            #     self._response = self._response.text

        except Exception as e:
            self._response['error'] = 'Internal Server Error'
            print(e)
        finally:
            return self._response

    # Method used to get the repsonse returned by an API instead of calling the API again
    def get_response(self):
        return self._response

    def set_headers(self, headers):
        self._headers = headers
        return self

    def get_headers(self):
        return self._headers

    def set_params(self, params):
        self._params = params
        return self

    def get_params(self):
        return self._params

    def get_payload(self):
        return self._payload

    def get_base_url(self):
        return self._base_url

    @property
    def get_identity_token(self):
        return self._identity_token