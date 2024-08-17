class License:
    def __init__(
            self,
            license_id: str,
            license_name: str,
            license_url: str,
            is_osi_approved: bool,
            is_fsf_libre: bool,
    ):
        self.license_id = license_id
        self.license_name = license_name
        self.license_url = license_url
        self.is_osi_approved = is_osi_approved
        self.is_fsf_libre = is_fsf_libre
