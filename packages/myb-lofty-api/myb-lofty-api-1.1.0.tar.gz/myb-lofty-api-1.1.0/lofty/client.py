import requests

from .constants import LoftyApi
from .client_auth import ClientAuth
from .responses.auth import AwsCredentials
from .pagination_options import PaginationOptions


class LoftyAiApi:
    def __init__(
            self,
            verbose: bool = False,
            api_host_override: str = None
    ):
        """
        Initializes the API client.

        Parameters:
        verbose (bool): Whether to print messages to the console verbosely.
        api_host_override (str): An override for the API Host defined in API Constants - only override for testing.
        """
        self._verbose: bool = verbose

        self._api_constants: LoftyApi = LoftyApi(api_host_override)
        self._client_auth: ClientAuth = ClientAuth(
            verbose,
            api_host_override
        )

    def _request(self, method: str, path: str, params: dict = None, body: dict = None):
        url = self._api_constants.api_endpoint + path
        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            auth=self._client_auth,
            headers={
                'Cache-Control': 'no-cache'
            },
            params=params,
            data=body
        )

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    # Returns a token if properly authenticated
    def login(self, username: str, password: str) -> AwsCredentials:
        return self._client_auth.login(username, password)

    def get_user_info(self) -> dict:
        return self._request('GET', '/users/v2/get')

    def get_user_bank_data(self) -> dict:
        return self._request('GET', '/users/v2/getbdata')

    def get_user_countries(self) -> dict:
        return self._request('GET', '/users/v2/countries')

    # def update_user(self, body: dict) -> dict:
    #     return self._request('POST', '/users/v2/update', body=body)

    # def create_user(self, body: dict) -> dict:
    #     return self._request('POST', '/users/v2/create', body=body)

    # def sign_dao_agreement(self, body: dict) -> dict:
    #     return self._request('GET', '/users/v2/sign-dao-agreement', body=body)

    def get_user_status_summary(self) -> dict:
        return self._request('GET', '/users/v2/status-summary')

    # def submit_kyc(self, body: dict) -> dict:
    #     return self._request('POST', '/verifications/v2/submit-kyc', body=body)

    # def poll_kyc(self) -> dict:
    #     return self._request('POST', '/verifications/v2/poll-kyc', body={})

    def get_verification_tokens(self) -> dict:
        return self._request('GET', '/verifications/v2/getTokens')

    # def retry_verification(self) -> dict:
    #     return self._request('GET', '/verifications/v2/retry')

    # def get_aml_questions(self) -> dict:
    #     return self._request('POST', '/verifications/v2/submit-kyc', body={})

    def get_payment_methods(self) -> dict:
        return self._request('GET', '/payments/v2/list-payment-methods')

    def get_success_statistics_summary(self) -> dict:
        return self._request('GET', '/transactions/v2/stats-summary')

    def get_transactions(self, pagination_options: PaginationOptions) -> dict:
        return self._request('GET', '/transactions/v2/getbyuser', params=pagination_options.to_params())

    def get_transactions_summary(self) -> dict:
        return self._request('GET', '/transactions/v2/getusersummary')

    def create_withdrawal(self, body: dict) -> dict:
        return self._request('POST', '/transactions/v2/createwithdrawal', body=body)

    def get_transaction_by_id(self, txn_id: str) -> dict:
        return self._request('GET', '/transactions/v2/getTransactionById', params={
            'txnId': txn_id
        })

    # Many more endpoints to come! Stay tuned!
