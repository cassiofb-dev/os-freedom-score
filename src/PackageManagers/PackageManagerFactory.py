import platform

from src.PackageManagers.PackageManager import PackageManager
from src.Enums.PlatformSystemEnum import PlatformSystemEnum
from src.Enums.LinuxDistroEnum import LinuxDistroEnum
from src.PackageManagers.APK import APK

class PackageManagerFactory:
    @staticmethod
    def createPackageManager() -> PackageManager:
        operating_system = platform.system()

        match operating_system:
            case PlatformSystemEnum.LINUX.value:
                linux_distro = platform.freedesktop_os_release().get("ID")

                match linux_distro:
                    case LinuxDistroEnum.CHIMERA.value:
                        return APK()

                    case _:
                        raise ValueError(f"Linux Distro '{linux_distro}' not suported")
            case _:
                raise ValueError(f"Operating System not '{operating_system}' supported")
