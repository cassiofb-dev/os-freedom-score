from abc import ABC, abstractmethod
from src.Classes.Package import Package

class PackageManager(ABC):
    @abstractmethod
    def packages(self) -> list[Package]:
        '''
        Returns a list of all packages in the package manager.
        '''
        pass
