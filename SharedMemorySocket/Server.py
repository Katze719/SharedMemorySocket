from . import shared_memory
from . import protocol
from typing import List

class Server:
    
    def __init__(self, name: str) -> None:
        
        self.shm_conn_info = shared_memory.SharedMemory(f"{name}_conn_info", create=True, size=1)
        self.shm_conn_info.buf[:] = b"\x00" * self.shm_conn_info.size
        
        self.shm_event_code = shared_memory.SharedMemory(f"{name}_event_code", create=True, size=1)
        self.shm_event_code.buf[:] = b"\x00" * self.shm_event_code.size
        
        self.shm_error_code = shared_memory.SharedMemory(f"{name}_error_code", create=True, size=1)
        self.shm_error_code.buf[:] = b"\x00" * self.shm_error_code.size
        
        self.shm_msg_buffer = shared_memory.SharedMemory(f"{name}_msg_buffer", create=True, size=1024)
        self.shm_msg_buffer.buf[:] = b"\x00" * self.shm_msg_buffer.size
        
        
        self.shm_client_buffers: List[shared_memory.SharedMemory] = []
        
    def free(self):
        self.shm_conn_info.close()
        self.shm_event_code.close()
        self.shm_error_code.close()
        self.shm_msg_buffer.close()
        
        for shm in self.shm_client_buffers:
            shm.close()
        
        self.shm_conn_info.unlink()
        self.shm_event_code.unlink()
        self.shm_error_code.unlink()
        self.shm_msg_buffer.unlink()