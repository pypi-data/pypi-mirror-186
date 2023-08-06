import base64
from dataclasses import asdict

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.resources import Resource, FileData, Base64FileData, DownloadOptions, \
    ResourceDownloadData


class Resources(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="resources")

    @api_call(str)
    def create_resource(self, resource: Resource) -> Response:
        print(asdict(resource))
        return self.session.post(self.get_url(), json=asdict(resource))

    @api_call_raw
    def upload_resource_data(self, resource_id: str, file: FileData):
        headers = {'Content-Type': 'application/octet-stream'}
        resource_id = sanitize_request_param(resource_id)
        if isinstance(file, Base64FileData):
            file_bytes = base64.b64decode(file.data)
            return self.session.put(self.get_url(f"/{resource_id}/data"), data=file_bytes, headers=headers)
        else:
            raise ValueError("Invalid file type")

    @api_call(ResourceDownloadData)
    def get_resource_download_url(self, resource_id: str, options: DownloadOptions) -> Response:
        resource_id = sanitize_request_param(resource_id)
        return self.session.post(self.get_url(f"/{resource_id}/downloadUrl"), json=asdict(options))
