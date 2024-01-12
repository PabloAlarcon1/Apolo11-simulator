from src.models.event_processing.mission import Mission
import uuid
from pydantic import computed_field

class Unkn(Mission):

    @property
    def hash(self):
        '''
        Overrides hash property in order to disable hash generation
        
        Parameters:
        
        Returns:
            None
        '''
        return None
    
    
    @computed_field
    @property
    def process_id(self) -> str:
        return str(uuid.uuid4())
    
    def generate_event(self) -> None:
        name: str = f'APLUNKN-0001.log'
        
        super().generate_event(name)
        