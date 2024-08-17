import platform

from src.PackageManagers.PackageManager import PackageManager
from src.Enums.PlatformSystemEnum import PlatformSystemEnum
from src.Enums.LinuxDistroEnum import LinuxDistroEnum
from src.PackageManagers.APK import APK

class PackageManagerFactory:
    @staticmethod
    def createPackageManager() -> PackageManager:
        match platform.system():
            case PlatformSystemEnum.LINUX.value:
                match platform.freedesktop_os_release().get("ID"):
                    case LinuxDistroEnum.CHIMERA.value:
                        return APK()

                    case _:
                        raise ValueError("Linux Distro not supported")
            case _:
                raise ValueError("Operating System not supported")
