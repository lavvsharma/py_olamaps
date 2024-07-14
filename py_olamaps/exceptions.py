class APIException(Exception):
    def __init__(self, err_msg, response=None, body=None):
        super().__init__(err_msg)
        self.err_msg = err_msg
        self.response = response.json()
        self.body = body

    def __str__(self):
        return f"{self.err_msg} (response={self.response}, body={self.body})"


class OlaMapsError(Exception):
    pass
