import subprocess, re

from src.Classes.Package import Package
from src.PackageManagers.PackageManager import PackageManager

class APK(PackageManager):
    """
    This class handle packages installed with APK (Alpine Package Manager):
    - https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper
    """

    def packages(self) -> list[Package]:
        command = "apk list -I | grep -oh '{.*)' | sort -u"
        result = subprocess.check_output(
            command,
            shell=True,
            text=True,
        )

        packages = []
        result_lines = result.split("\n")

        for line in result_lines:
            if len(line) == 0:
                continue

            package_name = re.findall(pattern=r'{.*}', string=line).pop()
            package_license = re.findall(pattern=r'\(.*\)', string=line).pop()

            package = Package(
                name=package_name[1:-1],
                license=package_license[1:-1],
                package_manager=self.__class__.__name__,
            )

            packages.append(package)

        return packages
