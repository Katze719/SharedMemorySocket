import ctypes
import enum

class SHMFlags(enum.Flag):
    FIN = 0x01 # 0b00000001
    SYN = 0x02 # 0b00000010
    RST = 0x04 # 0b00000100
    PSH = 0x08 # 0b00001000
    ACK = 0x10 # 0b00010000
    URG = 0x20 # 0b00100000
    ECE = 0x40 # 0b01000000
    CWR = 0x80 # 0b10000000
    
# header = 14 bytes, gives us 1010 bytes for the payload
class SHMHeader(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_ubyte),            # version number (1 - 255), 0 == drop package
        ("source_addr", ctypes.c_uint16),       # source client number (0 - 65535)
        ("destination_addr", ctypes.c_uint16),  # destination client number (1 - 65535), 0 == server
        ("squence_number", ctypes.c_uint32),    # sequence number (0 - 4294967295)
        ("package_count", ctypes.c_uint32),     # total number for how many packages are coming (0 - 4294967295)
        ("flags", ctypes.c_ubyte),              # flags (0 - 255)
        ("checksum", ctypes.c_uint16),          # checksum (0 - 65535)
    ]