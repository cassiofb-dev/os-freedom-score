import json

from src.PackageManagers.PackageManagerFactory import PackageManagerFactory
from src.Classes.Package import Package
from src.Classes.License import License

class OSFreedomScore:
    def __init__(self) -> None:
        self.__initPackages()
        self.__initSpdxLicenses()
        self.__initFreeNonSpdxCompliantPackages()
        self.__initFreeNonSpdxCompliantLicenses()

        self.__classifyPackages()

    def __initPackages(self):
        package_manager = PackageManagerFactory.createPackageManager()
        self.package_manager = package_manager
        self.packages = self.package_manager.packages()

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
                package.is_free = True
                package.is_fsf_libre = True
                package.is_osi_approved = True

        self.__classifySpdxCompliantPackages()
        self.__classifyNonSpdxCompliantPackages()

    def __classifySpdxCompliantPackages(self):
        for package in self.packages:
            for license in self.spdx_licenses:
                if license.license_id in package.license:
                    if license.is_osi_approved:
                        package.is_osi_approved = True
                        package.is_free = True
                    if license.is_fsf_libre:
                        package.is_fsf_libre = True
                        package.is_free = True

    def __classifyNonSpdxCompliantPackages(self):
        for package in self.packages:
            if package.is_free:
                continue

            for license in self.free_non_spdx_compliant_licenses:
                if license in package.license:
                    package.is_free = True
                    continue

            for package_name in self.free_non_spdx_compliant_packages:
                if package_name == package.name:
                    package.is_free = True

    def getOsiApprovedPackages(self) -> list[Package]:
        return [package for package in self.packages if package.is_osi_approved]

    def getFsfLibrePackages(self) -> list[Package]:
        return [package for package in self.packages if package.is_fsf_libre]

    def getFreePackages(self) -> list[Package]:
        return [package for package in self.packages if package.is_free]

    def getNonFreePackages(self) -> list[Package]:
        return [package for package in self.packages if not package.is_free]

    def getReport(self) -> str:
        osi_approved_packages = self.getOsiApprovedPackages()
        fsf_libre_packages = self.getFsfLibrePackages()
        free_packages = self.getFreePackages()
        fsf_score = len(fsf_libre_packages) / len(self.packages) * 100
        osi_score = len(osi_approved_packages) / len(self.packages) * 100
        free_score = len(free_packages) / len(self.packages) * 100

        report = f"""\
OS Freedom Score: {free_score:.2f}%
Open Source Initiative Score: {osi_score:.2f}%
Free Software Fundation Score: {fsf_score:.2f}%
Non-Free Score: {(100 - free_score):.2f}%

--- Details ---

Total Packages: {len(self.packages)}
Free Packages: {len(free_packages)}
OSI Approved Packages: {len(osi_approved_packages)}
FSF Libre Packages: {len(fsf_libre_packages)}
Non-Free Packages: {len(self.packages) - len(free_packages)}"""

        return report

    def getNonFreePackagesList(self) -> str:
        non_free_packages = self.getNonFreePackages()
        non_free_packages_list = """\
--- Non-Free Packages ---

"""
        for package in non_free_packages:
            non_free_packages_list += f"'{package.name}',\n"
        return non_free_packages_list

    def __initFreeNonSpdxCompliantLicenses(self):
        self.free_non_spdx_compliant_licenses = [
            'MPL',
            'BSD',
            'GPL',
            'OFL',
            'PSF',
            'SIL',
            'zlib',
            'ZLIB',
            'LGPL',
            'CDDL',
            'Apache',
            'PSF-2.0',
            'XFREE86',
            'isc-dhcp',
            'Sleepycat',
            'PerlArtistic',
            'Public Domain',
            'LicenseRef-Java',
        ]

    def __initFreeNonSpdxCompliantPackages(self):
        self.free_non_spdx_compliant_packages = [
            'xorg', # MIT-like license
            'xorg-xset', # MIT-like license
            'xorg-xrdb', # MIT-like license
            'xorg-xprop', # MIT-like license
            'xorg-xinit', # MIT-like license
            'xorg-xkill', # MIT-like license
            'xorg-xrandr', # MIT-like license
            'xorg-xinput', # MIT-like license
            'xorg-xkbcomp', # MIT-like license
            'xorg-xmodmap', # MIT-like license
            'xorg-xdpyinfo', # MIT-like license
            'xorg-setxkbmap', # MIT-like license
            'xkeyboard-config', # MIT-like license
            'xorg-fonts-encodings', # MIT-like license

            'libgd', # BSD-like license
            'bzip2', # BSD-like license
            'jasper', # MIT-like license
            'libpng', # zlib-like license
            'sqlite', # Public domain
            'snooze', # Public domain
            'libmng', # FSF approved
            'libavif', # BSD-like license

            'tzdata', # Public domain
            'tzutils', # Public domain

            'libyuv', # BSD-like license
            'libsasl', # BSD-like license   
            'libtiff', # BSD-like license
            'fdk-aac', # Unclear but free for FSF
            'libxext', # MIT-like license
            'openssh', # BSD-like license
            'libvdpau', # MIT-like license
            'licenses', # Public domain
            'libxrandr', # MIT-like license
            'libtommath', # Public domain
            'libmodplug', # Public domain
            'libxkbfile', # MIT-like license
            'imagemagick', # GPL Compatible
            'libpciaccess', # MIT-like license
            'fonts-dejavu', # Public domain
            'python-random2', # PSF-2.0 is on OSI list
            'dnssec-anchors', # Public domain

            'pam', # BSD-like license
            'linux-pam', # BSD-like license
            'linux-pam-base', # BSD-like license

            'mobile-broadband-provider-info', # Public domain
        ]
