from dataclasses import asdict

from coiote.utils import ApiEndpoint, api_call, api_call_raw
from coiote.v3.model.aws_integration import AwsCertificateData


class AwsIntegration(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="awsIntegration")

    @api_call_raw
    def add_certificate(self, certificate: AwsCertificateData):
        return self.session.post(self.get_url("/auth/externalCertificate"), json=asdict(certificate))

    @api_call_raw
    def delete_certificate(self):
        return self.session.delete(self.get_url("/auth/externalCertificate"))
