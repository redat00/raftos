# Python Standard Library
from dataclasses import dataclass
from typing import Callable, Union

# First Party
from raftos_plus.cryptors import Cryptor, DummyCryptor
from raftos_plus.serializers import JSONSerializer, MessagePackSerializer


@dataclass
class Configuration:
    """Dataclass representing the configuration of raftos-plus."""

    log_path: str = "/var/log/raftos-plus"
    serializer: Union[
        MessagePackSerializer, JSONSerializer
    ] = MessagePackSerializer
    heartbeat_interval: float = 0.3
    step_down_missed_heartbeats: int = 5
    election_interval_spread: int = 3
    secret_key: bytes = b"raftos-plus sample secret key"
    salt: bytes = b"raftos sample salt"
    cryptor: Union[Cryptor, DummyCryptor] = DummyCryptor
    on_leader: Callable = None
    on_follower: Callable = None

    step_down_interval = None
    election_interval = None

    def __post_init__(self) -> None:
        """Post init of dataclass Configuration."""

        self.step_down_interval = (
            self.heartbeat_interval * self.step_down_missed_heartbeats
        )
        self.election_interval(
            self.step_down_interval,
            self.step_down_interval * self.election_interval_spread,
        )
        if isinstance(self.cryptor, type):
            self.cryptor = self.cryptor(self)


config = Configuration()
