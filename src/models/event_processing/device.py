import hashlib

from src.models.event_processing.device_status import DeviceType
from pydantic import BaseModel


class Device(BaseModel):
    id: str
    device_type: str
    device_status: DeviceType
    device_age: int

    def get_hash(self, mission_date: str, mission_name: str) -> str:
        hash = hashlib.sha256()
        hash.update(mission_date.encode())
        hash.update(mission_name.encode())
        hash.update(self.device_type.encode())
        hash.update(self.device_status.value.encode())
        return hash.hexdigest()
        instancia_hash = hashlib.sha256()
        instancia_hash.update(fecha.encode())
        instancia_hash.update(mision.encode())
        instancia_hash.update(tipo_dispositivo.encode())
        instancia_hash.update(estado_dispositivo.encode())
        return instancia_hash.hexdigest()
