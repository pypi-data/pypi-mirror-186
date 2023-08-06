import requests
import json
from .abstractions import AClient
import os
from typing import Any, Dict
from .models import Network
from .enums import NetworksNames


class Client(AClient):
    def __init__(
        self, service_host: str, secret: str = os.environ.get("NETWORK_SERVICE_SECRET", "")
    ):

        self.host: str = service_host
        self.secret: str = secret

    def get_network_by_name(self, name: NetworksNames) -> Network:
        headers: Dict[str, Any] = {}
        r: Any = requests.get(
            f"{self.host}/network/network-handler/get_network_by_name/?network_name={name.value}/",
            headers=headers,
            timeout=5,
        )
        return Network(**r.json())

    