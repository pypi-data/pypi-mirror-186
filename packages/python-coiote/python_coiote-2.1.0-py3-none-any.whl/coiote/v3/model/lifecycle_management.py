from dataclasses import dataclass


@dataclass
class FactoryTestingRequest:
    endpointName: str
    domain: str
