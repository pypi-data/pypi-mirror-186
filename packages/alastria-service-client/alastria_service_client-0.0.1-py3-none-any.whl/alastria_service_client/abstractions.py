from abc import abstractmethod, ABC
from .validators import (
    PrepareIDValidator,
    GenericStrResponse
)


class AClient(ABC):

    @abstractmethod
    def prepare_alastria_id_encode_abi(self, body: PrepareIDValidator) -> GenericStrResponse:
        
        ...