from dataclasses import asdict
from typing import Optional

from requests import Response

from coiote.utils import ApiEndpoint, StringResult, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.domains import Domain, DomainUpdateRequest


class Domains(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="domains")

    @api_call_raw
    def get_all(self, search_criteria: Optional[str] = None) -> Response:
        return self.session.get(self.get_url(), params={"searchCriteria": search_criteria})

    @api_call(StringResult)
    def add_domain(self, domain: Domain) -> Response:
        return self.session.post(self.get_url(), json=asdict(domain))

    @api_call(Domain)
    def get_one(self, domain_id: str) -> Response:
        safe_domain = sanitize_request_param(domain_id)
        return self.session.get(self.get_url(f"/{safe_domain}"))

    @api_call_raw
    def update_one(self, domain_id: str, update: DomainUpdateRequest) -> Response:
        safe_domain = sanitize_request_param(domain_id)
        return self.session.put(self.get_url(f"/{safe_domain}"), json=asdict(update))

    @api_call_raw
    def delete_one(self, domain_id: str) -> Response:
        safe_domain = sanitize_request_param(domain_id)
        return self.session.delete(self.get_url(f"/{safe_domain}"))
