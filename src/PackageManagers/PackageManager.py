from abc import ABC, abstractmethod
from src.Classes.Package import Package

class PackageManager(ABC):
    @property
    @abstractmethod
    def is_spdx_compliant(self) -> str:
        '''
        Returns whether the package manager is SPDX compliant or not.
        For it to be SPDX compliant, it must have a valid SPDX license.
        See https://spdx.org/licenses/ for a list of valid SPDX licenses.
        '''
        pass

    @abstractmethod
    def packages(self) -> list[Package]:
        '''
        Returns a list of all packages in the package manager.
        '''
        pass
