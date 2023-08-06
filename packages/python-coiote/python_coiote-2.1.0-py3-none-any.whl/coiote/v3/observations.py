from dataclasses import asdict
from typing import List, Optional

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.observations import ObservationData, EntityObservationData, SetObservationRequest, \
    BasicSetObservationRequest


class Observations(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="observations")

    @api_call(List[EntityObservationData])
    def get_all(self, search_criteria: Optional[str] = None) -> Response:
        return self.session.get(self.get_url(), params={"searchCriteria": search_criteria})

    @api_call(ObservationData)
    def get_device_observation_data(self, device_id: str, path: str) -> Response:
        device_id = sanitize_request_param(device_id)
        path = sanitize_request_param(path)
        return self.session.get(self.get_url(f"/device/{device_id}/{path}"))

    @api_call_raw
    def set_observation_on_device(self, device_id: str, path: str, data: SetObservationRequest):
        device_id = sanitize_request_param(device_id)
        path = sanitize_request_param(path)
        return self.session.post(self.get_url(f"/device/{device_id}/{path}"), json=asdict(data))

    @api_call_raw
    def delete_observation_for_device(self, device_id: str, path: str):
        device_id = sanitize_request_param(device_id)
        path = sanitize_request_param(path)
        return self.session.delete(self.get_url(f"/device/{device_id}/{path}"))

    @api_call_raw
    def set_observation_on_group(self, group_id: str, path: Optional[str] = None, lwm2m_url: Optional[str] = None,
                                 data: BasicSetObservationRequest = BasicSetObservationRequest()):
        group_id = sanitize_request_param(group_id)
        if path is not None:
            path = sanitize_request_param(path)
            api_path = f"/group/resourcePath/{group_id}/{path}"
        elif lwm2m_url is not None:
            lwm2m_url = sanitize_request_param(lwm2m_url)
            api_path = f"/group/resourceUrl/{group_id}/{lwm2m_url}"
        else:
            raise ValueError("You must specify either datamodel path or LwM2M Url for the observation")
        return self.session.post(self.get_url(api_path), json=asdict(data))
