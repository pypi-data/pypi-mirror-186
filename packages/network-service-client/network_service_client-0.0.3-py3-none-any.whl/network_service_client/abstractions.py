from abc import abstractmethod, ABC
from .enums import NetworksNames
from .models import Network



class AClient(ABC):
    @abstractmethod
    def get_network_by_name(self, name: NetworksNames) -> Network:
        ...