import json

from src.PackageManagers.PackageManagerFactory import PackageManagerFactory
from src.Classes.Package import Package
from src.Classes.License import License

class OSFreedomScore:
    def __init__(self) -> None:
        self.__initPackages()
        self.__initSpdxLicenses()
        self.__classifyPackages()

    def __initPackages(self):
        package_manager = PackageManagerFactory.createPackageManager()
        packages = package_manager.packages()
        self.packages = packages

    def __initSpdxLicenses(self):
        with open("./data/spdx-licenses.json", "r") as file:
            spdx_licenses: list[dict] = json.load(file)['licenses']

            licenses: list[License] = []
            for license in spdx_licenses:
                licenses.append(
                    License(
                        license_id=license.get('licenseId'),
                        license_name=license.get('name'),
                        license_url=license.get('detailsUrl'),
                        is_osi_approved=license.get('isOsiApproved') or False,
                        is_fsf_libre=license.get('isFsfLibre') or False,
                    )
                )

            self.spdx_licenses = licenses

    def __classifyPackages(self):
        for package in self.packages:
            if 'meta' in package.license:
                package.is_osi_approved = True
                package.is_fsf_libre = True
                continue

            for license in self.spdx_licenses:
                if license.license_id in package.license:
                    if license.is_osi_approved:
                        package.is_osi_approved = True
                    if license.is_fsf_libre:
                        package.is_fsf_libre = True

    def getOsiApprovedPackages(self) -> list[Package]:
        return [package for package in self.packages if package.is_osi_approved]

    def getFsfLibrePackages(self) -> list[Package]:
        return [package for package in self.packages if package.is_fsf_libre]

    def getNonApprovedPackages(self) -> list[Package]:
        return [package for package in self.packages if not package.is_osi_approved and not package.is_fsf_libre]

    def getReport(self) -> str:
        osi_approved_packages = self.getOsiApprovedPackages()
        fsf_libre_packages = self.getFsfLibrePackages()
        non_approved_packages = self.getNonApprovedPackages()
        fsf_score = len(fsf_libre_packages) / len(self.packages) * 100
        osi_score = len(osi_approved_packages) / len(self.packages) * 100
        non_score = len(non_approved_packages) / len(self.packages) * 100

        report = f"""\
OS Freedom Score: {(100 - non_score):.2f}%
Open Source Initiative Score: {osi_score:.2f}%
Free Software Fundation Score: {fsf_score:.2f}%
Non-Approved Score: {non_score:.2f}%

--- Details ---

Total Packages: {len(self.packages)}
OSI Approved Packages: {len(osi_approved_packages)}
FSF Libre Packages: {len(fsf_libre_packages)}
Non-Approved Packages: {len(non_approved_packages)}"""

        return report
    
    def getNonApprovedPackagesList(self) -> str:
        non_approved_packages = self.getNonApprovedPackages()
        non_approved_packages_list = """\
--- Non-Approved Packages ---

"""
        for package in non_approved_packages:
            non_approved_packages_list += f"{package.name} - {package.license}\n"
        return non_approved_packages_list
