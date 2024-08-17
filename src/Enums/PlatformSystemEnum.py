from enum import Enum

class PlatformSystemEnum(Enum):
    """
    This enum class represents the supported platforms by the script.
    The possible values are defined at:
    - https://docs.python.org/3/library/platform.html#platform.system
    """

    LINUX = "Linux"
    DARWIN = "Darwin"
    JAVA = "Java"
    WINDOWS = "Windows"
