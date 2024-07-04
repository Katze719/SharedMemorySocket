import signal
import enum

class MSG(enum.IntEnum):
    REQUEST = signal.SIGUSR1
    SUCCESS = signal.SIGUSR2


class EventCode(enum.Enum):
    NONE = 0x0
    SAVE = 0x1
    SAVE_WITH_MSG = 0x5
    MSG = 0x2
    PID = 0x3
    HANDSHAKE = 0x4
    RESTART_APP = 0x6
    START_APP = 0x7
    COMBINE_TEST_RESULTS = 0x1A
    UNKNOWN = 0xFF
