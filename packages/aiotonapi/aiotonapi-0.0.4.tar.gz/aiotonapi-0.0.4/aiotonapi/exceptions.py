class TonapiException(Exception):
    def __init__(self, error):
        if isinstance(error, dict):
            error = f'Response error: {error}'
        super().__init__(error)


class TonapiError(TonapiException):
    ...


class TonapiUnauthorized(TonapiException):
    def __init__(self):
        error = (
            "Access token is missing or invalid. "
            "You can get an access token here https://tonapi_bot.t.me/"
        )
        super().__init__(error)
