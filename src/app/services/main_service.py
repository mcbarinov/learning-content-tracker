from app.services.base import AppService, AppServiceParams


class MainService(AppService):
    def __init__(self, base_params: AppServiceParams) -> None:
        super().__init__(base_params)
