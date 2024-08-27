import platform

from src.PackageManagers.PackageManager import PackageManager
from src.Enums.PlatformSystemEnum import PlatformSystemEnum
from src.Enums.LinuxDistroEnum import LinuxDistroEnum

from src.PackageManagers.APK import APK
from src.PackageManagers.Pacman import Pacman
from src.PackageManagers.Flatpak import Flatpak

class PackageManagerFactory:
    @staticmethod
    def createPackageManagers() -> list[PackageManager]:
        package_managers = []

        operating_system = platform.system()
        match operating_system:
            case PlatformSystemEnum.LINUX.value:
                package_managers.append(Flatpak())

                linux_distro = platform.freedesktop_os_release().get("ID")
                match linux_distro:
                    case LinuxDistroEnum.CHIMERA.value:
                        package_managers.append(APK())
                        return package_managers

                match linux_distro:
                    case LinuxDistroEnum.CACHYOS.value:
                        package_managers.append(Pacman())
                        return package_managers

                    case _:
                        raise ValueError(f"Linux Distro not '{linux_distro}' suported")
            case _:
                raise ValueError(f"Operating System not '{operating_system}' supported")
