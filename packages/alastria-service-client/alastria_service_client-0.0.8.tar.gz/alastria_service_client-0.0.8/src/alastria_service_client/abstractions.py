from abc import abstractmethod, ABC
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


class AClient(ABC):

    @abstractmethod
    def prepare_alastria_id_encode_abi(self, body: PrepareIDValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def create_alastria_identity(self, body: CreateAlastriaIdentityValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def identity_keys(self, address: Address, body: OnlyNetworkValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def signature(self, body: SignatureValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def delegate_call(self, body: DelegateCallValidator) -> GenericDictResponse:
        ...
    
    @abstractmethod
    def add_key(self, body: AddKeyValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def add_identity_issuer(self, body: AddIdentityIssuerValidator) -> GenericStrResponse:
        ...

    @abstractmethod
    def add_issuer_credential(self, body: AddIssuerCredentialValidator) -> GenericStrResponse:
        ...


    def run_raw_transaction(self, body: RunRawTransaction) -> GenericStrResponse:
        ...