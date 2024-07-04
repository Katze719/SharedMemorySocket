from . import shared_memory

class Client:
    
    def __init__(self, name: str) -> None:
        
        self.shm_conn_info = shared_memory.SharedMemory(f"{name}_conn_info", track=False)
        self.shm_event_code = shared_memory.SharedMemory(f"{name}_event_code", track=False)
        self.shm_error_code = shared_memory.SharedMemory(f"{name}_error_code", track=False)
        self.shm_msg_buffer = shared_memory.SharedMemory(f"{name}_msg_buffer", track=False)