from dataclasses import dataclass
from typing import List

@dataclass
class Contract:
    name: str
    abi: str
    address: str

@dataclass
class Node:
    network_name: str
    name: str
    path: str
    node_address: str

@dataclass
class Network:
    node: Node
    name: str
    did_prefix: str
    chain_id: int
    gas_price: int
    gas_max_price: int
    contracts: List[Contract]