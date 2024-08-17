from enum import Enum

class LinuxDistroEnum(Enum):
    """
    This enum class represents the supported linux distros by the script.
    Those values are the distro ID defined by the method:
    - https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release
    """

    CHIMERA = "chimera"
