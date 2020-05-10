from datetime import datetime


class AuthToken:

    def overwrite_token(self, access_token, refresh_token, expires_in):
        self.token_timestamp = datetime.now()
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = int(expires_in)