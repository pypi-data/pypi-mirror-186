import requests
from .validators import (
    PrepareIDValidator,
    GenericStrResponse,
    CreateAlastriaIdentityValidator,
    OnlyNetworkValidator,
    Address,
    SignatureValidator,
    DelegateCallValidator,
    GenericDictResponse,
    AddKeyValidator,
    AddIdentityIssuerValidator,
    AddIssuerCredentialValidator,
    RunRawTransaction,
)
import json
from .abstractions import AClient
import os
from typing import Any


class Client(AClient):
    def __init__(self, service_host: str, secret: str = os.environ.get("ALASTRIA_SERVICE_SECRET", "")):

        self.host: str = service_host
        self.secret: str = secret

    def prepare_alastria_id_encode_abi(self, body: PrepareIDValidator) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/prepare-alastria-id-encode-abi",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())

    def create_alastria_identity(self, body: CreateAlastriaIdentityValidator) -> GenericStrResponse:

        headers = {}
        r: Any = requests.post(
            f"{self.host}/create-alastria-identity",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())

    def identity_keys(self, address: Address, body: OnlyNetworkValidator) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/identity-keys/{address}",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())

    
    def signature(self, body: SignatureValidator) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/signature",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())

    def delegate_call(self, body: DelegateCallValidator) -> GenericDictResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/delegate-call",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericDictResponse(**r.json())

    
    def add_key(self, body: AddKeyValidator) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/add-key",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())

    
    def add_identity_issuer(self, body: AddIdentityIssuerValidator) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/addIdentity-issuer",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())


    def add_issuer_credential(self, body: AddIssuerCredentialValidator) -> GenericStrResponse:

        headers = {}
        r: Any = requests.post(
            f"{self.host}/add-issuer-credential",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())


    def run_raw_transaction(self, body: RunRawTransaction) -> GenericStrResponse:
        headers = {}
        r: Any = requests.post(
            f"{self.host}/run-raw-transaction",
            json=json.loads(body.json()),
            headers=headers,
        )
        return GenericStrResponse(**r.json())