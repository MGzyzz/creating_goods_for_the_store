from src.request import Request
from src.response import Response


class BaseController:
    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response
