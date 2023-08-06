from pydantic import BaseModel
from hexbytes import HexBytes
from typing import NewType
from enum import Enum
from typing import Any


class EidasLevelEnum(Enum):
    Null = 0
    Reputational = 1
    Low = 2
    Substantial = 3
    High = 4


Transaction = NewType("Transaction", dict)  
Address = NewType("Address", str)
TransactionHash = NewType("TransactionHash", str)  # TODO: CHECK RETURN TYPE


class NetworkValidator(BaseModel):
    provider: str
    identity_manager_contract_address: Address
    identity_manager_contract_abi: str
    public_key_registry_contract_address: Address
    public_key_registry_contract_abi: str
    credential_registry_contract_address: Address
    credential_registry_contract_abi: str
    chainId: str


class AddKeyValidator(BaseModel):
    network: NetworkValidator
    public_key: str

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}

class AddIdentityIssuerValidator(BaseModel):
    network: NetworkValidator
    new_issuer_address: Address
    eidas_level: EidasLevelEnum

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class AddIssuerCredentialValidator(BaseModel):
    network: NetworkValidator
    issuer_credential_hash: HexBytes

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class PrepareIDValidator(BaseModel):

    network: NetworkValidator
    sign_address: Address

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class SignatureValidator(BaseModel):
    transaction: dict
    private_key: str
    network: NetworkValidator

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class DelegateCallValidator(BaseModel):
    data: str
    issuer_address: Address
    network: NetworkValidator
    value: int = 0
    address_delegate_call: Address = Address("")

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class RunRawTransaction(BaseModel):
    raw_transaction: Any
    network: NetworkValidator

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class CreateAlastriaIdentityValidator(BaseModel):
    network: NetworkValidator
    add_public_key_call_data: str
    issuer_address: Address

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class GenericStrResponse(BaseModel):

    response: str

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class GenericDictResponse(BaseModel):

    response: dict

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}


class OnlyNetworkValidator(BaseModel):

    network: NetworkValidator

    def get_dict(self) -> dict:
        return {k: str(v) for k, v in self.__dict__.items()}
