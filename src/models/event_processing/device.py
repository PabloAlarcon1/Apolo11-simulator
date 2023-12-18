import hashlib

from src.models.event_processing.device_status import DeviceType
from pydantic import BaseModel


class Device(BaseModel):
    id: str
    device_type: str
    device_status: DeviceType
    device_age: int

    def get_hash(self, fecha: str, mision: str, tipo_dispositivo: str, estado_dispositivo: str) -> str:
        instancia_hash = hashlib.sha256()
        instancia_hash.update(fecha.encode())
        instancia_hash.update(mision.encode())
        instancia_hash.update(tipo_dispositivo.encode())
        instancia_hash.update(estado_dispositivo.encode())
        return instancia_hash.hexdigest()
