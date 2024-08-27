from abc import ABC, abstractmethod
from src.Classes.Package import Package

class PackageManager(ABC):
    @abstractmethod
    def packages(self) -> list[Package]:
        '''
        Returns a list of all packages in the package manager.
        '''
        pass

    def printPackages(self):
        '''
        Prints all packages in the package manager.
        '''
        for package in self.packages():
            print(f"{package.name} - {package.license}")
