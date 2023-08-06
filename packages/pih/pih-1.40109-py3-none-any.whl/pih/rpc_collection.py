
from dataclasses import dataclass
import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.const import ServiceCommands, ServiceRoles


@dataclass
class Subscribtion:
    service_command: ServiceCommands
    type: int = None
    name: str = None
    actiated: bool = False


@dataclass
class Subscriber:
    role: ServiceRoles = None
    type: int = None
    name: str = None
    available: bool = True
    enabled: bool = True