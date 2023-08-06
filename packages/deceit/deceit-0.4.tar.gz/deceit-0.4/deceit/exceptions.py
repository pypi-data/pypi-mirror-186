import json
from requests.models import Response


class ApiException(Exception):
    def __init__(self, status_code=None, content=None, text=None, data=None):
        super().__init__(status_code, content, text, data)
        self.status_code = status_code
        self.content = content
        self.text = text
        self.data = data

    def __str__(self):
        klass = self.__class__.__name__.lower()
        return f'[{klass}] [{self.status_code}] {self.text}'

    def _repr_pretty_(self, p, cycle):
        """
        for ipython / jupyter
        """
        klass = self.__class__.__name__.lower()
        if self.data:
            body = json.dumps(self.data, indent=2)
        else:
            body = self.text
        p.text(f'[{klass}] [{self.status_code}] => {body}')

    @classmethod
    def from_response(cls, response: Response):
        try:
            return cls(
                response.status_code,
                response.content,
                response.text,
                response.json(),
            )
        except json.JSONDecodeError:
            return cls(
                response.status_code,
                response.content,
                response.text,
            )
