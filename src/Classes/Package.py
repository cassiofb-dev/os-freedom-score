class Package:
    def __init__(
        self,
        name: str,
        license: str,
        is_osi_approved: bool = False,
        is_fsf_libre: bool = False,
        is_free: bool = False,
        package_manager: str = None,
    ) -> None:
        self.name = name
        self.license = license
        self.is_osi_approved = is_osi_approved
        self.is_fsf_libre = is_fsf_libre
        self.is_free = is_free
        self.package_manager = package_manager
