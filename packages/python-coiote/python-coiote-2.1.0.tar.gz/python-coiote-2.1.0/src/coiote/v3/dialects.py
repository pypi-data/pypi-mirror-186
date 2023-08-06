from requests import Response

from coiote.utils import ApiEndpoint, api_call
from coiote.v3.model.dialects import Dialect


class Dialects(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="dialects")

    @api_call(Dialect)
    def add_lwm2m_object_definition(self, xml_definition: str, overwrite: bool = False) -> Response:
        url = self.get_url("/addObject")
        headers = {'Content-Type': 'text/xml'}
        if overwrite:
            return self.session.put(url, data=xml_definition, headers=headers)
        else:
            return self.session.post(url, data=xml_definition, headers=headers)
