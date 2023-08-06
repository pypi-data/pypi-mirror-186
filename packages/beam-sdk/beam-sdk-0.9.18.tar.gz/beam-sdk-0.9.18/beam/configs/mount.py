from typing import List

from beam.base import AbstractDataLoader
from beam.serializer import VolumeConfiguration
from beam.types import MountType


class MountManager(AbstractDataLoader):
    def __init__(self) -> None:
        self.persistent_volumes: List[VolumeConfiguration] = []

    def PersistentVolume(self, name: str, app_path: str, **_):
        self.persistent_volumes.append(
            VolumeConfiguration(
                name=name,
                local_path=None,
                app_path=app_path,
                mount_type=MountType.Persistent,
            )
        )

    def dumps(self):
        return [
            *[pv.validate_and_dump() for pv in self.persistent_volumes],
        ]

    def from_config(self, mounts: List[dict]):
        if mounts is None:
            return

        for m in mounts:
            if m.get("mount_type") == MountType.Persistent:
                self.PersistentVolume(**m)
