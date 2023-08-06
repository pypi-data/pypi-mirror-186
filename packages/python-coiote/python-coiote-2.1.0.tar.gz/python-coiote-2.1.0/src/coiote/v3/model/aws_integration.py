from dataclasses import dataclass


@dataclass
class AwsCertificateData:
    certificatePem: str
    privateKey: str
