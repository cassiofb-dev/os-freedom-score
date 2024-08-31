import subprocess, re

from src.Classes.Package import Package
from src.PackageManagers.PackageManager import PackageManager

class Flatpak(PackageManager):
    """
    This class handle packages installed with Flatpak:
    - https://docs.flatpak.org/en/latest/flatpak-command-reference.html
    """

    def packages(self) -> list[Package]:
        if not self.hasFlatpak():
            return []

        command = "flatpak list --columns=application,arch,branch"
        result = subprocess.check_output(
            args=command,
            shell=True,
            text=True,
        )

        packages = []
        result_lines = result.split("\n")

        for line in result_lines:
            if len(line) == 0:
                continue

            package_name = re.sub(
                pattern=r'\s+',
                repl='/',
                string=line
            )

            package_license = self.getFlatpakLicense(package_name)

            package = Package(
                name=package_name,
                license=package_license,
                package_manager=self.__class__.__name__,
            )

            packages.append(package)

        return packages

    def hasFlatpak(self) -> bool:
        try:
            subprocess.check_output(
                args="which flatpak",
                shell=True,
                text=True,
                stderr=subprocess.DEVNULL,
            )

            return True
        except subprocess.CalledProcessError:
            return False

    def getFlatpakLicense(self, package_name: str) -> str:
        try:
            command = f"flatpak info {package_name} | grep -E 'License: '"
            result = subprocess.check_output(
                args=command,
                shell=True,
                text=True,
            )

            return result.split(": ")[1].strip()
        except subprocess.CalledProcessError:
            return "Unknown"
