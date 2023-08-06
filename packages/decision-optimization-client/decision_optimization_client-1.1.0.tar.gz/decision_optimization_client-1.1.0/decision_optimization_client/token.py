# --------------------------------------------------------------------------
# Source file provided under Apache License, Version 2.0, January 2004,
# http://www.apache.org/licenses/
# (c) Copyright IBM Corp. 2017, 2022
# --------------------------------------------------------------------------

from os import environ
import requests

class Token(object):
    
    def __init__(self, token, refresh_token = None, iam_url=None, token_file=None):
        self.token = token
        self.token_file = token_file
        self.refresh_token = refresh_token
        self.refreshable = (refresh_token != None or token_file != None )
        if(refresh_token != None and iam_url != None):
            self.iam_url = iam_url
        else:
            self.iam_url = None


class TokenRefresher(object):

    def __init__(self, oauth_client, oauth_secret, oauth_url, refresh_token, token_file):
        self.oauth_client = oauth_client
        self.oauth_secret = oauth_secret
        self.oauth_url = oauth_url
        self.refresh_token = refresh_token
        self.token_file = token_file
        return


    @classmethod
    def create(cls, token = None):
        '''Attempts to create a token refresher.
        Returns None if required environment variables are missing.
        '''
        params = {
            'oauth_client':  environ['RUNTIME_OAUTH_CLIENT_ID'],
            'oauth_secret':  environ['RUNTIME_OAUTH_CLIENT_SECRET'],
            'oauth_url':     token.iam_url if token.iam_url != None else environ['RUNTIME_OAUTH_URL'],
            'refresh_token': token.refresh_token if token.refresh_token != None else None,
            'token_file': token.token_file
        }
        return cls(**params)

    def get_fresh_token_from_file(self):
        return read_token_file(self.token_file)      
        
    def get_fresh_token(self):
        if self.token_file != None:
            return self.get_fresh_token_from_file()
        else:
            return self.get_fresh_token_from_iam()  

    def get_fresh_token_from_iam(self):
        '''Obtain a fresh user token.
        Returns the new token on success, None on failure.
        '''
        try:
            r = requests.post(self.oauth_url,
                              auth=(self.oauth_client, self.oauth_secret),
                              data={
                                  'grant_type': 'refresh_token',
                                  'refresh_token' : self.refresh_token,
                                  'expiry' : '600'
                              })
        except Exception as e:
            return None

        if r.status_code != requests.codes["ok"]:
            try:
                r = requests.post(self.oauth_url,
                                  auth=("jupyter-notebook", "jupyter-notebook"),
                                  data={
                                      'grant_type': 'refresh_token',
                                      'refresh_token' : self.refresh_token,
                                      'expiry' : '600'
                                  })
            except Exception as e:
                return None
            if r.status_code != requests.codes["ok"]:
                return None
            self.oauth_client = "jupyter-notebook" 
            self.oauth_secret = "jupyter-notebook"

        try:
            data = r.json()
        except Exception as e:
            return None

        if not 'access_token' in data:
            return None
        
        environ['USER_REFRESH_TOKEN'] = data['refresh_token']
        environ['USER_ACCESS_TOKEN'] = data['access_token']

        return data['access_token']


def attempt_refresh(handle):
    '''Attempts to refresh the token in the argument handle.
    Returns True if the token was refreshed, False otherwise.
    The reason for failed refresh is not exposed to the caller.
    '''

    if not handle.refreshable:
        return False

    if hasattr(handle, '_refresher_') and handle._refresher_:
        refresher = handle._refresher_
    else:
        refresher = TokenRefresher.create(handle)
        if not refresher:
            return False
        handle._refresher_ = refresher

    token = refresher.get_fresh_token()
    if not token:
        return False

    # pylogger.warning('@@@ token refreshed')
    handle.token = token
    return True

def read_token_file(token_file):
    token = None
    try:
        with open(token_file, 'r') as file:
            token = file.read()
    except Exception as e:
        msg = "Reading token from '{}' failed: ".format(token_file, e)
        raise RuntimeError(msg)
    return token