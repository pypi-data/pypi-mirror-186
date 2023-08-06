import jwt


class ClientToken:
    def __init__(self, client_token_data: dict):
        self.uid: int = client_token_data.get('uid')
        self.cid: int = client_token_data.get('cid')
        self.ctt: int = client_token_data.get('ctt')
        self.htt: int = client_token_data.get('htt')
        # Example: 'verify.berbix.com'
        self.aud: str = client_token_data.get('aud')
        self.exp: int = client_token_data.get('exp')
        self.iat: int = client_token_data.get('iat')
        self.sub: str = client_token_data.get('sub')


class VerificationToken:
    def __init__(self, verification_token_data: dict):
        self.client_token: str = verification_token_data.get('clientToken')

    def decode_client_token(self) -> ClientToken:
        decoded_jwt = jwt.decode(self.client_token, key=None, options={"verify_signature": False})
        return ClientToken(decoded_jwt)
