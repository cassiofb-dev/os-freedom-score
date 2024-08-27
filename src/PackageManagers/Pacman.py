import subprocess

from src.Classes.Package import Package
from src.PackageManagers.PackageManager import PackageManager

class Pacman(PackageManager):
    """
    This class handle packages installed with Pacman:
    - https://wiki.archlinux.org/title/Pacman
    """

    def packages(self) -> list[Package]:
        command = "pacman -Qi | grep -E '(Licenses        :)|(Name            :)'"
        result = subprocess.check_output(
            args=command,
            shell=True,
            text=True,
        )

        packages = []
        result_lines = result.split("\n")

        for line_index in range(int(len(result_lines) / 2)):
            package_name = result_lines[line_index * 2]
            package_license = result_lines[line_index * 2 + 1]

            package = Package(
                name=package_name[18:],
                license=package_license[18:],
                package_manager=self.__class__.__name__,
            )

            packages.append(package)

        return packages
