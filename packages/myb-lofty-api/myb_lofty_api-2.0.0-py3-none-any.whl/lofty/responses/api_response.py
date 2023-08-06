class ApiResponse:
    def __init__(self, api_response: dict):
        self.success: bool = bool(api_response.get('success', False))
        # Example: "ok"
        self.status: str = api_response.get('status')
        # Example: "success"
        self.message: str = api_response.get('message')
        self.data: dict = api_response.get('data')


class ApiListResponse:
    def __init__(self, api_response: dict):
        self.success: bool = bool(api_response.get('success', False))
        # Example: "ok"
        self.status: str = api_response.get('status')
        # Example: "success"
        self.message: str = api_response.get('message')
        self.data: list = api_response.get('data')

